from core import html

class web:

    html_pages = {}

    def __init__(self):
        self.html_pages = html.html()._get_html_pages()
    #end def

# end class
