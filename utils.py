from datetime import datetime
from exceptions import InvalidYearCupError, NegativeTitlesError, ImpossibleTitlesError


def data_processing(data):
    if 'first_cup' in data:
        first_cup_year = int(data["first_cup"].split("-")[0])
        current_year = datetime.now().year
        titles = data.get("titles", 0)
        possible_cups = (current_year - first_cup_year) // 4 + 1

        if titles < 0:
            raise NegativeTitlesError("titles cannot be negative")
        elif titles > possible_cups:
            raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
        elif first_cup_year < 1930:
            raise InvalidYearCupError("there was no world cup this year")

    return data
