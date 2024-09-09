from django.shortcuts import render


def menu_view(request, slug=None):
    return render(request, 'menu.html')
