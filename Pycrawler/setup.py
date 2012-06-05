#!/usr/bin/python
# ====== NAME ======
#    setup.py
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
#    29/05/2012: Creacion Antonio Carmona
# ================================

from setuptools import setup , find_packages
setup ( name = " crawler " ,
        version = " 1.0 " ,
        packages = find_packages () ,        
        scripts = [ 'crawler.py'] ,
        install_requires = [ 'BeatifulSoup','argparse'] ,
        package_data = { 'pycrawler ': [ '' ] , } ,
        author = "Antonio Carmona" ,
        description = "MSWL-DT exercise" ,
        license = "GPLv3" ,
        keywords = " " ,
        url = " " ,
        long_description = "MSWL-DT exercise" ,
        download_url = " " , )
