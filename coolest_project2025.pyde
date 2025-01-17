def setup():
    size(600, 400)


def draw_plane():
    noStroke()
    
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
    #draw body
    fill(250,213,123)
    ellipse(250,330,50,70)
    
    ellipse(250,370,50,50)
    
    #draw eyes
    fill(250,250,250)
    ellipse(230,370,20,20)

    ellipse(270,370,20,20)

    #draw beak
    fill(255,165,0)
    triangle( 260, 390 ,230,390, 250, 400)
    #draw wing
    fill(250,213,213)
    triangle(230,350,230,330,170,340)

    triangle(270,350,270,330,320,340)

def keyPressed():
    print(key)
    

#def keyReleased():
        

def draw():
    #print(keyCode)
    background(60,60,200)
    translate(0,170)
    draw_plane()
    draw_bird()
