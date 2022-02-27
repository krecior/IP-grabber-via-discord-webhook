import requests

url = "https://api.ipify.org/?format=json"
res = requests.get(url)

webhook = "your webhook url here"

data = {
    "content" : res,
    #"avatar_url": "", Leave blank if you dont want avatar in your webhook.
    "username" : "Webhook"
}

r = requests.post(webhook, data=data )
