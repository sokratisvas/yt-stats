from bs4 import BeautifulSoup
import re
import json
import requests

API_KEY = None
USER_ID = None

channel_url = "https://www.youtube.com/@" + USER_ID
soup = BeautifulSoup(requests.get(channel_url, cookies={'CONSENT': 'YES+42'}).text, 'lxml')
data = re.search(r"var ytInitialData = ({.*});", str(soup.prettify())).group(1)
json_data = json.loads(data)

with open("stats.json", "w") as f:
    f.write(json.dumps(json_data, indent=4))

EXTERNAL_ID = json_data["metadata"]["channelMetadataRenderer"]["externalId"]
channel_name = json_data["metadata"]["channelMetadataRenderer"]["title"]

url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={EXTERNAL_ID}&key={API_KEY}'
json_url = requests.get(url)
data = json.loads(json_url.text)
try:
    data = data["items"][0]["statistics"]
except:
    data = None

with open(f"{USER_ID}-stats.json", "w") as f:
    f.write(json.dumps(data, indent=4))

print(f'Channel Name:    {channel_name}')
print(f'Subscribers:     {data["subscriberCount"]}')
print(f'Total Views:     {data["viewCount"]}')
print(f'Total Videos:    {data["videoCount"]}')
