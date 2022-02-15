from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

def register_view(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		user_obj = form.save()

		return redirect("/login/")
	# Another way to pass context directly.
	return render(request, "accounts/register.html", {"form": form})

# Authenticate using AuthenticationForm.
def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			#get_user() is ONLY for AuthenticationForm
			user = form.get_user()
			login(request, user)
			return redirect("/")
	else:
		# Only Authentication form can be used like this since it is not creating
		# a new model, unlike other Forms
		form = AuthenticationForm(request)
	context = {
		"form": form,
	}
	return render(request, "accounts/login.html", context)

# def login_view(request):

# 	# Do stuff only for POST requests, otherwise it will be called
# 	# even when the page is loading.
# 	if request.method == 'POST':
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
# 		print(username, password)
# 		# authenticate() helps to verify the username and password
# 		user = authenticate(request, username=username, password=password)
# 		if user is None:
# 			# Context error is passed only if user is None
# 			context = {"error": "Invalid username or password"}
# 			return render(request, "accounts/login.html", context=context)
# 		# If successfully authenticated user should be logged in state.
# 		# login() helps to log in the user.
# 		login(request, user)
# 		# return redirect("/admin")
# 		return redirect("/")

# 	return render(request, "accounts/login.html", {})

def logout_view(request):
	if request.method == 'POST':
		# logout() helps to log out the user.
		logout(request)
		return redirect("/login/")
	return render(request, "accounts/logout.html", {})