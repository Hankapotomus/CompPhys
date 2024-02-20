
import numpy as np
import matplotlib.pyplot as mp



    
def rising1D(v0,g=9.8):
    h = v0**2/(2*g)
    t = v0/g
    return h,t



def falling1D(h,v0=0):
    # returns the time and velocity of an object falling from h and at an initial velocity v0
    g=9.8
    #solution to quadratic equation
    time = -v0/g + np.sqrt(v0**2/g**2+2*h/g)
    velo = np.sqrt(v0**2+2*g*h)
    return time,velo

def projectile(v0, angle, h):
    deg2rad = lambda ang: ang*np.pi/180
    angle = deg2rad(angle)
    vx= v0*np.cos(angle)
    vy0 = v0*np.sin(angle)
    [h1, t1] = rising1D(vy0)
    maxh = h + h1
    [t2, vf] = falling1D(maxh)
    time = t1 + t2  
    rang = vx*time
    time = np.round(time, decimals = 2)
    rang = np.round(rang, decimals = 2)
    vf = np.round(vf, decimals = 2)

   
    maxh = np.round(maxh, decimals = 2)

    vfangle = np.arccos(vf/vx)
    vfangle = np.round(vfangle, decimals = 2)
 
    return time, rang, vf, maxh, vy0, vx, vfangle


def projectilegraph (v0, angle, h):
   
    
   
    vf, rang, time, maxh, vy0, vx, vfangle = projectile(v0, angle, h)
    
    t= list(range(time))
    
    xrange = lambda t: vx * t

    yrange = lambda rang:  vy0 * t 
              
    
    


    plotP = mp.plot(xrange,yrange)
    mp.xlabel("time")
    mp.ylabel("range")
    mp.grid(True)
    plotP.show()

# return vairables vf, vfangle, vx, vy0
#define new prograph, v0, angle, h 

 

#t should take the launch velocity and launch angle, return the range and maximum height, and produce the trajectory graph




