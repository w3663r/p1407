# Create your tests here.
from django.test import TestCase
from django import test
from core.models import Student
from django.contrib.auth.models import User


class MovieTest(TestCase):
    def setUp(self):
		
        Student.objects.create(title="lion king", year="2000")
        Student.objects.create(title="cats and dogs", year="1950")

    def test_is_birth_ok(self):
        """I birth date is ok"""
        lion = Movie.objects.get(title="lion king")
        cat = Movie.objects.get(title="cats and dogs")
        years = list(range(1945,2018))		
        self.assertIn(int(lion.year), years)
        self.assertIn(int(cat.year), years)

    def test_is_title_str(self):
        lion = Movie.objects.get(title="lion king")
        self.assertIsInstance(lion.title, str)
        
    def test_search_for_smth(self):
        """Search test"""
        from django.db.models import Q
        q1 = Q(title__icontains='king')
        qobj = Movie.objects.filter(q1)[0]
        obj1 = Movie.objects.get(title='lion king')
        #self.assertIs(qobj[0],obj1)
        self.assertEqual(qobj,obj1)
        


