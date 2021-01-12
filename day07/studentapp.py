import studentapi
from studentapi import  Human, Student

human = Human('james', 20)
print(human)
print("이름: %s, 나이: %d" % (human.print()))

st = Student('kim',25,'En')
print('이름: %s, 나이: %s, 전공: %s' % st.print())
print(st.print())
print(st.study())