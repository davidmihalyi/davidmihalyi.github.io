import urllib.request as hivjadmeg
import json
url='http://resourceprojects.org/api/countries/400/0'
r=hivjadmeg.urlopen(url)
data=r.read()
encoding = r.info().get_content_charset('utf-8')
jsonresult=json.loads(data.decode(encoding))
with open('resourceproject.json', 'w') as outfile:
	json.dump(jsonresult, outfile, indent=4)
