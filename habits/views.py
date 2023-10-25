from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit, Location
from habits.paginators import HabitsPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer, LocationSerializer


class HabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)

        return queryset


class PublicHabitListAPIView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_public=True)

        return queryset


class HabitCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class LocationCreateAPIView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
