import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import torch
from torchvision import transforms
import time
from models import M_SFANet_UCF_QNRF
import warnings
warnings.filterwarnings('ignore')
trans = transforms.Compose([transforms.ToTensor(), 
                            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                           ])

model = M_SFANet_UCF_QNRF.Model()
model.load_state_dict(torch.load("weights/best_M-SFANet*_UCF_QNRF.pth", map_location = torch.device('cpu')))

def predict(path):
    #print('started')
    img = Image.open(path).convert('RGB')
    
    height, width = img.size[1], img.size[0]
    
    height = round(height / 32) * 16
    width = round(width / 32) * 16
    img = cv2.resize(np.array(img), (width,height), cv2.INTER_CUBIC)
    img = trans(Image.fromarray(img))[None, :]
    
    density_map = model(img)
    
    shapes = density_map.shape

    count = round(torch.sum(density_map).item())
    density_map = density_map.detach().numpy().reshape(shapes[2],shapes[3])
    
    #density_map = put_text("count : ".format(str(count)))
    #plt.imsave(density_map,cmap=cm.jet)
    
    return count,density_map
