from django.test import TestCase
from news.forms import  CommentForm, FovoriteForm
from home.forms import ContactForm
from accounts.forms import ProfileRegisterForm , ProfileEditForm
from news.models import News
from django.contrib.auth.models import User


class FormsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.news = News.objects.create(title='Test News', content='Some content')  # Assuming the News model has a title and content field

    def test_profile_register_form_valid(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'password': 'secret',
            'email': 'john@example.com',
            'profile_picture': 'path/to/picture.jpg',
            'phone': '1234567890',
            'Gender': 'M',
            'address': '123 Street'
        }
        form = ProfileRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_profile_register_form_invalid(self):
        form_data = {
            'first_name': '',
            'last_name': 'Doe',
            'username': 'johndoe',
            'password': 'secret',
            'email': 'notanemail',
            'profile_picture': 'path/to/picture.jpg',
            'phone': '1234567890',
            'Gender': 'M',
            'address': '123 Street'
        }
        form = ProfileRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_profile_edit_form_valid(self):
        form_data = {
            'profile_picture': 'path/to/picture.jpg',
            'phone': '1234567890',
            'Gender': 'M',
            'address': '123 Street'
        }
        form = ProfileEditForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contact_form_valid(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Hello there!',
            'subject': 'Greetings'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_valid(self):
        form_data = {
            'post': self.news.id,
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Interesting post',
            'message': 'Great read!'
        }
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_favorite_form_valid(self):
        form_data = {
            'user': self.user.id,
            'post': self.news.id
        }
        form = FovoriteForm(data=form_data)
        self.assertTrue(form.is_valid())
