import matplotlib.pyplot as plt
from robopy import transforms

def plotAxes(m, ax, lw=1, ln=1):
    ax.plot3D([m[0,3],m[0,0]*ln+m[0,3]], [m[1,3],m[1,0]*ln+m[1,3]], [m[2,3],m[2,0]*ln+m[2,3]], 'blue', linewidth=lw)
    ax.plot3D([m[0,3],m[0,1]*ln+m[0,3]], [m[1,3],m[1,1]*ln+m[1,3]], [m[2,3],m[2,1]*ln+m[2,3]], 'green', linewidth=lw)
    ax.plot3D([m[0,3],m[0,2]*ln+m[0,3]], [m[1,3],m[1,2]*ln+m[1,3]], [m[2,3],m[2,2]*ln+m[2,3]], 'red', linewidth=lw)

def setPlot():
    #set plot
    fig = plt.figure()
    ax  = fig.add_subplot(111, projection='3d')
    ax.set_zlim(-1, 2)  
    ax.set_xlim(-1, 2)  
    ax.set_ylim(-1, 2)
    
    plotAxes(transforms.transl(0,0,0), ax, lw=1, ln=2)
    return ax