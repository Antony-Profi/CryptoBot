import datetime
from dateutil import parser 
import timedelta

def getTimeDifference(isoStrDateTime):
    delta = timedelta.Timedelta(parser.isoparse(isoStrDateTime) - datetime.datetime.now(datetime.timezone.utc))
    return str(delta)

