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
from .intro import *
from .dictionary import *
from .enciklopedia import *
from .history import *
from .impressum import *
from .jobs import *
from .logout import *
from .main import *
from .news import *
from .registration import *
from .rules import *
from .xtendlogin import *
from .screens import *
from .ships import *
from .species import *
from .terms import *
from .universe import *