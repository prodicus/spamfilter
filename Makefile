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

pickle_run:
	python test_classifier_pickle.py

pickle:
	python create_pickle.py

clean:
	-find . -name '*.pyc' -delete
	-find . -name '__pycache__' -delete

.PHONY: help
help:
	@echo "\nPlease call with one of these targets:\n"
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F:\
        '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}'\
        | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs | tr ' ' '\n' | awk\
        '{print "    - "$$0}'
	@echo "\n"
