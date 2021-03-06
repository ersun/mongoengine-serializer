from models import *
from serializerExtensions import MongoEngineModelSerializer


class UserSerializer(MongoEngineModelSerializer):
    class Meta:
        model = User


class BlogSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Blog
        depth = 1
        related_model_validations = {'owner': User}


class PostSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Post
        depth = 1
        related_model_validations = {'author': User, 'blog': Blog}


class CommentSerializer(MongoEngineModelSerializer):
    class Meta:
        model = Comment
        depth = 2
        related_model_validations = {'owner': User, 'post': Post}
        exclude = ('isApproved',)

###############################################################################
###############################################################################
###                                                                         ###
###  class SomeSerializer(MongoEngineModelSerializer):                      ###
###     class Meta: -> Just like Model Serializer in Django Rest Framework  ###
###         model   -> Model the serializer will use                        ###
###         depth   -> The depth of JSON (when embedding Documents)         ###
###         related_model_validations -> Validates ReferenceField()         ###
###         exclude -> Exclude fields from serialization                    ###
###                                                                         ###
###############################################################################
###############################################################################