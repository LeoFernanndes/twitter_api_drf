from twitter_api.twitter_auth import twitter_authentication
from tweepy.models import User


def validate_arroba(arroba):
    api = twitter_authentication()
    try:
        api.get_user(screen_name=arroba)
        result = True
    except Exception as e:
        print(e)
        result = False
    return result


def get_arroba_attributes(validated_user) -> User:
    api = twitter_authentication()
    arroba = api.get_user(screen_name=validated_user)
    return arroba