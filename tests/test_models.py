from django.test import TestCase
from home.models import Contact  

class ContactModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Contact.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            subject='Test Subject',
            message='Test Message'
        )

    def test_name_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_email_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_subject_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('subject').verbose_name
        self.assertEqual(field_label, 'subject')

    def test_message_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('message').verbose_name
        self.assertEqual(field_label, 'message')

    def test_name_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_subject_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('subject').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_subject(self):
        contact = Contact.objects.get(id=1)
        expected_object_name = contact.subject
        self.assertEqual(expected_object_name, str(contact))
