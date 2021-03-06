# 作者：vincent
# code time：2022/3/31 19:52
import matlab.engine
import time

import cv2
import numpy as np
from scipy import io, integrate, linalg, signal

# # scipy.linalg.eigh
# cap = cv2.VideoCapture('./Jumps.avi')
# num_frames = int(cap.get(7)) - 2 # why - 2 ?
# H, W = int(cap.get(3)), int(cap.get(4))
# print(num_frames, H, W)
# X = np.zeros((num_frames, W, H, 3), np.uint8)
from tianshou.data import Batch

def call_matlab(data: Batch=None):
    # print(data)
    # input = np.hstack((data['obs'], data['act']))
    input = data.obs
    print(type(input.shape))
    eng = matlab.engine.start_matlab()
    tf = eng.test(matlab.double(input.tolist()), 950)
    print(tf)
