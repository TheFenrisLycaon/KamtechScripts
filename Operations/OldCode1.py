#! /home/fenris/anaconda3/envs/ML/bin/python

from PIL import ImageChops
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os


def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def compare_images(imageA, imageB, title):
    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap=plt.cm.gray)
    plt.axis("off")
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()

originalImgs = sorted(os.listdir('./out/Sample4/'))
testImgs = sorted(os.listdir('./out/temp4/'))


def equal(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None

for i in range(len(originalImgs)):
    # original = cv2.imread(f"./out/Sample4/{originalImgs[i]}")
    # test = cv2.imread(f"./out/Sample4/{testImgs[i]}")
    # original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    # test = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
    # fig = plt.figure("Images")
    # images = ("Original", original), ("test",test)
    # for (i, (name, image)) in enumerate(images):
    #     ax = fig.add_subplot(1, 3, i + 1)
    #     ax.set_title(name)
    #     plt.imshow(image, cmap=plt.cm.gray)
    #     plt.axis("off")
    # plt.show()

    # compare_images(original, test, "Original vs. test")

    print(equal(originalImgs[i], testImgs[i]))