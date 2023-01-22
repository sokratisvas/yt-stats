from bs4 import BeautifulSoup
import requests
import re
import json

def get_total_views() -> None:
    yt_channel = "https://www.youtube.com/@socrates4446"
    about_section = requests.get(yt_channel + "/about", cookies={"CONSENT": "YES+42"}).text
    with open("index.html", "w") as f:
        f.write(about_section)


    stats = re.findall(r"(?<=var ytInitialData = {)(.*)(?=};)", about_section)

    with open("stats.json", "w") as f:
        f.write(json.dumps(stats, indent=4))
    

    soup = BeautifulSoup(about_section, "html.parser")



    


if __name__ == "__main__":
    get_total_views()
