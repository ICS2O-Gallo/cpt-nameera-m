screen = 'screen'
start_loc = PVector(250, 600)
start_size = PVector(500, 100)
screen_number = 1
b_loc = PVector(50, 272)
b_size = PVector(35, 45)
a_loc = PVector(50, 172)
a_size = PVector(35, 45)
c_loc = PVector(50, 372)
c_size = PVector(35, 45)



def setup():
    size(1000, 800)
def draw():
    
    global correct_screen
    global incorrect_screen
    global screen
    global screen1
    global screen_number
    global screen2
    global screen3
    global screen4
    global screen5
    
    
    
    if screen == 'screen1':
        background(255)
        fill(0)
        rect(0, 0, 500, 800)
        fill(51, 255, 255)
        textSize(200)
        text("jeoPARTY",30 , 200)
        rect(start_loc.x, start_loc.y, start_size.x, start_size.y)
        textSize(50)
        fill(0)
        text("START", 410, 675)
        
    if screen == 'screen2':
        background(255)
        fill(255)
        # rect(50, 172, 35, 45)
        # rect(50, 272, 35, 45)
        # rect(50, 372, 35, 45)
        fill(0)
        textSize(32)
        text("What is one plus one?", 50, 100)
        text("a) 7", 50, 200)
        text("b) 2", 50, 300)
        text("c) 6", 50, 400)
        
    if screen == 'screen3':
        background(255)
        fill(0)
        textSize(32)
        text("What is the capital city of England?", 50, 100)
        text("a) London", 50, 200)
        text("b) Manchester", 50, 300)
        text("c) Ottawa", 50, 400)
        
    if screen == 'screen4':
        background(255)
        fill(0)
        textSize(32)
        text("What is the sum of 2225 and 3476?", 50, 100)
        text("a) 5700", 50, 200)
        text("b) 5701", 50, 300)
        text("c) 5702", 50, 400)
    
    if screen == 'screen5':
        background(255)
        fill(0)
        textSize(32)
        text("What is the population of Canada?", 50, 100)
        text("a) 30 million", 50, 200)
        text("b) 40 million", 50, 300)
        text("c) 36 million", 50, 400)
        
    if screen == 'screen6':
        background(255)
        fill(0)
        textSize(32)
        text("What city has the largest population?", 50, 100)
        text("a) Toronto", 50, 200)
        text("b) London", 50, 300)
        text("c) Tokyo", 50, 400)

    if screen == 'screen7':
        background(255)
        fill(0)
        textSize(32)
        text("What is the most spoken language in the world?", 50, 100)
        text("a) Chinese", 50, 200)
        text("b) English", 50, 300)
        text("c) Russian", 50, 400)
        
    if screen == 'screen8':
        background(255)
        fill(0)
        textSize(32)
        text("What is the longest river in the world?", 50, 100)
        text("a) Nile", 50, 200)
        text("b) Amazon", 50, 300)
        text("c) Mississippi", 50, 400)
        
    if screen == 'screen9':
        background(255)
        fill(0)
        textSize(32)
        text("Which planet has the most moons?", 50, 100)
        text("a) Jupiter", 50, 200)
        text("b) Saturn", 50, 300)
        text("c) Earth", 50, 400)
        
    if screen == 'screen10':
        background(255)
        fill(0)
        textSize(32)
        text("What does PM in the context of time stand for?", 50, 100)
        text("a) Post Malone", 50, 200)
        text("b) Past Meridiem", 50, 300)
        text("c) Post Meridiem", 50, 400)
        
    if screen == 'screen11':
        background(255)
        fill(0)
        textSize(32)
        text("CONGRATS YOU WON", 100, 100)
    
def mousePressed():
    global screen
    global screen_number
    global screen1
    global screen2
    global screen3
    global screen4
    global screen5
    global screen6
    global screen7
    global screen8
    global screen9
    global screen10
    
    if screen == 'screen1':
        if mouseX >= start_loc.x and mouseX <= start_loc.x + start_size.x:
            if mouseY >= start_loc.y and mouseY <= start_loc.y + start_size.y:
                screen_number += 1
            
    if screen == 'screen2':        
        if mouseX >= b_loc.x and mouseX <= b_loc.x + b_size.x:
            if mouseY >= b_loc.y and mouseY <= b_loc.y + b_size.y:
                screen_number += 1
            
    if screen == 'screen3':
        if mouseX >= a_loc.x and mouseX <= a_loc.x + a_size.x:
            if mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y:
                screen_number += 1
        
    if screen == 'screen4':
        if mouseX >= b_loc.x and mouseX <= b_loc.x + b_size.x:
            if mouseY >= b_loc.y and mouseX <= b_loc.y + b_size.y:
                screen_number += 1
        
        
    if screen == 'screen5':
        if mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x:
            if mouseY >= c_loc.y and mouseX <= c_loc.y + c_size.y:
                screen_number += 1
        
    if screen == 'screen6':
        if mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x:
            if mouseY >= c_loc.y and mouseX <= c_loc.y + c_size.y:
                screen_number += 1
                
    if screen == 'screen7':
        if mouseX >= a_loc.x and mouseX <= a_loc.x + a_size.x:
            if mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y:
                screen_number += 1
        
        
    if screen == 'screen8':
        if mouseX >= b_loc.x and mouseX <= b_loc.x + b_size.x:
            if mouseY >= b_loc.y and mouseX <= b_loc.y + b_size.y:
                screen_number += 1
                
    if screen == 'screen9':
        if mouseX >= a_loc.x and mouseX <= a_loc.x + a_size.x:
            if mouseY >= a_loc.y and mouseY <= a_loc.y + a_size.y:
                screen_number += 1    
                
    if screen == 'screen10':
        if mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x:
            if mouseY >= c_loc.y and mouseX <= c_loc.y + c_size.y:
                screen_number += 1
                
    if screen == 'screen11':
        if mouseX >= c_loc.x and mouseX <= c_loc.x + c_size.x:
            if mouseY >= c_loc.y and mouseX <= c_loc.y + c_size.y:
                screen_number += 1
        
        
    if screen != 'screen':
        screen = 'screen'
    screen = screen + str(screen_number)