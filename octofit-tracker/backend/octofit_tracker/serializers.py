from rest_framework import serializers
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.Serializer):
    _id = ObjectIdField()
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

class TeamSerializer(serializers.Serializer):
    _id = ObjectIdField()
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=ObjectIdField())

class ActivitySerializer(serializers.Serializer):
    _id = ObjectIdField()
    user = ObjectIdField()
    activity_type = serializers.CharField(max_length=100)
    duration = serializers.CharField()

class LeaderboardSerializer(serializers.Serializer):
    _id = ObjectIdField()
    user = ObjectIdField()
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    _id = ObjectIdField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
