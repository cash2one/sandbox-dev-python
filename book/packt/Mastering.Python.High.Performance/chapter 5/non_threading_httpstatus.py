import urllib2


sites = [
	"http://www.google.com",
	"http://www.bing.com",
	"http://stackoverflow.com",
	"http://facebook.com",
	"http://twitter.com"
]

def check_http_status(url):
	return urllib2.urlopen(url).getcode()

http_status = {}
for url in sites:
	http_status[url] = check_http_status(url)

for  url in http_status:
	print "%s: %s" % (url, http_status[url])

