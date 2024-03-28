def laundry_chatbot(input_text):
    input_text = input_text.lower()

    # 세탁기 모델 추천
    if '세탁기 추천' in input_text:
        return '''
        세탁기 추천 서비스입니다.
        - 가정용 소형: 모델 A123
        - 대용량 고성능: 모델 B456
        - 스마트 기능: 모델 C789
        귀하의 필요에 가장 적합한 모델을 선택해주세요.
        '''

    # 의류 재질에 따른 세탁 방법
    elif '면' in input_text:
        return '면 재질 의류는 미지근한 물에서 세탁하는 것이 좋으며, 강한 탈수는 피해주세요.'
    elif '울' in input_text:
        return '울 재질 의류는 찬물에서 손세탁하거나 울 전용 모드로 세탁하세요.'
    elif '실크' in input_text or '비스코스' in input_text:
        return '실크나 비스코스 재질 의류는 손세탁을 권장하며, 드라이클리닝을 고려해보세요.'
    elif '폴리에스터' in input_text:
        return '폴리에스터 재질 의류는 일반적인 세탁 방법으로 세탁할 수 있으나, 고온에서의 건조는 피해주세요.'
    else:
        return '죄송합니다. 해당 재질의 세탁 방법에 대한 정보를 찾을 수 없습니다. 다른 재질을 입력해주세요.'


while True:
    user_input = input("사용자: ")
    response = laundry_chatbot(user_input)
    print("챗봇: " + response)

    if '종료' in user_input.lower():
        print("챗봇: 대화를 종료합니다. 감사합니다!")
        break