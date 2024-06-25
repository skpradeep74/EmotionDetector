import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers=header)
    
    if response.status_code ==400:
        return {'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None}

    emotions = json.loads(response.text)
    dict_emotion = emotions['emotionPredictions'][0]['emotion']
    
    dominant_emotion =""
    dominant_score =0
    for emotion_type,value in dict_emotion.items():
        
        if dominant_score < value:
            dominant_score= value
            dominant_emotion=emotion_type

        if emotion_type=='anger':
            anger_score = value
        elif emotion_type=='disgust':
            disgust_score = value
        elif emotion_type=='fear':
            fear_score = value
        elif emotion_type=='joy':
            joy_score = value
        elif emotion_type=='sadness':
            sadness_score = value

    return {'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion}

