#!/usr/bin/env python
#
# Copyright (c) 2012, Yahoo! Inc.  All rights reserved.
# Copyrights licensed under the New BSD License. See the accompanying LICENSE file for terms.
#

import logging

#
# Logger class to be used in all modules
#
class Logger:

    def __init__(self, tag):
        self._l = logging.getLogger(tag)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(levelname)s [' + tag + '] %(message)s')
        handler.setFormatter(formatter)
        self._l.addHandler(handler)
        self._l.setLevel(logging.DEBUG)

    def get(self):
        return self._l
