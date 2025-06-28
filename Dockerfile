FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu20.04

RUN apt-get update && apt-get install -y \
    git wget ffmpeg libsm6 libxext6 libgl1-mesa-glx python3 python3-pip

WORKDIR /workspace
COPY . /workspace

RUN pip3 install --upgrade pip
RUN pip3 install torch==1.12.1 torchvision==0.13.1 numpy opencv-python Pillow yacs tqdm scipy scikit-image

CMD ["python3", "predict.py"]
