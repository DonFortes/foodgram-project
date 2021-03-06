import csv


def get_choices():
    CHOICES = []
    with open('ingredients.csv', 'r', newline='', encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            CHOICES.append(tuple(row))

    return CHOICES
