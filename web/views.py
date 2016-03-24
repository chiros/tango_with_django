from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'web/index.html', context_dict)

def about(request):
    return render(request, 'web/about.html')