from django.urls import path, include

from rest_framework import routers

from cinema.views import (
    GenreListView,
    GenreDetailView,
    ActorListView,
    ActorDetailView,
    CinemaHallViewSet,
    MovieViewSet
)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)

cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={"get": "retrieve", "put": "update",
             "patch": "partial_update", "delete": "destroy"}
)

movie_router = routers.DefaultRouter()

movie_router.register("movies", MovieViewSet)


urlpatterns = [
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("cinemahalls/", cinema_hall_list, name="cinema-hall-list"),
    path(
        "cinemahalls/<int:pk>/",
        cinema_hall_detail,
        name="cinema-hall-detail"
    ),
    path("", include(movie_router.urls)),
]

app_name = "cinema"
