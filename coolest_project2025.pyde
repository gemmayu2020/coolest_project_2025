translateY = 170
planeX = 0
planeWidth = 190
planeHeight = 170
wingX=0
wingY=60
birdY=200

def setup():
    size(600, 400)


def draw_plane():
    noStroke()
    #draw box
    fill(250,250,250)
    rect(0,-70,190,170)    
    #draw nose of plane
    fill(250,213,123)
    #ellipse(200,200,30,60)
    ellipse(140,27,30,60)
    
    fill(250,213,123)
    #ellipse(220,215,60,30)
    ellipse(160,42,60,30)
    #draw body of plane
    fill(231,0,231)
    #rect(60,173,150,55)
    rect(0,0,150,55)
    #draw wings
    fill(132,132,132)
    #triangle(120,100,110,173,150,173)
    triangle(60,-73,50,0,90,0)
    fill(132,132,132)
    #triangle(110,273,120,200,150,273)
    triangle(50,100,60,27,90,100)
    
    
    
def draw_bird():     
    fill(250,213,123)
    #draw head
    ellipse(0,0,50,50)
    
    #draw body
    ellipse(0,-50,50,70)
    
    #draw eyes
    #fill(250,250,250)
    #ellipse(230,370,20,20)
    #ellipse(270,370,20,20)

    #draw beak
    fill(255,165,0)
    triangle(-25,10,25,10,0,75)
    
    #draw wing
    fill(250,213,213)
    triangle(-20,-80,-25,-30,-80,-60) # left wing
    triangle(10,-80,5,-30,80,-60) # right wing



def keyPressed():
    global translateY
    if keyCode == 38:
        translateY-=10
        #print(translateY)
        
    elif keyCode == 40:
        translateY+=10




#def keyReleased():
 #   print("keyCode")    

def draw():
    global translateY, safe, planeX
    #print((frameCount%301)+50)
    safe = color(60,60,200)
    #birdX = (frameCount%600)-400
    birdX=270
    background(safe)
    #print("translateY: " + str(translateY))
     
    pushMatrix()
    translate(0, translateY)
    draw_plane()
    popMatrix()
    
    #print(planeX, translateY, planeWidth, planeHeight)
    wingX=birdX-80
    print(wingX,wingY)
    #print(frameCount)
    #print(bird_x)
    pushMatrix()
    translate(birdX,birdY)
    draw_bird()
    popMatrix()
