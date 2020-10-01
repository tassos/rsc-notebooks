import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import matplotlib.patches as patches
import time

def setPlot():
    #set plot
    img = plt.imread("artwork/DGM/fig2-3.png")
    fig, ax = plt.subplots()
    plt.axis('off')
    return ax, fig,img


def defineJoints():
    
    ax,fig,img  = setPlot()

    #first joint
    x_pos = 10
    y_pos = 885
    plt.text(x_pos, y_pos, "q",color='b',weight='bold', fontsize = 15)
    x_pos = 55
    y_pos = 900
    plt.text(x_pos, y_pos, "1",color='b',weight='bold')
    rect1 = patches.Rectangle((123,635),75,67,linewidth=1,edgecolor='b',facecolor='b')

    #second joint
    x_pos = 265
    y_pos = 515
    plt.text(x_pos, y_pos, "q",color='g',weight='bold', fontsize = 15)
    x_pos = 300
    y_pos = 525
    plt.text(x_pos, y_pos, "2",color='g',weight='bold')
    rect2 = patches.Rectangle((125,225),67,100,linewidth=1,edgecolor='g',facecolor='g')

    #third joint
    x_pos = 348
    y_pos = 120
    plt.text(x_pos, y_pos, "q",color='m',weight='bold', fontsize = 15)
    x_pos = 390
    y_pos = 135
    plt.text(x_pos, y_pos, "3",color='m',weight='bold')
    rect3 = patches.Rectangle((470,250),107,55,linewidth=1,edgecolor='m',facecolor='m')


    rectangles = [rect1, rect2, rect3]


    for i in rectangles:
        ax.add_patch(i)
   
    ax.imshow(img)

def step1_Z():
    ax,fig,img = setPlot()
    addZ(4,ax,fig,img)
    ax.imshow(img)

    
def step2_X():
    ax,fig,img = setPlot()
    addZ(1,ax,fig,img)
    addX(4,ax,fig,img)
    ax.imshow(img)
    
        
def step3_Y():
    ax,fig,img = setPlot()
    addZ(1,ax,fig,img)
    addX(1,ax,fig,img)
    addY(4,ax,fig,img)
    ax.imshow(img)
    
def step4_refandfin():
    ax,fig,img = setPlot()
    addZ(1,ax,fig,img)
    addX(1,ax,fig,img)
    addY(1,ax,fig,img)
    ref_and_fin(4,ax,fig,img)
    ax.imshow(img)


def addZ(lw,ax,fig,img):
    
    #Z1
    x_pos = 190
    y_pos = 630
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 220
    y_pos = 640
    plt.text(x_pos, y_pos, "1",color='r',weight='bold')
    plt.plot([170,170],[710,600], color="red", linewidth=lw)

    #Z2
    x_pos = 190
    y_pos = 175
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 220
    y_pos = 185
    plt.text(x_pos, y_pos, "2",color='r',weight='bold')
    plt.plot([170,170],[285,175], color="red", linewidth=lw)

    #Z3
    x_pos = 590
    y_pos = 335
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 620
    y_pos = 345
    plt.text(x_pos, y_pos, "3",color='r',weight='bold')
    plt.plot([540,650],[285,285], color="red", linewidth=lw)

    return ax
    
    
def addX(lw,ax,fig,img):
    

    x_pos = 320
    y_pos = 780
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 350
    y_pos = 790
    plt.text(x_pos, y_pos, "1",color='b',weight='bold')
    plt.plot([170,320],[710,710], color="blue", linewidth = lw)


    x_pos = 110
    y_pos = 385
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 140
    y_pos = 395
    plt.text(x_pos, y_pos, "2",color='b',weight='bold')
    plt.plot([170,70],[285,385], color="blue", linewidth = lw)


    x_pos = 550
    y_pos = 201
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 580
    y_pos = 215
    plt.text(x_pos, y_pos, "3",color='b',weight='bold')
    plt.plot([540,540],[285,175], color="blue", linewidth = lw)


    
    
def addY(lw,ax,fig,img):
    
    
    #CF1
    x_pos = 240
    y_pos = 630
    plt.text(x_pos, y_pos, "Y",color='g',weight='bold')
    x_pos = 260
    y_pos = 640
    plt.text(x_pos, y_pos, "1",color='g',weight='bold')
    plt.plot([170,240],[710,605], color="green", linewidth = lw)

    #CF2
    x_pos = 320
    y_pos = 345
    plt.text(x_pos, y_pos, "Y",color='g',weight='bold')
    x_pos = 350
    y_pos = 355
    plt.text(x_pos, y_pos, "2",color='g',weight='bold')
    plt.plot([170,340],[285,285], color="green", linewidth = lw)

    #CF3
    x_pos = 490
    y_pos = 395
    plt.text(x_pos, y_pos, "Y",color='g',weight='bold')
    x_pos = 520
    y_pos = 405
    plt.text(x_pos, y_pos, "3",color='g',weight='bold')
    plt.plot([540,440],[285,385], color="green", linewidth = lw)

    
    
def ref_and_fin(lw,ax,fig,img):
        
    #CF0
    x_pos = 20
    y_pos = 630
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 50
    y_pos = 640
    plt.text(x_pos, y_pos, "0",color='r',weight='bold')
    x_pos = 390
    y_pos = 780
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 420
    y_pos = 790
    plt.text(x_pos, y_pos, "0",color='b',weight='bold')


    #Zn
    x_pos = 970
    y_pos = 345
    plt.text(x_pos, y_pos, "Z",color='r',weight='bold')
    x_pos = 1000
    y_pos = 355
    plt.text(x_pos, y_pos, "4",color='r',weight='bold')
    x_pos = 900
    y_pos = 205
    plt.text(x_pos, y_pos, "X",color='b',weight='bold')
    x_pos = 930
    y_pos = 215
    plt.text(x_pos, y_pos, "4",color='b',weight='bold')
    
    plt.plot([870,870],[285,175], color="blue",linewidth = lw)
    plt.plot([870,1020],[285,285], color="red",linewidth = lw)

