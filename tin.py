"""
+-----+
| tin |
+-----+
Cook your muffins on here

"""

# core modules
from core import config
from core import directory

from modules import home
from modules import select_sample

class tin(config.web):

    def __init__(self):
        config.web.__init__(self)

    def index(self, **kwargs):

        kwargs["tulisan1"] = "your"
        kwargs["tulisan2"] = "Name"
        kwargs["html"] = self.html_pages["index.html"]
        html_page = home.home().html(kwargs)
        return html_page

    index.exposed = True

    def sample(self, **kwargs):

        kwargs["html"] = self.html_pages["select_sample.html"]
        html_page = select_sample.select_sample().html(kwargs)
        return html_page

    sample.exposed = True
