from django.http import HttpResponse
from .models import Album
from django.template import loader

# Create your views here
def index(request):
    all_albums = Album.object.all()
    template = loader.get_template("film/index.html")
    context = {"all_albums" : all_albums}
    return HttpResponse(template.render(context, request))

def detail(request, album_id):
    return HttpResponse("<h2> Details for Album ID: " + str(album_id) + "</h2>")

