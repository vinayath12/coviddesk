from .models import Place


def menu_link(request):
    links=Place.objects.all()
    return dict(links=links)