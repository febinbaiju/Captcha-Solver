import requests
import os
from cutimages import image_crop

folder = "images/"

if os.path.exists(folder)==False:
    os.mkdir(folder)

url = "http://www.afreesms.com/image.php?o=3726129114027745300"

iterations = 1

while iterations<=100:
    #break #remove for actual running
    access = requests.get(url,stream=True)
    fullpath = folder+"image{0}.png".format(str(iterations))
    with open(fullpath,"wb") as handle:
        handle.write(access.content)
    print("Path"+fullpath)
    image_crop(fullpath,"cut/")
    iterations += 1
