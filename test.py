def simple_chatbot(input_text):
    # 사용자의 입력을 소문자로 변환
    input_text = input_text.lower()

    # 대답 정의
    if '안녕' in input_text:
        return '안녕하세요! 무엇을 도와드릴까요?'
    elif '이름' in input_text:
        return '저는 파이썬으로 만든 간단한 챗봇입니다.'
    elif '끝' in input_text or '종료' in input_text:
        return '대화를 종료합니다. 다시 만나요!'
    else:
        return '죄송해요, 이해하지 못했습니다. 다른 질문을 해주세요.'


# 챗봇 실행
while True:
    user_input = input("당신: ")
    response = simple_chatbot(user_input)
    print("챗봇: " + response)

    if '끝' in user_input.lower() or '종료' in user_input.lower():
        break