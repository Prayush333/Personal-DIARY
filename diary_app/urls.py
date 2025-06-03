
from django.contrib import admin
from django.urls import path
from diary_app import views

urlpatterns = [
    path('', views.NoteListView.as_view(), name="note_list"),
    path('detail_note/<int:pk>/', views.NoteDetailView.as_view(), name="detail_note"),
    path('add_note/', views.NoteAddView.as_view(), name="add_note"),
    path('edit_note/<int:pk>/', views.NoteEditView.as_view(), name="edit_note"),
    path('delete_note/<int:pk>/', views.NoteDeleteView.as_view(), name="delete_note"),
    path('register/', views.RegisterView.as_view(), name='register'),
]