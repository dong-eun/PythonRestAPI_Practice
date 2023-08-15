import requests

ENDPOINT = "https://apis.data.go.kr/B552061/frequentzoneBicycle"
serviceKey = "8hJkZbQonEqg1vk6uj53kYxkX6fol6yW5eCAjtrIynh1O64/ucaxhGuopQujkH9kRF8yfK8xfe00e6kMs58b6g=="

params = {
  'ServiceKey': serviceKey,
  'searchYearCd': '2021',
  'siDo': '11',
  'guGun': '110',
  'type': 'json',
  'numOfRows': '10',
  'pageNo': '1'
}

accident_response = requests.get(ENDPOINT + "/getRestFrequentzoneBicycle", params=params)

# assert accident_response.status_code == 200
assert accident_response.status_code == 200

jsonString = accident_response.json()
print(jsonString)
print(type(jsonString))
print(jsonString["items"]["item"][0]['afos_fid'])
sido = jsonString["items"]["item"]
print(sido[0]["spot_cd"])