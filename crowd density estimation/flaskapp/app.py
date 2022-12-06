from M1_SFANet import predict
from flask import Flask, request, jsonify
import base64
from PIL import Image
from os import path, remove
from io import StringIO,BytesIO
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import cv2

base_dir = os.getcwd()
img_dir = os.path.join(base_dir, '../.images')

if not os.path.isdir(img_dir):
    os.mkdir(img_dir)

app = Flask(__name__)
@app.route('/count', methods=["POST"])
def getcount():
    data = {}
    if request.method == "POST":
        try:
            data = request.json
            base64_img = data['image'] 
            img_id = data['id']
            base64_img_bytes = base64_img.encode('utf-8')
            
            density_img = img_dir+str(img_id)+'.png'
            #img = Image.open(BytesIO(base64.b64decode(base64_img_bytes)))
            #file_like = BytesIO(base64_img_bytes)
            #img = Image.open(file_like.read())
            
            img = BytesIO(base64.b64decode(base64_img_bytes))
            count,density_map = predict(img)
            plt.imsave(density_img,density_map,cmap=cm.jet)
            with open(density_img, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
            resp = {'id':img_id,'count':count,'density_map':encoded_string.decode("utf-8")}
            remove(density_img)
            return jsonify(resp)
        except Exception as ex:
            remove(img)
            return jsonify({"message": ex}), 500
    return jsonify(data)
if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5003)