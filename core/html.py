import  sys
import  os
from    config import directory

class html:

    html_dict = {}

    def __init__(self):
        pass
    #end def

    def _get_html_pages(self):
        html_page_list  = os.listdir( directory.html )
        for html_page in html_page_list:
            full_path   = directory.html + "/" + html_page
            html_handle = open( full_path , 'r' )
            html_raw    = html_handle.read()
            self.html_dict[html_page] = html_raw
        #end for
        return self.html_dict
    #end def

#end class
