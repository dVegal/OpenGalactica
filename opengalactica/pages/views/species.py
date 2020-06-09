# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.views import View

from pages.views import BaseView

class species(View, BaseView):
    def call(self, request, *args, **kwargs):
        initial = {}
        return render(request,"species.html", self.data)
