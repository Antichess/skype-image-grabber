import json
import os
from PIL import Image
import glob

for file in glob.glob("*.jfif"):
     im = Image.open(file)
     rgb_im = im.convert('RGB')
     rgb_im.save(file.replace("jfif", "jpeg"), quality=95)
