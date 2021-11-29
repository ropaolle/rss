import os
from mutagen.mp3 import MP3

mp3filename = './mp3/medito-will-10m.mp3'

statinfo = os.stat(mp3filename)
size = str(statinfo.st_size)

audio = MP3(mp3filename)
length = str(audio.info.length)

xmlfile = ''
xmlfile += "<enclosure url='https://PODCAST URL/{}' length='{}' type='audio/mpeg'/>\n".format(mp3filename,size)
xmlfile += "<itunes:duration>{}</itunes:duration>\n".format(length)

print(xmlfile)

from email.utils import parsedate_to_datetime
datestr = 'Sun, 09 Mar 1997 13:45:00 -0500'
datetime = parsedate_to_datetime(datestr)
# datetime.
# datetime.
# datetime(1997, 3, 9, 13, 45, tzinfo=datetime.timezone(datetime.timedelta(-1, 68400)))

print(datetime)
