from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class MasterTestWrapper(object):
    class MasterTest(APITestCase):
        endpoint = None
        methods = []
        kwargs = {}

        def get_url(self, *args, **kwargs):
            return reverse(self.endpoint, args=args, kwargs=kwargs)

        def get_kwargs(self):
            return self.kwargs

        def setUp(self):
            self.user = User.objects.create_user(
                username='michal2',
                password='michal11',
            )

        def authenticate(self):
            self.refresh = RefreshToken.for_user(self.user)
            self.access_token = self.refresh.access_token
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        def test_unauthorized_requests(self):
            url = self.get_url(**self.get_kwargs())
            for m in self.methods:
                try:
                    method = getattr(self.client, m.lower())
                    response = method(url)
                    if response:
                        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
                except AttributeError:
                    raise Exception(f"No such method {m}")


