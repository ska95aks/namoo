import turtle as t
t.bgcolor("black")#배경색을 검정색으로 설정합니다.
for x in range(100):#0부터 99번까지 반복합니다.
    t.color("purple")#선 색을 보라색으로 설정합니다.
    t.fd(3*x)#앞으로 3*x만큼 이동합니다
    t.rt(30)#오른쪽으로 30만큼 회전합니다.
