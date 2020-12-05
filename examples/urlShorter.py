# pip install pyshorteners
import pyshorteners 

url = input('Enter URL\n')
print('URL After Shortening : ' + pyshorteners.Shortener().tinyurl.short(url))