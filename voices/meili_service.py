from .meili_client import get_meili
import os

import dotenv
dotenv.load_dotenv()

aidio_index = os.getenv('MEILI_INDEX', 'audio_index')


def add_audio_documents(voice, text):
    meili = get_meili()
    meili.index(aidio_index).add_documents([{
        'title': voice.title,
        'text': text,
        'voice_id': voice.id
    }])