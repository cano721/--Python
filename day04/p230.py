st = [
    {'id': 'str', 'ko':90, 'en':100, 'ma':99},
    {'id': 'str2', 'ko':91, 'en':90, 'ma':98},
    {'id': 'str3', 'ko':92, 'en':91, 'ma':97}
]

#학생 별 성적 평균과
#전체 학생의 과목 별 평균을 출력 하시오


for sts in st:
    print("%s 학생의 평균 %.2f" % (sts.get('id'),((sts.get('ko') + sts.get('en') + sts.get('ma'))/3)))

kosum = 0;
ensum = 0;
masum = 0;

for sts in st:
    kosum += sts.get('ko')
    ensum += sts.get('en')
    masum += sts.get('ma')
cnt = len(st)
print('과목별 평균 %.2f %.2f %.2f' % ((kosum/cnt),(ensum/cnt),(masum/cnt)))





    # sum += i[1:].values()
    # print(sum)