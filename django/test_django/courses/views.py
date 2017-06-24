# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Course, Step
# Create your views here.

#def course_list(request):
#	courses = Course.objects.all()
#	output = ', '.join([str(course) for course in courses]) # has a string
#	return HttpResponse(output)

# https://teamtreehouse.com/library/python-comprehensions

def course_list(request):
	courses = Course.objects.all()
	return render(request, 'courses/course_list.html', {'courses' : courses})
	# https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/#render

def course_detail(request, pk):
	#course = Course.objects.get(pk=pk)
	course = get_object_or_404(Course, pk=pk)
	return render(request, 'courses/course_detail.html', {'course': course})

# LONG WAY FOR 404
# from django.http import Http404
#
# from .models import Course
#
# def course_detail(request, pk):
#    try:
#        course = Course.objects.get(pk=pk)
#    except Course.DoesNotExist:
#        raise Http404()
#    else:
#        return render(request, 'courses/course_detail.html', {'course': course})

def step_detail(request, course_pk, step_pk):
	step = get_object_or_404(Step, course_id=course_pk, pk=step_pk) # course_id is the foreign key field
	return render(request, 'courses/step_detail.html', {'step': step})