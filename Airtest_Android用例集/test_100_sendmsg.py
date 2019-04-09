# -*- encoding=utf8 -*-
__author__ = "mijiawei"

from airtest.core.api import *
from util import img

def runCase(self,vars):

    touch(Template(img("tpl1553153382411")))
    touch(Template(img("tpl1553153396677")))
    sleep(3)
    touch(Template(img("tpl1553153649925")))
    assert_exists(Template(img("tpl1553153435531")))

    touch(Template(img("tpl1553153473212")))
    text("test")
    touch(Template(img("tpl1553153513477")))
    sleep(5)
    assert_exists(Template(img("tpl1553153795486")))
    touch(Template(img("tpl1553153580927")))
