import urllib2
import urllib



class HtmlDownloader(object):
     def download(self,url):
         if url is None:
             return None
         response = urllib2.urlopen(url)
         if response.getCode()!=200:
             return None
         else:
             return response.read()