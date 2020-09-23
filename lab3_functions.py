import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import matplotlib.patches as patches
import time

def defineJoints():
    
    img = plt.imread("artwork/DGM/fig2-3.png")
    fig, ax = plt.subplots()
    plt.axis('off')



    #first joint
    x_pos = 120
    y_pos = 865
    plt.text(x_pos, y_pos, "q",color='b',weight='bold')
    x_pos = 140
    y_pos = 890
    plt.text(x_pos, y_pos, "1",color='b',weight='bold')
    rect1 = patches.Rectangle((215,650),70,55,linewidth=1,edgecolor='b',facecolor='b')

    #second joint
    x_pos = 350
    y_pos = 520
    plt.text(x_pos, y_pos, "q",color='g',weight='bold')
    x_pos = 375
    y_pos = 555
    plt.text(x_pos, y_pos, "2",color='g',weight='bold')
    rect2 = patches.Rectangle((215,260),60,100,linewidth=1,edgecolor='g',facecolor='g')

    #third joint
    x_pos = 428
    y_pos = 160
    plt.text(x_pos, y_pos, "q",color='m',weight='bold')
    x_pos = 456
    y_pos = 187
    plt.text(x_pos, y_pos, "3",color='m',weight='bold')
    rect3 = patches.Rectangle((528,280),105,55,linewidth=1,edgecolor='m',facecolor='m')

    rectangles = [rect1, rect2, rect3]


    for i in rectangles:
        ax.add_patch(i)
   
    ax.imshow(img)

def addZ():
    
    img = plt.imread("artwork/DGM/fig2-3.png")
    fig, ax = plt.subplots()
    plt.axis('off')


    #Z1
    x_pos = 270
    y_pos = 630
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 300
    y_pos = 640
    plt.text(x_pos, y_pos, "1",color='r',weight='bold')
    plt.plot([250,250],[710,600], color="red", linewidth=4)

    #Z2
    x_pos = 270
    y_pos = 200
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 300
    y_pos = 210
    plt.text(x_pos, y_pos, "2",color='r',weight='bold')
    plt.plot([250,250],[310,200], color="red", linewidth=4)

    #Z3
    x_pos = 650
    y_pos = 370
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 680
    y_pos = 380
    plt.text(x_pos, y_pos, "3",color='r',weight='bold')
    plt.plot([600,700],[310,310], color="red", linewidth=4)


    ax.imshow(img)
    
    
def addX():
    
    img = plt.imread("artwork/DGM/fig2-3.png")
    fig, ax = plt.subplots()
    plt.axis('off')


    #Z1
    x_pos = 270
    y_pos = 630
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 300
    y_pos = 640
    plt.text(x_pos, y_pos, "1",color='r',weight='bold')
    plt.plot([250,250],[710,600], color="red")
    x_pos = 400
    y_pos = 780
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 430
    y_pos = 790
    plt.text(x_pos, y_pos, "1",color='b',weight='bold')
    plt.plot([250,400],[710,710], color="blue", linewidth = 4)

    #Z2
    x_pos = 270
    y_pos = 200
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 300
    y_pos = 210
    plt.text(x_pos, y_pos, "2",color='r',weight='bold')
    plt.plot([250,250],[310,200], color="red")
    x_pos = 190
    y_pos = 410
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 220
    y_pos = 420
    plt.text(x_pos, y_pos, "2",color='b',weight='bold')
    plt.plot([250,150],[310,410], color="blue", linewidth = 4)

    #Z3
    x_pos = 650
    y_pos = 370
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 680
    y_pos = 380
    plt.text(x_pos, y_pos, "3",color='r',weight='bold')
    plt.plot([600,700],[310,310], color="red")
    x_pos = 610
    y_pos = 230
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 640
    y_pos = 240
    plt.text(x_pos, y_pos, "3",color='b',weight='bold')
    plt.plot([600,600],[310,200], color="blue", linewidth = 4)


    ax.imshow(img)
    
    
def addY():
    
    img = plt.imread("artwork/DGM/fig2-3.png")
    fig, ax = plt.subplots()
    plt.axis('off')


    #Z1
    x_pos = 170
    y_pos = 630
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 200
    y_pos = 640
    plt.text(x_pos, y_pos, "1",color='r',weight='bold')
    plt.plot([250,250],[710,600], color="red")
    x_pos = 400
    y_pos = 780
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 430
    y_pos = 790
    plt.text(x_pos, y_pos, "1",color='b',weight='bold')
    plt.plot([250,400],[710,710], color="blue")
    x_pos = 310
    y_pos = 630
    plt.text(x_pos, y_pos, "Y",color='g',weight='bold')
    x_pos = 340
    y_pos = 640
    plt.text(x_pos, y_pos, "1",color='g',weight='bold')
    plt.plot([250,310],[710,605], color="green", linewidth = 4)

    #Z2
    x_pos = 270
    y_pos = 200
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 300
    y_pos = 210
    plt.text(x_pos, y_pos, "2",color='r',weight='bold')
    plt.plot([250,250],[310,200], color="red")
    x_pos = 190
    y_pos = 410
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 220
    y_pos = 420
    plt.text(x_pos, y_pos, "2",color='b',weight='bold')
    plt.plot([250,150],[310,410], color="blue")
    x_pos = 400
    y_pos = 370
    plt.text(x_pos, y_pos, "Y",color='g',weight='bold')
    x_pos = 430
    y_pos = 380
    plt.text(x_pos, y_pos, "2",color='g',weight='bold')
    plt.plot([250,420],[310,310], color="green", linewidth = 4)

    #Z3
    x_pos = 650
    y_pos = 370
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 680
    y_pos = 380
    plt.text(x_pos, y_pos, "3",color='r',weight='bold')
    plt.plot([600,700],[310,310], color="red")
    x_pos = 610
    y_pos = 230
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 640
    y_pos = 240
    plt.text(x_pos, y_pos, "3",color='b',weight='bold')
    plt.plot([600,600],[310,200], color="blue")
    x_pos = 550
    y_pos = 420
    plt.text(x_pos, y_pos, "Y",color='g',weight='bold')
    x_pos = 580
    y_pos = 430
    plt.text(x_pos, y_pos, "3",color='g',weight='bold')
    plt.plot([600,500],[310,410], color="green", linewidth = 4)

    ax.imshow(img)
    
    
def ref_and_fin():
    img = plt.imread("artwork/DGM/fig2-3.png")
    fig, ax = plt.subplots()
    plt.axis('off')


    #Z0
    x_pos = 100
    y_pos = 630
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 130
    y_pos = 640
    plt.text(x_pos, y_pos, "0",color='r',weight='bold')
    x_pos = 460
    y_pos = 780
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 490
    y_pos = 790
    plt.text(x_pos, y_pos, "0",color='b',weight='bold')

    #Z1
    x_pos = 170
    y_pos = 630
    plt.text(x_pos, y_pos, "Z",color='r')
    x_pos = 200
    y_pos = 640
    plt.text(x_pos, y_pos, "1",color='r')
    plt.plot([250,250],[710,600], color="red")
    x_pos = 400
    y_pos = 780
    plt.text(x_pos, y_pos, "X",color='b')
    x_pos = 430
    y_pos = 790
    plt.text(x_pos, y_pos, "1",color='b')
    plt.plot([250,400],[710,710], color="blue")
    x_pos = 310
    y_pos = 630
    plt.text(x_pos, y_pos, "Y",color='g',weight='bold')
    x_pos = 340
    y_pos = 640
    plt.text(x_pos, y_pos, "1",color='g',weight='bold')
    plt.plot([250,310],[710,605], color="green")

    #Z2
    x_pos = 270
    y_pos = 200
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 300
    y_pos = 210
    plt.text(x_pos, y_pos, "2",color='r',weight='bold')
    plt.plot([250,250],[310,200], color="red")
    x_pos = 190
    y_pos = 410
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 220
    y_pos = 420
    plt.text(x_pos, y_pos, "2",color='b',weight='bold')
    plt.plot([250,150],[310,410], color="blue")
    x_pos = 400
    y_pos = 370
    plt.text(x_pos, y_pos, "Y",color='g',weight='bold')
    x_pos = 430
    y_pos = 380
    plt.text(x_pos, y_pos, "2",color='g',weight='bold')
    plt.plot([250,420],[310,310], color="green")

    #Z3
    x_pos = 650
    y_pos = 370
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 680
    y_pos = 380
    plt.text(x_pos, y_pos, "3",color='r',weight='bold')
    plt.plot([600,700],[310,310], color="red")
    x_pos = 610
    y_pos = 230
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 640
    y_pos = 240
    plt.text(x_pos, y_pos, "3",color='b',weight='bold')
    plt.plot([600,600],[310,200], color="blue")
    x_pos = 550
    y_pos = 420
    plt.text(x_pos, y_pos, "Y",color='g',weight='bold')
    x_pos = 580
    y_pos = 430
    plt.text(x_pos, y_pos, "3",color='g',weight='bold')
    plt.plot([600,500],[310,410], color="green")

    #Zn
    x_pos = 1000
    y_pos = 370
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 1030
    y_pos = 380
    plt.text(x_pos, y_pos, "4",color='r',weight='bold')
    x_pos = 930
    y_pos = 230
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 960
    y_pos = 240
    plt.text(x_pos, y_pos, "4",color='b',weight='bold')
    plt.plot([900,900],[310,200], color="blue",linewidth = 4)
    plt.plot([900,1050],[310,310], color="red",linewidth = 4)

    ax.imshow(img)