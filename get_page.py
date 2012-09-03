def get_page(url):
	try:
		import urllib2
		#import urllib
		return urllib2.urlopen(url).read()
		#return urllib.urlopen(url).read()
	except:
		return ""
