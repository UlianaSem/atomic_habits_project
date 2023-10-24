from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitListAPIView, PublicHabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView,
                          HabitDeleteAPIView, LocationCreateAPIView)

app_name = HabitsConfig.name


urlpatterns = [
    path("list/", HabitListAPIView.as_view(), name="habit-list"),
    path("public_list/", PublicHabitListAPIView.as_view(), name="habit-public-list"),
    path("create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("update/<int:pk>", HabitUpdateAPIView.as_view(), name="habit-update"),
    path("delete/<int:pk>", HabitDeleteAPIView.as_view(), name="habit-delete"),

    path("create_location/", LocationCreateAPIView.as_view(), name="location-create"),
]
