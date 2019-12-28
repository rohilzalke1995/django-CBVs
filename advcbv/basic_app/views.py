from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from basic_app import models
from django.urls import reverse_lazy

# Create your views here.


# class CBView(View):
#     def get(self, request):
#         return HttpResponse("Class Based views are cool.")



#
class IndexView(TemplateView):
    template_name = 'index.html'


class schoollistview(ListView):
    context_object_name = 'schools'
    model = models.School

class schooldetailview(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_details.html'

class schoolcreateview(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class schoolupdateview(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class schooldeleteview(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
