from django.shortcuts import render
# from django import forms
from first_app import forms

# Create your views here.
def tao_cookie(request):
    response = render(request, 'first_app/tao_cookie.html')
    response.set_cookie('ho_ten', 'Nguyen Van A')
    return response

def register(request):
    registered = False
    if request.method == "POST":
        form_user = forms.UserForm(data = request.POST)
        form_por = forms.UserProfileInfoForm(data = request.POST)
        if form_user.is_valid() and form_por.is_valid():
            user = form_user.save()
            user.set_password(user.password)
            user.save()
            profile = form_por.save(commit = False)
            profile.user = user
            print(request.FILES)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(form_user.errors, form_por.errors)
    else:
        form_user = forms.UserForm()
        form_por = forms.UserProfileInfoForm()
    
    return render(request, "first_app/registration.html", {'user_form':form_user, 'profile_form': form_por, 'registered': registered})