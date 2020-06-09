# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.views import View

from pages.views import BaseView

class history(View, BaseView):
    def call(self, request, *args, **kwargs):
        initial = {}
        return render(request,"history.html", self.data)
