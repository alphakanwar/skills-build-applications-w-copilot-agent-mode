from bson import ObjectId

class User:
    def __init__(self, username, email, password):
        self._id = ObjectId()
        self.username = username
        self.email = email
        self.password = password

class Team:
    def __init__(self, name, members):
        self._id = ObjectId()
        self.name = name
        self.members = members

class Activity:
    def __init__(self, user, activity_type, duration):
        self._id = ObjectId()
        self.user = user
        self.activity_type = activity_type
        self.duration = duration

class Leaderboard:
    def __init__(self, user, score):
        self._id = ObjectId()
        self.user = user
        self.score = score

class Workout:
    def __init__(self, name, description):
        self._id = ObjectId()
        self.name = name
        self.description = description
