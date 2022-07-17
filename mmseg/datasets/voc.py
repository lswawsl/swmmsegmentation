# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
# CLASSES
# 调色盘PALETTE
class PascalVOCDataset(CustomDataset):
    """Pascal VOC dataset.

    Args:
        split (str): Split txt file for Pascal VOC.
    """

    # CLASSES = ('background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle',
    #            'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog',
    #            'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa',
    #            'train', 'tvmonitor')
    CLASSES = ('background', 'cell')

    PALETTE = [[0, 0, 0], [128, 0, 0]]

    def __init__(self, split, **kwargs):
        super(PascalVOCDataset, self).__init__(
            img_suffix='.jpg', seg_map_suffix='.png', split=split, **kwargs)
        assert osp.exists(self.img_dir) and self.split is not None
