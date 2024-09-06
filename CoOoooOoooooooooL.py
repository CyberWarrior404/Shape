import pgzrun

WIDTH = 500
HEIGHT = 500

def draw():
    screen.fill("White")
    r1 = Rect((0,0),(500,100))
    r1.center = WIDTH/2,HEIGHT/2
    screen.draw.rect(r1,color="cyan")
pgzrun.go()