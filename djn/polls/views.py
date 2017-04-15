from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse(
	"<html>"
	"<head>"
	"<title>Dobrii vecher!</title>"
	"</head>"
	"<body>"
	"<text>Здравствуйте</text>"
	"</body>"
	"</html>"
	)