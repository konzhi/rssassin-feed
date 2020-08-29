from bs4 import BeautifulSoup
from django.http import HttpResponse
import xml.etree.ElementTree as ET
import requests

CONFIG = {
    'url': 'https://www.calvertjournal.com/',
    'title': 'Calvert Journal'
}

# Create your views here.
def index(request: HttpResponse):

    # res = requests.get(SITE_URL)
    bs = fetch_page()
    rss = ET.Element("rss")
    rss.set("version", "2.0")

    channel = build_channel(rss, bs)
    build_items(channel, bs)

    return HttpResponse(ET.tostring(rss), content_type='application/rss+xml')


def build_items(channel: ET.SubElement, bs: BeautifulSoup):
    divs = list(filter(
        lambda d: d.has_attr('class') and ('entry-thumbnail' in d['class'] or 'hero-entry-thumbnail' in d['class']),
        bs.find_all('div')
    ))

    for div in divs:
        a = div.find('a', {'class': 'entry-link'})
        h4 = div.find('h4', {'class': 'description-text'})
        build_item(channel, a['href'], h4.text.strip())


def build_item(channel: ET.SubElement, link: str, description: str):
    i = ET.SubElement(channel, 'item')
    t = ET.SubElement(i, 'title')
    t.text = description
    d = ET.SubElement(i, 'description')
    d.text = description
    l = ET.SubElement(i, 'link')
    l.text = link
    g = ET.SubElement(i, 'guid')
    g.text = link


def build_channel(rss: ET.Element, bs) -> ET.SubElement:
    channel = ET.SubElement(rss, 'channel')

    title = ET.SubElement(channel, 'title')
    title.text = CONFIG['title']

    description = ET.SubElement(channel, 'description')
    description.text = bs.html.head.title.text

    link = ET.SubElement(channel, 'link')
    link.text = CONFIG['url']
    return channel


def fetch_page():
    res = requests.get(CONFIG['url'])
    return BeautifulSoup(res.text, 'html.parser')