from django.shortcuts import render

# Create your views here.
def burger(request):
	context = {"msg": "Hello World!" ,}
	return render (request, "cheese.html", context)