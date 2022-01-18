from django.http import HttpResponse

def course(request):
    return HttpResponse("course list")

def courseDetails(request,courseid):
    return HttpResponse(courseid)