from django.shortcuts import render 

# Create your views here.
def index(request):
        return render(request, 'index.html')

def submit(request):
        context={
                'firstName':request.POST['first_name'],
                'lastName':request.POST['last_name'],
                'birthday':request.POST['Birthday'],
                'gender':request.POST['gender'],
                'fav':request.POST['Favorite']
        }
        return render(request,'confirm.html', context)