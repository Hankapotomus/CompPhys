
import numpy as np
import matplotlib.pyplot as mp



    
def rising1D(v0,g=9.8):
    h = v0**2/(2*g)
    t = v0/g
    return h,t   #defines the first part of the projectile motion, until upwards velocity equals gravity at the crit point



def falling1D(h,v0=0):
    # returns the time and velocity of an object falling from h and at an initial velocity v0
    g=9.8
    #solution to quadratic equation
    time = -v0/g + np.sqrt(v0**2/g**2+2*h/g)
    velo = np.sqrt(v0**2+2*g*h)
    return time,velo  #returns the final time and final velocy

def projectile(v0, angle, h):   #defines the entire trajectory, inputs inital velocity, angle, and height from launch
    deg2rad = lambda ang: ang*np.pi/180  #lambda function, simple code, iterated often
    angle = deg2rad(angle) #uses lambda function
    vx= v0*np.cos(angle)   #x component velocity
    vy0 = v0*np.sin(angle) #y component velocity
    [h1, t1] = rising1D(vy0)     #height from start and time at crit point
    maxh = h + h1      #inital height plus added height too get to crit point
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


def projectilegraph (v0, angle, h): #it should take the launch velocity and launch angle, return the range and maximum height, and produce the trajectory graph
    vf, rang, time, maxh, vy0, vx, vfangle = projectile(v0, angle, h) # return vairables vf, vfangle, vx, vy0
    
    g = 9.8
    interval= 1000
    Tinterval = time / interval #makes 1000 points to calculate the time
    Tvalues = [ex * Tinterval for ex in range(interval+1) ]
   
    
    xrange = lambda t: vx * t
    yrange = lambda t: h + vy0 * t - 0.5 * g *t**2
    
    distance = [xrange(t) for t in Tvalues]       
    height = [yrange(t) for t in Tvalues]
    


    mp.plot(distance,height)
    mp.xlabel("distance")
    mp.ylabel("height")
    mp.axis ((0,500,0,100))
    mp.grid(True)
    mp.show()
    
    return rang, maxh, vf, time


    
projectile(62,25,26.5)
projectilegraph (62,25,26.5)
    


