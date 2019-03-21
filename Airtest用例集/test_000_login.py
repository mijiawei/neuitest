# -*- encoding=utf8 -*-
__author__ = "mijiawei"
from util import img
from airtest.core.api import *
def runCase(self,vars):

    start_app("com.glow.patient.debug")
    touch(Template(img("tpl1553138614895")))

    text("zxcvbnm@qatest.com")
    touch(Template(img("tpl1553138700598")))

    touch(Template(img("tpl1553138712470")))
    text("zxcvbnm")
    touch(Template(img("tpl1553138700598")))


