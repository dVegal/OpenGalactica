# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.views import View

from pages.views import BaseView

class main(View, BaseView):
    def call(self, request, *args, **kwargs):
        initial = {}
        return render(request,"main.html", self.data)
