#!/usr/bin/python3

###########
#
# Given a TW stock num, return instant stock info
#
###########

import urllib.request
import ssl
import json
import sys

if (len(sys.argv) < 2):
    print('Invalid input')
    sys.exit(1)

num = sys.argv[1]
ss = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_" + num + ".tw"

ssl._create_default_https_context = ssl._create_unverified_context
o = urllib.request.urlopen(ss)
js = json.loads(o.read())

####
# JSON key mapping
# v -> volumn accumulation
# o -> open
# y -> yesterday price
# l -> lowest
# h -> highest
# z -> 
# tv -> 
####

#print(json.dumps(js, sort_keys=True, indent=4))

try :
    dictInfo = js["msgArray"][0]
    #print(dictInfo)
    print(f'Volunm {dictInfo["v"]}')
    print(f'Open {dictInfo["o"]}')
    print(f'High {dictInfo["h"]}')
    print(f'Low {dictInfo["l"]}')
    print(f'Current {dictInfo["z"]}')
    print(f'Yesterday {dictInfo["y"]}')
    
    print(f'Increase {((float(dictInfo["z"])-float(dictInfo["y"]))/float(dictInfo["y"])*100)}%')

except:
    print('Invalid num ', num)
