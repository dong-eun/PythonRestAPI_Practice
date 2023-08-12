import requests
import xmltodict

ENDPOINT = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade"

params = {
  'LAWD_CD': '11110',
  'DEAL_YMD': '201512',
  'serviceKey': '8hJkZbQonEqg1vk6uj53kYxkX6fol6yW5eCAjtrIynh1O64/ucaxhGuopQujkH9kRF8yfK8xfe00e6kMs58b6g=='
}

response = requests.get(ENDPOINT, params=params)
assert response.status_code == 200

print(response.text)
print(type(response.text))
string = xmltodict.parse(response.text)
print(type(string))
print(string)
print(string['response']['body']['items']['item'])