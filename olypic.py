import turtle as t

t.speed(20)  # 거북이 속도 #
t.pensize(20)  # 펜 두께조절 #

t.circle(100)  # 원크기 #

t.up()
t.forward(240)  # 앞으로 이동 거리 #
t.down()
t.pencolor('red')  # 원 색상 #
t.circle(100)  # 원 크기 #

t.up()
t.backward(480)
t.down()
t.pencolor('blue')
t.circle(100)

t.up()
t.forward(240)
t.down()
t.pencolor('black')
t.circle(100)

t.up()
t.backward(120)
t.goto(-110, -100)  ## 좌표 x,y 값 ##
t.down()
t.pencolor('yellow')
t.circle(100)

t.up()
t.forward(240)
t.goto(120, -100)
t.down()
t.pencolor('green')
t.circle(100)






t.done()