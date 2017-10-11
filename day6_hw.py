import turtle as t 
t.shape("turtle") 
angle=205 
t.bgcolor("black") 
t.speed("fastest") 
for x in range(600): 
    if x%3==0: 
        color="red" 
    if x%3==1: 
        color="blue" 
    if x%3==2:
        color="white" 
    t.color(color) 
    t.forward(x) 
    t.left(angle) 
