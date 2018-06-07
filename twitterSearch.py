# Display User Data using Python-Twitter Library

import twitter

consumer_key = 'WOAH'
consumer_secret = 'NOTHING'
access_token = 'TO SEE'
access_secret = 'HERE'
 

api = twitter.Api(consumer_key, consumer_secret, access_token, access_secret)

## search = api.GetSearch("mustang")
## for tweet in search:
##     print(tweet.id, tweet.text)

print("Bobby Patel's Last 5 Tweets")

words = api.GetUserTimeline(screen_name = "thebobbypatel", count = 5)
words = [i.AsDict() for i in words]
for words in words:
    print(words['text'])

print()
print("Elon Musk's Last 5 Tweets")

words = api.GetUserTimeline(screen_name = "elonmusk", count = 5)
words = [i.AsDict() for i in words]
for words in words:
    print(words['text'])

##Bobby Patel's Last 5 Tweets
##@krptxt I was trying to get a physics lab done but my lab partners were too hyped about the trade smh...
##@elonmusk When do we get the jet packs ‼️
##@elonmusk @ultralightbeam @elonmusk is doing his best to make things more boring. @boringcompany
##RT @ieatsleepfly: Embraer Aiming For Flying Uber Taxi Launch In 2024 https://t.co/Xjui1oJsAP
##@krptxt @solarcity @elonmusk  https://t.co/PSNTt11U0n
##
##Elon Musk's Last 5 Tweets
##@lexiheft @Tesla Coming soon
##@shwetp We are ramping production as fast as possible. Wait should be closer to 6 months though, not 2 years.
##RT @Tesla: Model 3 is now the best-selling mid-sized premium sedan in the USA https://t.co/xI7LsgRI6D
##RT @Tesla: Watch the Tesla Shareholders Meeting live at 2:30pm PT: https://t.co/KRgSMMYIvw
##RT @Tesla: We have now installed over 1 gigawatt-hour of energy storage across the globe
##https://t.co/9PJhOFPy5Y
##>>> 
