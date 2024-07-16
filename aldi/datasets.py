from detectron2.data.datasets import register_coco_instances

# Cityscapes 
register_coco_instances("cityscapes_train", {},         "datasets/cityscapes/annotations/cityscapes_train_instances.json",                  "datasets/cityscapes/leftImg8bit/train/")
register_coco_instances("cityscapes_val",   {},         "datasets/cityscapes/annotations/cityscapes_val_instances.json",                    "datasets/cityscapes/leftImg8bit/val/")

# Foggy Cityscapes
register_coco_instances("cityscapes_foggy_train", {},   "datasets/cityscapes/annotations/cityscapes_train_instances_foggyALL.json",   "datasets/cityscapes/leftImg8bit_foggy/train/")
register_coco_instances("cityscapes_foggy_val", {},     "datasets/cityscapes/annotations/cityscapes_val_instances_foggyALL.json",     "datasets/cityscapes/leftImg8bit_foggy/val/")
# for evaluating COCO-pretrained models: category IDs are remapped to match
register_coco_instances("cityscapes_foggy_val_coco_ids", {},     "datasets/cityscapes/annotations/cityscapes_val_instances_foggyALL_coco.json",     "datasets/cityscapes/leftImg8bit_foggy/val/")

# Sim10k
register_coco_instances("sim10k_cars_train", {},             "datasets/sim10k/coco_car_annotations.json",                  "datasets/sim10k/images/")
register_coco_instances("cityscapes_cars_train", {},         "datasets/cityscapes/annotations/cityscapes_train_instances_cars.json",                  "datasets/cityscapes/leftImg8bit/train/")
register_coco_instances("cityscapes_cars_val",   {},         "datasets/cityscapes/annotations/cityscapes_val_instances_cars.json",                    "datasets/cityscapes/leftImg8bit/val/")

# CFC
register_coco_instances("cfc_train", {},         "datasets/cfc/coco_labels/cfc_train.json",                  "datasets/cfc/images/cfc_train/")
register_coco_instances("cfc_val",   {},         "datasets/cfc/coco_labels/cfc_val.json",                    "datasets/cfc/images/cfc_val/")
register_coco_instances("cfc_channel_train", {},         "datasets/cfc/coco_labels/cfc_channel_train.json",                  "datasets/cfc/images/cfc_channel_train/")
register_coco_instances("cfc_channel_test",   {},         "datasets/cfc/coco_labels/cfc_channel_test.json",                    "datasets/cfc/images/cfc_channel_test/")

# XC
register_coco_instances("xc_train", {}, "datasets/xc/annotations/xc-train.json", "datasets/xc/images/train/")
register_coco_instances("xc_val", {}, "datasets/xc/annotations/xc-val.json", "datasets/xc/images/val/")

# Song 9
register_coco_instances("song9_train", {}, "datasets/song9/annotations/song9-train.json", "datasets/song9/images/train/")
register_coco_instances("song9_val", {}, "datasets/song9/annotations/song9-val.json", "datasets/song9/images/val/")
register_coco_instances("song9_test", {}, "datasets/song9/annotations/song9-test.json", "datasets/song9/images/test/")

# PNRE
register_coco_instances("pnre_train", {}, "datasets/pnre/annotations/pnre-train.json", "datasets/pnre/images/train/")
register_coco_instances("pnre_val", {}, "datasets/pnre/annotations/pnre-val.json", "datasets/pnre/images/val/")
register_coco_instances("pnre_test", {}, "datasets/pnre/annotations/pnre-val.json", "datasets/song9/images/val/")


# XC small sample
register_coco_instances("xc_sample_train", {}, "datasets/xc-sample/annotations/xc-train.json", "datasets/xc-sample/images/train/")
register_coco_instances("xc_sample_val", {}, "datasets/xc-sample/annotations/xc-val.json", "datasets/xc-sample/images/val/")
