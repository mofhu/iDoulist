# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist output_tag_cloud.py

"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

path.exists('/Users/FrankHu/Library/Fonts/WeibeiSC-Bold.otf')


#d = path.dirname(__file__)

# Read the whole text.
#text = open(path.join(d, 'py.txt')).read()

frequencies = [[u'C', 2144], [u'编程', 1399], [u'c语言', 1363], [u'计算机', 803], [u'程序设计', 715]]

wordcloud = WordCloud(font_path='WeibeiSC-Bold.otf').generate_from_frequencies(frequencies)
# Open a plot of the generated image.
plt.imshow(wordcloud)
plt.axis("off")
plt.show()