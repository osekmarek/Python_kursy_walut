import requests
import json

response = requests.get('http://api.nbp.pl/api/exchangerates/tables/b/last/1/?format=json')

status_code = response.status_code
print(status_code)

result = response.json()
print(result)

a=result[0]
print(a)   
for i in a:
    print(i)

print("Kursy walut z tabeli:",a['table'],"z dnia:",a['effectiveDate'])
print('nazwa waluty;','symbol waluty;','kurs waluty')
for i in a['rates']:
    print(i['currency']+';',i['code']+';',i['mid'])   
