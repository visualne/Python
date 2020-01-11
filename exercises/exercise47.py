from datetime import datetime,tzinfo,timedelta

#  Times
#  Sun 10 May 2015 13:54:36 -0700
#  Sun 10 May 2015 13:54:36 -0000
#  Sat 02 May 2015 19:54:36 +0530
#  Fri 01 May 2015 13:54:36 -0000

#  Need a way to represent the utcoffset.


class TZ(tzinfo):

  def __init__(self,hour,minutes):
      self.hour = hour
      self.minutes = minutes
      pass

  def utcoffset(self, _):
    return timedelta(hours=self.hour,minutes=self.minutes)

  # def dst(self, _):
  #   return timedelta(0)
  #
  # def tzname(self, _):
  #   return 'UTC+1'

times = [
    'Sun 10 May 2015 13:54:36 -0700',
    'Sun 10 May 2015 13:54:36 -0000',
    'Sat 02 May 2015 19:54:36 +0530',
    'Fri 01 May 2015 13:54:36 -0000'
]

tzObj = TZ(-04,00)
dt = datetime(1970, 1, 1, 1, tzinfo=tzObj)
tzObj = TZ(-05,00)
dt2 = datetime(1970, 1, 1, 1, tzinfo=tzObj)
difference = dt2 - dt
print difference.seconds

# dt = datetime(1970, 1, 1, 1, tzinfo=TZ())

print dt