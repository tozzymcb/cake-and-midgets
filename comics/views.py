from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from comics.models import Comic

import os
# Create your views here.

def home(request):
	comics = Comic.objects.filter(published=True).order_by("-posted_on")[:2]
	if(comics):
		latest_comic = comics[0]
		if len(comics) > 1:
			previous_comic = comics[1]
			return render_response(request, 'home.html', {'latest':latest_comic, 'previous':previous_comic})	
		else:
			return render_response(request, 'home.html', {'latest':latest_comic})	
	else:
		return render_response(request, 'home.html')

def _get_prev(comic):
	prev = Comic.objects.filter(posted_on__lt=comic.posted_on, published=True).order_by('-posted_on')[:1]
	if(len(prev) > 0):
		return prev[0]
	else:
		return None

def _get_next(comic):
	next_c = Comic.objects.filter(posted_on__gt=comic.posted_on, published=True)[:1]
	if(len(next_c) > 0):
		return next_c[0]
	else:
		return None


def comic(request, comic_name):
	this_comic = Comic.objects.get(slug=comic_name, published=True)
	prev_comic = _get_prev(this_comic)
	next_comic = _get_next(this_comic)
	return render_response(request, 'comic.html', {'latest': this_comic, 'previous':prev_comic, 'next':next_comic})

def archive(request):
	comics = Comic.objects.filter(published=True).order_by('-posted_on')
	return render_response(request, 'archive.html', {'archive':comics})


def random(request):
	random_comic = Comic.objects.filter(published=True).order_by('?')[:1][0]
	prev_comic = _get_prev(random_comic)
	next_comic = _get_next(random_comic)
	return render_response(request, 'home.html', {'latest':random_comic, 'previous':prev_comic, 'next':next_comic})

def deploy(request):
	response = ""
	p = os.popen('cd /home/chris/public_html/cake-and-midgets; git pull origin master; python manage.py migrate')
	for line in iter(p.readline,''):
		response = response + line
	p.close()
	return HttpResponse(response)

def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)


