
import urllib2
import re

html = urllib2.urlopen('http://www.last.fm/user/BurbotsRevenge/library/recent')
library_recent = html.read()

toFind = "user/BurbotsRevenge/library/recent?sortBy=date&amp;sortOrder=desc&amp;page="
index = 0
pages = []
while index < len(library_recent):
	index = library_recent.find(toFind, index)
	if index==-1:
		break
	size = len(toFind)
	end = library_recent.find('"', index+size)
	pages.append(int(library_recent[index+size:end]))
	index += size

pages.sort()
last = pages[-1]
finalUrl = "http://www.last.fm/user/BurbotsRevenge/library/recent?page=" + str(last)

html = urllib2.urlopen(finalUrl)
lastPage = html.read()
unique = (last*20) + lastPage.count('<tr ')
print("Unique tracks in library: " + str(unique))
