import requests


uuid = 'exshapebialystok'
apiSource = 'test_michal'
apiGuid = ''
apiKey = ''

response = requests.get(f'https://app.fitssey.com/{uuid}/api/v4/public')

if (response.status_code != requests.codes.ok):
    print('Coś poszło nie tak')
else:
    print(response.json())
