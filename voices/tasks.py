from celery import shared_task
from django.db import transaction
from .models import Voice

from .whisper_service import transcribe_audio_file
from .es_service import index_voice

import logging
logger = logging.getLogger(__name__)

@shared_task
def add(a, b):
    return a + b


@shared_task
def transcribe_voice(voice_id):
    voice = Voice.objects.get(id=voice_id)
    voice.transcribe_status = "running"
    voice.save(update_fields=['transcribe_status'])

    text = transcribe_audio_file(voice.audio_file.path)
    index_voice(voice, text)

    voice.transcribe_status = "done"
    voice.save(update_fields=['transcribe_status'])
    return text