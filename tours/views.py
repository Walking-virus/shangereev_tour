from django.shortcuts import render, redirect
from . models import Trips, Travel, Comment, Command, Timetable, Images, AboutUs, ContactUs
from . forms import CommentForm, ContactUsForm

def header(request):
    trips = Trips.objects.all()
    form = ContactUsForm(request.POST)
    if request.method == "POST":
    	if form.is_valid():
    		form.save()
    return render(request, 'tours/header.html', locals())

def command(request):
	trips = Trips.objects.all()
	command = Command.objects.all()
	trips = Trips.objects.all()
	form = ContactUsForm(request.POST)
	if request.method == "POST":
		if form.is_valid():
			form.save()
	return render(request, 'tours/command.html', locals())


def timetable(request):
	trips = Trips.objects.all()
	timetable = Timetable.objects.all()
	trips = Trips.objects.all()
	form = ContactUsForm(request.POST)
	if request.method == "POST":
		if form.is_valid():
			form.save()
	return render(request, 'tours/timetable.html', locals())


def about_us(request):
	trips = Trips.objects.all()
	aboutUs = AboutUs.objects.all()
	trips = Trips.objects.all()
	form = ContactUsForm(request.POST)
	if request.method == "POST":
		if form.is_valid():
			form.save()
	return render(request, 'tours/about_us.html', locals())


def page_travels(request, slug):
	travel = Travel.objects.filter(trips__url = slug)
	trips = Trips.objects.get(url = slug)
	trips = Trips.objects.all()
	trips = Trips.objects.all()
	form = ContactUsForm(request.POST)
	if request.method == "POST":
		if form.is_valid():
			form.save()
	return render(request, 'tours/page_travels.html', locals())


def detail_about_travel(request, slug):
	title = "detail_about_travel"
	images = Images.objects.all()
	trips = Trips.objects.all()
	travel = Travel.objects.get(url = slug)
	trips = Trips.objects.all()
	form = ContactUsForm(request.POST)
	if request.method == "POST":
		if form.is_valid():
			form.save()
	comment = travel.comment.order_by('-release_date')
	forms = CommentForm(request.POST)
	if forms.is_valid():
		forms = forms.save(commit=False)
		forms.comment_travel = travel
		forms.save()
		return redirect(detail_about_travel, slug)
	
	return render(request, 'tours/detail_about_travel.html', locals())