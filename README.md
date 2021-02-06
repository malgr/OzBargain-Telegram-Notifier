# OzBargain-Telegram-Notifier
Get notified by deals containing user defined keywords using Telegram's Bot API.

## How to create a Telegram bot?
1. Message [@botfather](https://t.me/botfather) on Telegram and follow the steps [here](https://core.telegram.org/bots#6-botfather). 
2. Take note of your bot's `token`.
3. Send a message to your bot then go to the url below replacing `<BOT_TOKEN>` with your bot's token.

        https://api.telegram.org/bot<BOT_TOKEN>/getUpdates

4. Look at the result and note the from/chat `id`.

## Example credentials<span>.</span>py
Create a credentials<span>.</span>py in the same folder as main<span>.</span>py:

    bot_token = "YOUR BOT TOKEN"
    receiver_id = "YOUR USER ID"

## Example deals.json and keywords.json
`deals.json` is a list of ids of ozbargain deals that match keywords in `keywords.json`. 

deals.json should start out empty while keywords.json should be populated with your search keywords:
    
    ["Amazon", "Eneloop", "Woolworths", "Coles"]

## TODO
* Add command handlers to be able to respond to `/addkeywords`, `/removekeywords` and `/showkeywords` within Telegram removing the need to edit keywords.json manually.
