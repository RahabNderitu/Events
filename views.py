from django.shortcuts import render
# from django.template import loader
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model



# Create your views here.
def index(request): 
    # context = {
    #     'page': 'index',
    #     'coverHeading': 'Search Events'
    # }
    return render(request, 'events/login.html')

# def login(request):
#     return render(request, 'registration/login.html')  
# def register(request):
#     return render(request, 'registration/register.html')  
def forgotpassword(request):
    return render(request, 'events/forgotpassword.html')  
def dashboard(request):
    return render(request, 'events/dashboard.html')
def register(request):
    return render(request, 'events/register.html')

def login(request):
    return render(request, 'events/login.html')

def do_login(request):
    request_method = request.method
    print('request_method = ' + request_method)
    if request_method == 'POST':
        user_name = request.POST.get('user_name','')
        password = request.POST.get('password', '')
        # authenticate user account.
        user = auth.authenticate(request, username=user_name, password=password)
        if user is not None:
            # login user account.
            auth.login(request, user)
            response = HttpResponseRedirect('/events/dashboard')
            # set cookie to transfer user name to login success page.
            response.set_cookie('user_name', user_name, 3600)
            return response
        else:
            error_json = {'error_message': 'User name or password is not correct.'}
            return render(request, '/events/login.html', error_json)
    else:
        return render(request, '/events/login.html')
def do_register(request):
    request_method = request.method
    print('request_method = ' + request_method)
    if request_method == 'POST':
        user_name = request.POST.get('user_name', '')
        user_password = request.POST.get('user_password', '')
        user_email = request.POST.get('user_email', '')
        if len(user_name) > 0 and len(user_password) > 0 and len(user_email) > 0:
            # check whether user account exist or not.
            user = auth.authenticate(request, username=user_name, password=user_password)
            # if user account do not exist.
            if user is None:
                # create user account and return the user object.
                user = get_user_model().objects.create_user(username=user_name, password=user_password, email=user_email)
                # update user object staff field value and save to db.
                if user is not None:
                    user.is_staff = True
                    # save user properties in sqlite auth_user table.
                    user.save()
                # redirect web page to register success page.
                response = HttpResponseRedirect('/events/login/')
                # set user name, pasword and email value in session.
                request.session['user_name'] = user_name
                request.session['user_password'] = user_password
                request.session['user_email'] = user_email
                return response
            else:
                error_json = {'error_message': 'User account exist, please register another one.'}
                return render(request, 'events/register.html', error_json)
        else:
            error_json = {'error_message': 'User name, password and email can not be empty.'}
            return render(request, 'events/register.html', error_json)
    else:
        return render(request, 'events/register.html')

# def register(request):
#     # dec vars
#     username = str(request.POST['username']).lower()
#     email = str(request.POST['email']).lower()
#     password = str(request.POST['password'])

#     # check if username or email is used
#     username_check = User.objects.filter(username=username)
#     email_check = User.objects.filter(email=email)

#     if username_check:
#         response = {
#             'status': 'fail',
#             'error_msg': 'username already in use'
#         }
#     elif email_check:
#         response = {
#             'status': 'fail',
#             'error_msg': 'email already in use'
#         }
#     elif len(password) < 8:
#         response = {
#             'status': 'fail',
#             'error_msg': 'password must be atleast 8 characters long'
#         }
#     else:
#         # creating a  user
#         user = User.objects.create_user(username, email, password)

#         # login user
#         login(request, user)

#         # create response
#         response = {
#             'status': 'success',
#         }

#     # send reponse JSON
#     return JsonResponse(response)


# def login(request):
#     # dec vars
#     username = request.POST['username']
#     password = request.POST['password']
#     # user Auth
#     user = authenticate(request, username=username, password=password)

#     if user:
#         login(request, user)
#         # creating response
#         response = {
#             'status': 'success'
#         }
#     else:
#         # creating response
#         response = {
#             'status': 'fail'
#         }

#     # send reponse JSON
#     return JsonResponse(response)
   
# def formView(request):
#    if request.session.has_key('username'):
#       username = request.session['username']
#       return render(request, 'loggedin.html', {"username" : username})
#    else:
#       return render(request, 'login.html', {})

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             userObj = form.cleaned_data
#             username = userObj['username']
#             email =  userObj['email']
#             password =  userObj['password']
#             if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
#                 User.objects.create_user(username, email, password)
#                 user = authenticate(username = username, password = password)
#                 login(request, user)
#                 return HttpResponseRedirect('/login/')    
#             else:
#                 raise forms.ValidationError('Looks like a username with that email or password already exists')
                
#     else:
#         form = UserRegistrationForm()
        
#     return render(request, '/register.html', {'form' : form})  


# def register(request):
#     context = {
#         'page': 'register'
#     }
#     return render(request, 'events/register.html', context)


# def createEventPage(request):
#     context = {
#         'page': 'createEvent',
#         'coverHeading': 'Create Event'
#     }
#     return render(request, 'events/createEvent.html', context)


# def allEvents(request):
#     # Get Events
#     events = Event.objects.all()

#     context = {
#         'page': 'allEvents',
#         'coverHeading': 'All Events',
#         'events': events
#     }
#     return render(request, 'events/allEvents.html', context)


# def myEvents(request):
#     # Dec  Vars
#     user = request.user

#     # redirect to signin page if user not found
#     try:
#         events = Event.objects.filter(creator=user)
#     except TypeError:
#         return redirect('register')

#     context = {
#         'page': 'myEvents',
#         'coverHeading': 'My Events',
#         'events': events
#     }
#     return render(request, 'events/myEvents.html', context)


# def editEvent(request, event_id):
#     # Dec  Vars
#     event = get_object_or_404(Event, pk=event_id)
#     context = {
#         'page': 'editEvent',
#         'coverHeading': 'Edit Event',
#         'event': event
#     }
#     return render(request, 'events/editEvent.html', context)


# # AJAX




# def logoutUser(request):
#     # log out user
#     logout(request)

#     # send to home page
#     return redirect('index')


# def searchEvents(request):
#     # dec vars
#     event_search = json.loads(request.body)['event_search']

#     # filter for matching events and serialize for json
#     event_search_results = list(Event.objects.filter(
#         name__icontains=event_search
#     ).values(
#         'id',
#         'name',
#         'event_type',
#         'start_date',
#         'attendees'
#     ))

#     # create response
#     response = {
#         'status': 'success',
#         'event_search_results': event_search_results
#     }

#     # send reponse JSON
#     return JsonResponse(response)


# def eventDetails(request):
#     # get event
#     event_id = json.loads(request.body)['event_id']
#     event = get_object_or_404(Event, pk=event_id)

#     # serialize json
#     serialized_event = serializers.serialize('json', [event])

#     # create response
#     response = {
#         'status': 'success',
#         'event': serialized_event
#     }

#     # send reponse JSON
#     return JsonResponse(response)


# def eventJoin(request):
#     # get event
#     user_id = int(request.POST['user-id'])
#     event_id = int(request.POST['event-id'])
#     user = User.objects.get(pk=user_id)
#     event = Event.objects.get(pk=event_id)

#     # add user to event
#     event.attendees.add(user)

#     # get updated attendance count
#     attendance = event.attendees.all().count()

#     # create response
#     response = {
#         'status': 'success',
#         'attendance': attendance
#     }

#     # send reponse JSON
#     return JsonResponse(response)


# def createEvent(request):
#     # dec vars
#     event_title = str(request.POST['event-title']).title()
#     event_type = str(request.POST['event-type'])
#     event_location = str(request.POST['event-location'])
#     event_description = str(request.POST['event-description'])
#     event_start_date = str(request.POST['event-start-date'])
#     event_start_time = str(request.POST['event-start-time'])
#     event_end_date = str(request.POST['event-end-date'])
#     event_end_time = str(request.POST['event-end-time'])
#     creator = request.user

#     # create event
#     Event.objects.create(
#         name=event_title,
#         event_type=event_type,
#         creator=creator,
#         location=event_location,
#         description=event_description,
#         start_date=event_start_date,
#         start_time=event_start_time,
#         end_date=event_end_date,
#         end_time=event_end_time
#     )

#     # #create response
#     response = {
#         'status': 'success',
#     }

#     # send reponse JSON
#     return JsonResponse(response)


# def updateEvent(request, event_id):
#     # dec vars
#     event_title = str(request.POST['event-title']).title()
#     event_type = str(request.POST['event-type'])
#     event_location = str(request.POST['event-location'])
#     event_description = str(request.POST['event-description'])
#     event_start_date = str(request.POST['edit-event-start-date'])
#     event_start_time = str(request.POST['edit-event-start-time'])
#     event_end_date = str(request.POST['edit-event-end-date'])
#     event_end_time = str(request.POST['edit-event-end-time'])
#     event = get_object_or_404(Event, pk=event_id)

#     # Update Event
#     event.name = event_title
#     event.event_type = event_type
#     event.location = event_location
#     event.description = event_description

#     # only update new dates/times
#     if event_start_date:
#         event.start_date = event_start_date

#     if event_end_date:
#         event.end_date = event_end_date

#     if event_start_time:
#         event.start_time = event_start_time

#     if event_end_time:
#         event.end_time = event_end_time

#     # Save updated event
#     event.save()

#     # create response
#     response = {
#         'status': 'success',
#     }

#     # send reponse JSON
#     return JsonResponse(response)


# def removeEvent(request):
#     # dec vars
#     event_id = json.loads(request.body)['event_id']
#     event = get_object_or_404(Event, pk=event_id)

#     # delete event
#     event.delete()

#     # create response
#     response = {
#         'status': 'success',
#     }

#     # send reponse JSON
#     return JsonResponse(response)


# def searchSystems(request):
#     system_query = json.loads(request.body)['system_query']
#     results = list(SolarSystem.objects.filter(name__icontains=system_query).values('name')[:5])

#     # create response
#     response = {
#         'status': 'success',
#         'results': results
#     }

#     # send reponse JSON
#     return JsonResponse(response)



   
    





