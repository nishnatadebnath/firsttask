# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 05:37:28 2019

@author: NISHNATA
"""

from bs4 import BeautifulSoup
infile = open("Task.xml","r")
soup = BeautifulSoup(infile,'xml')
p_name=input()
frame=input()
page_find=soup.find("Page",{"name":p_name})
frame_find=page_find.find("step",{"frame":frame})
s=""+frame_find["pose"]+" "
p=""
for x in range(len(s)):
    if(s[x]!=' '):
        p=p+s[x]
    else:
        print(p)
        p=""
        
        
    
