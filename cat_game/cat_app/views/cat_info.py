from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from random import randint

from cat_app.views.base import cat


def cat_info_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'warning.html')
    else:
        if request.POST.get('cat_name') is None:
            cat.cat_name = cat.cat_name
        else:
            cat.cat_name = request.POST.get('cat_name')
        cat.action = request.POST.get('action')
        cat.state = generating_data_about_a_cat()
        cat.image = set_image()
    context = {
        'cat_name': cat.cat_name,
        'age': cat.age,
        'satiety': cat.satiety,
        'happiness': cat.happiness,
        'action': cat.action,
        'state': cat.state,
        'image': cat.image
    }
    return render(request, 'cat_info.html', context)


def generating_data_about_a_cat():
    if cat.action == 'put the cat to bed':
        cat.state = 'sleep'
    elif cat.action == 'feed the cat':
        feed_cat()
    elif cat.action == 'play with a cat':
        play_with_cat()
    return cat.state


def set_image():
    match cat.state:
        case 'sleep':
            return 'images/sleep.png'
        case 'angry':
            return 'images/angry.png'
        case 'high_satiety':
            return 'images/high_satiety.png'

    if 0 <= cat.happiness < 20:
        return 'images/cry.png'
    if 15 <= cat.happiness < 30:
        return 'images/low_happy.png'
    if 30 <= cat.happiness < 60:
        return 'images/main_happy.png'
    if 60 <= cat.happiness < 80:
        return 'images/happy.png'
    if 80 <= cat.happiness <= 100:
        return 'images/love.png'


def feed_cat():
    if cat.state == 'sleep':
        return cat.state
    else:
        if cat.satiety == 100:
            if cat.happiness - 30 < 0:
                cat.happiness = 0
                cat.state = 'high_satiety'
            else:
                cat.happiness -= 30
        elif cat.satiety + 15 > 100:
            cat.happiness -= 30
            if cat.happiness < 0:
                cat.happiness = 0
            cat.satiety = 100
            cat.state = 'high_satiety'
        else:
            cat.satiety += 15
            if cat.happiness + 5 > 100:
                cat.happiness = 100
            else:
                cat.happiness += 5


def play_with_cat():
    if cat.state == 'sleep':
        cat.state = 'game'
        if cat.happiness - 5 > 0:
            cat.happiness -= 5
        else:
            cat.happiness = 0
    else:
        cat.state = 'game'
        angry_chance = randint(1, 3)
        if angry_chance == 1:
            cat.happiness = 0
            cat.state = 'angry'
        else:
            if cat.satiety == 100:
                cat.satiety -= 10
                cat.happiness += 15
            elif cat.happiness + 15 > 100:
                cat.happiness = 100
                cat.satiety -= 10
            else:
                if cat.satiety - 10 < 0:
                    cat.satiety = 0
                else:
                    cat.happiness += 15
                    cat.satiety -= 10
