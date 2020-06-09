# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.views import View

from pages.views import BaseView

class xtendlogin(View, BaseView):
    def call(self, request, *args, **kwargs):
        initial = {}
        return render(request,"xtendlogin.html", self.data)
