from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from ventureprime.books.models import Book
from ventureprime.forms import ContactForm, CreateUser
from django.shortcuts import render
from django.core.mail import send_mail
import datetime
from django.utils.timezone import utc
from ventureprime.emailcollection.forms import EmailCollectionForm
from ventureprime.emailcollection.models import VPUser
from django.template import RequestContext, TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from emailusernames.utils import create_user
import OpenTokSDK

def method_splitter(request, *args, **kwargs):
#Redirects requests based on request type. *args passes through unknown positional
#arguments; kwargs passes through unknown keyword arguments (but we explicitly check
# GET and POST to see if views for these request types were specified, which they
#should've been in urls.py when calling this function)
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404

def homepage_get(request):
#serves up the home page if request method was GET
	#confirm the form was submitted via GET method, which includes first time 
	#views of the homepage
	assert request.method == 'GET'
	#make an EmailCollectionForm object to be passed in as context
	form = EmailCollectionForm()
	#serve up the home page with the specified form 
	return render(request, 'homepage/index.html', {'form': form})

def homepage_post(request):
#processes submission data from homepage
	#confirm the form was submitted (via POST method)
	assert request.method == 'POST'
	#find the current time (with utc timezone) to be stored with the submission
	current_datetime = datetime.datetime.utcnow().replace(tzinfo=utc)
	#store the submitted data in the variable 'form'
	form = EmailCollectionForm(request.POST)
	#check to make sure all required info was entered in proper format, type, etc
	if form.is_valid():
		#strip our just the data we want from the submission
		form_data = form.cleaned_data
		#store that data in a VPUser model object
		new_user = VPUser(
			date=current_datetime,
			email=form_data['email'],
			user_type=form_data['user_type']
			)
		##save this new user to the database
		new_user.save()
		##redirect the user to the confirmation page
		return HttpResponseRedirect('confirm_email')
		#return render_to_response('homepage/confirm.html',{'email': form_data['email']})
	#if something wasn't valid in their submission, show them what it was
	else:
		return render(request, 'homepage/index.html', {'form': form})

def confirm_email(request):
	return render_to_response('homepage/confirm.html')

def howvpworks_pages(request, user_type, page):
    try:
        return direct_to_template(request, 
        	template="howvpworks/%s/%s.html" % (user_type, page))
    except TemplateDoesNotExist:
        raise Http404()

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'none_provided@ventureprime.co'),
                ['lukehharris@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'footer/contact.html', {'form': form})

def comic(request):
	return render_to_response('tests/comic.html')

@login_required
def login_home(request):
    return render_to_response('accounts/login_home.html', {},
		context_instance=RequestContext(request))

@login_required
def start_video_session(request):
    OPENTOK_API_KEY = '21024092'
    OPENTOK_API_SECRET = '32081ce29ba11c87a2cafa5c2050a19aa5eda40c'
    opentok_sdk = OpenTokSDK.OpenTokSDK(OPENTOK_API_KEY,OPENTOK_API_SECRET)
    #try to establish P2P connection. If it fails, will use TokBox's servers
    session_properties = {OpenTokSDK.SessionProperties.p2p_preference: "enabled"}
    session = opentok_sdk.create_session(None, session_properties)
    token = opentok_sdk.generate_token(session.session_id)

    return render_to_response('accounts/video_session.html', 
        {'api_key': OPENTOK_API_KEY,
        'session': session, 
        'token': token},
        context_instance=RequestContext(request))

def create_account(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = create_user(
            	email=cd['email'], 
            	password=cd['password'])
            #login_new_user = authenticate(email=user.email, password=user.password)
            return HttpResponseRedirect('/accounts/create_successful/')
    else:
        form = CreateUser()
    return render(request, 'registration/create_account.html', {'form': form})