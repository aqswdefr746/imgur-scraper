import sys
import os
import random
import requests


logo = '''
  _____                               _____                                
 |_   _|                            / ____|                               
   | |  _ __ ___   __ _ _   _ _ __ | (___   ___ _ __ __ _ _ __   ___ _ __ 
   | | | '_ ` _ \ / _` | | | | '__| \___ \ / __| '__/ _` | '_ \ / _ \ '__|
  _| |_| | | | | | (_| | |_| | |    ____) | (__| | | (_| | |_) |  __/ |   
 |_____|_| |_| |_|\__, |\__,_|_|   |_____/ \___|_|  \__,_| .__/ \___|_|   
                   __/ |                                 | |              
                  |___/                                  |_|              
'''
disclaimer = '''
                            Author: aqswdefr746
                               Version: 0.3
############################### DISCLAIMER ################################
| All images are publicly available and are public. The parser simply     |
| generates random links and, if the image exists, downloads it.          |                             
###########################################################################
'''
print(logo)
print(disclaimer)
print('email for bug reports : gthyjuki786@gmail.com')
print('GitHub : github.com/aqswdefr746')
print('Images will be download to /imgur-img')
print('Yes, it`s work. Just wait...')
str1 = ('abcdefghijklmnopqrstuvwxyz')
str2 = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
str3 = ('1234567890')
str4 = str1 + str2 + str3
ls = list(str4)
#
#
VALID_PATH = "images"
if not os.path.exists(VALID_PATH):
    os.mkdir(VALID_PATH)
while True:
    try:
        random.shuffle(ls)
        img = ''.join([random.choice(ls) for x in range(5)])
        url = 'https://' + 'imgur.com' + '/' + img
        urrl = 'https://' + 'i.imgur.com' + '/' + img + '.png'
        response = requests.head(url)
        response.raise_for_status()
        print(url,'is working')
        if response.status_code == 200:
            r = requests.get(urrl, stream=True)  # stream for partial download
            with open(os.path.join(VALID_PATH, img)+".png", 'bw') as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)
        pass
    except requests.exceptions.HTTPError as err:
        print(url, 'is not working')
        pass
