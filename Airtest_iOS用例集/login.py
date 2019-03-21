# -*- encoding=utf8 -*-
__author__ = "mijiawei"

from airtest.core.api import *
from poco.drivers.ios import iosPoco
from util import img

def runCase(self,vars):
    poco = iosPoco()
    poco("Patient Beta").click()
    touch(Template(img("tpl1553160183364")))
    text("zxcvbnm@qatest.com")
    touch(Template(img("tpl1553160262626")))

    touch(Template(img("tpl1553160280476")))
    text("zxcvbnm")
    touch(Template(img("tpl1553160262626")))

    sleep(3)

    assert_exists(Template(img("tpl1553160329233")), "should display tool bar")

