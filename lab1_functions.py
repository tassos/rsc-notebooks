import numpy as np
import matplotlib.pyplot as plt
import math as m
    
def TransX(d):
    ch  = np.linspace(0,d,25)

    #set plot
    fig = plt.figure()
    ax  = fig.add_subplot(111, projection='3d')

    X  = np.linspace(0, 1, 50)
    Y  = np.linspace(0, 1, 50)
    Z  = np.linspace(-1, 1, 50)
    
    X1, Y1 = np.meshgrid(X, Y)
    Z1 = X1+Y1
    
    # Set the axes' limits so they aren't recalculated each frame.
    ax.set_zlim(-1, 1)  
    ax.set_xlim(0, 1)  
    ax.set_ylim(0, 1)

    
    #the reference system of axes
    Zx = np.array([0,0])
    Zy = np.array([1,1])
    Zz = np.array([-1,1])
    Yx = np.array([0,1])
    Yy = np.array([1,1])
    Yz = np.array([-1,-1])
    Xx = np.array([0,0])
    Xy = np.array([1,0])
    Xz = np.array([-1,-1])

    ax.plot3D(Zx,Zy,Zz,'red')
    ax.plot3D(Xx,Xy,Xz,'blue')
    ax.plot3D(Yx,Yy,Yz,'green')


    #moving system of axes
    Yxch = np.array([0,0.5])
    Xych = np.array([0.5,1])
    Zzch = np.array([-1,0])
    
    linex, = ax.plot(Xx,Xych,Xz,'blue', linewidth=4)
    liney, = ax.plot(Yxch,Yy,Yz,'green', linewidth=4)
    linez, = ax.plot(Zx,Zy,Zzch,'red', linewidth=4) 
    
    linex.set_data(Xx+d, Xych)
    linex.set_3d_properties(Xz)
        
    liney.set_data(Yxch+d, Yy)
    liney.set_3d_properties(Yz)
    
    linez.set_data(Zx+d, Zy)
    linez.set_3d_properties(Zzch)


def TransY(d):
    ch  = np.linspace(0,d,25)

    #set plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.linspace(0, 1, 50)
    Y = np.linspace(0, 1, 50)
    Z  = np.linspace(-1, 1, 50)

    X1, Y1 = np.meshgrid(X, Y)
    Z1 = X1+Y1

    # Set the z axis limits so they aren't recalculated each frame.
    ax.set_zlim(-1, 1)  
    ax.set_xlim(0, 1)  
    ax.set_ylim(0, 1)  

    
    #the reference plane
    Zx = np.array([0,0])
    Zy = np.array([1,1])
    Zz = np.array([-1,1])

    Yx = np.array([0,1])
    Yy = np.array([1,1])
    Yz = np.array([-1,-1])
    Xx = np.array([0,0])
    Xy = np.array([1,0])
    Xz = np.array([-1,-1])

    ax.plot3D(Zx,Zy,Zz,'red')
    ax.plot3D(Xx,Xy,Xz,'blue')
    ax.plot3D(Yx,Yy,Yz,'green')


    #moving
    Yxch = np.array([0,0.5])
    Xych = np.array([0.5,1])
    Zzch = np.array([-1,0])

    linex, = ax.plot(Xx,Xych,Xz,'blue', linewidth=4)
    liney, = ax.plot(Yxch,Yy,Yz,'green', linewidth=4)
    linez, = ax.plot(Zx,Zy,Zzch,'red', linewidth=4) 

    linex.set_data(Xx, Xych+d)
    linex.set_3d_properties(Xz)

    liney.set_data(Yxch, Yy+d)
    liney.set_3d_properties(Yz)

    linez.set_data(Zx, Zy+d)
    linez.set_3d_properties(Zzch)



def TransZ(d):
    ch  = np.linspace(0,d,25)

    #set plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.linspace(0, 1, 50)
    Y = np.linspace(0, 1, 50)
    Z  = np.linspace(-1, 1, 50)

    X1, Y1 = np.meshgrid(X, Y)
    Z1 = X1+Y1

    # Set the axis limits so they aren't recalculated each frame.
    ax.set_zlim(-1, 1)  
    ax.set_xlim(0, 1)  
    ax.set_ylim(0, 1)  

    
    #the reference plane
    Zx = np.array([0,0])
    Zy = np.array([1,1])
    Zz = np.array([-1,1])

    Yx = np.array([0,1])
    Yy = np.array([1,1])
    Yz = np.array([-1,-1])
    Xx = np.array([0,0])
    Xy = np.array([1,0])
    Xz = np.array([-1,-1])

    ax.plot3D(Zx,Zy,Zz,'red')
    ax.plot3D(Xx,Xy,Xz,'blue')
    ax.plot3D(Yx,Yy,Yz,'green')


    #moving
    Yxch = np.array([0,0.5])
    Xych = np.array([0.5,1])
    Zzch = np.array([-1,0])

    linex, = ax.plot(Xx,Xych,Xz,'blue', linewidth=4)
    liney, = ax.plot(Yxch,Yy,Yz,'green', linewidth=4)
    linez, = ax.plot(Zx,Zy,Zzch,'red', linewidth=4) 


    linex.set_data(Xx, Xych)
    linex.set_3d_properties(Xz+d)

    liney.set_data(Yxch, Yy)
    liney.set_3d_properties(Yz+d)

    linez.set_data(Zx, Zy)
    linez.set_3d_properties(Zzch+d)




def RotX(theta):
    ch  = np.linspace(0,theta,25)

    #set plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.linspace(0, 1, 50)
    Y = np.linspace(0, 1, 50)
    Z  = np.linspace(0, 1, 50)

    X1, Y1 = np.meshgrid(X, Y)
    Z1 = X1+Y1

    # Set the axis limits so they aren't recalculated each frame.
    ax.set_zlim(0, 1)  
    ax.set_xlim(0, 1)  
    ax.set_ylim(0, 1)  

    
    
    #the reference plane
    Zx = np.array([0,0])
    Zy = np.array([0,0])
    Zz = np.array([0,1])

    Xx = np.array([0,1])
    Xy = np.array([0,0])
    Xz = np.array([0,0])
    Yx = np.array([0,0])
    Yy = np.array([0,1])
    Yz = np.array([0,0])

    ax.plot3D(Zx,Zy,Zz,'red')
    ax.plot3D(Xx,Xy,Xz,'blue')
    ax.plot3D(Yx,Yy,Yz,'green')



    #moving
    Xxch = np.array([0,0.5])
    Yych = np.array([0,0.5])
    Zzch = np.array([0,0.5])

    linex, = ax.plot(Xxch,Xy,Xz,'blue', linewidth=4)
    liney, = ax.plot(Yx,Yych,Yz,'green', linewidth=4)
    linez, = ax.plot(Zx,Zy,Zzch,'red', linewidth=4) 

    linex.set_data(Xxch, Xy)
    linex.set_3d_properties(Xz)

    Yy = np.array([0,0.5*m.sin(m.pi/2+theta)])     
    Yz = np.array([0,0.5*m.cos(m.pi/2+theta)])
    liney.set_data(Yx, Yy)
    liney.set_3d_properties(Yz)

    Zy = np.array([0,0.5*m.sin(theta)])     
    Zz = np.array([0,0.5*m.cos(theta)])
    linez.set_data(Zx, Zy)
    linez.set_3d_properties(Zz)

    
    
def RotY(theta):
    ch  = np.linspace(0,theta,25)

    #set plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.linspace(0, 1, 50)
    Y = np.linspace(0, 1, 50)
    Z  = np.linspace(0, 1, 50)

    X1, Y1 = np.meshgrid(X, Y)
    Z1 = X1+Y1

    # Set the axis limits so they aren't recalculated each frame.
    ax.set_zlim(0, 1)  
    ax.set_xlim(0, 1)  
    ax.set_ylim(0, 1)  

    
    
    #the reference plane
    Zx = np.array([0,0])
    Zy = np.array([0,0])
    Zz = np.array([0,1])

    Xx = np.array([0,1])
    Xy = np.array([0,0])
    Xz = np.array([0,0])
    Yx = np.array([0,0])
    Yy = np.array([0,1])
    Yz = np.array([0,0])

    ax.plot3D(Zx,Zy,Zz,'red')
    ax.plot3D(Xx,Xy,Xz,'blue')
    ax.plot3D(Yx,Yy,Yz,'green')



    #moving
    Xxch = np.array([0,0.5])
    Yych = np.array([0,0.5])
    Zzch = np.array([0,0.5])

    linex, = ax.plot(Xxch,Xy,Xz,'blue', linewidth=4)
    liney, = ax.plot(Yx,Yych,Yz,'green', linewidth=4)
    linez, = ax.plot(Zx,Zy,Zzch,'red', linewidth=4) 

    
    Xx = np.array([0,0.5*m.sin(m.pi/2+theta)])     
    Xz = np.array([0,0.5*m.cos(m.pi/2+theta)])
    linex.set_data(Xx, Xy)
    linex.set_3d_properties(Xz)

    liney.set_data(Yx, Yych)
    liney.set_3d_properties(Yz)

    Zx = np.array([0,0.5*m.sin(theta)])     
    Zz = np.array([0,0.5*m.cos(theta)])
    linez.set_data(Zx, Zy)
    linez.set_3d_properties(Zz)
    
def RotZ(theta):
    ch  = np.linspace(0,theta,25)

    #set plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.linspace(0, 1, 50)
    Y = np.linspace(0, 1, 50)
    Z  = np.linspace(0, 1, 50)

    X1, Y1 = np.meshgrid(X, Y)
    Z1 = X1+Y1

    # Set the axis limits so they aren't recalculated each frame.
    ax.set_zlim(0, 1)  
    ax.set_xlim(0, 1)  
    ax.set_ylim(0, 1)  

    
    
    #the reference plane
    Zx = np.array([0,0])
    Zy = np.array([0,0])
    Zz = np.array([0,1])

    Xx = np.array([0,1])
    Xy = np.array([0,0])
    Xz = np.array([0,0])
    Yx = np.array([0,0])
    Yy = np.array([0,1])
    Yz = np.array([0,0])

    ax.plot3D(Zx,Zy,Zz,'red')
    ax.plot3D(Xx,Xy,Xz,'blue')
    ax.plot3D(Yx,Yy,Yz,'green')



    #moving
    Xxch = np.array([0,0.5])
    Yych = np.array([0,0.5])
    Zzch = np.array([0,0.5])

    linex, = ax.plot(Xxch,Xy,Xz,'blue', linewidth=4)
    liney, = ax.plot(Yx,Yych,Yz,'green', linewidth=4)
    linez, = ax.plot(Zx,Zy,Zzch,'red', linewidth=4) 

 
    Xx = np.array([0,0.5*m.sin(m.pi/2+theta)])     
    Xy = np.array([0,0.5*m.cos(m.pi/2+theta)])
    linex.set_data(Xx, Xy)
    linex.set_3d_properties(Xz)

    Yx = np.array([0,0.5*m.sin(theta)])     
    Yy = np.array([0,0.5*m.cos(theta)])
    liney.set_data(Yx, Yy)
    liney.set_3d_properties(Yz)

    linez.set_data(Zx, Zy)
    linez.set_3d_properties(Zzch)
    
    

def tfrx(a):    
    return np.array([[1,0,0,0],[0,m.cos(a),-m.sin(a),0],
                     [0,m.sin(a),m.cos(a),0],[0,0,0,1]])
def tfry(a):
    return np.array([[m.cos(a),0,m.sin(a),0],[0,1,0,0],[-m.sin(a),0,m.cos(a),0],[0,0,0,1]])

def tfrz(a):
    return np.array([[m.cos(a),-m.sin(a),0,0],[m.sin(a),m.cos(a),0,0],[0,0,1,0],[0,0,0,1]])

def tft(a):
    return np.array([[1,0,0,a[0]],[0,1,0,a[1]],[0,0,1,a[2]],[0,0,0,1]])


def RotateOnXRight(a):
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim3d([-0.5, 1])
    ax.set_ylim3d([-0.5, 1])
    ax.set_zlim3d([0, 1])

    ax.view_init(30, 30)

    # load some test data for demonstration and plot a wireframe
    ax.plot([0, 1], [0, 0], [0, 0], c='blue')
    ax.plot([0, 0], [0, 1], [0, 0], c='green')
    ax.plot([0, 0], [0, 0], [0, 1], c='red')


    x_line, = ax.plot([0, 0.5], [0, 0], [0, 0], lw=6, c='blue')
    y_line, = ax.plot([0, 0], [0, 0.5], [0, 0], lw=6, c='green')
    z_line, = ax.plot([0, 0], [0, 0], [0, 0.5], lw=6, c='red')


    matrix = np.array([[1.,  0.,  0., 0.5],
                       [0.,  1.,  0., 0.5],
                       [0.,  0.,  1., 0],
                       [0.,  0.,  0., 1]])
    
    mat = np.matmul( matrix, tfrz(1));
    tf = np.matmul( mat,tfrx(a));

    CoX = tf[:,0];
    CoY = tf[:,1];
    CoZ = tf[:,2];
    CoO = tf[:,3];
    l = 0.5;

    
    x_line.set_data([CoO[0], CoO[0]+l*CoX[0]],[CoO[1], CoO[1]+l*CoX[1]]);
    x_line.set_3d_properties([CoO[2], CoO[2]+l*CoX[2]]);
    y_line.set_data([CoO[0], CoO[0]+l*CoY[0]],[CoO[1], CoO[1]+l*CoY[1]]);
    y_line.set_3d_properties([CoO[2], CoO[2]+l*CoY[2]]);
    z_line.set_data([CoO[0], CoO[0]+l*CoZ[0]],[CoO[1], CoO[1]+l*CoZ[1]]);
    z_line.set_3d_properties([CoO[2], CoO[2]+l*CoZ[2]]);
    
def RotateOnXLeft(a):
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim3d([-0.5, 1])
    ax.set_ylim3d([-0.5, 1])
    ax.set_zlim3d([0, 1])

    ax.view_init(30, 30)

    # load some test data for demonstration and plot a wireframe
    ax.plot([0, 1], [0, 0], [0, 0], c='blue')
    ax.plot([0, 0], [0, 1], [0, 0], c='green')
    ax.plot([0, 0], [0, 0], [0, 1], c='red')


    x_line, = ax.plot([0, 0.5], [0, 0], [0, 0], lw=6, c='blue')
    y_line, = ax.plot([0, 0], [0, 0.5], [0, 0], lw=6, c='green')
    z_line, = ax.plot([0, 0], [0, 0], [0, 0.5], lw=6, c='red')


    matrix = np.array([[1.,  0.,  0., 0.5],
                       [0.,  1.,  0., 0.5],
                       [0.,  0.,  1., 0],
                       [0.,  0.,  0., 1]])
    
    
    mat = np.matmul( matrix, tfrz(1));
    tf = np.matmul(tfrx(a),mat);

    CoX = tf[:,0];
    CoY = tf[:,1];
    CoZ = tf[:,2];
    CoO = tf[:,3];
    l = 0.5;

    
    x_line.set_data([CoO[0], CoO[0]+l*CoX[0]],[CoO[1], CoO[1]+l*CoX[1]]);
    x_line.set_3d_properties([CoO[2], CoO[2]+l*CoX[2]]);
    y_line.set_data([CoO[0], CoO[0]+l*CoY[0]],[CoO[1], CoO[1]+l*CoY[1]]);
    y_line.set_3d_properties([CoO[2], CoO[2]+l*CoY[2]]);
    z_line.set_data([CoO[0], CoO[0]+l*CoZ[0]],[CoO[1], CoO[1]+l*CoZ[1]]);
    z_line.set_3d_properties([CoO[2], CoO[2]+l*CoZ[2]]);
    
    
def TranslateOnXLeft(a):
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim3d([-0.5, 1])
    ax.set_ylim3d([-0.5, 1])
    ax.set_zlim3d([0, 1])

    ax.view_init(30, 30)

    # load some test data for demonstration and plot a wireframe
    ax.plot([0, 1], [0, 0], [0, 0], c='blue')
    ax.plot([0, 0], [0, 1], [0, 0], c='green')
    ax.plot([0, 0], [0, 0], [0, 1], c='red')


    x_line, = ax.plot([0, 0.5], [0, 0], [0, 0], lw=6, c='blue')
    y_line, = ax.plot([0, 0], [0, 0.5], [0, 0], lw=6, c='green')
    z_line, = ax.plot([0, 0], [0, 0], [0, 0.5], lw=6, c='red')


    matrix = np.array([[1.,  0.,  0., 0.5],
                       [0.,  1.,  0., 0.5],
                       [0.,  0.,  1., 0],
                       [0.,  0.,  0., 1]])
    
    mat = np.matmul( matrix, tfrz(1));
    tf = np.matmul( tft([a,0,0]), mat);

    CoX = tf[:,0];
    CoY = tf[:,1];
    CoZ = tf[:,2];
    CoO = tf[:,3];
    l = 0.5;

    
    x_line.set_data([CoO[0], CoO[0]+l*CoX[0]],[CoO[1], CoO[1]+l*CoX[1]]);
    x_line.set_3d_properties([CoO[2], CoO[2]+l*CoX[2]]);
    y_line.set_data([CoO[0], CoO[0]+l*CoY[0]],[CoO[1], CoO[1]+l*CoY[1]]);
    y_line.set_3d_properties([CoO[2], CoO[2]+l*CoY[2]]);
    z_line.set_data([CoO[0], CoO[0]+l*CoZ[0]],[CoO[1], CoO[1]+l*CoZ[1]]);
    z_line.set_3d_properties([CoO[2], CoO[2]+l*CoZ[2]]);
     
        
        
def TranslateOnXRight(a):
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim3d([-0.5, 1])
    ax.set_ylim3d([-0.5, 1])
    ax.set_zlim3d([0, 1])

    ax.view_init(30, 30)

    # load some test data for demonstration and plot a wireframe
    ax.plot([0, 1], [0, 0], [0, 0], c='blue')
    ax.plot([0, 0], [0, 1], [0, 0], c='green')
    ax.plot([0, 0], [0, 0], [0, 1], c='red')


    x_line, = ax.plot([0, 0.5], [0, 0], [0, 0], lw=6, c='blue')
    y_line, = ax.plot([0, 0], [0, 0.5], [0, 0], lw=6, c='green')
    z_line, = ax.plot([0, 0], [0, 0], [0, 0.5], lw=6, c='red')


    matrix = np.array([[1.,  0.,  0., 0.5],
                       [0.,  1.,  0., 0.5],
                       [0.,  0.,  1., 0],
                       [0.,  0.,  0., 1]])
    
    mat = np.matmul( matrix, tfrz(1));
    tf = np.matmul( mat,tft([a,0,0]));

    CoX = tf[:,0];
    CoY = tf[:,1];
    CoZ = tf[:,2];
    CoO = tf[:,3];
    l = 0.5;

    
    x_line.set_data([CoO[0], CoO[0]+l*CoX[0]],[CoO[1], CoO[1]+l*CoX[1]]);
    x_line.set_3d_properties([CoO[2], CoO[2]+l*CoX[2]]);
    y_line.set_data([CoO[0], CoO[0]+l*CoY[0]],[CoO[1], CoO[1]+l*CoY[1]]);
    y_line.set_3d_properties([CoO[2], CoO[2]+l*CoY[2]]);
    z_line.set_data([CoO[0], CoO[0]+l*CoZ[0]],[CoO[1], CoO[1]+l*CoZ[1]]);
    z_line.set_3d_properties([CoO[2], CoO[2]+l*CoZ[2]]);
    


