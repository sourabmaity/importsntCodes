import os
import random
import shutil
image_paths=[]
yolo_file="E:/DefectScanner/6_3_23/19_08_23/"
allAugImg="E:/DefectScanner/6_3_23/19_08_23/allAug2"
for file in os.listdir(allAugImg):
    if file.endswith(".png"):
        text_lo = os.path.join(allAugImg, file)
        image_paths.append(text_lo)
# image_paths
print(len(image_paths))
random.shuffle(image_paths)
train_data = image_paths[:int((len(image_paths)+1)*.70)]
val_data = image_paths[int((len(image_paths)+1)*.70):]
print(len(train_data),len(val_data))
for i in image_paths:
    # print(i)
    if i in train_data:
        shutil.move(i, f"{yolo_file}/yolov8/train/images")
        shutil.move(i[:-4]+".txt", f"{yolo_file}/yolov8/train/labels")
    if i in val_data:
        shutil.move(i, f"{yolo_file}/yolov8/valid/images")
        shutil.move(i[:-4]+".txt", f"{yolo_file}/yolov8/valid/labels")

