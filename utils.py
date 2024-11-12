from datetime import datetime
from exceptions import InvalidYearCupError, NegativeTitlesError, ImpossibleTitlesError


def data_processing(data):
    first_cup_year = int(data["first_cup"].split("-")[0])
    current_year = datetime.now().year
    titles = data["titles"]
    possible_cups = (current_year - first_cup_year) // 4 + 1

    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")
    elif first_cup_year < 1933:
        raise InvalidYearCupError("there was no world cup this year")
    elif titles > possible_cups:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")

    return data


data = {
    "name": "França",
    "titles": 9,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2002-10-18",
}

print(data_processing(data))