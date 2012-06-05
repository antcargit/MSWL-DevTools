#!/usr/bin/python
# ====== NAME ======
#    __init__.py
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

import argparse
from Crawler import Crawler

def start():
  parser=argparse.ArgumentParser(description="")
  parser.add_argument("-n","--number-of-levels",type=int,default=1,help="")
  parser.add_argument("url",nargs=1,help="target URL")

  args=parser.parse_args()
  target_url=args.url.pop()
  deep=args.number_of_levels

  mycrawler=Crawler()
  currentDeep=1
  mycrawler.startCrawler(target_url,currentDeep,deep)
