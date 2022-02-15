from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):

	# Do stuff only for POST requests, otherwise it will be called
	# even when the page is loading.
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username, password)
		# authenticate() helps to verify the username and password
		user = authenticate(request, username=username, password=password)
		if user is None:
			# Context error is passed only if user is None
			context = {"error": "Invalid username or password"}
			return render(request, "accounts/login.html", context=context)
		# If successfully authenticated user should be logged in state.
		# login() helps to log in the user.
		login(request, user)
		# return redirect("/admin")
		return redirect("/")

	return render(request, "accounts/login.html", {})

def logout_view(request):
	if request.method == 'POST':
		# logout() helps to log out the user.
		logout(request)
		return redirect("/login/")
	return render(request, "accounts/logout.html", {})


def register_view(request):

	return render(request, "accounts/register.html", {})