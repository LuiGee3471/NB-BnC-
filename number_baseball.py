from random import sample

class Num_baseball(object):
    one_to_ten = [i for i in range(1, 10)]

    def __init__(self):
        print("숫자 야구 게임에 오신 것을 환영합니다.")
        _history = []
        self._history = _history

    def select_digit(self):
        while True:
            digit = input('\n플레이할 자리 수를 골라주세요. (3 / 4) ')
            try:
                digit = int(digit)
            except ValueError:
                print('\n숫자를 입력해주세요.')
                continue
            else:
                if digit not in (3, 4):
                    print('\n3이나 4를 입력해주세요')
                    continue
                else:
                    self.digit = digit
                    break
        answer = list(sample(Num_baseball.one_to_ten,  k=digit))
        self.answer = answer
        self.history_or_guess()

    def history_or_guess(self):
        loop = 'on'
        while loop == 'on':
            check = input(
                '\n1. 숫자 추측하기\n2. 지금까지의 기록 보기\n'
                )
            if check not in ('1', '2'):
                print("\n'1'이나 '2'를 입력해주세요.")
                continue
            elif check == '1':
                loop = 'off'
            else:
                self.history()
        self.guess_number(self.answer)

    def history(self):
        for record in self._history:
            print(record, end='\n')
            
    def guess_number(self, answer):
        ball = 0
        strike = 0
        
        try:
            guess = [
                int(input('\n{0}번째 숫자를 입력해주세요. (1 ~ 9) '\
                .format(i + 1))) for i in range(self.digit)
                ]
        except ValueError:
            print('\n숫자를 입력해주세요.')

        dupl = []
        for i in guess:
            if i not in dupl:
                dupl.append(i)

        if dupl != guess:
            print('\n서로 다른 숫자를 입력해주세요.')
            self.history_or_guess()

        for i in guess:
            if i in answer and guess.index(i) ==answer.index(i):
                strike += 1
            elif i in answer and guess.index(i) !=answer.index(i):
                ball += 1
        print(
            '\nB {0}      ({2}B {3}S)\nS {1}'\
            .format('●'*ball, '●'*strike, ball, strike)
            )

        if strike == self.digit:
            print('\n{0}스트라이크입니다. 정답입니다!'.format(self.digit))
            self._history.clear()
        else:
            self._history.append('{0}, {1}B {2}S'.format(tuple(guess), ball, strike))
            self.history_or_guess()

    def replay(self):
        re = 'Y'
        while re != 'N':
            re = input('\n다시 하시겠어요? (Y / N) ').upper()
            if re not in ('Y', 'N'):
                print("\n'Y'나 'N'으로 입력해주세요.")
            elif re == 'Y':
                return 'replay'
        return 'end'

replay = 'replay'
play = Num_baseball()
while replay != 'end':
    play.select_digit()
    replay = play.replay()
