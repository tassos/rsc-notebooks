import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import matplotlib.patches as patches
import time

def step1():
    
    img = plt.imread("artwork/DGM/fig2-3.png")
    fig, ax = plt.subplots()
    plt.axis('off')



    #first joint
    x_pos = 10
    y_pos = 885
    plt.text(x_pos, y_pos, "q",color='b',weight='bold', fontsize = 15)
    x_pos = 55
    y_pos = 900
    plt.text(x_pos, y_pos, "1",color='b',weight='bold')
    rect1 = patches.Rectangle((215,650),70,55,linewidth=1,edgecolor='b',facecolor='b')

    #second joint
    x_pos = 265
    y_pos = 515
    plt.text(x_pos, y_pos, "q",color='g',weight='bold', fontsize = 15)
    x_pos = 300
    y_pos = 525
    plt.text(x_pos, y_pos, "2",color='g',weight='bold')
    rect2 = patches.Rectangle((215,260),60,100,linewidth=1,edgecolor='g',facecolor='g')

    #third joint
    x_pos = 348
    y_pos = 120
    plt.text(x_pos, y_pos, "q",color='m',weight='bold', fontsize = 15)
    x_pos = 390
    y_pos = 135
    plt.text(x_pos, y_pos, "3",color='m',weight='bold')
    rect3 = patches.Rectangle((528,280),105,55,linewidth=1,edgecolor='m',facecolor='m')

    rectangles = [rect1, rect2, rect3]


    for i in rectangles:
        ax.add_patch(i)
   
    ax.imshow(img)


def step2():
    

    img = plt.imread("artwork/DGM/fig2-3.png")
    fig, ax = plt.subplots()
    plt.axis('off')

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
    
    
    img = plt.imread("artwork/DGM/fig2-3.png")

    #points_2st_y_ini = np.linspace(710,600,30)
    points_2st_y_fin = np.linspace(710,660,30)
    #points_3st_y_ini = np.linspace(710,320,30)
    points_3st_y_fin = np.linspace(800,815,30)
    points_3st_x_fin = np.linspace(160,190,30)


    fig, ax = plt.subplots()
    plt.axis('off')

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
    
    
    img = plt.imread("artwork/DGM/fig2-3.png")

    points_1st_y_ini = np.linspace(710,320,30)
    points_1st_y_fin = np.linspace(660,270,30)
    points_2st_y_ini = np.linspace(710,320,30)
    points_2st_y_fin = np.linspace(600,210,30)
    points_3st_y_ini = np.linspace(710,320,30)
    points_3st_y_fin = np.linspace(815,425,30)


    fig, ax = plt.subplots()
    plt.axis('off')

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


    img = plt.imread("artwork/DGM/fig2-3.png")

    points_1st_x_ini = np.linspace(250,900,30)
    points_1st_x_fin = np.linspace(250,900,30)
    points_2st_x_ini = np.linspace(250,900,30)
    points_2st_x_fin = np.linspace(150,800,30)
    points_3st_x_ini = np.linspace(250,900,30)
    points_3st_x_fin = np.linspace(420,1050,30)


    fig, ax = plt.subplots()
    plt.axis('off')

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


def Drawit(M):
## Function for drawing the segments of a robot and their coordinate frames
# Input:        M          Array of size N. Each element represents a
#                                fundamendal transformation (Rotation or
#                                Translation). The coordinate frames are
#                                drawn after each transformation and
#                                segments are drawn between transformations
  
    def DrawCoord(M,L,ax,lw): 
    
        CoX = M[0:3,3]+L*M[0:3,0]
        CoY = M[0:3,3]+L*M[0:3,1]
        CoZ = M[0:3,3]+L*M[0:3,2]
        CoO = M[0:3,3]

        ax.scatter(CoO[0],CoO[1],CoO[2],c='Black')
        ax.plot([CoO[0],CoX[0]],[CoO[1],CoX[1]],[CoO[2],CoX[2]],c='Red',lw=lw)
        ax.plot([CoO[0],CoY[0]],[CoO[1],CoY[1]],[CoO[2],CoY[2]],c='Blue',lw=lw)
        ax.plot([CoO[0],CoZ[0]],[CoO[1],CoZ[1]],[CoO[2],CoZ[2]],c='Green',lw=lw)
        plt.show()
    
    def DrawSegment(M1,M2,ax):
        M=np.array([M1[0:3,3],M2[0:3,3]])
        ax.plot(M[:,0],M[:,1],M[:,2],lw=8)

    def axisEqual3D(ax):
        extents = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
        sz = extents[:,1] - extents[:,0]
        centers = np.mean(extents, axis=1)
        maxsize = max(abs(sz))
        r = maxsize/2
        for ctr, dim in zip(centers, 'xyz'):
            getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)
            
            

    fig = plt.figure()
    ax  = fig.gca(projection='3d')
    ax.set_xlim3d(-2, 8)
    ax.set_ylim3d(-2, 8)
    ax.set_zlim3d(-2, 8)

    P   = np.identity(4)
    DrawCoord(P,2,ax,5)

    for i in range(0,len(M)):
        N = np.identity(4)

        for k in range(i,0,-1):
            N = np.dot(M[k],N)
        DrawCoord(N,1,ax,2)
        DrawSegment(P,N,ax)
        P=N

    axisEqual3D(ax)
    
    
            
            
            
            
            

