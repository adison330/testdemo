#! /usr/bin/env python
#! -*- coding: utf-8 -*-

from PIL import Image
import sys
# 将图片填充为正方形
def fill_image(image):
    width,height = image.size
    # 选取长和宽中较大值作为新图片
    new_image_length = width if width > height else height
    # 生成新图片
    new_image = image.new(image.mode,(new_image_lenght,new_image_lenght), color = 'white')

    #将之前的图粘贴在新图上，居中
