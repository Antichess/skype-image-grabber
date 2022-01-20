# Skype Image Grabber
Using your messages.json only, grab all your skype images and download them with cookies!

### What is this?
This python script reads through your skype `messages.json`, a file that contains a json of all your messages that you've ever sent and recieved in Skype, including conversations. However, images are only shown as a link, and even then are annoying to access. Using a browser cookie generated from a [Skype Web](https://web.skype.com/) login, you can extract your session cookie and use that with Python requests.

### Why the need for the script?
* Built in `.jfif` to `.jpg` converter
* Skype won't allow you to access your own images without a cookie
* I don't want to download hundreds of images manually

# Prerequisites
### Python
In order to run the scripts and load the data, you must have a version of **Python 3.6+.** This is because of requests, which will be explained in the next step. You can quickly download Python from [python.org](https://www.python.org/). Not sure? Download the latest version, and it should work. Make sure you install pip as well.

*Note: This script was written in Python 3.7.*

### Requests
[Python requests](https://pypi.org/project/requests/) are required in order to request from the Skype API server. If you don't have Skype API, open up `cmd` and put the following command to install Python requests:
```
$ python -m pip install requests
```
Make sure you are in a version that is at least **Python 3.6** in order for requests to work.

# Usage
### Getting your Skype data
Now it's time to get to the fun part, actually executing this script. First, go over to the [Skype Export Tool](https://secure.skype.com/en/data-export) and request a copy of your **conversations and files.** Make sure you have the files selected, otherwise you will have to make another request. Personally, the request took me around 20 minutes to arrive, so be patient and sit tight. 

After recieving your `.tar` file, use an unzipping service to extract the `messages.json` from it. 

If you want to understand more of your data, you may use the [Skype Parser](https://go.skype.com/skype-parser) to see chat logs in a readable format.

### Organizing the folder

Organize a new folder that is like the repository shown above.
```
📁    skype-image-grabber
    📁    Images    
    ⌞     cookies.txt    
    ⌞     grab_media.py
    ⌞     messages.json
```
In the cookies.txt folder, you need to get a session of your cookies from an api.asm.skype.com request. Go ahead and run the script **with the messages.json** in the folder. You do not need to worry about the cookies.txt file yet, if you have not put it in there. Go ahead and copy any link starting with **api.asm.skype.com** from the shell, and paste it in your browser. If you have logged in correctly in the past, you should not have to worry about signing in. 

After copying and accessing a link, go ahead and inspect the page. In the network tab, reload your network activity and you should see `imgpsh_fullsize_anim`. Right click that, and copy `Copy request headers`. If you are a Chrome user, an image is provided below.

![image](https://raw.githubusercontent.com/Antichess/skype-image-grabber/main/images/network_inspect.png)
