from __future__ import print_function
import robopy.base.model as model
import robopy.base.util as util
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import robopy


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
    traj = util.ctraj(Ts, Te, N)._list
                     
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
    
    xs = 0.0 
    xe = Px
    ys = 0.0 
    ye = Py
    zs = 0.0 
    ze = Pz 
    T  = 5
    dss, dse, ddss, ddse = 0,0,0,0
    steps = 100*T
    time = np.linspace(0,T,steps)
    timed = np.array((np.power(time,5),np.power(time,4),np.power(time,3),np.power(time,2),time,np.ones((1,steps))))
    
    A = np.array([[0,0,0,0,0,1],
                  [T**5, T**4, T**3,T**2, T, 1],
                  [0,0,0,0,1,0],
                  [5*T**4,4*T**3,3*T**2,2*T,1,0],
                  [0,0,0,2,0,0],
                  [20*T**3,12*T**2,6*T,2,0,0]]) 
    
    inpt = np.array([0,1,dss,dse,ddss,ddse])
    inpt.shape = (6,1)
    sol = np.linalg.inv(A).dot(inpt)
    
    s = sol[0]*timed[0]+sol[1]*timed[1]+sol[2]*timed[2]+sol[3]*timed[3]+sol[4]*timed[4]+sol[5]*timed[5]
    x = (1-s)*xs+s*xe
    y = (1-s)*ys+s*ye
    z = (1-s)*zs+s*ze
    
    x.shape = (steps,1)
    y.shape = (steps,1)
    z.shape = (steps,1)
    
    robot = model.Puma560()
    qs = np.zeros((steps,6))
    for i in range(steps):
        if i == 0:
            qs[i,:] = robot.ikine(robopy.transl(x[i,0],y[i,0],z[i,0])*rpy2tr(), q0=[0,0,0,0,0,0], unit="rad")
        else:
            qs[i,:] = robot.ikine(robopy.transl(x[i,0],y[i,0],z[i,0]), q0=qs[i-1,:], unit="rad")

    print("The joint angles for each iteration are:")
    for i in range(steps):
        print("-----\n q1 = %r, q2 = %r, q3 = %r, q4 = %r, q5 = %r, q6 = %r"
              % (qs[i,0], qs[i,1],qs[i,2], qs[i,3], qs[i,4], qs[i,5]))
        
    plot_robot(qs)
    


                      
