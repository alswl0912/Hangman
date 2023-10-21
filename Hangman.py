import string
import random

# 알파벳 소문자를 사용하기 위한 문자열
letters_set = string.ascii_lowercase

# 랜덤한 단어 길이를 3에서 10 사이에서 선택
word_length = random.randint(3, 10)

# 랜덤한 알파벳으로 이루어진 랜덤한 단어 생성
random_word = ''.join(random.choice(letters_set) for _ in range(word_length))

# 정답 단어를 표시하는 함수
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# 행맨 게임 로직을 포함한 함수
def hangman():
    word_to_guess = random_word
    guessed_letters = []
    max_attempts = 6
    remaining_attempts = max_attempts

    # 게임 시작 메시지 출력
    print("✧ʚ .·:*¨༺행맨 게임༻¨*:·. ɞ✧")
    
    while True:
        # 현재 상태 표시
        print("\n단어:", display_word(word_to_guess, guessed_letters))
        print("시도한 글자:", " ".join(guessed_letters))
        print(f"남은 시도 횟수: {remaining_attempts}")
        
        # 게임 종료 조건 확인
        if "_" not in display_word(word_to_guess, guessed_letters):
            print(f"축하합니다! \n✧ʚ .·:*¨༺정답은: {word_to_guess} 입니다.༻¨*:·. ɞ✧")
            break
        
        if remaining_attempts == 0:
            print(f"남은 목숨이 없습니다. \n✧ʚ .·:*¨༺정답은: {word_to_guess} 입니다.༻¨*:·. ɞ✧")
            break
        
        # 사용자의 추측 입력 받기
        guess = input("한 글자를 추측해보세요: ").lower()
        
        if len(guess) == 1 and guess in string.ascii_lowercase:
            if guess in word_to_guess:
                print("맞췄습니다!")
            else:
                print("틀린 추측입니다!")
                guessed_letters.append(guess)
                remaining_attempts -= 1
        else:
            print("올바른 영단어를 입력해주세요.")
    
    # 게임 종료 메시지 출력
    print("게임 종료")

if __name__ == "__main__":
    hangman()