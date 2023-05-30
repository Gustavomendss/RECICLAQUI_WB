from teste.models import latitude
import csv


def run():
    with open('films/pixar.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        latitude.objects.all().delete()
