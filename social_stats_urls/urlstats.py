#!/usr/bin/python
# Filename: urlstats.py
# Prithviraj M Billa
import requests
import json

def get_facebook_shares(url):
	f = requests.get('http://graph.facebook.com/?id=%s'%(url))
	if f.status_code == 200:
		stat = f.json()
		if 'error' in stat:
			return 0
		else:
			return stat['shares']
	else:
		return 0
def get_twitter_shares(url):
	f = requests.get("https://cdn.api.twitter.com/1/urls/count.json?url=%s"%(url))
	try:
		return f.json()['count']
	except Exception,e:
		return 0

def get_pinterest_shares(url):
	f = requests.get("http://api.pinterest.com/v1/urls/count.json?url=%s"%(url))
	try:
		js = f.text
		js = js[13:]
		js = js[:-1]
		return json.loads(js)['count']
	except Exception,e:
		return 0

def get_linkedin_shares(url):
	f = requests.get("http://www.linkedin.com/countserv/count/share?url=%s&format=json"%(url))
	try:
		return f.json()['count']
	except Exception,e:
		return 0

def get_stumbleupon_shares(url):
	 f = requests.get("http://www.stumbleupon.com/services/1.01/badge.getinfo?url=%s"%(url))
	 try:
	 	return (f.json())['result']['views']
	 except Exception,e:
	 	return 0
		
def get_googleplus_shares(url):
		f = requests.get("https://plusone.google.com/_/+1/fastbutton?url=%s"%(url))
		try:
			cont = f.content
			index = cont.find("window.__SSR")
			cont = cont[index+len("window.__SSR"):]
			cont = cont[7:]
			findspace = cont.find(".")
			cont = cont[:findspace]
			return int(cont)
		except Exception, e:
			return 0
