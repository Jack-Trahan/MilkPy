# -*- coding: utf-8 -*-
"""
A script used to download and configure an image for use as a Sprite in WinAmp's MilkDrop

Usage (command line):
    python [PATH to milkPy.py] [Image Url] [Name for Image]

Example:
    python "/Users/Jack/Documents/Python Scripts/WinamPy/milkPy.py" https://thumbs.dreamstime.com/b/illustration-human-head-energy-waves-subject-powers-mind-mind-energy-109105181.jpg Mind

"""
import urllib.request
import re
from sys import argv


spriteConfigPath = "/Users/Jack/Documents/Python Scripts/WinamPy/output.txt"
spriteImageFolder = "/Users/Jack/Documents/Python Scripts/WinamPy/Images/"
spriteName = argv[2]+argv[1][-4:]   # Second command line arg plus image file extension




def downloadImg(url=argv[1]):
    # Download the image from the url specified in argument 1
    writePath = spriteImageFolder + spriteName
    # Download the image
    print("Downloading the image...")
    urllib.request.urlretrieve(url, writePath)
    print("Success!")



def assignSpriteNumber():
    # asssign a MilkDrop sprite reference number to image

    # First open and search configFile for the last img number:
    pattern = re.compile("\[img(\d\d)\]")

    try:
        with open(spriteConfigPath, 'r') as f:
            configText = f.read()
        lastNum = re.findall(pattern, configText)[-1]

        newNum = str(int(lastNum) + 1)
        if len(newNum) == 1:
            newNum = '0' + newNum
    except FileNotFoundError:
        newNum = '01'

    return newNum

def writeConfig():
    # Write the entry for the MilkDrop Sprite config file.
    spriteNum = assignSpriteNumber()

    configText = f"""[img{spriteNum}]
img=textures\{spriteName}
init_1=blendmode = 3;
init_2=x = 1;
init_3=orig_y = 0.5;
code_1=time_to_reset = below(x,-0.5);
code_2=x = x*(1-time_to_reset) + time_to_reset*(1.5 + 0.01*rand(100) + 1);
code_3=orig_y = orig_y*(1-time_to_reset) + time_to_reset*(0.3 + 0.4*0.01*rand(100));
code_4=sx = sx*(1-time_to_reset) + time_to_reset*(0.25 + 0.4*0.01*rand(100));
code_5=sy = sx;
code_6=x = x - 0.008 + 0.0033*sin(time*1.371);
code_7=y = orig_y + 0.12*sin(time*1.9);
code_8=done=above(frame,80);
code_9=burn=done;
"""



    with open(spriteConfigPath, 'a') as f:
        print(configText, file=f)



def main():
    downloadImg()
    writeConfig()


if __name__ == "__main__":
    main()
