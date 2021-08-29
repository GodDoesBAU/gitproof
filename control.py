#! /usr/bin/python3

import wordcloud
import argparse
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# Here is a list of punctuations and uninteresting words you can use to process your text
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

file_contents=str()
parser = argparse.ArgumentParser(description='Make a wordcloud')
parser.add_argument('text', type=open, nargs='+',
                    help='The txt file where text is stored')
parser.add_argument('--mask', dest='mask', nargs='?', type=str,
                    help='Get the mask for wordcloud')
args = parser.parse_args()

for line in args.text:
    file_contents+=line.read()

file_contents = file_contents.translate(str.maketrans('','',punctuations))
resultwords  = [word for word in file_contents.split() if word.lower() not in uninteresting_words]
frequencies=dict()
for i in resultwords:
    frequencies[i]=frequencies.get(i,0)+1
if(args.mask):
    random_mask = np.array(Image.open(args.mask))
    cloud = wordcloud.WordCloud(mask=random_mask, background_color="black")
    cloud.generate_from_frequencies(frequencies)
    plt.imshow(cloud, interpolation="nearest")
    plt.axis('off')
    plt.savefig('mywordcloud.png')
else:
    cloud = wordcloud.WordCloud(width=1920, height=1080)
    cloud.generate_from_frequencies(frequencies)
    cloud.to_file("myfile.jpg")
