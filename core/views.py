from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def signup(request):
    return render(request, 'core/signup.html')
def magic(request):
    if request.method == "POST":
        random_number = random.randint(0, 10)
        user_guess = int(request.POST['user_guess'])
        if random_number == user_guess:
            result = "Win"
        else:
            result = f'lose! magic number:{random_number}'
        return render(request, 'core/magic.html', {'result' : result})
    return render(request, 'core/magic.html')

