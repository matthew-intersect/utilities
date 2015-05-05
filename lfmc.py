import sys
import os
import pylast

net = None
user = None

def main():
  print "connecting..."
  API_KEY="cd46db2d0a17bb100773cbd56dcac707"
  API_SECRET="27576ed4e97e19c61e57f68408c088c1"
  username = "testdead"
  pass_hash = pylast.md5("testing")
  global net
  net = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = pass_hash)
  global user
  user = net.get_user('burbotsrevenge')


  print_help()
  while True:
    sys.stdout.write(">>")
    input = raw_input()
    process_input(input)
    

def print_artist_count():
  sys.stdout.write("Artist: ")
  artist = raw_input()
  try:
    print pylast.Artist(artist, net, username=user.get_name()).get_userplaycount()
  except pylast.WSError:
    print "could not find artist"

def print_top_artists():
  top_artists = user.get_top_artists()
  long = 0
  for i in range(0,20):
    if len(top_artists[i].item.get_name()) > long:
      long = len(top_artists[i].item.get_name())    
  max = top_artists[0].weight
  for x in range(0, 20):
    sys.stdout.write(str(top_artists[x].item))
    for i in range(0,long+1-len(top_artists[x].item.get_name())):
      sys.stdout.write(" ")
    sys.stdout.write("||")
    sys.stdout.write(top_artists[x].weight)
    for i in range(0,95*int(top_artists[x].weight)/int(max)):
      sys.stdout.write("|")
    print ""

def process_input(input):
  if input == "exit" or input == "e":
    sys.exit(0)
  elif input == "a":
    print_artist_count()
  elif input == "ta":
    print_top_artists()
  elif input == "clear":
    os.system('clear')
  elif input == "":
    pass
  elif input == "h":
    print_help()
  else:
    print "invalid command"

def print_help():
  print "-------------------------"
  print "Last FM Command Line"
  print ""
  print "[a] Print playcount for given artist"
  print "[ta] Print top artists chart"
  print "[h] Reprint this help"
  print "[exit] Exit the program"
  print "-------------------------"

if __name__ == "__main__":
  main()
