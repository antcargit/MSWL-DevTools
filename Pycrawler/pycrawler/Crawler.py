#!/usr/bin/python
# ====== NAME ======
#    Crawler.py
# ===LICENSE===
#    Copyright (c) 2012 Antonio Carmona. All rights reserved.
#
#    This file is part of crawler
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ====== LAST MODIFICATIONS ======
#     29/05/2012: Creacion Antonio Carmona
# ================================
import urllib2
import re
import sys
from BeautifulSoup import BeautifulSoup as Soup
from urlparse import urlparse

class Crawler:
 def __init__(self): 
   self.user_agent = "Mozilla/5.0 (X11; U; Linux x86_64; es-ES; rv:1.9.1.15) Gecko/20101028 Iceweasel/3.5.15 (like Firefox/3.5.15)"
        
 def startCrawler(self,target_url,currentDeep,maxDeep):    
   raw_code=""
   try:
      opener= urllib2.build_opener()
      opener.addheaders = [('User-agent', self.user_agent)]
      raw_code=opener.open(target_url).read()
   except Exception, e:
      print "No se puede abrir: " + target_url + " Error: " + str(e)
   soup_code=Soup(raw_code)
   links=[link['href'] for link
                    in soup_code.findAll('a')
                    if link.has_key('href')]
   if currentDeep==1:
      print ("Root: " + target_url).encode('utf8')
   if maxDeep==0:
      sys.exit()
   for line in links:
        isLink=0      
        p=re.compile('^(http:)')  
        if p.match(line):
            isLink=1     
        else:  ## Es un enlace a pagina local
            locallinks=re.compile('^\#(\S)*')
            if not locallinks.match(line):
                baseUrl=urlparse(target_url)
                line="http://"+baseUrl.netloc +"/"+ line
                isLink=1                                               
        if isLink==1:
           for i in range(0,currentDeep): print "*",
           print (": " + line).encode('utf8')
           if currentDeep<maxDeep:
               target_url=line
               Crawler.startCrawler(self,line,currentDeep+1,maxDeep)

