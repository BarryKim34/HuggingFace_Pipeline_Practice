import torch
import json
from transformers import pipeline

def reset_model():
    device = 0 if torch.cuda.is_available() else -1
    return pipeline('zero-shot-classification', model='MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7', device=device)


def set_up():
    mbti_labels = {
            '자기 외부에 주의 집중, 외향적인 활동과 사람을 선호': 'E',
            '자기 내부에 주의 집중, 내향적인 휴식과 혼자만의 시간을 선호': 'I',
            '현실주의적, 오감 및 경험에 의존': 'S',
            '이상주의적, 직관 및 영감에 의존': 'N',
            '논리적이고 객관적인 판단을 중시': 'T', 
            '인간관계와 감정적 공감을 중시': 'F',
            '계획적이고 체계적인 생활을 선호': 'J', 
            '즉흥적이고 유연한 상황 대처를 선호': 'P'
        }

    personality_labels = {
            'EI': ['자기 외부에 주의 집중, 외향적인 활동과 사람을 선호', '자기 내부에 주의 집중, 내향적인 휴식과 혼자만의 시간을 선호'],
            'SN': ['현실주의적, 오감 및 경험에 의존', '이상주의적, 직관 및 영감에 의존'],
            'TF': ['논리적이고 객관적인 판단을 중시', '인간관계와 감정적 공감을 중시'],
            'JP': ['계획적이고 체계적인 생활을 선호', '즉흥적이고 유연한 상황 대처를 선호']
        }
    return mbti_labels, personality_labels

def load_questions(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)