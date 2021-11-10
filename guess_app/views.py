import random

import requests

from django.shortcuts import render
from guess_app.forms import GuessForm


def guess_app(request):
    form = GuessForm()
    context = {'guess_result': '', 'form': form}
    if request.method == "POST":
        form = GuessForm(request.POST)
        if form.is_valid():
            guess = form.cleaned_data["body"]
            locations_request = requests.get('https://countriesnow.space/api/v0.1/countries/capital')
            locations = locations_request.json()['data']
            number_of_locations = len(locations)
            choice_index = random.randint(0, number_of_locations - 1)
            correct_location = locations[choice_index]
            if guess.lower() == correct_location['capital'].lower():
                context['guess_result'] = 'Correct!'
            else:
                context['guess_result'] = (
                    f'Wrong :( I was thinking of {correct_location["capital"]} in {correct_location["name"]}. '
                    'Try again!'
                )

    return render(request, 'guess_app.html', context)
