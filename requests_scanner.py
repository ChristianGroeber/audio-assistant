from requests import get
import json

backup_file_path = "backup.json"

r = get('https://redacted.ch/ajax.php?action=requests', headers={'Authorization': '659cea5b.e4ee9d19895538431bb6d4105d5ccfc9'})
requests = r.json()['response']['results']

for request in requests:
    print(request)
