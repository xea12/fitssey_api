import requests


uuid = 'exshapebialystok'
apiSource = 'test_michal'
apiGuid = '31422255-D1F1-4E0C-8856-8E1A078EB0A5'
apiKey = 'X5JHNRXXM57XG2N'

response = requests.get(f'https://app.fitssey.com/{uuid}/api/v4/public')

if (response.status_code != requests.codes.ok):
    print('Coś poszło nie tak')
else:
    print(response.json())