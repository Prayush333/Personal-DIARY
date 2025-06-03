from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note


