import threading
import turtle  
window = turtle.Screen() 


def worker(step):
    timmy = turtle.Turtle()  
    timmy.forward(step) 
    timmy.right(90) 
    timmy.forward(100) 
    return

t = threading.Thread(target=worker, args=(100,))
t.start()

t = threading.Thread(target=worker, args=(200,))
t.start()

window.exitonclick() 
