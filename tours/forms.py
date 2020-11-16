from django import forms
from django.forms import ModelForm
from . models import Comment, ContactUs

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['user_name', 'user_comment']


class ContactUsForm(ModelForm):
	class Meta:
		model = ContactUs
		fields = ['name', 'email', 'tel', 'message']