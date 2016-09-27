from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello , Youre at the polls.")
# Create your views here.
