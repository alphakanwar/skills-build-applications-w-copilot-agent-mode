from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient
from django.conf import settings
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

# Connect to MongoDB
client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
db = client[settings.DATABASES['default']['NAME']]

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://super-duper-journey-wrxxg6q54xg5h5xw-8000.app.github.dev/'
    return Response({
        'users': base_url + 'api/users/',
        'teams': base_url + 'api/teams/',
        'activities': base_url + 'api/activities/',
        'leaderboard': base_url + 'api/leaderboard/',
        'workouts': base_url + 'api/workouts/',
    })

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = list(db.users.find())
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            db.users.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        teams = list(db.teams.find())
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            db.teams.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        activities = list(db.activities.find())
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            db.activities.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        leaderboard = list(db.leaderboards.find())
        serializer = LeaderboardSerializer(leaderboard, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LeaderboardSerializer(data=request.data)
        if serializer.is_valid():
            db.leaderboards.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutViewSet(viewsets.ViewSet):
    def list(self, request):
        workouts = list(db.workouts.find())
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            db.workouts.insert_one(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
