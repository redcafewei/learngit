from xml.sax.handler import ContentHandler
from xml.sax import parse

class PageMaker(ContentHandler):
	passthrough = False
	def startElement(self,name,attrs):
		if name == 'httpSample':
			self.passthrough = True
			self.out = open(attrs['tn']+'.html','w')
			self.out.write('<html><head>\n')
			self.out.write('<title>%s</title>\n' % attrs['tn'])
			self.out.write('</head><body>\n')
		elif self.passthrough:
			self.out.write('<'+name)
			for key,val in attrs.items():
				self.out.write('%s = %s' % (key,val))
			self.out.write('>')
			
	def endElement(self,name):
		if name == 'httpSample':
			self.passthrough = False
			self.out.write('\n</body></html>\n')
			self.out.close()
		elif self.passthrough:
			self.out.write('</%s>' % name)
	
	def characters(self,chars):
		if self.passthrough:self.out.write(chars)
		
parse('result.xml',PageMaker())
