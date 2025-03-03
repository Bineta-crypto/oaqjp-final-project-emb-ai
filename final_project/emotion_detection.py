import requests
import json

def emotion_detector(text_to_analyze):
    # Définir l'URL de l'API Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Définir les en-têtes de la requête
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Créer le corps de la requête (le texte à analyser)
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
