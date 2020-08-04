import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import math as m
from matplotlib import animation

def showAxes(Z):


    ### setting up 3d figure with limits on axes
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_zlim(-1, 1)  
    ax.set_xlim(-1, 1)  
    ax.set_ylim(-1, 1)  

    l = Z[0,:].size

    ### cross product with a helper vector that is not on the same axis, for X
    ### cross product of X and Z for Y

    helper = np.full((50,3), [1,0,0])
    val = bool(0)

    for i in range(0,l):
        if  np.array_equal(Z[:,i], np.array([1.,0.,0.])):
            val = bool(1)

    if val == bool(1):
        helper = np.full((50,3), [0,1,0])

    X = np.empty([l,3])
    Y = np.empty([l,3])

    for i in range(0,l):
        aux = np.cross([Z[:,i]],[helper[i,:]])
        X[i,:] = aux
    #     b1[i,:] /= np.linalg.norm(b1[i,:])

    
    for i in range(0,l):
        aux = np.cross(Z[:,i],X[i,:])
        Y[i,:] = aux
    #     b2[i,:] /= np.linalg.norm(b2[i,:])

    

    ax.plot3D(Z[0,:], Z[1,:], Z[2,:], 'red')
    ax.plot3D(X[:,0], X[:,1], X[:,2], 'blue')
    ax.plot3D(Y[:,0], Y[:,1], Y[:,2], 'green')

    
    ### axes labels
    zdirs = ( 'x', 'y', 'z')
    xs = ( X[-1,0]/2, Y[-1,0]/2, Z[-1,0]/2 )
    ys = ( X[-1,1]/2, Y[-1,1]/2, Z[-1,1]/2 )
    zs = ( X[-1,2]/2, Y[-1,2]/2, Z[-1,2]/2 )

    for zdir, x, y, z in zip(zdirs, xs, ys, zs):
        label = '%s' % (zdir)
        ax.text(x, y, z, label, zdir)
    
    
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

    def init():
      
        linex.set_data(Xx, Xych)
        linex.set_3d_properties(Xz)
        
        liney.set_data(Yxch, Yy)
        liney.set_3d_properties(Yz)
    
        linez.set_data(Zx, Zy)
        linez.set_3d_properties(Zzch)
            
        return linex, liney, linez,

    def update(i, linex, liney, linez, Xx, Xy, Xz, Yx, Yy, Yz, Zx, Zy, Zz, d):
            
        var = d*i/25
    
        linex.set_data(Xx+var, Xy)
        linex.set_3d_properties(Xz)
        
        liney.set_data(Yx+var, Yy)
        liney.set_3d_properties(Yz)
    
        linez.set_data(Zx+var, Zy)
        linez.set_3d_properties(Zz)
    
        return linex,liney,linez,
    
    anim = animation.FuncAnimation(fig, update, fargs=(linex,liney,linez, Xx, Xych, Xz, Yxch, Yy, Yz, Zx, Zy, Zzch, d),
                               frames = len(ch)+1, interval = 200,
                               repeat_delay = 1000, blit = False, repeat = True)
    
    return anim



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

    def init():
  
        linex.set_data(Xx, Xych)
        linex.set_3d_properties(Xz)
    
        liney.set_data(Yxch, Yy)
        liney.set_3d_properties(Yz)
    
        linez.set_data(Zx, Zy)
        linez.set_3d_properties(Zzch)
        
        return linex, liney, linez,

    def update(i, linex, liney, linez, Xx, Xy, Xz, Yx, Yy, Yz, Zx, Zy, Zz, d):

        var = d*i/25
    
        linex.set_data(Xx, Xy+var)
        linex.set_3d_properties(Xz)
    
        liney.set_data(Yx, Yy+var)
        liney.set_3d_properties(Yz)
    
        linez.set_data(Zx, Zy+var)
        linez.set_3d_properties(Zz)
    
        return linex,liney,linez,

    anim = animation.FuncAnimation(fig, update, fargs=(linex,liney,linez, 
                                                   Xx, Xych, Xz, Yxch, 
                                                   Yy, Yz, Zx, Zy, Zzch, d),
                           frames = len(ch)+1, interval=200,
                           repeat_delay=1000, blit=False, repeat = True)
    return anim


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

    def init():
      
        linex.set_data(Xx, Xych)
        linex.set_3d_properties(Xz)
    
        liney.set_data(Yxch, Yy)
        liney.set_3d_properties(Yz)
    
        linez.set_data(Zx, Zy)
        linez.set_3d_properties(Zzch)
        
        return linex, liney, linez,

    def animate(i, linex, liney, linez, Xx, Xy, Xz, Yx, Yy, Yz, Zx, Zy, Zz, d):

        var = i*d/25
    
        linex.set_data(Xx, Xy)
        linex.set_3d_properties(Xz+var)
    
        liney.set_data(Yx, Yy)
        liney.set_3d_properties(Yz+var)
    
        linez.set_data(Zx, Zy)
        linez.set_3d_properties(Zz+var)
    
        return linex,liney,linez,

    anim = animation.FuncAnimation(fig, animate, fargs=(linex,liney,linez, Xx, Xych, Xz, Yxch, Yy, Yz, Zx, Zy, Zzch, d),
                           frames = len(ch)+1, interval=200,
                           repeat_delay=1000, blit=False, repeat = True)
    return anim

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

    def init():
  
        linex.set_data(Xxch, Xy)
        linex.set_3d_properties(Xz)
    
        liney.set_data(Yx, Yych)
        liney.set_3d_properties(Yz)
    
        linez.set_data(Zx, Zy)
        linez.set_3d_properties(Zzch)
        
        return linex, liney, linez,


    def update(i, linex, liney, linez, Xx, Xy, Xz, Yx, Yy, Yz, Zx, Zy, Zz, theta):

        var = theta*i/25
    
        linex.set_data(Xx, Xy)
        linex.set_3d_properties(Xz)
      
        Yy = np.array([0,0.5*m.sin(m.pi/2+var)])     
        Yz = np.array([0,0.5*m.cos(m.pi/2+var)])
        liney.set_data(Yx, Yy)
        liney.set_3d_properties(Yz)
    
        Zy = np.array([0,0.5*m.sin(var)])     
        Zz = np.array([0,0.5*m.cos(var)])
        linez.set_data(Zx, Zy)
        linez.set_3d_properties(Zz)
    
        return linex,liney,linez,

    anim = animation.FuncAnimation(fig, update, fargs=(linex,liney,linez, Xxch, Xy, Xz, Yx, Yych, Yz, Zx, Zy, Zzch, theta),frames = len(ch)+1, interval=200,
                           repeat_delay=1000, blit=False, repeat = True)
        
    return anim



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

    def init():
  
        linex.set_data(Xxch, Xy)
        linex.set_3d_properties(Xz)
    
        liney.set_data(Yx, Yych)
        liney.set_3d_properties(Yz)
    
        linez.set_data(Zx, Zy)
        linez.set_3d_properties(Zzch)
        
        return linex, liney, linez,


    def update(i, linex, liney, linez, Xx, Xy, Xz, Yx, Yy, Yz, Zx, Zy, Zz, theta):

        var = theta*i/25
    
        Xx = np.array([0,0.5*m.sin(m.pi/2+var)])     
        Xz = np.array([0,0.5*m.cos(m.pi/2+var)])
        linex.set_data(Xx, Xy)
        linex.set_3d_properties(Xz)
      
        liney.set_data(Yx, Yy)
        liney.set_3d_properties(Yz)
    
        Zx = np.array([0,0.5*m.sin(var)])     
        Zz = np.array([0,0.5*m.cos(var)])
        linez.set_data(Zx, Zy)
        linez.set_3d_properties(Zz)
    
        return linex,liney,linez,

    anim = animation.FuncAnimation(fig, update, fargs=(linex,liney,linez, Xxch, Xy, Xz, Yx, Yych, Yz, Zx, Zy, Zzch, theta),frames = len(ch)+1, interval=200,
                           repeat_delay=1000, blit=False, repeat = True)
        
    return anim


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

    def init():
  
        linex.set_data(Xxch, Xy)
        linex.set_3d_properties(Xz)
    
        liney.set_data(Yx, Yych)
        liney.set_3d_properties(Yz)
    
        linez.set_data(Zx, Zy)
        linez.set_3d_properties(Zzch)
        
        return linex, liney, linez,


    def update(i, linex, liney, linez, Xx, Xy, Xz, Yx, Yy, Yz, Zx, Zy, Zz, theta):

        var = theta*i/25
    
        Xx = np.array([0,0.5*m.sin(m.pi/2+var)])     
        Xy = np.array([0,0.5*m.cos(m.pi/2+var)])
        linex.set_data(Xx, Xy)
        linex.set_3d_properties(Xz)
      
        Yx = np.array([0,0.5*m.sin(var)])     
        Yy = np.array([0,0.5*m.cos(var)])
        liney.set_data(Yx, Yy)
        liney.set_3d_properties(Yz)
    
        linez.set_data(Zx, Zy)
        linez.set_3d_properties(Zz)
    
        return linex,liney,linez,

    anim = animation.FuncAnimation(fig, update, fargs=(linex,liney,linez, Xxch, Xy, Xz, Yx, Yych, Yz, Zx, Zy, Zzch, theta),frames = len(ch)+1, interval=200,
                           repeat_delay=1000, blit=False, repeat = True)
        
    return anim


