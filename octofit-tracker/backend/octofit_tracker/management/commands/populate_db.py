from django.core.management.base import BaseCommand
from pymongo import MongoClient
from bson import ObjectId
from datetime import timedelta
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboards.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword').__dict__,
            User(username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword').__dict__,
            User(username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword').__dict__,
            User(username='crashoverride', email='crashoverride@mhigh.edu', password='crashoverridepassword').__dict__,
            User(username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword').__dict__,
        ]
        db.users.insert_many(users)

        # Create teams
        team = Team(name='Blue Team', members=[user['_id'] for user in users]).__dict__
        db.teams.insert_one(team)

        # Create activities
        activities = [
            Activity(user=users[0]['_id'], activity_type='Cycling', duration=str(timedelta(hours=1))).__dict__,
            Activity(user=users[1]['_id'], activity_type='Crossfit', duration=str(timedelta(hours=2))).__dict__,
            Activity(user=users[2]['_id'], activity_type='Running', duration=str(timedelta(hours=1, minutes=30))).__dict__,
            Activity(user=users[3]['_id'], activity_type='Strength', duration=str(timedelta(minutes=30))).__dict__,
            Activity(user=users[4]['_id'], activity_type='Swimming', duration=str(timedelta(hours=1, minutes=15))).__dict__,
        ]
        db.activities.insert_many(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0]['_id'], score=100).__dict__,
            Leaderboard(user=users[1]['_id'], score=90).__dict__,
            Leaderboard(user=users[2]['_id'], score=95).__dict__,
            Leaderboard(user=users[3]['_id'], score=85).__dict__,
            Leaderboard(user=users[4]['_id'], score=80).__dict__,
        ]
        db.leaderboards.insert_many(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event').__dict__,
            Workout(name='Crossfit', description='Training for a crossfit competition').__dict__,
            Workout(name='Running Training', description='Training for a marathon').__dict__,
            Workout(name='Strength Training', description='Training for strength').__dict__,
            Workout(name='Swimming Training', description='Training for a swimming competition').__dict__,
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
