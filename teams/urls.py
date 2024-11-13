from django.urls import path
from teams.views import TeamViews


urlpatterns = [
    path("teams/", TeamViews.as_view()),
]
