from django.test import TestCase

from rest_framework import status
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from .serializers import ProfileSerializer
from .views import ProfileViewSet


class ProfileTests(TestCase):
    def setUp(self):
        self.new_user_data = {
            'username': 'user1',
            'email': 'user1@example.com',
            'description': ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do '
                            'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
        }

    def test_use_serializer_directly(self):
        serializer = ProfileSerializer(data=self.new_user_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        profile = serializer.save()
        self.assertEquals(profile.user.username, self.new_user_data['username'])
        self.assertEquals(profile.description, self.new_user_data['description'])

    def test_profile_create_view(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', self.new_user_data)

        create_view = ProfileViewSet.as_view({'post': 'create'})
        response = create_view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_profile_create_view_json(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', self.new_user_data, format='json')

        create_view = ProfileViewSet.as_view({'post': 'create'})
        response = create_view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_serializer_with_querydict(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', self.new_user_data)

        serializer = ProfileSerializer(data=request.POST)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        profile = serializer.save()
        self.assertEquals(profile.user.username, self.new_user_data['username'])
        self.assertEquals(profile.description, self.new_user_data['description'])



