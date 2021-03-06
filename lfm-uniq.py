import pylast
import urllib2
import re

#
# Total Plays
#

API_KEY="cd46db2d0a17bb100773cbd56dcac707"
API_SECRET="27576ed4e97e19c61e57f68408c088c1"
username = "testdead"
pass_hash = pylast.md5("testing")
net = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = pass_hash)

bur = net.get_user('burbotsrevenge')
print("Total plays in library: " + str(bur.get_playcount()))

#
# Unique tracks
#
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
unique = ((last-1)*20) + lastPage.count('<tr ')
print("Unique tracks in library: " + str(unique))

#
# Unique artists
#
html = urllib2.urlopen('http://www.last.fm/user/BurbotsRevenge/library')
library_recent = html.read()

toFind = 'class="pagenumber">1</span>'
index = library_recent.find(toFind)
index = index + len(toFind) + 4
page = int(library_recent[index:library_recent.find(" ", index)])

finalUrl = 'http://www.last.fm/user/BurbotsRevenge/library?page=' + str(page)
html = urllib2.urlopen(finalUrl)
lastPage = html.read()

unique = ((page-1)*18) + lastPage.count('class="pictureFrame"')
print("Unique artists in library: " + str(unique))
