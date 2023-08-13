import json
import requests
import xmltodict



url = "http://data.ex.co.kr/openapi/toll/bhoinstIntoTollList"
queryParams = {
  'key' : 'test',
  'type' : 'json',
  'umOfRows' : '10',
  'arrvTolofCd' : '101',
  'dprtrTolofCd' : '102',
  'hoinstCd' : '00',
  'pageNo' : '1',
  'numOfRows' : '10'
}

repones = requests.get(url, params=queryParams)

# print(repones.status_code)
# data = repones.text
# diction = xmltodict.parse(data)
# jsonString = json.dumps(diction, indent=4)
# print(jsonString)

data = repones.json()
print(type(data))
print(data)
print(type(data['list']))
print(data['list'])
data_list = data['list']
data_dict = data_list[0]
print(data_dict)
print(data_dict['arrvTolofCd'])