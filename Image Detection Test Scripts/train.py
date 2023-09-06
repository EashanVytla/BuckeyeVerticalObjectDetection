from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.yaml')  # build a new model from YAML
    model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
    model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights
    model.train(data='C:\\Data\\Buckeye Vertical\\Prelim Detection Dataset\\data.yaml', imgsz=1080, batch=10, epochs=30, name="BVTargetModel")

if __name__ == '__main__':
    main()
