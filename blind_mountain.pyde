
###########################
# Created by Eric Davidson
# 7/7/19
###########################
point_count = 50

line_weight = 4

w = 1600
h = 1000

line_count = 300
line_width = w*2
line_sep = 10

ran_mov_max = 100

def setup():
    # Set up the image
    size(w, h)
    global img
    img = createImage(w, h, ARGB)
    
    # Take advantage of retina display
    pixelDensity(2)
    
    # Color in the background
    background(76, 124, 150)
    
    # Color of the line
    stroke(196, 165, 192)
    
    # Start the drawing based on line width 
    x_start = -100
    y_start = -h

    # Thicker
    strokeWeight(line_weight)
    
    for i in range(line_count):
        
        # We don't want to fill in the curves
        fill(99, 141, 164)
        
        # Start the curve vertex
        beginShape()
        
        deform = False
        mountain_life = 0
        for j in range(0, line_width, line_width/point_count):
            # Coordinates are calculated at circle centers essentially
            x_coord = x_start+j
            y_coord = y_start + (i*line_sep) + j*.32
            
            if deform == False and random(1) < .03:
                deform = True
            if deform == True and random(1) < .15:
                deform = False
                mountain_life = 0
            
            mov = 0
            if deform == True:
                mov = int(random(ran_mov_max))
                mov += 5 * mountain_life
                mountain_life += 1
                
            x_coord += mov
            y_coord -= mov

            curveVertex(x_coord, y_coord)
            
        # Draw the curvy line
        endShape()
        
    # Generate a 'seed' just to distinguish image files
    seed = int(random(600))
    
    # Save the image with line count and 'seed'
    save("Examples/blind-" + str(seed) + ".png")
    
    # Only need to draw once
    noLoop()
    
def draw():
    image(img, 0, 0)
    
    
    
