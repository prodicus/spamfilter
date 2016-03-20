# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-12
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-15
# @MIT License
# @http://tasdikrahman.me
# @https://github.com/prodicus

run:
	python test.py

clean:
	find /home/tasdik/Dropbox/projects/spamfilter -iname "*.pyc" \
	-exec rm "{}" \;
	-exec rm logfile.txt;