from .meili_client import get_meili
import os

import dotenv
dotenv.load_dotenv()

audio_index = os.getenv('MEILI_INDEX', 'audio_index')


def add_audio_documents(voice, text):
    meili = get_meili()
    meili.index(audio_index).add_documents([{
        'title': voice.title,
        'text': text,
        'voice_id': voice.id
    }])

def search_audio_ids(query):
    meili = get_meili()
    results = meili.index(audio_index).search(query)
    hit_ids = []
    for hit in results['hits']:
        hit_ids.append(hit['voice_id'])
    return hit_ids