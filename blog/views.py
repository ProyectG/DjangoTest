# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
#from django.template.loader import get_template
#from django.template import Template, Context
#from django.http import HttpResponse
#from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.


def post_list(request):
	posts = Post.objects.filter(publicado_fecha__lte=timezone.now()).order_by('publicado_fecha')
	#t = get_template('post.html')
	#html = t.render(Context({'posts':posts}))
	return  render_to_response('post.html', {'posts':posts})
