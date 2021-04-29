import requests
import json
# ACTIVITIES_URL = 'https://<your_tenant>.<tenant_region>.contoso.com/api/v1/activities/'
ACTIVITIES_URL = 'https://smartdocuments.eu2.portal.cloudappsecurity.com/api/v1/entities/'


your_token = 'XEJOXVtLQExaQkpBW1wBSlodAV9AXVtOQwFMQ0BaS05fX1xKTFpdRltWAUxAQlNNG0wbF05LGxkWTEseSxhOS0sZHx8dHEwWSUoeGUkeHkpKFxhMThxJTRxOFhcZHB0aGE0YGB5JHUkbHx9OGh0f'
headers = {
'Authorization': 'Token {}'.format(your_token),
}

filters = {
  # optionally, edit to match your filters
  'date': {'gte_ndays': 1},
  'service': {'eq': [20893]}
}
request_data = {
  'filters': filters,
  'isScan': True
}

records = []
has_next = True
while has_next:
    content = json.loads(requests.post(ACTIVITIES_URL, json=request_data, headers=headers).content)
    response_data = content.get('data', [])
    records += response_data
    print('Got {} more records'.format(len(response_data)))
    has_next = content.get('hasNext', False)
    request_data['filters'] = content.get('nextQueryFilters')

print('Got {} records in total'.format(len(records)))
