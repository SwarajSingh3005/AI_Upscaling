import unittest
import numpy as np
from PIL import Image

from dataset import mydata
from dataset import crop



class TestDataset(unittest.TestCase):
    def test_imgLoad(self):
        dataset = mydata("/home/s5501445/ASE_ML_Labs/SRGAN/DIV2K/minibatch_LR",
                         "/home/s5501445/ASE_ML_Labs/SRGAN/DIV2K/minibatch_HR")

        test_image = dataset[1]
        self.assertIsInstance(test_image["LR"], np.ndarray)
        self.assertIsInstance(test_image["GT"], np.ndarray)
        self.assertEqual(test_image["LR"].shape[0], 3)
        self.assertEqual(test_image["GT"].shape[0], 3)
        
    def __getitem__(self, i):
        
        img_item = {}
        
        if self.in_memory:
            GT = self.GT_img[i].astype(np.float32)
            LR = self.LR_img[i].astype(np.float32)
            
        else:
            GT = np.array(Image.open(os.path.join(self.GT_path, self.GT_img[i])).convert("RGB"))
            LR = np.array(Image.open(os.path.join(self.LR_path, self.LR_img[i])).convert("RGB"))

        img_item['GT'] = (GT / 127.5) - 1.0
        img_item['LR'] = (LR / 127.5) - 1.0
                
        if self.transform is not None:
            img_item = self.transform(img_item)
            
        img_item['GT'] = img_item['GT'].transpose(2, 0, 1).astype(np.float32)
        img_item['LR'] = img_item['LR'].transpose(2, 0, 1).astype(np.float32)
        
        return img_item
    
    def test_crop(self):
        pass