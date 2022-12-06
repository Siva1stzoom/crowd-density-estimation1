FROM ubuntu:18.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    tzdata \
    sudo
RUN apt-get update && apt-get install software-properties-common -y 
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get install -y python3.8 \
    python3-pip
RUN python3.8 -m pip install --upgrade --force-reinstall pip
RUN ln -s /usr/bin/pip3 /usr/bin/pip && \
    ln -s /usr/bin/python3.8 /usr/bin/python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
RUN apt-get install -y python3.8-venv

ENV TZ="America/New_York"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN chmod +x -R /usr/src/
COPY ./flaskapp /usr/src/flaskapp
WORKDIR /usr/src/flaskapp
CMD ["/usr/src/flaskapp/setup.sh"]