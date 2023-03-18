import cv2
import numpy as np
import glob
import os
from natsort import natsorted, ns

frameSize = (1280, 720)

out = cv2.VideoWriter('output_video.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)
png_ = glob.glob('D:/EVA/EVA8/EVA8_Assignments/S12/q2_custom_yolo_object_detection/YoloV3/out_out/*.png')


png_ = natsorted(png_, key=lambda y: int(os.path.split(y)[-1].split('.')[0].split('-')[-1]))

for filename in png_:
        img = cv2.imread(filename)
        print(filename)
        out.write(img)
out.release()