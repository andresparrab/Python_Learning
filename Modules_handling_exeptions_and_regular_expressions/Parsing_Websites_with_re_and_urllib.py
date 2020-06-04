import urllib.request
import urllib.parse
import re


url = 'https://pythonprogramming.net/search/?'
values = {'q':'basics'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

# print(respData)

'''
We going to use regular expression to parse all thi text and get paragraphs
the regular expression (.*?) is . any character * 0or more repetitions ? is match 0 ormore repetition
(.*?) is a very good regular expression remember that
'''
paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

for eachP in paragraphs:
    print(eachP)