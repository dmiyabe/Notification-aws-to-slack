#coding: UTF-8

import random

import slackweb

WEBHOOK_URL = "https://hooks.slack.com/services/xxxxxxxxxxxxx"

CHA_WARDS = ["風邪ひくなよ", "風呂入れよ", "宿題やれよ", "歯磨けよ"]

def lambda_handler(event, context):
    slack = slackweb.Slack(url=WEBHOOK_URL)
    slack.notify(text=random.choice(CHA_WARDS), channel='#slack-channel')
