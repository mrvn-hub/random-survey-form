from django.shortcuts import render
from django.core import serializers
from django.http import Http404, HttpResponseNotAllowed, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Form
from .myform import MyForm
from django.template import loader
import json, pyrebase, math, os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()



firebaseConfig = {
	"apiKey": os.getenv("FIREBASE_API_KEY"),
	"authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
	"projectId": os.getenv("FIREBASE_PROJECT_ID"),
	"storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
	"messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
	"appId": os.getenv("FIREBASE_APP_ID"),
	"databaseURL": os.getenv("FIREBASE_DB_URL")
}

survey = pyrebase.initialize_app(firebaseConfig)
db = survey.database()

def index(request):
	myform = MyForm()
	session = db.child("Session").child("Name").get().val
	all_sess = db.child("sessions").get().val()
	session_count = all_sess.__len__()
	total_count = session_count + 17
	if request.method=="POST":
		print(request.POST)
		form = MyForm(request.POST)
		if form.is_valid():

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
		"count": session_count,
		"total_count": total_count
	}
	return HttpResponse(template.render(context, request))

