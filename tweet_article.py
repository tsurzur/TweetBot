#!/usr/bin/env python
# coding: utf-8

import sys
import os
import random
import xml_parser
from twython import Twython

if __name__ == "__main__":
    param = sys.argv

    # twitterの認証情報を入力
    CONSUMER_KEY = "*****"
    CONSUMER_SECRET = "*****"
    ACCESS_KEY = "*****"
    ACCESS_SECRET = "*****"
    api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

    # comment文
    list_comment = []
    list_comment.append("私のブログからの記事をピックアップ！ ")
    list_comment.append("こんな記事どう？ ")
    list_comment.append("ラズパイ君がブログから選んでくれた記事 -> ")
    list_comment.append("こういう記事いかがでしょう？ ")
    list_comment.append("RaspberryPi2からbotで記事を選んでみました。 ")
    list_comment.append("こんなの書いてたなぁ ")
    list_comment.append("私のブログから記事を一つチョイス！ ")
    list_comment.append("昔の記事からオススメをチョイス！")
    list_comment.append("今日のおすすめ記事 -> ")
    list_comment.append("こんな記事いかがでしょう？")
    list_comment.append("ラズパイ君の今日のセレクト記事")
    list_comment.append("〜過去の記事から〜")
    list_comment.append("〜ブログ記事紹介〜")
    list_comment.append("昔の自分の考えを思い出すなぁ")
    list_comment.append("こんな記事もあったな")

    # Tweet [num] times per day about article(get_article) in [url]
    url = param[1]
    num_tweet = int(param[2])
    probability = random.randint(1,54)
    if probability <= num_tweet:
        num_comment = random.randint(1,len(list_comment))
        api.update_status(status = list_comment[num_comment-1] + xml_parser.get_article(url))
        #print list_comment[num_comment-1] + xml_parser.get_article(url)
