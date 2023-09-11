from django.contrib import admin

# Register your models here.
from .models import FormOne, Attack, User, Message

admin.site.register(FormOne)
admin.site.register(Attack)
admin.site.register(User)
admin.site.register(Message)