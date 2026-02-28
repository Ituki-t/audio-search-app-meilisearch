from .meili_client import get_meili
import os
import dotenv
dotenv.load_dotenv()

audio_index = os.getenv('MEILI_AUDIO_INDEX', 'audio_index')

def add_audio_documents(voice, segment):
    meili = get_meili()
    doc_id = f"{voice.id}_{int(segment['start']*1000)}"
    docs = [{
        'id': doc_id,
        'title': voice.title,
        'text': segment['text'],
        'start': segment['start'],
        'end': segment['end'],
        'voice_id': voice.id
    }]
    meili.index(audio_index).add_documents(docs)

def search_audio_ids(query):
    meili = get_meili()
    results = meili.index(audio_index).search(query)
    hit_ids = []
    for hit in results['hits']:
        hit_ids.append(hit['voice_id'])
    return hit_ids
