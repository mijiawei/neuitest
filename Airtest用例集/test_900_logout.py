# -*- encoding=utf8 -*-
__author__ = "mijiawei"
from airtest.core.api import *
from util import img

def runCase(self,vars):

    sleep(3)
    assert_exists(Template(img("tpl1552968891231")))

    touch(Template(img("tpl1553147221601")))
    touch(Template(img("tpl1553147239778")))
    touch(Template(img("tpl1553147255115")))
    sleep(3)
    touch(Template(img("tpl1553147265150")))

