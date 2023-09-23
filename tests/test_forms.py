from django.test import SimpleTestCase
from home.froms import ContactForm


class TestForms(SimpleTestCase):
    def test_contact_form_valid_data(self):
        form = ContactForm(data={
            "name" : 'ahmad',
            'email': 'karim@gmail.com',
            'subject' : 'test1',
            'message' : 'content'
        })

        self.assertTrue(form.is_valid())

    
    def test_contact_no_data(self):
        form = ContactForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)