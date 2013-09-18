import pylast
import sys
from decimal import *

API_KEY="cd46db2d0a17bb100773cbd56dcac707"
API_SECRET="27576ed4e97e19c61e57f68408c088c1"
username = "testdead"
pass_hash = pylast.md5("testing")
net = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = pass_hash)

bur = net.get_user('burbotsrevenge')
top_artists = bur.get_top_artists()
long = 0
for i in range(0,20):
    if len(top_artists[i].item.get_name()) > long:
        long = len(top_artists[i].item.get_name())    
max = top_artists[0].weight
for x in range(0, 20):
    sys.stdout.write(str(top_artists[x].item))
    for i in range(0,long+1-len(top_artists[x].item.get_name())):
        sys.stdout.write(" ")
    for i in range(0,99*int(top_artists[x].weight)/int(max)):
        sys.stdout.write("|")
    print ""
