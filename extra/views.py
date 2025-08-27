from django.shortcuts import render

# Create your views here.
def personalidades_historicas(request):
    return render(request, 'extra/personalidades_historicas.html')