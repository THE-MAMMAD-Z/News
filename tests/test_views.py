from django.test import TestCase , Client
from django.urls import reverse
from news.models import News , Category
from home.models import Contact
import json


class Testviews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse("news:news")
        self.poroje1 = News.objects.create(
            title='nubmer1',
            image='G:\PICTURE\facq6.jpg',
            content='nubmer1',
            author='nubmer1',
        )
        self.detail_url = reverse('news:detail' , args=[self.poroje1.id])
        


    def test_blog_list_GET(self):  

        response = self.client.get(reverse('news:news'))

        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response,'news/blog.html')


    def test_project_detail_GET(self):
        response = self.client.get(self.detail_url)

        context = {

        }
    
        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed(response,"news/blog_details.html")
        

    def test_contact_view_POST(self):
        # Test POST request to the contact view with valid data
        form_data = {
            'name': 'ali',  # Replace with actual form field names and values
            'subject' : 'mohem',
            'email' : 'ali@yahoo.com',
            'message' : "content",
        }
        response = self.client.post(reverse('home:contact'), data=form_data)  # Replace 'contact' with your actual URL name
        self.assertEqual(response.status_code, 302)  # Check that the response is a redirect (status code 302)
        self.assertRedirects(response, reverse('home:home'))  # Check that it redirects to the home page (replace with your actual URL)
        # Test POST request with invalid data (missing or incorrect fields)
        invalid_form_data = {}  # Provide invalid form data here
        response = self.client.post(reverse('home:contact'), data=invalid_form_data)  # Replace 'contact' with your actual URL name
        self.assertEqual(response.status_code, 200)  # Check that the response status code is 200
        # self.assertFormError(response, 'form', 'your_field_name', 'Your error message')  # Replace with actual form field name and error message
        # Add more form field error checks as needed