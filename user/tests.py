from rest_framework.test import APITestCase
from django.urls import reverse


class SignUpTest(APITestCase):
    def test_signup(self):
        url=reverse('signup_view')
        user_data={
            'username':'test',
            'email':'test@test.com',
            'password':'1234',
            'password_check':'1234'
        }
        response=self.client.post(url,user_data)
        print(response.data)
        self.assertEqual(response.data['message'],"회원가입이 완료되었습니다!")