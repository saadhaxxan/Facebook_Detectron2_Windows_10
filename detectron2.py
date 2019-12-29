from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
import cv2
import torch
from PIL import Image




im = cv2.imread(#path of your image here)

	# Create Config

cfg = get_cfg()
cfg.merge_from_file('mask_rcnn_R_50_FPN_3x.yaml')#pretrained model you need to download this
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
cfg.MODEL.WEIGHTS = "model_final_f10217.pkl"#pretrained weights you need to download this file
cfg.MODEL.DEVICE = "cpu"#selecting inference to cpu comment this line if you have gpu.

predictor = DefaultPredictor(cfg)

outputs = predictor(im)

v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
cv2.imshow("Segmented image",v.get_image()[:, :, ::-1])
cv2.imwrite('path where image to be saved',v.get_image()[:, :, ::-1])
