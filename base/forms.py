from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import FormOne, User
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class RoomForm(forms.ModelForm):
    class Meta:
        model = FormOne
        fields = ['protocol_service', 'protocol_type', 'src_bytes', 'dst_bytes', 'the_count', 'srv_count', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'label']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']