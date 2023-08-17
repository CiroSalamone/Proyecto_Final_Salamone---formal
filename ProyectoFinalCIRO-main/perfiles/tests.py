from django.test import TestCase
from django.db import IntegrityError
from blog.models import *
class UserTest(TestCase):

   def test_creacion_user(self):
       user = User(first_name="Martin", last_name="Disalvo", username="MartinDisalvo2608", email="Maperez@example.com")
       user.save()

       self.assertEqual(User.objects.count(), 1)
       self.assertEqual(user.first_name, "Martin")
       self.assertEqual(user.last_name, "Disalvo")
       self.assertEqual(user.username, "Mapdisalvo2608")
       self.assertEqual(user.email, "Maperez@example.com")