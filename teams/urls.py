from django.urls import path
from teams.views import TeamDetailViews, TeamViews


urlpatterns = [
    path("teams/", TeamViews.as_view()),
    path("teams/<int:team_id>/", TeamViews.as_view()),
    path("teams/<int:team_id>/", TeamDetailViews.as_view()),
]
