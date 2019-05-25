from mako.template import Template

class home:

	def __init__(self):
 		pass
	#end def

	def html(self, params):

		html_page = params['html']
		tulisan1 = params['tulisan1']
		tulisan2 = params['tulisan2']

		return Template(html_page).render(
            tulisan1=tulisan1,
            tulisan2=tulisan2
        )
	# end def

#end class
