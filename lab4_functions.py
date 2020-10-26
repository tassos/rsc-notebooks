from __future__ import print_function
import robopy.base.model as model
import robopy.base.util as util
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from robopy import *
from robopy import util as ut
from sympy import *

def plot_robot(qs):
    robot = model.Puma560()
    robot.animate(stances=qs, frame_rate=30, unit='rad')
    del robot
    plt.show()
    

def see_end_effector(q1, q2, q3, q4, q5, q6):
    
    robot = model.Puma560()
    
    qe = np.asmatrix([q1,q2,q3,q4,q5,q6])
    qs = np.asmatrix([0,0,0,0,0,0])
    
    Te = robot.fkine(qe)
    Ts = robot.fkine(qs)
    
    N = 100
    traj = ut.ctraj(Ts, Te, N)._list
                     
    q = np.zeros((N,6))      
    for i in range(N):
            if i == 0:
                q[i,:] = robot.ikine((traj[i]), q0=[0,0,0,0,0,0], unit="rad")
            else:
                q[i,:] = robot.ikine((traj[i]), q0=q[i-1,:], unit="rad")

    print("the final pose of the end effector is \n %r" % (Te))
    print("The poses through which it passes are:")

    for i in range(N):
        print("-----\n",traj[i])
        
        
    plot_robot(q)
    
    
def see_joint_angles(Px,Py,Pz):
    
    robot = model.Puma560() 
    T = transl(Px,Py,Pz)
    qs = robot.ikine(T)
    print("-----\n q1 = %r, q2 = %r, q3 = %r, q4 = %r, q5 = %r, q6 = %r"
               % (qs[0,0], qs[0,1],qs[0,2], qs[0,3], qs[0,4], qs[0,5]))
    plot_robot(qs)
    
       
def trotx_sym(theta):
    
    ct = cos(theta)
    st = sin(theta)
    tm = Matrix([[1, 0, 0], [0, ct, -st], [0, st, ct]])
    
    tm = tm.row_insert(3, Matrix([[0,0,0]]))
    tm = tm.col_insert(3, Matrix([0,0,0,1]))
    
    return tm
    
    
    
def troty_sym(theta):
    
    ct = cos(theta)
    st = sin(theta)
    tm = Matrix([[ct, 0, st], [0, 1, 0], [-st, 0, ct]])
    
    tm = tm.row_insert(3, Matrix([[0,0,0]]))
    tm = tm.col_insert(3, Matrix([0,0,0,1]))
    
    return tm
    
    
def trotz_sym(theta):
    
    ct = cos(theta)
    st = sin(theta)
    tm = Matrix([[ct, -st, 0], [st, ct, 0], [0, 0, 1]])
    
    tm = tm.row_insert(3, Matrix([[0,0,0]]))
    tm = tm.col_insert(3, Matrix([0,0,0,1]))
    
    return tm  
    
    
    
def transl_sym(x,y,z):
     
    t = Matrix([[1,0,0,x], [0,1,0,y], [0,0,1,z], [0,0,0,1]])
    
    return t


    
    
    
    
    
    
    
    
    