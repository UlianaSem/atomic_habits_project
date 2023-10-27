from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit, Location
from users.models import User


class LocationTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.ru', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

    def test_create(self):
        response = self.client.post(
            reverse('habits:location-create'),
            data={"location": "test"}
        )

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.assertEquals(response.json(),
                          {
                              "id": 7,
                              "location": "test"
                          }
                          )


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.ru', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

        self.location = Location.objects.create(location="test")

        self.first_habit = Habit.objects.create(time="16:03", action="test action 1", duration=50, is_pleasant=False,
                                                periodicity=1, is_public=True, reward="test reward 1",
                                                location=self.location, user=self.user)

        self.second_habit = Habit.objects.create(time="11:03", action="test action 2", duration=60, is_pleasant=False,
                                                 periodicity=1, is_public=False, reward="test reward 2",
                                                 location=self.location, user=self.user)

    def test_list_my_habit(self):
        response = self.client.get(
            reverse('habits:habit-list')
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.json(), {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.first_habit.pk,
                    "bound_habit": self.first_habit.bound_habit,
                    "periodicity": self.first_habit.periodicity,
                    "duration": self.first_habit.duration,
                    "day": datetime.utcnow().date().strftime("%Y-%m-%d"),
                    "time": "16:03:00",
                    "action": self.first_habit.action,
                    "reward": self.first_habit.reward,
                    "is_pleasant": self.first_habit.is_pleasant,
                    "is_public": self.first_habit.is_public,
                    "user": self.first_habit.user.pk,
                    "location": self.first_habit.location.pk
                },
                {
                    "id": self.second_habit.pk,
                    "bound_habit": self.second_habit.bound_habit,
                    "periodicity": self.second_habit.periodicity,
                    "duration": self.second_habit.duration,
                    "day": datetime.utcnow().date().strftime("%Y-%m-%d"),
                    "time": "11:03:00",
                    "action": self.second_habit.action,
                    "reward": self.second_habit.reward,
                    "is_pleasant": self.second_habit.is_pleasant,
                    "is_public": self.second_habit.is_public,
                    "user": self.second_habit.user.pk,
                    "location": self.second_habit.location.pk
                }
            ]
        })

    def test_list_public_habit(self):
        response = self.client.get(
            reverse('habits:habit-public-list')
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.json(), {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.first_habit.pk,
                    "bound_habit": self.first_habit.bound_habit,
                    "periodicity": self.first_habit.periodicity,
                    "duration": self.first_habit.duration,
                    "day": datetime.utcnow().date().strftime("%Y-%m-%d"),
                    "time": "16:03:00",
                    "action": self.first_habit.action,
                    "reward": self.first_habit.reward,
                    "is_pleasant": self.first_habit.is_pleasant,
                    "is_public": self.first_habit.is_public,
                    "user": self.first_habit.user.pk,
                    "location": self.first_habit.location.pk
                }
            ]
        })

    def test_create(self):
        response = self.client.post(
            reverse('habits:habit-create'),
            data={"time": "14:00", "action": "test", "duration": 20, "is_pleasant": False, "periodicity": 3,
                  "is_public": True, "reward": "test"}
        )

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.assertEquals(response.json(),
                          {
                              "id": 3,
                              "bound_habit": None,
                              "periodicity": 3,
                              "duration": 20,
                              "day": datetime.utcnow().date().strftime("%Y-%m-%d"),
                              "time": "14:00:00",
                              "action": "test",
                              "reward": "test",
                              "is_pleasant": False,
                              "is_public": True,
                              "user": 1,
                              "location": 1
                          }
                          )

    def test_update(self):
        response = self.client.patch(
            reverse('habits:habit-update', args=[self.first_habit.pk]),
            data={"time": "14:00"}
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.json(),
                          {
                              "id": self.first_habit.pk,
                              "bound_habit": None,
                              "periodicity": 1,
                              "duration": 50,
                              "day": datetime.utcnow().date().strftime("%Y-%m-%d"),
                              "time": "14:00:00",
                              "action": "test action 1",
                              "reward": "test reward 1",
                              "is_pleasant": False,
                              "is_public": True,
                              "user": 6,
                              "location": 6
                          }
                          )

    def test_delete(self):
        response = self.client.delete(
            reverse('habits:habit-delete', args=[self.first_habit.pk])
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_error(self):
        response_for_error = self.client.post(
            reverse('habits:habit-create'),
            data={"time": "14:00", "action": "test", "duration": 150, "is_pleasant": False, "periodicity": 3,
                  "is_public": True, "reward": "test"}
        )

        self.assertEquals(response_for_error.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEquals(response_for_error.json(),
                          {'duration': ['Duration should be less 120 sec']}
                          )

        response_for_error = self.client.post(
            reverse('habits:habit-create'),
            data={"time": "14:00", "action": "test", "duration": 50, "is_pleasant": False, "periodicity": 12,
                  "is_public": True, "reward": "test"}
        )

        self.assertEquals(response_for_error.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEquals(response_for_error.json(),
                          {'periodicity': ['Periodicity should be not more 7 days']}
                          )

        response_for_error = self.client.post(
            reverse('habits:habit-create'),
            data={"time": "14:00", "action": "test", "duration": 50, "is_pleasant": False, "periodicity": 12,
                  "is_public": True, "reward": "test"}
        )

        self.assertEquals(response_for_error.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEquals(response_for_error.json(),
                          {'periodicity': ['Periodicity should be not more 7 days']}
                          )
