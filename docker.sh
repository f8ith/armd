docker run --name yolov7 --runtime=nvidia --gpus all -it -v ./data:/data/ -v ./yolov7:/yolov7 --shm-size=24g nvcr.io/nvidia/pytorch:24.08-py3
