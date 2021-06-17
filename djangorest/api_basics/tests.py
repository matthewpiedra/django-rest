from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# Create your tests here.


# Simple unit test for airplane endpoint
class AirplaneTestCase(APITestCase):
    
    def test_airplanes_list(self):
        url = reverse("airplanes-list")

        # Use api test case to make a GET request for airplanes data to make sure it's properly configured
        response = self.client.get(url)

        # test to see if the status code is 200 - successful HTTP request and requested data would be displayed
        self.assertEqual(response.status_code, status.HTTP_200_OK)