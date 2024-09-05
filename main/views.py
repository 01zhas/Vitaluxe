from django.shortcuts import render
from .models import Advertisement


def home(request):
    return render(request, 'main/home.html')


def base(request):
    return render(request, 'main/base.html')


def shop_all(request):
    return render(request, 'main/shop_all.html')


def ingredients(request):
    return render(request, 'main/ingredients.html')


def advertisement_view(request):
    # Получаем последнюю запись из таблицы Advertisement
    advertisement = Advertisement.objects.last()

    # Проверяем, является ли баннер видео (оканчивается на .mp4)
    is_video = advertisement.banner.url.endswith('.mp4') if advertisement.banner else False
    
    return render(request, 'main/advertisement.html', {
        'advertisement': advertisement,
        'is_video': is_video
    })
