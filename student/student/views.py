from django.http import HttpResponse
def home(request):
    d1 = "hello world"
    d2 = (2+2)
    name = "vasu"
    age = 18
    return HttpResponse(f"{d1}\n{d2}\n{name}\n{age}")
def about(request):
    return HttpResponse("about")
def contact(request):
    return HttpResponse("contact")