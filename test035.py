#! /usr/bin/env python

# 对分词文本生成词云
# 生成词云，需要指定支持中文的字体，否则无法生成中文词云。

wc = WordCloud
    # 设置词云图片背景色，默认黑色
    background_color = "white",
    # 设置词云最大单数
    max_words = 200
    # 设置词云中字号最大值
    max_font_size = 80
    # 设置词云图片宽，高
    width = 768
    heighe = 1024

    # 设置词云文字字体（美化和解决中文乱码问题）
    font_path = r '../example/fonts/FZXingKai-S04S.TTF’
    ).generate(new_text)

# 绘图（标准长方形）
pyplot.imshow(wc, interpolation = "bilinear")
pyplot.figure()
pyplot.axis("off")
# 将图片输出到文件
wc.to_file(r"./images/wc.png")