import os

from wordcloud import WordCloud
import matplotlib.pyplot as plt


# 入力テキストの読み込み
text = open('input.txt').read()

# ストップワードの読み込み
stop_words = open('stop_words.txt').read().strip().split('\n')

# ワードクラウドのイメージを作成
wordcloud = WordCloud(
            font_path='/Library/Fonts/Arial Unicode.ttf',
            background_color="whitesmoke",
            colormap="viridis",
            width=900, 
            height=500,
            stopwords=set(stop_words)
            ).generate(text)

# ワードクラウドのイメージをファイル保存
wordcloud.to_file('output.png')

# matplotlibでワードクラウドのイメージを描画
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
