from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

text = open("Hello World!")

wc = WordCloud().generate(text)
plt.imshow(wc)
plt.axis("off")
plt.show()