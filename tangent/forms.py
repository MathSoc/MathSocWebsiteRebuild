from django import forms
from tangent.models import Organization, Announcement, OrganizationDocument, Position, Scholarship, Meeting, Member
from django.contrib.auth.models import User
#
# TODO idk what this is..
# class PageForm(forms.ModelForm):
# title = forms.CharField(max_length = 128,
#                             help_text = "Please enter the title of the page.")
#     url = forms.URLField(max_length = 200,
#                          help_text = "Please enter the URL of the page.")
#     views = forms.IntegerField(widget = forms.HiddenInput(),
#                                initial = 0)
#
#     class Meta:
#         model = Page
#
#         fields = ('title', 'url', 'views')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = {'username', 'email', 'password'}


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('website', 'picture')