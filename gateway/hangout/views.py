from django.shortcuts import render

# Create your views here.
def home(request):
	if request.user.is_authenticated():
		username_is = "oliverrrrr"
		context = {"username_is": username_is}
	else:
		context = {"username_is": request.user}

	template = 'home.html'
	
	return render(request, template, context)