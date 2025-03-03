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

    # Faire une requête POST à l'API Watson NLP
    response = requests.post(url, headers=headers, json=input_data)

    # Vérifier que la réponse est valide (code 200)
    if response.status_code == 200:
        # Convertir la réponse en dictionnaire
        response_data = response.json()

        # Afficher la réponse complète pour débogage
        print("Réponse de l'API:", response_data)

        # Accéder aux émotions dans la première prédiction
        emotions = response_data['emotionPredictions'][0]['emotion']

        # Extraire les émotions et leurs scores
        anger_score = emotions.get("anger", 0)
        disgust_score = emotions.get("disgust", 0)
        fear_score = emotions.get("fear", 0)
        joy_score = emotions.get("joy", 0)
        sadness_score = emotions.get("sadness", 0)

        # Trouver l'émotion dominante (celle avec le score le plus élevé)
        emotion_scores = {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)  # Trouver l'émotion avec le score le plus élevé

        # Créer le dictionnaire de sortie avec la structure demandée
        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

        return result
    else:
        print("Erreur lors de la requête à l'API, code:", response.status_code)
        return None

# Exemple d'appel à la fonction
text_to_analyze = "Je déteste travailler de longues heures"
result = emotion_detector(text_to_analyze)

if result:
    print(result)
