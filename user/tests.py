from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Users


class UserSignupTest(APITestCase):
    def test_signup(self):
        url=reverse('signup_view')
        user_data={
            'username':'test',
            'email':'test@test.com',
            'password':'1234',
            'password_check':'1234'
        }
        response=self.client.post(url,user_data) 
        self.assertEqual(response.status_code,201)
    
class UserLoginTest(APITestCase):    
    def setUp(self):
        self.user=Users.objects.create_user(email='test@test.com',username='username',password='1234') #변수 없어도 됨
        self.data = {   
                        'username':'test',
                        'email':'test@test.com',
                        'password':'1234',
                        'password_check':'1234'
                    }

    def test_login(self):
        url=reverse('login_view')
        response=self.client.post(url,self.data) 
        self.assertEqual(response.status_code,200)