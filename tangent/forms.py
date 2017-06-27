from django import forms
from tangent.models import Announcement
from django.contrib.auth.models import User

class ListField(forms.CharField):
	def clean(self, value):
		if self.required and not value:
			raise ValidationError
		return value.split()

class AddMembersForm(forms.Form):
	watids = ListField(required=True, widget=forms.Textarea)
