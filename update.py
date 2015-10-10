import json
import requests


RAW = 'https://raw.githubusercontent.com/'

if __name__ == "__main__":
	f = open ('list.json', 'r')
	d = json.loads (f.read ())
	f.close ()

	for dapp in d['dapps']:
		rawurl = dapp['source'].split ('/')
		rawurl = RAW + rawurl[-2] + '/' + rawurl[-1] + '/master/manifest.json'
		r = requests.get (rawurl)
		dappj = json.loads (r.text)
		print ('Parsing', dappj['name'])
		dapp['name'] = dappj['name']
		dapp['description'] = dappj['description']
	f = open ('list.json', 'w')
	f.write (json.dumps (d, indent=4, separators=(',', ': ')))
	f.close ()