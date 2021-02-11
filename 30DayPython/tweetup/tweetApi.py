import twitter

key = 'HcaPdI1bISwYc8DwJgFOyjfNU'
secret = '4R8qs5J5aGqRLHe9d0oHxNdkoeCA6KAUTD3AVdf2DmSuCt1Vcj'

bearer = 'AAAAAAAAAAAAAAAAAAAAAAVJMQEAAAAAky8dEIThIRebTFl%2Bl1gn9tLQRTI%3DHrp0IgLaPFHrVEb8RxCzd86hoq4jxEcL908pcYWENrE0QsRERU'
token = '1356192802586173440-bL7kppc0zElRa0LvFeHGy7lLRAF48e'
tknsecret = 'gnZ9Pr2ttbWtO8gXrpzccMolXQz1MrF5c2DLDB5lrdYlD'

api = twitter.Api(consumer_key=key,
                consumer_secret=secret,
                access_token_key=token,
                access_token_secret=tknsecret)

cred = api.VerifyCredentials()
followers = api.GetFollowers
friends = api.GetFriends
