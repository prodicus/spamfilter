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

pickle:
	python create_pickle.py

clean:
	-find /home/tasdik/Dropbox/projects/spamfilter -iname "*.pyc" \
	-exec rm "{}" \;

	# cleaning the saved classifiers if any found
	-rm saved_classifiers/spam_classifier.pickle \
        saved_classifiers/trainer.pickle

	# cleaning the log files
	-rm logfiles/logfile.txt

.PHONY: help
help:
	@echo "\nPlease call with one of these targets:\n"
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F:\
        '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}'\
        | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs | tr ' ' '\n' | awk\
        '{print "    - "$$0}'
	@echo "\n"
