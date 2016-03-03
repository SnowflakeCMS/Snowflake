from django.template import loader
from django.http import HttpResponse
from core.models import Blog


# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    blog_entries = Blog.objects.all()
    context = {
        "blogs": blog_entries,
    }
    print("----------->", context)
    return HttpResponse(template.render(context, request))