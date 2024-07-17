from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import UserProfile 
from home.models import Contact
from news.models import News, Category, Comment, Favorite, Tag
class UserProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = UserProfile.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone='1234567890'
        )

    def test_user_profile_str(self):
        self.assertEqual(str(self.profile), 'testuser')

    def test_default_gender(self):
        self.assertEqual(self.profile.Gender, UserProfile.man)

class ContactModelTest(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(
            name='Jane Smith',
            email='jane.smith@example.com',
            subject='Test Subject',
            message='This is a test message.'
        )

    def test_contact_str(self):
        self.assertEqual(str(self.contact), 'Test Subject')

class NewsModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.tag = Tag.objects.create(name='Test Tag')
        self.news = News.objects.create(
            title='Test News',
            image='path/to/image.jpg',
            content='This is test content.',
            author='Author Name'
        )
        self.news.category.add(self.category)
        self.news.tags.add(self.tag)

    def test_news_str(self):
        self.assertEqual(str(self.news), 'Test News')

    def test_news_ordering(self):
        self.assertEqual(News.objects.first(), self.news)

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')

class CommentModelTest(TestCase):

    def setUp(self):
        self.news = News.objects.create(
            title='Test News',
            image='path/to/image.jpg',
            content='This is test content.',
            author='Author Name'
        )
        self.comment = Comment.objects.create(
            post=self.news,
            name='Commenter Name',
            email='commenter@example.com',
            subject='Comment Subject',
            message='This is a comment.'
        )

    def test_comment_str(self):
        self.assertEqual(str(self.comment), 'Commenter Name')

class FavoriteModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.news = News.objects.create(
            title='Test News',
            image='path/to/image.jpg',
            content='This is test content.',
            author='Author Name'
        )
        self.favorite = Favorite.objects.create(user=self.user, post=self.news)

    def test_favorite_str(self):
        self.assertEqual(str(self.favorite), 'testuser - Test News')

class TagModelTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name='Test Tag')

    def test_tag_str(self):
        self.assertEqual(str(self.tag), 'Test Tag')
