from django.contrib import admin
from .models import Voice

# Register your models here.


class VoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploaded_at')

admin.site.register(Voice, VoiceAdmin)