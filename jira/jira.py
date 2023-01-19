import requests, base64, pytz, yaml
from datetime import date, datetime, timedelta, timezone

def date_for_weekday(today: date, day: int):
    # weekday returns the offsets 0-6
    # If you need 1-7, use isoweekday
    weekday = today.weekday()
    return today + timedelta(days=day - weekday)

def time_format(dt):
    return "%s:%.3f%s" % (
        dt.strftime('%Y-%m-%dT%H:%M'),
        float("%.3f" % (dt.second + dt.microsecond / 1e6)),
        dt.strftime('%z')
    )

config = yaml.safe_load(open("config.yaml"))

headers = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
	'Authorization' : 'Bearer ' + config['access_key']
}

req_ds = {
    "comment": "DS",
    "timeSpent": "15m"
}
url_ds = "https://jira.icellmobilsoft.hu/rest/api/2/issue/" + config['task_ds'] + "/worklog" 
url_guild = "https://jira.icellmobilsoft.hu/rest/api/2/issue/" + config['task_guild'] + "/worklog" 

req_guild = {
    "comment": "ceh",
    "timeSpent": "1h"
}

today = datetime.now(timezone.utc) + timedelta(7*config['week_offset'])

for i in range(5):
	#print(date_for_weekday(today, i).isoformat())
	req_ds["started"] = time_format(date_for_weekday(today, i))
	req_guild["started"] = time_format(date_for_weekday(today, i))
	response = requests.post(url_ds, json=req_ds, headers=headers )
	print(response.json())
	# thursday
    if(i == 3):
		response = requests.post(url_guild, json=req_guild, headers=headers )
		print(response.json())
		#print(date_for_weekday(today, i).isoformat() + ' ceh')
