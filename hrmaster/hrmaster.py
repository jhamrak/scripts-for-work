import requests, base64, pytz, yaml, json
from datetime import date, datetime, timedelta, timezone

config = yaml.safe_load(open("config.yaml"))

headers = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
	'Authorization' : 'Bearer ' + config['access_token']
}

get_request = {
    "legalRelationshipId": "191"
}

set_request = {
    "legalRelationshipId":191,
    "isStandBy": "false"
}


start_date = date.today()
end_date = config['end_date']
delta = timedelta(days=1)
home = 1367
office = 1368
officedays = config['officedays']
    

while start_date <= end_date:
    request_date = start_date.strftime("%Y-%m-%d")+"T20:34:51.900Z"
    print('date: ' + request_date)
    
    get_request["date"]=request_date
    get_response = requests.post('https://icell.hrmaster.hu/Datacenter/WorkingTime/getMyWorkingPlace', json=get_request, headers=headers )
    print("get response:")
    print(get_response.json())
    
    if not get_response.json()["isDisabled"]:
        set_request["date"]=request_date
        if start_date.weekday() in officedays:
            set_request["workingPlaceTypeId"] = office
        else:
            set_request["workingPlaceTypeId"] = home
        set_response = requests.post('https://icell.hrmaster.hu/Datacenter/WorkingTime/setMyWorkingPlace', json=set_request, headers=headers )
        print("set response")
        print(set_response)
    start_date += delta