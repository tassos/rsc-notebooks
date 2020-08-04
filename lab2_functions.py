import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import matplotlib.patches as patches
import time

def step1():
    
    img = plt.imread("fig2-3.png")
    fig, ax = plt.subplots()



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


def step2():
    

    img = plt.imread("fig2-3.png")
    fig, ax = plt.subplots()

    #reference, first
    x_pos = 270
    y_pos = 770
    plt.text(x_pos, y_pos, "O",color='r',weight='bold')
    x_pos = 305
    y_pos = 800
    plt.text(x_pos, y_pos, "1",color='r',weight='bold')
    plt.plot([250,250],[710,600], color="red")
    plt.plot([250,160],[710,800], color="red")
    plt.plot([250,400],[710,710], color="red")

    #second
    x_pos = 335
    y_pos = 800
    plt.text(x_pos, y_pos, "2",color='b',weight='bold')
    plt.plot([240,240],[710,600], color="blue")
    plt.plot([250,190],[710,815], color="blue")
    plt.plot([250,420],[710,660], color="blue")

    
    #third
    x_pos = 260
    y_pos = 397
    plt.text(x_pos, y_pos, "O",color='g',weight='bold')
    x_pos = 295
    y_pos = 415
    plt.text(x_pos, y_pos, "3",color='g',weight='bold')
    plt.plot([250,250],[310,200], color="green")
    plt.plot([250,150],[310,410], color="green")
    plt.plot([250,420],[310,310], color="green")


    #forth
    x_pos = 908
    y_pos = 385
    plt.text(x_pos, y_pos, "O",color='m',weight='bold')
    x_pos = 950
    y_pos = 405
    plt.text(x_pos, y_pos, "4",color='m',weight='bold')
    plt.plot([900,900],[310,200], color="magenta")
    plt.plot([900,800],[310,410], color="magenta")
    plt.plot([900,1050],[310,310], color="magenta")


    ax.imshow(img)
    
    
    
    
def first_to_2nd():
    
    
    img = plt.imread("fig2-3.png")

    #points_2st_y_ini = np.linspace(710,600,30)
    points_2st_y_fin = np.linspace(710,660,30)
    #points_3st_y_ini = np.linspace(710,320,30)
    points_3st_y_fin = np.linspace(800,815,30)
    points_3st_x_fin = np.linspace(160,190,30)


    fig, ax = plt.subplots()

    x2_ini, y2_ini = 250, 710
    x2_fin, y2_fin = 400, 800 #250, 600
    x3_ini, y3_ini = 250, 710
    x3_fin, y3_fin = 400, 710 #190, 815


    ln2, = ax.plot(x2_ini, y2_ini, color='b')
    ln3, = ax.plot(x3_ini, y3_ini, color='b')


    plt.plot([x2_ini], [y2_ini], 'b', ms=10)



    #first
    x_pos = 270
    y_pos = 770
    plt.text(x_pos, y_pos, "O",color='r',weight='bold')
    x_pos = 305
    y_pos = 800
    plt.text(x_pos, y_pos, "1",color='r',weight='bold')
    plt.plot([250,250],[710,600], color="red")
    plt.plot([250,160],[710,800], color="red")
    plt.plot([250,400],[710,710], color="red")


    #second
    x_pos = 335
    y_pos = 800
    plt.text(x_pos, y_pos, "2",color='b',weight='bold')



    def init():
        ax.set_xlim(0, 1200)
        ax.set_ylim(900, 0)
        return ln2,


    def update(frame):
    
        
        #y2_ini = points_2st_y_ini[frame]
        y2_fin = points_2st_y_fin[frame]
    
        ln2.set_data([x2_ini,x2_fin], [y2_ini,y2_fin])
    
        #y3_ini = points_3st_y_ini[frame]
        y3_fin = points_3st_y_fin[frame]
        x3_fin = points_3st_x_fin[frame]

        ln3.set_data([x3_ini,x3_fin], [y3_ini,y3_fin])


        return ln2,ln3          


    ani = FuncAnimation(fig, update, frames=range(len(points_2st_y_fin)),
            init_func=init, blit=True, repeat_delay = 2000)

    ax.imshow(img)
    
    return ani



def second_to_3rd():
    
    
    img = plt.imread("fig2-3.png")

    points_1st_y_ini = np.linspace(710,320,30)
    points_1st_y_fin = np.linspace(660,270,30)
    points_2st_y_ini = np.linspace(710,320,30)
    points_2st_y_fin = np.linspace(600,210,30)
    points_3st_y_ini = np.linspace(710,320,30)
    points_3st_y_fin = np.linspace(815,425,30)


    fig, ax = plt.subplots()
    x1_ini, y1_ini = 250, 710
    x1_fin, y1_fin = 400, 600
    x2_ini, y2_ini = 250, 710
    x2_fin, y2_fin = 250, 600
    x3_ini, y3_ini = 250, 710
    x3_fin, y3_fin = 190, 815


    ln,  = ax.plot(x1_ini, y1_ini, color='g')
    ln2, = ax.plot(x2_ini, y2_ini, color='g')
    ln3, = ax.plot(x3_ini, y3_ini, color='g')


    plt.plot([x1_ini], [y1_ini], 'g', ms=10)



    #second
    x_pos = 270
    y_pos = 770
    plt.text(x_pos, y_pos, "O",color='b',weight='bold')
    x_pos = 335
    y_pos = 800
    plt.text(x_pos, y_pos, "2",color='b',weight='bold')
    plt.plot([250,250],[710,600], color="blue")
    plt.plot([250,190],[710,815], color="blue")
    plt.plot([250,420],[710,660], color="blue")


    #third
    x_pos = 260
    y_pos = 397
    plt.text(x_pos, y_pos, "O",color='g',weight='bold')
    x_pos = 295
    y_pos = 415
    plt.text(x_pos, y_pos, "3",color='g',weight='bold')



    def init():
        ax.set_xlim(0, 1200)
        ax.set_ylim(900, 0)
        return ln,


    def update(frame):
        y1_ini = points_1st_y_ini[frame]
        y1_fin = points_1st_y_fin[frame]
        ln.set_data([x1_ini,x1_fin], [y1_ini,y1_fin])
        
        y2_ini = points_2st_y_ini[frame]
        y2_fin = points_2st_y_fin[frame]
        ln2.set_data([x2_ini,x2_fin], [y2_ini,y2_fin])
    
        y3_ini = points_3st_y_ini[frame]
        y3_fin = points_3st_y_fin[frame]
        ln3.set_data([x3_ini,x3_fin], [y3_ini,y3_fin])


        return ln,ln2,ln3          


    ani = FuncAnimation(fig, update, frames=range(len(points_1st_y_ini)),
            init_func=init, blit=True, repeat_delay =1000)
 
    ax.imshow(img)

    return ani
        

    

    
def third_to_4th():


    img = plt.imread("fig2-3.png")

    points_1st_x_ini = np.linspace(250,900,30)
    points_1st_x_fin = np.linspace(250,900,30)
    points_2st_x_ini = np.linspace(250,900,30)
    points_2st_x_fin = np.linspace(150,800,30)
    points_3st_x_ini = np.linspace(250,900,30)
    points_3st_x_fin = np.linspace(420,1050,30)


    fig, ax = plt.subplots()
    x1_ini, y1_ini = 250, 310
    x1_fin, y1_fin = 250, 200
    x2_ini, y2_ini = 250, 310
    x2_fin, y2_fin = 150, 400
    x3_ini, y3_ini = 250, 310
    x3_fin, y3_fin = 420, 310


    ln,  = ax.plot(x1_ini, y1_ini, color='m')
    ln2, = ax.plot(x2_ini, y2_ini, color='m')
    ln3, = ax.plot(x3_ini, y3_ini, color='m')


    plt.plot([x1_ini], [y1_ini], 'm', ms=10)



    #third
    x_pos = 260
    y_pos = 397
    plt.text(x_pos, y_pos, "O",color='g',weight='bold')
    x_pos = 295
    y_pos = 415
    plt.text(x_pos, y_pos, "3",color='g',weight='bold')
    plt.plot([250,250],[310,200], color="green")
    plt.plot([250,150],[310,410], color="green")
    plt.plot([250,420],[310,310], color="green")

    #fourth
    x_pos = 908
    y_pos = 385
    plt.text(x_pos, y_pos, "O",color='m',weight='bold')
    x_pos = 950
    y_pos = 405
    plt.text(x_pos, y_pos, "4",color='m',weight='bold')


    def init():
        ax.set_xlim(0, 1200)
        ax.set_ylim(900, 0)
        return ln,


    def update(frame):
        x1_ini = points_1st_x_ini[frame]
        x1_fin = points_1st_x_fin[frame]
        ln.set_data([x1_ini,x1_fin], [y1_ini,y1_fin])

        x2_ini = points_2st_x_ini[frame]
        x2_fin = points_2st_x_fin[frame]
        ln2.set_data([x2_ini,x2_fin], [y2_ini,y2_fin])

        x3_ini = points_3st_x_ini[frame]
        x3_fin = points_3st_x_fin[frame]
        ln3.set_data([x3_ini,x3_fin], [y3_ini,y3_fin])


        return ln          


    ani = FuncAnimation(fig, update, frames=range(len(points_1st_x_ini)),
            init_func=init, blit=True, repeat_delay = 1000)

    ax.imshow(img)
   
    
    return ani


