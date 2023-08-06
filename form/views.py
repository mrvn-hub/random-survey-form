from django.shortcuts import render
from django.core import serializers
from django.http import Http404, HttpResponseNotAllowed, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Form
from .myform import MyForm
from django.template import loader
import json 
import pyrebase
import math


firebaseConfig = {
	"apiKey": "AIzaSyDRww6gG2JiC7x5C5rqPNiqkPKThLjgyBQ",
	"authDomain": "random-survey-form.firebaseapp.com",
	"projectId": "random-survey-form",
	"storageBucket": "random-survey-form.appspot.com",
	"messagingSenderId": "764014336225",
	"appId": "1:764014336225:web:3a02a4b3bf043282693fa0",
	"databaseURL": "https://random-survey-form-default-rtdb.europe-west1.firebasedatabase.app"
}

survey = pyrebase.initialize_app(firebaseConfig)
db = survey.database()


# analytics = getAnalytics(survey);
# Application views.

def get_session(request):
	if request.method=="POST":
		form = MyForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect("/thanks")
	else:
		form = MyForm()
	return render(request, "index.html", {"form": form})


def register_session(request):
	if request.method=="POST":
		# body = json.loads(request.body.decode("utf-8"))
		print(body)
		new_name = body.get("name")
		new_agreement = body.get("agreement")
		new_date = body.get("current_date")
		new_time = body.get("current_time")
		
		new_session = Form(name=new_name, agreement=new_agreement, current_date=new_date, current_time=new_time)
		new_session.save()
		return HttpResponse(status=200)
	else:
		return HttpResponseNotAllowed("Not supported")

def index(request):
	myform = MyForm()
	session = db.child("Session").child("Name").get().val
	all_sess = db.child("sessions").get().val()
	session_count = all_sess.__len__()
	total_count = session_count + 17
	# print(g)
	if request.method=="POST":
		print(request.POST)
		# print("G shit: ", g.__len__())#.val().__len__())
		form = MyForm(request.POST)
		if form.is_valid():
			# post = (request.POST)
			# pist = json.loads({"yes": "ans"})
			# merged_dict = {post** + pist**}
			data ={
				json.dumps(form.cleaned_data),
				"mess", "HU"
			}
			print("Pushin g to db",  (data))
			db.child("sessions").push(request.POST)
			print("Form pushed")
			# form.save()
		print("OUT")
	template = loader.get_template("index.html")
	context = {
		"myform": myform,
		# "session": session,
		"count": session_count,
		"total_count": total_count
	}
	return HttpResponse(template.render(context, request))

