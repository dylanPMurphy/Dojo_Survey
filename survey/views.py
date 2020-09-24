from django.shortcuts import render, redirect 

# Create your views here.
def index(request):
        return render(request, 'index.html')

def submit(request):
        # context={
        #         'firstName':request.POST['first_name'],
        #         'lastName':request.POST['last_name'],
        #         'birthday':request.POST['Birthday'],
        #         'gender':request.POST['gender'],
        #         'fav':request.POST['Favorite']
        # }
        print(request.POST)
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['Birthday'] = request.POST['Birthday']
        request.session['gender'] = request.POST['gender']
        request.session['Favorite'] = request.POST['Favorite']
        return redirect('/result' )
        print(request.session)
def result(request):
        return render(request, 'confirm.html')