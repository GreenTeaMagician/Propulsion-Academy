from django.contrib.auth import get_user_model
from rest_framework import status

from project.feed.models import Post
from django.urls import reverse

from project.api.tests.master import MasterTestWrapper

User = get_user_model()


class FeedDisplayTests(MasterTestWrapper.MasterTest):
    endpoint = 'api:feed_display'
    methods = ['GET']

    def setUp(self):
        super().setUp()
        for i in range(10):
            Post.objects.create(
                user=self.user,
                content=f'Test post! {i}',
            )

    def unauthorized_request(self):
        super().test_unauthorized_requests()

    def test_post_feed(self):
        #self.authenticate()
        response = self.client.get(self.get_url(), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
        self.assertEqual(response.data[0].get('content'), 'Test post! 9')

    def test_post_feed_descending_order2(self):
        return 'TBD'

class FeedUserID(MasterTestWrapper.MasterTest):
    endpoint = "api:feed/1/"
    methods = ['GET']

    def setUp(self):
        super().setUp()
        for i in range(10):
            Post.objects.create(
                user=self.user,
                content=f'Test post! {i}',
        )

    def test_get(self):
        self.authenticate()
        response = self.client.get(self.get_url(), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
        self.assertEqual(response.data[0].get('content'), 'Test post! 9')

    def test_unauthorized_requests(self):
        url = self.get_url(**self.get_kwargs())
        for m in self.methods:
            try:
                method = getattr(self.client, m.lower())
                response = method(url)
                if response:
                    self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
            except AttributeError:
                raise Exception(f"No such method {m}")


# class PostRequests(MasterTestWrapper.MasterTest):
#
#     def test_post(self, view):
#         url = reverse(view)
#         self.client.login(username='michal2', password='michal11')
#         response = self.client.get(url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#
# class DeleteRequests(MasterTestWrapper.MasterTest):
#
#     def test_delete(self, view):
#         url = reverse(view)
#         self.client.login(username='michal2', password='michal11')
#         response = self.client.get(url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
