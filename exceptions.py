# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-14
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-03-14
# @MIT License
# @http://tasdikrahman.me
# @https://github.com/prodicus

# defining some custom exceptions here

class TrainingException(Exception):
    pass

class UnicodeError(TrainingException):
    pass