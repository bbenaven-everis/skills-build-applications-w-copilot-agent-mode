from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import connection
from bson import ObjectId

# Datos de ejemplo
USERS = [
    {"_id": ObjectId(), "name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"_id": ObjectId(), "name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"_id": ObjectId(), "name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
    {"_id": ObjectId(), "name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"_id": ObjectId(), "name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Marvel"},
    {"_id": ObjectId(), "name": "Captain Marvel", "email": "captainmarvel@marvel.com", "team": "Marvel"},
]
TEAMS = [
    {"_id": ObjectId(), "name": "Marvel"},
    {"_id": ObjectId(), "name": "DC"},
]
ACTIVITIES = [
    {"_id": ObjectId(), "user": "superman@dc.com", "activity": "Volar", "duration": 60},
    {"_id": ObjectId(), "user": "ironman@marvel.com", "activity": "Volar traje", "duration": 45},
]
LEADERBOARD = [
    {"_id": ObjectId(), "user": "superman@dc.com", "score": 100},
    {"_id": ObjectId(), "user": "ironman@marvel.com", "score": 95},
]
WORKOUTS = [
    {"_id": ObjectId(), "name": "Entrenamiento de fuerza", "description": "Rutina de fuerza para superhéroes"},
    {"_id": ObjectId(), "name": "Cardio extremo", "description": "Rutina de cardio para héroes veloces"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        db = connection.cursor().db_conn
        # Eliminar datos previos
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        # Insertar datos de ejemplo
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)
        # Índice único en email
        db.users.create_index([("email", 1)], unique=True)
        self.stdout.write(self.style.SUCCESS('octofit_db poblada con datos de ejemplo.'))
