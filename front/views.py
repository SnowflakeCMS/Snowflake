from django.template import loader
from django.http import HttpResponse
from django.apps import apps as django_apps
from core.models import Blog


# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    blog_entries = Blog.objects.all()
    core_app = django_apps.get_app_config("core")

    context = {
        "blogs": blog_entries,
        "title": core_app.get_setting_value("title"),
        "subtitle": core_app.get_setting_value("subtitle"),
    }

    return HttpResponse(template.render(context, request))