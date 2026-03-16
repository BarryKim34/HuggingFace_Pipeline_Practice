import random
from src.feat.preparation import reset_model, set_up, load_questions
from src.feat.analyze_mbti import analyze_mbti, print_result

def run_process():
    clf = reset_model()
    mbti_labels, personality_labels = set_up()
    questions = load_questions('./src/data/questions.json')
    total_score = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

    selected_questions = random.sample(questions, 3)

    print('간이 MBTae 분석을 시작합니다.\n만약 나라면 어떤 생각을 할까에 대하여 답변해주세요.\n(최소 3문장 이상의 답변으로 부탁드립니다!)')

    for i, item in enumerate(selected_questions):
        print(f'\nQ{i+1}: {item['q']}')
        answer = input('답변: ')
        print(f'A{i+1}: {answer}')
        total_score = analyze_mbti(clf, answer, item['targets'], mbti_labels, personality_labels, total_score)
    
    final_mbti, mbti_detail = print_result(total_score)

if __name__ == "__main__":
    run_process()