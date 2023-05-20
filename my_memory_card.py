from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import randint

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.q = question
        self.ra = right_answer
        self.w1 = wrong1
        self.w2 = wrong2
        self.w3 = wrong3

q1 = Question('Какой национальности не существует?','Энцы','Смурфы','Чулымцы','Алеуты')
q2 = Question('2+2x2','8','6','16','2')
q3 = Question('Государственный язык Бразилии','Португальский','Испанский','Английский','Бразильский')

button_ok = QPushButton('Ответить')
question_label = QLabel('Какой национальности не существует?')

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

AnsGroupBox = QGroupBox('Результаты теста')
q1_result = QLabel('прав ты или нет?')
ans_result = QLabel('ответ на вопрос')

ans = QVBoxLayout()
ans.addWidget(q1_result,alignment = (Qt.AlignVCenter | Qt.AlignHCenter))

ans2 = QVBoxLayout()
ans2.addWidget(ans_result,alignment = (Qt.AlignHCenter))
setLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question_label, aligment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStrech(1)
layout_line3.addWidget(button_ok, strech=2)
layout_line3.addStrech(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, strech=2)
layout_card.addLayout(layout_line2, strech=8)
layout_card.addLayout(layout_line3, strech=2)

layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button_ok.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button_ok.setText('Ответить')
    RadioGroupBox.setExlusive(False)
    rbtn_1.setCheched(False)
    rbtn_2.setCheched(False)
    rbtn_3.setCheched(False)
    rbtn_4.setCheched(False)
    RadioGroupBox.setExlusive(True)

def start_test():
    if button_ok.text() == 'Ответить':
        show_result()
    else:
        show_question()

def ask(question, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[rbtn_1].setText(right_answer)
    answers[rbtn_2].setText(wrong1)
    answers[rbtn_3].setText(wrong2)
    answers[rbtn_4].setText(wrong3)
    q1_question.setText('')
    q1_correct.setText(right_answer)
    show_question()

#def show_correct():


#def check_answer():


questions_list = [q1,q2,q3]

def next_question():
    cur_question = randint(0, len(question_left) - 1)
    q = questions_list[cur_question]

q: Question

next_question()
window.setLayout(layout_card)
window.show()
app.exec()