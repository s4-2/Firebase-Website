from django.shortcuts import render
from django.contrib import auth
import pyrebase
import requests

from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

from google.oauth2 import id_token
from google.auth.transport import requests

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


'''firebaseConfig = {
  'apiKey': "AIzaSyCFbFeFrp4js-p4BFk2HNvQb_QdvmFo0l4",
  'authDomain': "stem-edce1.firebaseapp.com",
  'databaseURL' : "https://stem-edce1.firebaseio.com",
  'projectId': "stem-edce1",
  'storageBucket': "stem-edce1.appspot.com",
  'messagingSenderId': "778883960934",
  'appId': "1:778883960934:web:c36aad7df7ac6960bd9da7",
  'measurementId': "G-TMSFTMRVF6"
}'''



firebaseConfig = {
    'apiKey': "AIzaSyAiSuhBQNTgBAnL8-j6KcVksPBSpt-c7Bc",
    'authDomain': "fir-96fc3.firebaseapp.com",
    'databaseURL' : "https://fir-96fc3.firebaseio.com",
    'projectId': "fir-96fc3",
    'storageBucket': "fir-96fc3.appspot.com",
    'messagingSenderId': "928851673689",
    'appId': "1:928851673689:web:285bc84c01dc4e4980e748",
    'measurementId': "G-3QG74644C3"
  }


import firebase_admin
from firebase_admin import credentials

'''cred = credentials.Certificate("myproject/admin.json")
firebase_admin.initialize_app(cred)'''


firebase = pyrebase.initialize_app(firebaseConfig)


authe=firebase.auth()
database=firebase.database()

def signin(request):
    return render(request, "signin.html")

def postsign(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')

    try:
        user=authe.sign_in_with_email_and_password(email,passw)
    except:
        message="Invalid Credentials"
        return render(request, "signin.html", {'m':message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request, "welcome.html", {"e":email})

def logout(request):
    auth.logout(request)
    return render(request,'signin.html')


def signup(request):
    return render(request, 'signup.html')

def postsignup(request):
    
    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
    except:
        msg='Unable to create account try again'
        return render(request,'signin.html', {'msg':msg} )
    uid= user['localId']
   
    print('-------------->',uid)
    data={'name':name,'status':'1'}
    database.child('users').child(uid).child('details').set(data)
    return render(request, 'signin.html')

def create(request):
    return render(request, 'create.html')

@csrf_exempt
def post_create(request):
    import time
    from datetime import datetime, timezone
    import pytz

    tz = pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print("millis"+str(millis))

    work=request.POST.get('work')
    progress=request.POST.get('progress')
    idtoken = request.session['uid']
    
    a = authe.get_account_info(idtoken)
    print("Info"+str(a))

    data={ 
        "work":work,
        "progress":progress
    }
    database.child('users').child(a).child('reports').child('millis').set(data)
    return render(request, 'welcome.html')
    

