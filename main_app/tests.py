import random

from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from django.test import TestCase
from django.urls import reverse

from main_app.models import Memory


class MemoriesViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create one User and 14 memories for tests
        number_of_memories = 14
        User.objects.create(first_name='John', last_name='Smith',
                            username='testuser', password='12345')
        test_author = User.objects.get(username='testuser')
        for memory_num in range(number_of_memories):
            latitude = random.uniform(-90, 90)
            longitude = random.uniform(-180, 180)
            Memory.objects.create(author=test_author,
                                  title='Memory %s' % memory_num,
                                  description='Detailed description %s' % memory_num,
                                  location=Point(latitude, longitude)
                                  )

    def test_view_url_exists_for_login_user(self):
        self.client.force_login(User.objects.get(username='testuser'))
        responce = self.client.get('/memories/')
        self.assertEqual(responce.status_code, 200)

    def test_view_url_does_not_exists_for_no_login_user(self):
        responce = self.client.get('/memories/')
        self.assertNotEqual(responce.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.force_login(User.objects.get(username='testuser'))
        responce = self.client.get(reverse('memories'))
        self.assertEqual(responce.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.force_login(User.objects.get(username='testuser'))
        responce = self.client.get(reverse('memories'))
        self.assertEqual(responce.status_code, 200)

        self.assertTemplateUsed(responce, 'main.html')


class MemoriesCreateViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='John', last_name='Smith',
                            username='testuser', password='12345')

    def test_view_url_exists(self):
        self.client.force_login(User.objects.get(username='testuser'))
        responce = self.client.get('/add-memory/')
        self.assertEqual(responce.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.force_login(User.objects.get(username='testuser'))
        responce = self.client.get(reverse('memory_create'))
        self.assertEqual(responce.status_code, 200)

    def test_uses_correct_template(self):
        self.client.force_login(User.objects.get(username='testuser'))
        responce = self.client.get(reverse('memory_create'))
        self.assertEqual(responce.status_code, 200)

        self.assertTemplateUsed(responce, 'addmemory.html')

    def test_form_cool(self):
        current_user = User.objects.get(username='testuser')
        form_data = {'author': current_user,
                     'title': 'test_title',
                     'description': 'test_description',
                     'location': Point(60, 60),
                     }

        self.client.force_login(current_user)
        self.client.post(reverse('memory_create'), data=form_data)
        print(Memory.objects.count(), '- count')
