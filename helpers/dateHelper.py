import datetime
from dateutil import parser 


def getHoursDifferenceWithCurrentDateTime(isoStrDateTime):
    delta = (parser.isoparse(isoStrDateTime) - datetime.datetime.now(datetime.timezone.utc)).total_seconds()
    return divmod(delta, 3600)[0]
