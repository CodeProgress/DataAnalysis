# -*- coding: utf-8 -*-

#Plots and displays the chess ratings of Grandmasters rated 2700+ using pylab.
#Labels the highest rated player (Last Name - Rating)
#Uses regular expressions package to extract data from http://www.2700chess.com/

import re
import urllib2
import pylab

#chess ratings from 2700chess.com

source = urllib2.urlopen('http://www.2700chess.com/')

text = source.read()

findRatings = re.findall(r'(<td><b>)(\d+.\d)(</b></td>)', text)

#use to label highest plot point
findWorldNumOne = re.search(r'(target="_self">)(\w+)(</a></td>)', text)
worldNumOne = findWorldNumOne.group(2)

ratings = []

for i in findRatings:
    ratings.append(float(i[1]))

  
pylab.xkcd() #for styling
pylab.scatter(range(1, len(ratings)+1), ratings)

#annotate highest rating
pylab.annotate(worldNumOne +' - ' +str(ratings[0]), xy = (0, ratings[0]), xytext = (10, ratings[0]), \
bbox = dict(boxstyle = 'round,pad=0.3', fc = 'yellow', alpha = 0.5), \
arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0', shrinkB=15))

pylab.xlabel("World Rank")
pylab.ylabel("FIDE Rating")
pylab.title("Chess Ratings for GMs 2700+")
pylab.xticks([1] + range(5, int(len(ratings)*1.1), 5))
pylab.show()
