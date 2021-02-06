import feedparser
import requests
import re
import json
import time
import credentials


# Check if deal contains the keywords
def match_keyword(dealbody):
    match = False
    for keyword in keywords:
        if keyword.lower() in dealbody.lower():
            match = True
    return match


# Save the new bargain into the list
def update_deals(deal_id):
    if len(deal_list) == 30:
        deal_list.pop(0)
    deal_list.append(deal_id)
    with open('deals.json', 'w') as fout:
        json.dump(deal_list, fout)


# Parse the feed
def get_feed(feed):
    d = feedparser.parse(feed)
    for entry in d['entries']:
        title = entry['title']
        link = entry['link']
        summary = entry['summary']
        deal_id = re.search(r'\d+', entry['id']).group()
        if match_keyword(title + summary) and (deal_id not in deal_list):
            # send a deal only once
            update_deals(deal_id)
            # send a telegram message
            bot_send_message(credentials.bot_token,
                             credentials.receiver_id,
                             title + '\n' + link)


# Send a message using Telegram's Bot API
def bot_send_message(bot_token, receiver_id, message):
    payload = {'chat_id': receiver_id,
               'parse_mode': 'Markdown',
               'text': message}
    requests.get('https://api.telegram.org/bot' +
                 bot_token +
                 '/sendMessage',
                 params=payload)


if __name__ == "__main__":
    rss_feed = 'https://www.ozbargain.com.au/deals/feed/'
    with open('deals.json', 'r') as f:
        deal_list = json.load(f)
    with open('keywords.json', 'r') as f:
        keywords = json.load(f)

    while True:
        get_feed(rss_feed)
        time.sleep(15*60)  # Change this to run every x minutes
