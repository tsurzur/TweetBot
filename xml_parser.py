#!/usr/bin/env python
# coding: utf-8
 
from xml.dom import minidom
import random
import urllib2

def get_article(url):
    # list for blog articles
    list_article = []
    list_xml = []

    # sitemap.xmlを取得する
    #wget.download(url+"/sitemap.xml")
    sitemap_xml = urllib2.urlopen(url+"/sitemap.xml").read()
    # sitemap.xmlを読み込む
    file_xml = minidom.parseString(sitemap_xml)
    # sitemap.xmlの中から<loc>をすべて取得する(sitemapの全ページを取得する)
    pages_xmls = file_xml.getElementsByTagName("loc")

    # sitemapの全ページから、全記事を取得する
    for i, page in enumerate(pages_xmls) :
        # ページごとのxmlを取得する
        sitemap_xml = urllib2.urlopen(page.childNodes[0].data).read()
        # ページごとのxmlを読み込む
        file_xml = minidom.parseString(sitemap_xml)
        # xml内の全記事のurlを取得する)
        pages_xml = file_xml.getElementsByTagName("loc")
        # 各記事をlist_articleに格納していく
        for j, article in enumerate(pages_xml) :
            list_article.append(article.childNodes[0].data)

    # list_articleの中からランダムに一つ選択
    return random.choice(list_article)

# debug
#print get_article("http://tsurzur.hatenablog.com")
