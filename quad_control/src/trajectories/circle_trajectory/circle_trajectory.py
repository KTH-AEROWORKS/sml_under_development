"""This class implements a fixed-point trajectory,
i.e., a trajectory that stays in the same point forever.
"""

from .. import trajectory as tj
import numpy as np
import json


class CircleTrajectory(tj.Trajectory):


    @classmethod
    def description(cls):
        return "<b>Circle trajectory</b> with <b>radius</b> in (m), and <b>speed</b> (linear velocity) in (m/s)"
        
        
    def __init__(self,
            offset=np.array([0.0, 0.0, 1.0]),
            rotation=np.zeros(3),
            radius=1.0,
            speed=0.1):

        tj.Trajectory.__init__(self, offset=offset, rotation=rotation)
        self.radius = radius
        self.speed = speed
    
    def object_description(self):
        string  = tj.Trajectory.object_description(self)+"\n"
        string += "Circle trajectory with <b>radius = "+ str(self.radius) + "</b> in (m),"
        string += "and <b>speed = "+ str(self.speed) + "</b> (linear velocity) in (m/s)"        
        return string
        
    def desired_trajectory(self, time):
        c = np.cos
        s = np.sin
        r = self.radius
        w = self.speed
        t = time
        pos = r*w**0*np.array([ c(w*t),-s(w*t),0.0]);
        vel = r*w**1*np.array([-s(w*t),-c(w*t),0.0]);
        acc = r*w**2*np.array([-c(w*t), s(w*t),0.0]);
        jrk = r*w**3*np.array([ s(w*t), c(w*t),0.0]);
        snp = r*w**4*np.array([ c(w*t),-s(w*t),0.0]);
        return pos, vel, acc, jrk, snp

    
# """Test"""
#string = CircleTrajectory.to_string()
#print string
#tr = CircleTrajectory.from_string(string)
#print tr


