from django.shortcuts import render
from MicroIDE.decorators import visit_record
# Create your views here.


@visit_record
def index(request):
    return render(request, 'ide/index.html')
