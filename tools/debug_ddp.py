#!/usr/bin/env python
# Copyright (c) Facebook, Inc. and its affiliates.
"""
Copied directly from detectron2/tools/train_net.py except where noted.
"""

import detectron2.utils.comm as comm
from detectron2.checkpoint import DetectionCheckpointer
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.engine import default_argument_parser, default_setup, launch
from detectron2.evaluation import verify_results
import matplotlib.pyplot as plt

from config import add_da_config
from trainer import DATrainer
import datasets # register datasets with Detectron2
import rcnn # register DA R-CNN model with Detectron2

def setup(args):
    """
    Copied directly from detectron2/tools/train_net.py
    """
    cfg = get_cfg()
    add_da_config(cfg)
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    cfg.freeze()
    default_setup(cfg, args)
    return cfg

class TestTrainer(DATrainer):
    def __init__(self, cfg):
        super().__init__(cfg)

    def train(self):
        self.max_iter = 1
        super().train()

    def after_train(self):
        return

def main(args):
    """
    Copied directly from detectron2/tools/train_net.py
    But replace Trainer with DATrainer and disable TTA.
    """
    cfg = setup(args)

    trainer = TestTrainer(cfg)
    trainer.resume_or_load(resume=args.resume)
    trainer.train()

    labeled, unlabeled = trainer._trainer._last_labeled, trainer._trainer._last_unlabeled
    unlabeled_before, unlabeled_after = trainer._trainer._last_unlabeled_before_teacher, trainer._trainer._last_unlabeled_after_teacher
    student_preds = trainer._trainer._last_student_preds

    for i, (l, ul, ul_b, ul_a, sp) in enumerate(zip(labeled, unlabeled, unlabeled_before, unlabeled_after, student_preds)):
        fig, ax = plt.subplots(4,1, figsize=(20,20))
        labeled_im = l['image'].permute(1,2,0).cpu().numpy()
        unlabeled_im = ul['image'].permute(1,2,0).cpu().numpy()
        unlabeled_before_im = ul_b['image'].permute(1,2,0).cpu().numpy()
        unlabeled_after_im = ul_a['image'].permute(1,2,0).cpu().numpy()

        # plot images
        ax[0].imshow(labeled_im)
        ax[1].imshow(unlabeled_im)
        ax[2].imshow(unlabeled_before_im)
        ax[3].imshow(unlabeled_after_im)

        # plot instances as rectangles
        for inst in l['instances'].gt_boxes.tensor:
            x1,y1,x2,y2 = inst.cpu().numpy()
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            ax[0].add_patch(plt.Rectangle((x1,y1), x2-x1, y2-y1, fill=False, edgecolor='r', linewidth=2))
        for inst in ul['instances'].gt_boxes.tensor:
            x1,y1,x2,y2 = inst.cpu().numpy()
            ax[1].add_patch(plt.Rectangle((x1,y1), x2-x1, y2-y1, fill=False, edgecolor='r', linewidth=2))
        for inst in ul_b['instances'].gt_boxes.tensor:
            x1,y1,x2,y2 = inst.cpu().numpy()
            ax[2].add_patch(plt.Rectangle((x1,y1), x2-x1, y2-y1, fill=False, edgecolor='r', linewidth=2))
        for inst in ul_a['instances'].gt_boxes.tensor:
            x1,y1,x2,y2 = inst.cpu().numpy()
            ax[3].add_patch(plt.Rectangle((x1,y1), x2-x1, y2-y1, fill=False, edgecolor='r', linewidth=3))
        # add student instances in blue
        for inst in sp.pred_boxes.tensor:
            x1,y1,x2,y2 = inst.cpu().numpy()
            ax[3].add_patch(plt.Rectangle((x1,y1), x2-x1, y2-y1, fill=False, edgecolor='b', linewidth=1))

        ax[0].set_title('Labeled')
        ax[1].set_title('Unlabeled (raw)')
        ax[2].set_title('Unlabeled before teacher')
        ax[3].set_title('Unlabeled after teacher')

        plt.savefig(f'debug_{l["image_id"]}_{i}.png')
        plt.close()


if __name__ == "__main__":
    args = default_argument_parser().parse_args()
    print("Command Line Args:", args)
    launch(
        main,
        args.num_gpus,
        num_machines=args.num_machines,
        machine_rank=args.machine_rank,
        dist_url=args.dist_url,
        args=(args,),
    )