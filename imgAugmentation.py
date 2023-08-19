import os
import pybboxes as pbx
import cv2
import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import uuid


def convert(size, boxes): # x1,y1,x2,y2,id
  conBbox=[]
  for box in boxes:
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box.x1 + box.x2) / 2.0 - 1
    y = (box.y1 + box.y2) / 2.0 - 1
    w = box.x2 - box.x1
    h = box.y2 - box.y1
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    conBbox.append([box.label,x,y,w,h]) # id,x,y,w,h
  return conBbox


W=800
labels=['split_pin','castle_nut']
for file in os.listdir("E:/DefectScanner/Axle_code_transfer/labelling (1)/labelling/washermodelSo"):
    if file.endswith(".txt"):
        text_lo=os.path.join("E:/DefectScanner/Axle_code_transfer/labelling (1)/labelling/washermodelSo", file)
        print(file)
        img=cv2.imread(text_lo[:-4]+".jpg")
        h,w,_=img.shape
        bbox = []
        with open(text_lo) as f:
            for line in f.readlines():
                l=line.split(" ")
                x1,y1,x2,y2=pbx.convert_bbox((float(l[1]),float(l[2]),float(l[3]),float(l[4])), from_type="yolo", to_type="voc", image_size=(w, h))
                # print(x1,y1,x2,y2)
                bbox.append(BoundingBox(x1=x1, y1=y1, x2=x2, y2=y2,label=int(l[0])))
            bbs = BoundingBoxesOnImage(bbox, shape=img.shape)
            # print("bbs",bbs)
            for angle in range(0, 360, 10):
                seq = iaa.Sequential([
                    iaa.Resize(W),
                    # iaa.AddToBrightness((-20, 20))
                    # iaa.AddToHue((-10, 10))
                    # iaa.AddToSaturation((-15, 15))
                    iaa.Affine(
                        rotate=angle
                    )
                ])
                image_aug, bbs_aug = seq(image=img, bounding_boxes=bbs)
                file_name = str(uuid.uuid4())
                # print(bbs_aug)
                conBbox = convert((W,W), bbs_aug.bounding_boxes)
                cv2.imwrite(f'E:/DefectScanner/Axle_code_transfer/labelling (1)/labelling/washerModelAugAll/{file_name}.png', image_aug)
                out_file = open(f'E:/DefectScanner/Axle_code_transfer/labelling (1)/labelling/washerModelAugAll/{file_name}.txt', 'w')
                for bb in conBbox:
                    out_file.write(" ".join([str(a) for a in bb]) + '\n')
                out_file.close()
                # img_after = bbs_aug.draw_on_image(image_aug, size=2, color=[0, 0, 255])
                # cv2.imshow("augResult",img_after)
                # cv2.waitKey(0)
                # break

            seq = iaa.Sequential([
                iaa.Resize(W),
                iaa.AddToBrightness((-20, 20))
                # iaa.AddToHue((-10, 10))
                # iaa.AddToSaturation((-15, 15))
                # iaa.Affine(
                #     rotate=angle
                # )
            ])
            image_aug, bbs_aug = seq(image=img, bounding_boxes=bbs)
            file_name = str(uuid.uuid4())
            # print(bbs_aug)
            conBbox = convert((W, W), bbs_aug.bounding_boxes)
            cv2.imwrite(f'E:/DefectScanner/Axle_code_transfer/labelling (1)/labelling/washerModelAugAll/{file_name}.png',
                        image_aug)
            out_file = open(
                f'E:/DefectScanner/Axle_code_transfer/labelling (1)/labelling/washerModelAugAll/{file_name}.txt', 'w')
            for bb in conBbox:
                out_file.write(" ".join([str(a) for a in bb]) + '\n')
            out_file.close()

            seq = iaa.Sequential([
                iaa.Resize(W),
                # iaa.AddToBrightness((-20, 20))
                iaa.AddToHue((-10, 10))
                # iaa.AddToSaturation((-15, 15))
                # iaa.Affine(
                #     rotate=angle
                # )
            ])
            image_aug, bbs_aug = seq(image=img, bounding_boxes=bbs)
            file_name = str(uuid.uuid4())
            # print(bbs_aug)
            conBbox = convert((W, W), bbs_aug.bounding_boxes)
            cv2.imwrite(f'E:/DefectScanner/Axle_code_transfer/labelling (1)/labelling/washerModelAugAll/{file_name}.png',
                        image_aug)
            out_file = open(
                f'E:/DefectScanner/Axle_code_transfer/labelling (1)/labelling/washerModelAugAll/{file_name}.txt', 'w')
            for bb in conBbox:
                out_file.write(" ".join([str(a) for a in bb]) + '\n')
            out_file.close()

            seq = iaa.Sequential([
                iaa.Resize(W),
                # iaa.AddToBrightness((-20, 20))
                # iaa.AddToHue((-10, 10))
                iaa.AddToSaturation((-15, 15))
                # iaa.Affine(
                #     rotate=angle
                # )
            ])
            image_aug, bbs_aug = seq(image=img, bounding_boxes=bbs)
            file_name = str(uuid.uuid4())
            # print(bbs_aug)
            conBbox = convert((W, W), bbs_aug.bounding_boxes)
            cv2.imwrite(f'E:/DefectScanner/Axle_code_transfer/labelling (1)/labelling/washerModelAugAll/{file_name}.png',
                        image_aug)
            out_file = open(
                f'E:/DefectScanner/Axle_code_transfer/labelling (1)/labelling/washerModelAugAll/{file_name}.txt', 'w')
            for bb in conBbox:
                out_file.write(" ".join([str(a) for a in bb]) + '\n')
            out_file.close()

            # break



cv2.destroyAllWindows()