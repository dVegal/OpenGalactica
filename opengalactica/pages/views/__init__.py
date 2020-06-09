class BaseView():
    data = {}

    def get_news(self):
        pass
#        self.data["news"] = Blog.objects.filter(schelude=None).order_by("-timestamp")[:10]
#        self.data["subscription_form"] = SubscriptionForm({})

    def post(self, request, *args, **kwargs):
        self.get_news()
        return self.call(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.get_news()
        return self.call(request, *args, **kwargs)

from .home import *
