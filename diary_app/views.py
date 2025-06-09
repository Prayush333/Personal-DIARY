from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView,UpdateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from django.contrib.auth.forms import UserCreationForm


class NoteListView( LoginRequiredMixin, ListView):
    model= Note
    template_name='diary/note_list.html'
    context_object_name = 'notes'
     
    def get_queryset(self):
        qs = Note.objects.filter(user=self.request.user).order_by('created_at')
        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(title__icontains=search)

        return qs

    def get_paginate_by(self, queryset):
        paginate_by = self.request.GET.get('paginate', 5)
        try:
            return int(paginate_by)
        
        except (ValueError, TypeError):
            return 5
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paginate_options'] = ['5', '10', '20', '50']
        return context


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'diary/detail_note.html'
    context_object_name = 'note'


class NoteAddView( LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'diary/add_note.html'
    success_url = reverse_lazy('note_list') 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

     


class NoteEditView(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'diary/edit_note.html'
    fields = ['title', 'content']
    success_url =reverse_lazy('note_list')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)



class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'diary/delete_note.html'
    success_url = reverse_lazy('note_list') 

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    

      


