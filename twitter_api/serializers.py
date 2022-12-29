from rest_framework import serializers

from twitter_api.models import TwitterUser
from twitter_api.utils import validate_arroba, get_arroba_attributes


class TwitterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = TwitterUser
        fields = ['id', 'id_str', 'name', 'screen_name', 'location', 'profile_location', 'description',
            'url', 'protected', 'followers_count', 'friends_count', 'statuses_count', 'lang',
            'profile_image_url', 'profile_image_url_https']
        read_only_fields = ['id', 'id_str', 'name', 'location', 'profile_location', 'description',
                  'url', 'protected', 'followers_count', 'friends_count', 'statuses_count', 'lang',
                  'profile_image_url', 'profile_image_url_https']

    def validate_screen_name(self, scree_name):
        if validate_arroba(scree_name):
            return scree_name
        else:
            raise serializers.ValidationError('Invalid or not found twitter user.')

    def create(self, validated_data):
        twitter_user_create_data = {}
        twitter_user_api_json_response = get_arroba_attributes(validated_data['screen_name']).__dict__['_json']

        twitter_user_create_data['id_str'] = twitter_user_api_json_response['id_str']
        twitter_user_create_data['name'] = twitter_user_api_json_response['name']
        twitter_user_create_data['screen_name'] = twitter_user_api_json_response['screen_name']
        twitter_user_create_data['location'] = twitter_user_api_json_response['location']
        twitter_user_create_data['profile_location'] = twitter_user_api_json_response['profile_location']
        twitter_user_create_data['description'] = twitter_user_api_json_response['description']
        twitter_user_create_data['url'] = twitter_user_api_json_response['url']
        twitter_user_create_data['protected'] = twitter_user_api_json_response['protected']
        twitter_user_create_data['followers_count'] = twitter_user_api_json_response['followers_count']
        twitter_user_create_data['friends_count'] = twitter_user_api_json_response['friends_count']
        twitter_user_create_data['statuses_count'] = twitter_user_api_json_response['statuses_count']
        twitter_user_create_data['lang'] = twitter_user_api_json_response['lang']
        twitter_user_create_data['profile_image_url'] = twitter_user_api_json_response['profile_image_url']
        twitter_user_create_data['profile_image_url_https'] = twitter_user_api_json_response['profile_image_url_https']

        return super(TwitterUserSerializer, self).create(twitter_user_create_data)

