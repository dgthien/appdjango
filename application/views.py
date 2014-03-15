from django.http import HttpResponse


def index(request):
    return HttpResponse(""
        "Hello, world. You're at the polls index. "
        "<ul><li><a href='/polls'>Home</a></li><li><a href='/admin'>Administration</a></li></ul>"
    "")