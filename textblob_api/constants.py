# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-04-10 22:20:06
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-10 22:30:59
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/prodicus

import os

PATH = os.path.abspath('.')
PARENT_DIR = os.path.dirname(PATH)
CLASSIFIER_FOLDER = os.path.join(PARENT_DIR, 'saved_classifiers')
TEXTBLOB_PICKLE_FILE = os.path.join(CLASSIFIER_FOLDER, 'textblob_api.pickle')