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
