from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.




def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            un = form.cleaned_data.get('username') # pylint: disable=invalid-name
            messages.success(request, f'Account created for {un}.')
            return redirect('sign_in')

    elif request.method == "GET":
        form = UserSignUpForm()

    return render(request, 'users/signup.html', {'form': form})
# def sign_up(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		form = UserSignUpForm()
# 		if request.method == 'POST':
# 			form = UserSignUpForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request,"Account was created for "+ user)
# 				return redirect('sign_in')

# 		context = {'form':form}
# 		return render(request,'users/signup.html',context)



# #login page
# def sign_in(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:

# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			password = request.POST.get('password')
# 			user = authenticate(request,username=username,password=password)
# 			if user is not None:
# 				login(request,user)
# 				return redirect('home')
# 			else:
# 				messages.info(request,'Username or password is incorrect')
# 		context = {}
# 		return render(request,'signin.html',context)

# #logout page
# def sign_out(request):
# 	logout(request)
# 	return redirect('signin.html')

