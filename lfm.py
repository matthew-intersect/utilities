import pylast
from datetime import *
from decimal import *
import calendar

API_KEY="cd46db2d0a17bb100773cbd56dcac707"
API_SECRET="27576ed4e97e19c61e57f68408c088c1"
username = "testdead"
pass_hash = pylast.md5("testing")
net = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = pass_hash)

bur = net.get_user('burbotsrevenge')
playcount = Decimal(bur.get_playcount())
start_date = date(2007, 11, 3)
curr_date = date.today()
total_days = Decimal((curr_date - start_date).days)
avg = Decimal(playcount/total_days)
print "Average daily playcount: " + str(avg.quantize(Decimal('.01'), rounding=ROUND_DOWN))

avg_wanted = avg.quantize(Decimal('1.'), rounding=ROUND_HALF_EVEN) + Decimal(0.5)
playcount_needed = (avg_wanted * total_days) - playcount
print "Extra plays needed: " + str(playcount_needed.quantize(Decimal('1.'), rounding=ROUND_UP))

#million plays
plays_needed = 1000000 - playcount
days_needed = Decimal(plays_needed/avg).quantize(Decimal('1.'), rounding=ROUND_UP)
million_date = curr_date + timedelta(days=int(days_needed))
days_till = (million_date-curr_date).days
years_till = days_till/365
age = bur.get_age()
million_age = age + years_till
print "Date (Age) million plays reached: " + str(million_date) + str(" (Age: ") + str(million_age) + ")"

start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)-timedelta(hours=10)
end = datetime.now()-timedelta(hours=10)
utc_start = calendar.timegm(start.utctimetuple())
utc_end = calendar.timegm(end.utctimetuple())
rec = bur.get_recent_tracks(time_from=utc_start, time_to=utc_end, limit=200)
day_ago = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
day_count = 0
artists_today = []
for track in rec:
    artists_today.append(track[0].get_artist().get_name())
print "Tracks played today: " + str(len(rec))
if len(rec) != 0:
    day_winner = max(set(artists_today), key=artists_today.count)
    print "Most played Artist today: " + day_winner + " (" + str(artists_today.count(day_winner)) + ")"
