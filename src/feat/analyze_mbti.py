def analyze_mbti(clf, answer, targets, m_labels, p_labels, total_score):
    # 답변 분석
    for target in targets:
        candidate_labels = p_labels[target]
        output = clf(
            answer,
            candidate_labels=candidate_labels,
            hypothesis_template='이 사람은 {}하는 사람이다.'
        )        
        for label, score in zip(output['labels'], output['scores']):
            short_label = m_labels[label]
            total_score[short_label] += score
            
    return total_score

def print_result(total_score):
    # 결과 출력
    result = ''
    result += 'E' if total_score['E'] > total_score['I'] else 'I'
    result += 'S' if total_score['S'] > total_score['N'] else 'N'
    result += 'T' if total_score['T'] > total_score['F'] else 'F'
    result += 'J' if total_score['J'] > total_score['P'] else 'P'
    print(f'\n당신의 MBTI는 {result}입니다.')
    
    mbti_detail = {
        'E': {'score': 0, 'description': '외향형'},
        'I': {'score': 0, 'description': '내향형'},
        'S': {'score': 0, 'description': '감각형'},
        'N': {'score': 0, 'description': '직관형'},
        'T': {'score': 0, 'description': '사고형'},
        'F': {'score': 0, 'description': '감정형'},
        'J': {'score': 0, 'description': '판단형'},
        'P': {'score': 0, 'description': '인지형'},                            
    }
    
    sections = [('E', 'I'), ('S', 'N'), ('T', 'F'), ('J', 'P')]
    
    for former, latter in sections:
        mbti_detail[former]['score'] = round(total_score[former] / (total_score[former] + total_score[latter]), 2) * 100
        mbti_detail[latter]['score'] = 100 - mbti_detail[former]['score']
        if mbti_detail[former]['score'] > mbti_detail[latter]['score']:
            print(f'{former}({mbti_detail[former]['description']}): {mbti_detail[former]['score']}%')
        else:
            print(f'{latter}({mbti_detail[latter]['description']}): {mbti_detail[latter]['score']}%')
    
    return result, mbti_detail