import json
import datetime
import os
import re
import requests


links = []
f = open("cookies.txt","r")
c = f.read().strip("\n")
print(c)
f.close()

with open("messages.json",encoding="utf8") as f:
    data = json.load(f)
    conversations = data["conversations"]
   
    for a in conversations:
        for x in a["MessageList"]:
            if "url_thumbnail" in x["content"]:
                s = x["content"]

                result = re.search(r'url_thumbnail=\"(.*?)\"', s).group(1)
                split = result.split("/")
                split[-1] = "imgpsh_fullsize_anim"
                file_name = split[5]
                filepath = os.path.join(os.getcwd(), "images", file_name+".jfif")
                fullstr = ""
                for items in split:
                    fullstr = fullstr + items + "/"
                links.append(fullstr)
                url = fullstr
                try:
                    cookies = dict(skypetoken_asm=c)
                    response = requests.get(url, cookies=cookies)
                    if response.status_code == 200:
                        with open(filepath, 'wb') as f:
                            f.write(response.content)
                except:
                    pass
                    

with open("links.txt", "w") as f:
    for x in links:
        f.write(f"{x}\n")
