from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class UserAPITestCase(APITestCase):
    def test_create_user(self):
        data = {"username": "testuser", "email": "testuser@example.com", "password": "password123"}
        response = self.client.post("/api/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamAPITestCase(APITestCase):
    def test_create_team(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        data = {"name": "Test Team", "members": [user.id]}
        response = self.client.post("/api/teams/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityAPITestCase(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        data = {"user": user.id, "activity_type": "Running", "duration": "01:00:00"}
        response = self.client.post("/api/activities/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardAPITestCase(APITestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        data = {"user": user.id, "score": 100}
        response = self.client.post("/api/leaderboard/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutAPITestCase(APITestCase):
    def test_create_workout(self):
        data = {"name": "Test Workout", "description": "Test Description"}
        response = self.client.post("/api/workouts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
