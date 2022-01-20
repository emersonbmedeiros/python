import requests
import json
import time

"""
Um monte de código por aqui
[...] 
""""
def get_content():
    timestamp = time.strftime("Date: %Y-%m-%d %H:%M", time.localtime())
    msg = []
    msg.append("Stockholm")
    msg.append(timestamp)

    url = "https://api.forecast.io/forecast/%s/%s" % (wth_key, wth_loc)
    req = requests.get(url)
    jdata = json.loads(req.text)

    summary = jdata["currently"]["summary"]
    temp = jdata["currently"]["temperature"]
    temp = Far2Celsius(temp)

    msg.append(u"Temperature: %s°C" % temp)
    msg.append("Summary: %s" %summary)

    return msg
