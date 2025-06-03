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
        return Note.objects.filter(user=self.request.user)


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
    

      


