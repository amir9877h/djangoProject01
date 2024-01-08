from django.http import HttpResponse

# Create your views here.
def post_list(request, year = None, month = None, day = None):
    return HttpResponse("Posts List Page")

def categories_list(request):
    return HttpResponse("Categories List Page")

def post_details(request, post_title):
    return HttpResponse("Posts Details Page: " + post_title)