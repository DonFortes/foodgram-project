import csv

from dishes.models import Ingredient


def put_ingridients():
    CHOICES = []
    with open('ingredients.csv', 'r', newline='', encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            Ingredient.objects.get_or_create(
                name=row[0],
                measure=row[-1],
            )


# print(put_ingridients())
