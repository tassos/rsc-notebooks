from ipywidgets import interact, interact_manual, widgets
from mpl_toolkits.mplot3d import axes3d
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
from matplotlib.patches import Circle, PathPatch, Ellipse


def velocity(q1, q2, joint, j_type):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.axis('equal')

    ax.set_xlim([-0.5, 3.5])
    ax.set_ylim([-0.5, 3.5])

    # load some test data for demonstration and plot a wireframe
    ax.plot([0, 1], [0, 0], [0, 0], c='blue')
    ax.plot([0, 0], [0, 1], [0, 0], c='green')

    link_1, = ax.plot([0, 1], [0, 0], lw=6, c='blue')
    link_2, = ax.plot([1, 2], [0, 0], lw=6, c='green')

    l1 = 1
    l2 = 1
 
    
    def update(i, q1, q2, val1, val2):
        
        
        val2 = np.radians(val2)
        imp = 90/val1
        it = np.radians(-(abs(i-90)-90)/imp) 
        point1 = np.array([l1*np.cos(it+q1),l1*np.sin(it+q1)])
        point2 = np.array([point1[0]+l2*np.cos(it-(abs(i-90)-90)*val2/90+q1+q2),
                           point1[1]+l2*np.sin(it-(abs(i-90)-90)*val2/90+q1+q2)])

        link_1.set_data([0, point1[0]],[0, point1[1]])
        link_2.set_data([point1[0], point2[0]],[point1[1], point2[1]])
    
    
    def update_p1(i, q1, q2, val1, val2):
        
        point1 = np.array([(l1+i/180/5)*np.cos(q1),(l1+i/180/5)*np.sin(q1)])
        point2 = np.array([point1[0]+l2*np.cos(q1+q2),point1[1]+l2*np.sin(q1+q2)])

        link_1.set_data([0, point1[0]],[0, point1[1]])
        link_2.set_data([point1[0], point2[0]],[point1[1], point2[1]])
    
    
    def update_p2(i, q1, q2, val1, val2):
        
        point1 = np.array([l1*np.cos(q1),l1*np.sin(q1)])
        point2 = np.array([point1[0]+(l2+i/180/5)*np.cos(q1+q2),point1[1]+(l2+i/180/5)*np.sin(q1+q2)])

        link_1.set_data([0, point1[0]],[0, point1[1]])
        link_2.set_data([point1[0], point2[0]],[point1[1], point2[1]])
    
        
    
    if (joint =='q1'):
        val1, val2 = 6, 0.01  #degrees 
    else:
        val1, val2 = 0.01, 6
    
    
    if (j_type == 'prismatic' and joint == 'q1' ):
        line_ani = animation.FuncAnimation(fig, update_p1, 180, interval=1, blit=False, fargs=(q1, q2, val1, val2,), repeat = True )
        return line_ani

    elif (j_type == 'prismatic' and joint == 'q2'):
        line_ani = animation.FuncAnimation(fig, update_p2, 180, interval=1, blit=False, fargs=(q1, q2, val1, val2,), repeat = True )
        return line_ani

    else:
        line_ani = animation.FuncAnimation(fig, update, 180, interval=1, blit=False, fargs=(q1, q2, val1, val2,), repeat = True )
        return line_ani
    
    

def velocity_ell(q1, q2):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.axis('equal')

    ax.set_xlim([-2.5, 3.5])
    ax.set_ylim([-2.5, 3.5])

    # load some test data for demonstration and plot a wireframe
    ax.plot([0, 1], [0, 0], [0, 0], c='blue')
    ax.plot([0, 0], [0, 1], [0, 0], c='green')

    link_1, = ax.plot([0, 0], [1, 0], lw=6, c='blue')
    link_2, = ax.plot([1, 2], [0, 0], lw=6, c='green')

    el = Ellipse((2,0),1,0,angle=90,linewidth=3, fill=False)

    ax.add_patch(el)

    l1 = 1
    l2 = 1

    point1 = np.array([l1*np.cos(q1),l1*np.sin(q1)])
    point2 = np.array([point1[0]+l2*np.cos(q2+q1),point1[1]+l2*np.sin(q2+q1)])

    link_1.set_data([0, point1[0]],[0, point1[1]]);
    link_2.set_data([point1[0], point2[0]],[point1[1], point2[1]]);
    
    Jac = np.array([[-l1*np.sin(q1)-l2*np.sin(q1+q2),-l2*np.sin(q1+q2)],[l1*np.cos(q1)+l2*np.cos(q1+q2),l2*np.cos(q1+q2)]])

    A = np.matmul(Jac,np.transpose(Jac))
    w, v = np.linalg.eig(A)
    el.center = (point2[0],point2[1])
    el.height = np.sqrt(min(w))
    el.width = np.sqrt(max(w))
    el.angle = np.degrees(np.arccos(v[1][0]))
    
    plt.show()




    
