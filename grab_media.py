import json
import datetime
import os
import re
import requests
from PIL import Image
import glob

links = []
c = ""
try:
    f = open("cookies.txt","r")
    arr = f.readlines()
    c = re.search(r'skypetoken_asm=(.*?)\n', arr[-1]).group(1)
    f.close()
except:
    pass
print(c)

with open("messages.json",encoding="utf8") as f:
    data = json.load(f)
    conversations = data["conversations"]
   
    for a in conversations:
        for x in a["MessageList"]:
            if "url_thumbnail" in x["content"]:
                s = x["content"]
                ts = datetime.datetime.fromtimestamp(int(x["version"]/1000)).strftime('%Y-%m-%d_%H-%M-%S')
                
                result = re.search(r'url_thumbnail=\"(.*?)\"', s).group(1)
                split = result.split("/")
                split[-1] = "imgpsh_fullsize_anim"
                file_name = ts + "_" + split[5]
                filepath = os.path.join(os.getcwd(), "images", file_name+".jfif")
                fullstr = ""
                for items in split:
                    fullstr = fullstr + items + "/"
                links.append(fullstr)
                url = fullstr
                try:
                    if not os.path.isfile(filepath):
                        cookies = dict(skypetoken_asm=c)
                        response = requests.get(url, cookies=cookies)
                        if response.status_code == 200:
                            with open(filepath, 'wb') as write_file:
                                write_file.write(response.content)
                                im = Image.open(filepath)
                                rgb_im = im.convert('RGB')
                                rgb_im.save(filepath.replace("jfif", "jpg"))
                            os.remove(filepath)
                        else:
                            print(f"{response.status_code} {url}")

                except:
                    pass
                    

with open("links.txt", "w") as f:
    for x in links:
        f.write(f"{x}\n")
