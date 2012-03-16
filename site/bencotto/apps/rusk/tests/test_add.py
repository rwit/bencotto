"""
Tests related to adding new rusks
"""
import os.path
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from rusk.models import rusk

class AddTest(TestCase):
    def setUp(self):
        self.username = 'admin'
        self.password = 'admin'
        self.user = User.objects.create_user(self.username, '', self.password)
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.assertTrue(self.client.login(username = self.username, password = self.password))
        
    def tearDown(self):
        self.client.logout()
        
    def test_add(self):
        post_data = {
            'title': u'New Rusk',
            'description': u'This is the new rusk description',
            'image': open(os.path.join(os.path.dirname(__file__), 'data', 'test_image.gif'), 'r'),
        }
        response = self.client.post(reverse('add_rusk'), post_data, follow=False)

        #Rusk in db?
        self.assertEqual(rusk.objects.count(), 1)
        ruskAdded = rusk.objects.get(title='New Rusk') #twijfel of dit wel safe is; assert namelijk als er geen rusk is met deze title
        #self.assertContains(response, 'New Rusk') #enable als list view in orde is
        
        #Expect redirect to list view after new rusk is added
        self.assertRedirects(response, reverse('latest'))
