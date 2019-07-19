import os
from os import *

system("python train.py \
  --bottleneck_dir=/home/shanawaz/MultiClassImageClassification/bottleneck \
  --how_many_training_steps=2000 \
  --model_dir=/home/shanawaz/MultiClassImageClassification/imagenet \
  --summaries_dir=/home/shanawaz/MultiClassImageClassification/retrain_logs \
  --output_graph=/home/shanawaz/MultiClassImageClassification/output_graph.pb \
  --output_labels=/home/shanawaz/MultiClassImageClassification/output_labels.txt \
  --image_dir=/home/shanawaz/MultiClassImageClassification/dataset \
")

















 




































