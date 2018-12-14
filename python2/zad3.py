import xml.sax
import sys
read1 = sys.argv[1]
write1 = sys.argv[2]
class SaxHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.CurrentData = ""
		self.to = ""
		self.froms = ""
		self.heading = ""
		self.body = ""		
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "note":
			print("Note")
	def endElement(self,tag):
		if self.CurrentData == "to":
			print("To:", self.to)
		elif self.CurrentData == "froms":
			print("From:", self.froms)
		elif self.CurrentData == "heading":
			print("Heading:", self.heading)
		elif self.CurrentData == "body":
			print("Body:", self.body)
		self.CurrentData = ""
	def characters(self, content):
		if self.CurrentData == "to":
			self.to = content
		elif self.CurrentData == "froms":
			self.froms = content
		elif self.CurrentData == "heading":
			self.heading = content
		elif self.CurrentData == "body":
			self.body = "changed message"
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
Handler = SaxHandler()
parser.setContentHandler(Handler)
parser.parse(read1)





