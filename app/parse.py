import requests
import bs4
from lxml import etree, html
import urllib2


cities = {'Arlington, VA': 'http://parks.arlingtonva.us/rentals/basketball-courts/'}

response = requests.get(cities['Arlington, VA'])

tree = html.fromstring(response.text)
ltree = etree.HTML(cities['Arlington, VA'])
lists = tree.findall(".//ul")

outdoor = tree.xpath('//div[@class="text-field-gizmo gizmo position-0 third"]//div//ul//li//a')
outdoor_courts = []
for i in outdoor:
	if "Court" not in i.text_content():

		outdoor_courts.append((i.text_content(), i.attrib['href']))
		#print(i.text_content(), outdoor_courts[i.text_content()])
	
indoor = tree.xpath('//div[@class="text-field-gizmo gizmo position-1"]//ul//li//a')
indoor_courts = []

for i in indoor:
	if "Court" not in i.text_content():

		indoor_courts.append((i.text_content(), i.attrib['href']))
		#print(i.text_content(), indoor_courts[i.text_content()])

