from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
from ventureprime.books.models import Book

def homepage(request):
    current_date = datetime.datetime.now()
    return render_to_response('homepage/index.html', locals())

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
	return render_to_response('footer/contact.html')

def comic(request):
	return render_to_response('tests/comic.html')