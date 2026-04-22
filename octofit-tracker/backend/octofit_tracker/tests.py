from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)
        Activity.objects.create(user=tony, type='Run', duration=30)
        Workout.objects.create(name='Avengers HIIT', description='HIIT for Marvel')
        Leaderboard.objects.create(user=tony, points=100)

    def test_user_team(self):
        tony = User.objects.get(name='Tony Stark')
        self.assertEqual(tony.team.name, 'Marvel')

    def test_leaderboard(self):
        entry = Leaderboard.objects.get(user__name='Tony Stark')
        self.assertEqual(entry.points, 100)
