from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from ventureprime.books.models import Book
from ventureprime.forms import ContactForm
from django.shortcuts import render
from django.core.mail import send_mail
from ventureprime.emailcollection.forms import EmailCollectionForm
import datetime
from django.utils.timezone import utc
from ventureprime.emailcollection.models import VPUser

def homepage(request):
	current_datetime = datetime.datetime.utcnow().replace(tzinfo=utc)
	if request.method == 'POST':
		form = EmailCollectionForm(request.POST)
		if form.is_valid():
			form_data = form.cleaned_data
			#do stuff with the data entered here
			new_user = VPUser(date=current_datetime,email=form_data['email'],
				user_type=form_data['user_type'])
			new_user.save()
			return HttpResponseRedirect('confirm_email')
	else:
		form = EmailCollectionForm()
	return render(request, 'homepage/index.html', {'form': form})

def confirm_email(request):
	return render_to_response('homepage/confirm.html')

def email_submit(request):
    if 'email' in request.GET:
        message = 'You entered: %r' % request.GET['entry']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('tests/current_datetime.html', locals())

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
        	error = True
        else:
        	books = Book.objects.filter(title__icontains=q)
        	return render_to_response('tests/search_results.html',
            	{'books': books, 'query': q})
    return render_to_response('tests/search_form.html', {'error': error})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'footer/contact.html', {'form': form})

def comic(request):
	return render_to_response('tests/comic.html')