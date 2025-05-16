import random
translateY = 170
planeX = 0
planeWidth = 190
planeHeight = 170
wingX=0
wingY=60
birdY=200
has_collided = False
score= 0
#TODO:lower_bound_speed=1
#TODO:higher_bound_speed=4
#TODO:speed_multiplyer = 1

def setup():
    size(600, 400)
    textAlign(CENTER, CENTER)
    textSize(50)

def draw_plane():
    noStroke()
    
    #draw box
    #fill(250,250,250)
    #rect(0,-70,190,170)
        
    #draw nose of plane
    fill(255,255,255)
    #ellipse(200,200,30,60)
    ellipse(140,27,30,60)
    
    #ellipse(220,215,60,30)
    ellipse(160,42,60,30)
    
    #draw top wing
    fill(243,91,4)
    #triangle(120,100,110,173,150,173)
    triangle(60,-50,50,23,90,23)
    
    #draw body of plane
    fill(255,255,255)
    #rect(60,173,150,55)
    rect(0,0,150,55)
    
    #draw bottom wing
    fill(243,91,4)
    #triangle(110,273,120,200,150,273)
    triangle(50,40,60,110,90,40)
    
    #DRAW TEXT
    
    fill(0,0,0)
    textSize(20)
    text("Me Airlines",50,20)
def draw_bird():     
    fill(250,213,123)
    #draw head
    ellipse(0,0,50,50)
    
    #draw tail
    fill(255,216,1)
    triangle(-10,-45,10,-45,0,-150)
    
    #draw body
    fill(250,213,123)
    ellipse(0,-50,50,70)
    
    #draw eyes
    fill(0,0,0)
    ellipse(-10,0,5,5)
    ellipse(13,0,5,5)

    #draw wing
    fill(181,101,29)
    triangle(-20,-80,-25,-30,-80,-60) # left wing
    triangle(10,-80,5,-30,80,-60) # right wing
        
    #draw beak
    fill(255,165,0)
    triangle(-25,10,25,10,0,75)
    
def collision_detection (rectTopLeftX, rectTopLeftY, rectWidth, rectHeight, dotX, dotY):
    if dotX <= rectTopLeftX+rectWidth and dotY <= rectTopLeftY+rectHeight and dotX >= rectTopLeftX and dotY >= rectTopLeftY:    
        return True
    else:
        return False
def keyPressed():
    global translateY
    if keyCode == 38:
        translateY-=10
        #print(translateY)
        
    elif keyCode == 40:
        translateY+=10
 

def draw():
    global translateY, safe, planeX, has_collided, score, birdY, speed_multiplyer
    #birdX=269
    realPlaneY = translateY - 70
    
    
    background(90,86,188)
    
    #print(has_collided)
    if has_collided == True:    
        fill(241,135,1)
        textSize(60)
        text("You CRASHED!!!", 300, 200)    
        text(score,300,240)
        return 
    else:
        #TODO:#birdX = ((-frameCount*speed_multiplyer)%600)
        birdX = (-frameCount%600)
        #print(birdX)
        if birdX == 599:
            lower_bound = 150
            higher_bound = 325
            random_int = random.randint(lower_bound ,higher_bound)
            birdY = random_int
            #TODO:speed_multiplyer=4#random.randint(lower_bound_speed,higher_bound_speed)
        if birdX == 0 :
            score+=1
        wingX = birdX - 80
        wingY = birdY - 60
        has_collided = collision_detection(planeX, realPlaneY, planeWidth, planeHeight, wingX, wingY)
        fill(118,120,237)
        textSize(50)
        text(score,350,20)
    
    pushMatrix()
    translate(0, translateY)
    draw_plane()
    popMatrix()
        
    #print(planeX, realPlaneY, planeWidth, planeHeight, wingX, wingY)
    
   
    pushMatrix()
    translate(birdX, birdY)
    draw_bird()
    popMatrix()
