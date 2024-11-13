from rest_framework.views import APIView, Response, Request
from django.forms.models import model_to_dict
from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError
from teams.models import Team
from utils import data_processing


class TeamViews(APIView):
    def post(self, request: Request) -> Response:
        try:
            validated_data = data_processing(request.data)
            team = Team.objects.create(**validated_data)
            return Response(model_to_dict(team), 201)
        except (InvalidYearCupError, NegativeTitlesError, ImpossibleTitlesError) as error:
            return Response({"error": error.message}, 400)

    def get(self, request: Request) -> Response:

        teams_dict = [
            model_to_dict(team)
            for team in Team.objects.all()
        ]

        return Response(teams_dict, 200)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            validated_data = data_processing(request.data)

            team = Team.objects.get(id=team_id)

            for key, value in validated_data.items():
                if hasattr(team, key):
                    setattr(team, key, value)

            team.save()

            return Response(model_to_dict(team), 200)
        except (InvalidYearCupError, NegativeTitlesError, ImpossibleTitlesError) as error:
            return Response({"error": error.message}, 400)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
            team.delete()
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        return Response({"message": "Team deleted"}, 204)


class TeamDetailViews(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        team_dict = model_to_dict(team)
        return Response(team_dict, 200)

