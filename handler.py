from core   import web
from config import directory
from config import server

from modules import home
from modules import select_sample

class handler(web.web):

    def __init__(self):
        web.web.__init__(self)

    def index(self, **kwargs):
        kwargs["tulisan1"] = server.FirstName
        kwargs["tulisan2"] = server.LastName
        kwargs["html"] = self.html_pages["index.html"]
        return home.home().html(kwargs)
    index.exposed = True

    def select(self, **kwargs):
        kwargs["html"] = self.html_pages["select_sample.html"]
        return select_sample.select_sample().html(kwargs)
    select.exposed = True

    class sample:

        def __init__(self):
            web.web.__init__(self)

        def routes(**kwargs):
            return "This is routes"
        routes.exposed = True

        def select(self):
            kwargs["html"] = self.html_pages["select_sample.html"]
            return select_sample.select_sample().html(kwargs)
        select.exposed = True

    # End class sample
