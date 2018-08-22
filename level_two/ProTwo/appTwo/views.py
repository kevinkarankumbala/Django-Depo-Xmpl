from django.shortcuts import render
from appTwo.models import User
from appTwo.forms import NewUserForm
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'templates/appTwo/index.html' )

def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error')

    return render(request, 'templates/appTwo/users.html',{'form':form})
