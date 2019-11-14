import pyrosim
import constantsFinal as c
import random

class ROBOT:
    def __init__(self,sim,wts,label):
        self.send_objects(sim,label)
        self.send_joints(sim,label)
        self.send_sensors(sim,label)
        self.send_neurons(sim)
        self.send_synapses(sim,wts)
        del self.O
        del self.J
        del self.SN
        del self.MN
        
    def send_objects(self,sim,label):
        self.O = {}
        if (label == 'prey'):
            #self.O[0] = sim.send_box(x=-1, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2*c.R, r=1, g=0, b=0)
            self.O[0] = sim.send_box(x=-1, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2*c.R, r=0, g=1, b=0)
            sim.send_light_source( body_id = self.O[0] )
            self.O[6] = sim.send_cylinder(x=1.5*c.L-1, y=0, z=c.L/2+c.R, length=c.L, radius=c.R, r=0, g=0, b=0)
            self.O[8] = sim.send_cylinder(x=-1.5*c.L-1, y=0, z=c.L/2+c.R, length=c.L, radius=c.R, r=0, g=0, b=0)
            self.O[5] = sim.send_cylinder(x=-1, y=1.5*c.L, z=c.L/2+c.R, length=c.L, radius=c.R, r=0, g=0, b=0)
            self.O[7] = sim.send_cylinder(x=-1, y=-1.5*c.L, z=c.L/2+c.R, length=c.L, radius=c.R, r=0, g=0, b=0)
            
            self.O[2] = sim.send_cylinder(x=c.L-1, y=0, z=c.L+c.R, length=c.L, radius=c.R, r=0, g=0, b=0,r1=1 , r2=0, r3=0)
            self.O[4] = sim.send_cylinder(x=-c.L-1, y=0, z=c.L+c.R, length=c.L, radius=c.R, r=0, g=0, b=0,r1=1 , r2=0, r3=0)
            self.O[1] = sim.send_cylinder(x=-1, y=c.L, z=c.L+c.R, length=c.L, radius=c.R, r=0, g=0, b=0,r1=0 , r2=1, r3=0)
            self.O[3] = sim.send_cylinder(x=-1, y=-c.L, z=c.L+c.R, length=c.L, radius=c.R, r=0, g=0, b=0,r1=0 , r2=1, r3=0)

            self.O[9] = sim.send_cylinder(x=c.L/2-1, y=c.L/3, z=c.L+c.R, length=c.L/8, radius=c.R/8, r=0, g=0, b=0.5,r1=1 , r2=0, r3=0)
            self.O[10] = sim.send_cylinder(x=c.L/2-1, y=-c.L/3, z=c.L+c.R, length=c.L/8, radius=c.R/8, r=0, g=0, b=0.5,r1=1 , r2=0, r3=0)
            
            #self.O[11] = sim.send_cylinder(x=c.L/2-1, y=c.L/3, z=c.L+c.R, length=c.L/8, radius=c.R/8, r=0, g=0, b=0.5,r1=1 , r2=1, r3=0)
            #self.O[12] = sim.send_cylinder(x=c.L/2-1, y=-c.L/3, z=c.L+c.R, length=c.L/8, radius=c.R/8, r=0, g=0, b=0.5,r1=1 , r2=-1, r3=0)
            
            #self.O[13] = sim.send_cylinder(x=-c.L/2-1, y=c.L/3, z=c.L+c.R, length=c.L/8, radius=c.R/8, r=0, g=0, b=0.5,r1=-1, r2=0, r3=0)
            #self.O[14] = sim.send_cylinder(x=-c.L/2-1, y=-c.L/3, z=c.L+c.R, length=c.L/8, radius=c.R/8, r=0, g=0, b=0.5,r1=-1, r2=0, r3=0)
            
        else:
            self.O[0] = sim.send_box(x=0, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2*c.R, r=1, g=0, b=0)
            #self.O[0] = sim.send_box(x=0, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2*c.R, r=0, g=1, b=0)
            self.O[6] = sim.send_cylinder(x=1.5*c.L, y=0, z=c.L/2+c.R, length=c.L, radius=c.R, r=0, g=0, b=0)
            self.O[8] = sim.send_cylinder(x=-1.5*c.L, y=0, z=c.L/2+c.R, length=c.L, radius=c.R, r=0, g=0, b=0)
            self.O[5] = sim.send_cylinder(x=0, y=1.5*c.L, z=c.L/2+c.R, length=c.L, radius=c.R, r=0, g=0, b=0)
            self.O[7] = sim.send_cylinder(x=0, y=-1.5*c.L, z=c.L/2+c.R, length=c.L, radius=c.R, r=0, g=0, b=0)
            
            self.O[2] = sim.send_cylinder(x=c.L, y=0, z=c.L+c.R, length=c.L, radius=c.R, r=0, g=0, b=0,r1=1 , r2=0, r3=0)
            self.O[4] = sim.send_cylinder(x=-c.L, y=0, z=c.L+c.R, length=c.L, radius=c.R, r=0, g=0, b=0,r1=1 , r2=0, r3=0)
            self.O[1] = sim.send_cylinder(x=0, y=c.L, z=c.L+c.R, length=c.L, radius=c.R, r=0, g=0, b=0,r1=0 , r2=1, r3=0)
            self.O[3] = sim.send_cylinder(x=0, y=-c.L, z=c.L+c.R, length=c.L, radius=c.R, r=0, g=0, b=0,r1=0 , r2=1, r3=0)
            
##            self.O[0] = sim.send_box(x=1, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2*c.R, r=1, g=0, b=0)
##            #self.O[0] = sim.send_box(x=1, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2*c.R, r=0, g=.5, b=0)
##            self.O[6] = sim.send_cylinder(x=1.5*c.L+1, y=0, z=c.L/2+c.R, length=c.L, radius=c.R, r=0, g=0, b=0)
##            self.O[8] = sim.send_cylinder(x=-1.5*c.L+1, y=0, z=c.L/2+c.R, length=c.L, radius=c.R, r=0, g=0, b=0)
##            self.O[5] = sim.send_cylinder(x=1, y=1.5*c.L, z=c.L/2+c.R, length=c.L, radius=c.R, r=0, g=0, b=0)
##            self.O[7] = sim.send_cylinder(x=1, y=-1.5*c.L, z=c.L/2+c.R, length=c.L, radius=c.R, r=0, g=0, b=0)
##            
##            self.O[2] = sim.send_cylinder(x=c.L+1, y=0, z=c.L+c.R, length=c.L, radius=c.R, r=0, g=0, b=0,r1=1 , r2=0, r3=0)
##            self.O[4] = sim.send_cylinder(x=-c.L+1, y=0, z=c.L+c.R, length=c.L, radius=c.R, r=0, g=0, b=0,r1=1 , r2=0, r3=0)
##            self.O[1] = sim.send_cylinder(x=1, y=c.L, z=c.L+c.R, length=c.L, radius=c.R, r=0, g=0, b=0,r1=0 , r2=1, r3=0)
##            self.O[3] = sim.send_cylinder(x=1, y=-c.L, z=c.L+c.R, length=c.L, radius=c.R, r=0, g=0, b=0,r1=0 , r2=1, r3=0)
 
    def send_joints(self,sim,label):
        self.J = {}
        if (label == 'prey'):
            self.J[0] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[1], x=-1 , y=c.L/2 , z=c.L + c.R, n1 = 1 , n2 = 0 , n3 = 0)
            self.J[1] = sim.send_hinge_joint( first_body_id = self.O[1] , second_body_id = self.O[5], x=-1 , y=1.5*c.L , z=c.L + c.R, n1 = 1 , n2 = 0 , n3 = 0)
            self.J[2] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[2], x=c.L/2-1 , y=0 , z=c.L + c.R, n1 = 0 , n2 = 1 , n3 = 0)
            self.J[3] = sim.send_hinge_joint( first_body_id = self.O[2] , second_body_id = self.O[6], x=1.5*c.L-1 , y=0 , z=c.L + c.R, n1 = 0 , n2 = 1 , n3 = 0)
            self.J[4] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[3], x=-1 , y=-c.L/2 , z=c.L + c.R, n1 = 1 , n2 = 0 , n3 = 0)
            self.J[5] = sim.send_hinge_joint( first_body_id = self.O[3] , second_body_id = self.O[7], x=-1 , y=-1.5*c.L , z=c.L + c.R, n1 = 1 , n2 = 0 , n3 = 0)
            self.J[6] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[4], x=-c.L/2-1 , y=0 , z=c.L + c.R, n1 = 0 , n2 = 1 , n3 = 0)
            self.J[7] = sim.send_hinge_joint( first_body_id = self.O[4] , second_body_id = self.O[8], x=-1.5*c.L-1 , y=0 , z=c.L + c.R, n1 = 0 , n2 = 1 , n3 = 0)
            self.J[8] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[9], x=-1, y=c.L/3, z=c.L+c.R, n1 = 1 , n2 = 0 , n3 = 0, lo = 0, hi= 0)
            self.J[9] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[10], x=-1, y=-c.L/3, z=c.L+c.R, n1 = 1 , n2 = 0 , n3 = 0, lo = 0, hi= 0)
            #self.J[10] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[11], x=-1, y=c.L/3, z=c.L+c.R, n1 = 1 , n2 = 1 , n3 = 0, lo = 0, hi= 0)
            #self.J[11] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[12], x=-1, y=-c.L/3, z=c.L+c.R, n1 = 1 , n2 = -1 , n3 = 0, lo = 0, hi= 0)
            #self.J[12] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[13], x=-1, y=c.L/3, z=c.L+c.R, n1 = -1 , n2 = 0 , n3 = 0, lo = 0, hi= 0)
            #self.J[13] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[14], x=-1, y=-c.L/3, z=c.L+c.R, n1 = -1 , n2 = 0 , n3 = 0, lo = 0, hi= 0)

        else:
            self.J[0] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[1], x=0 , y=c.L/2 , z=c.L + c.R, n1 = 1 , n2 = 0 , n3 = 0)
            self.J[1] = sim.send_hinge_joint( first_body_id = self.O[1] , second_body_id = self.O[5], x=0 , y=1.5*c.L , z=c.L + c.R, n1 = 1 , n2 = 0 , n3 = 0)
            self.J[2] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[2], x=c.L/2+0 , y=0 , z=c.L + c.R, n1 = 0 , n2 = 1 , n3 = 0)
            self.J[3] = sim.send_hinge_joint( first_body_id = self.O[2] , second_body_id = self.O[6], x=1.5*c.L+0 , y=0 , z=c.L + c.R, n1 = 0 , n2 = 1 , n3 = 0)
            self.J[4] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[3], x=0 , y=-c.L/2 , z=c.L + c.R, n1 = 1 , n2 = 0 , n3 = 0)
            self.J[5] = sim.send_hinge_joint( first_body_id = self.O[3] , second_body_id = self.O[7], x=0 , y=-1.5*c.L , z=c.L + c.R, n1 = 1 , n2 = 0 , n3 = 0)
            self.J[6] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[4], x=-c.L/2+0 , y=0 , z=c.L + c.R, n1 = 0 , n2 = 1 , n3 = 0)
            self.J[7] = sim.send_hinge_joint( first_body_id = self.O[4] , second_body_id = self.O[8], x=-1.5*c.L+0 , y=0 , z=c.L + c.R, n1 = 0 , n2 = 1 , n3 = 0)

##            self.J[0] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[1], x=1 , y=c.L/2 , z=c.L + c.R, n1 = 1 , n2 = 0 , n3 = 0)
##            self.J[1] = sim.send_hinge_joint( first_body_id = self.O[1] , second_body_id = self.O[5], x=1 , y=1.5*c.L , z=c.L + c.R, n1 = 1 , n2 = 0 , n3 = 0)
##            self.J[2] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[2], x=c.L/2+1 , y=0 , z=c.L + c.R, n1 = 0 , n2 = 1 , n3 = 0)
##            self.J[3] = sim.send_hinge_joint( first_body_id = self.O[2] , second_body_id = self.O[6], x=1.5*c.L+1 , y=0 , z=c.L + c.R, n1 = 0 , n2 = 1 , n3 = 0)
##            self.J[4] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[3], x=1 , y=-c.L/2 , z=c.L + c.R, n1 = 1 , n2 = 0 , n3 = 0)
##            self.J[5] = sim.send_hinge_joint( first_body_id = self.O[3] , second_body_id = self.O[7], x=1 , y=-1.5*c.L , z=c.L + c.R, n1 = 1 , n2 = 0 , n3 = 0)
##            self.J[6] = sim.send_hinge_joint( first_body_id = self.O[0] , second_body_id = self.O[4], x=-c.L/2+1 , y=0 , z=c.L + c.R, n1 = 0 , n2 = 1 , n3 = 0)
##            self.J[7] = sim.send_hinge_joint( first_body_id = self.O[4] , second_body_id = self.O[8], x=-1.5*c.L+1 , y=0 , z=c.L + c.R, n1 = 0 , n2 = 1 , n3 = 0)


    def send_sensors(self,sim,label):
        self.S = {}
        self.S[0] = sim.send_touch_sensor( body_id = self.O[5] )
        self.S[1] = sim.send_touch_sensor( body_id = self.O[6] )
        self.S[2] = sim.send_touch_sensor( body_id = self.O[7] )
        self.S[3] = sim.send_touch_sensor( body_id = self.O[8] )
        if (label == 'prey'):
            self.S[4] = sim.send_ray_sensor( body_id = self.O[1], x=-1, y= 1.5*c.L+c.R, z=c.L + c.R, r1 = 0 , r2 = 1, r3 = 0)
            self.S[5] = sim.send_ray_sensor( body_id = self.O[2], x=-1+1.5*c.L+c.R, y= 0, z=c.L + c.R, r1 = 1 , r2 = 0, r3 = 0)
            self.S[6] = sim.send_ray_sensor( body_id = self.O[3], x=-1, y= -(1.5*c.L+c.R), z=c.L + c.R, r1 = 0 , r2 = -1, r3 = 0)
            self.S[7] = sim.send_ray_sensor( body_id = self.O[4], x=-1-1.5*c.L-c.R, y= 0, z=c.L + c.R, r1 = -1 , r2 = 0, r3 = 0)
            
            self.S[8] = sim.send_ray_sensor( body_id = self.O[9], x=-1+c.L/2+c.L/16+c.R/8 , y= c.L/3, z=c.L+c.R , r1 = 1 , r2 = 0, r3 = 0)
            self.S[9] = sim.send_ray_sensor( body_id = self.O[10], x=-1+c.L/2+c.L/16+c.R/8 , y= -c.L/3, z=c.L+c.R , r1 = 1 , r2 = 0, r3 = 0)

            #self.S[10] = sim.send_ray_sensor( body_id = self.O[11], x=-1+c.L/2+ ((c.L/16-c.R/8)/2**0.5) , y= c.L/3+((c.L/16-c.R/8)/2**0.5), z=c.L+c.R , r1 = 1 , r2 = 1, r3 = 0)
            #self.S[11] = sim.send_ray_sensor( body_id = self.O[12], x=-1+c.L/2+ ((c.L/16-c.R/8)/2**0.5) , y= -c.L/3+((c.L/16-c.R/8)/2**0.5), z=c.L+c.R , r1 = 1 , r2 = -1, r3 = 0)

            #self.S[12] = sim.send_ray_sensor( body_id = self.O[13], x=-1-c.L/2-c.L/16-c.R/8 , y= c.L/3, z=c.L+c.R , r1 = -1 , r2 = 0, r3 = 0)
            #self.S[13] = sim.send_ray_sensor( body_id = self.O[14], x=-1-c.L/2-c.L/16-c.R/8 , y= -c.L/3, z=c.L+c.R , r1 = -1 , r2 = 0, r3 = 0)

        else:
            self.S[4] = sim.send_light_sensor( body_id = self.O[0] )
##            self.S[5] = sim.send_light_sensor( body_id = self.O[1] )
##            self.S[6] = sim.send_light_sensor( body_id = self.O[2] )
##            self.S[7] = sim.send_light_sensor( body_id = self.O[3] )
##            self.S[8] = sim.send_light_sensor( body_id = self.O[4] )
##            self.S[5] = sim.send_light_sensor( body_id = self.O[5] )
##            self.S[6] = sim.send_light_sensor( body_id = self.O[6] )
##            self.S[7] = sim.send_light_sensor( body_id = self.O[7] )
##            self.S[8] = sim.send_light_sensor( body_id = self.O[8] )
            
    def send_neurons(self,sim):
        self.SN = {}
        self.MN = {}
        for s in self.S:
            self.SN[s] = sim.send_sensor_neuron( sensor_id = self.S[s] )
        for j in self.J:
            self.MN[j] = sim.send_motor_neuron( joint_id = self.J[j] ,tau = 0.3)

    def send_synapses(self,sim,wts):           
        for j in self.SN:
            for i in self.MN:
                sim.send_synapse( source_neuron_id = self.SN[j] , target_neuron_id = self.MN[i] , weight = wts[j,i] )




#################### CODE GRAVE #####################
##        if (idnum == 0):
##            self.S[4] = sim.send_ray_sensor( body_id = self.O[0], x=-1, y= 0, z=c.L + c.R, r1 = 0 , r2 = 1, r3 = 0)
##            self.S[5] = sim.send_ray_sensor( body_id = self.O[0], x=-1, y= 0, z=c.L + c.R, r1 = 0 , r2 = -1, r3 = 0)
##            self.S[6] = sim.send_ray_sensor( body_id = self.O[0], x=-1, y= 0, z=c.L + c.R, r1 = -1 , r2 = 0, r3 = 0)
##            self.S[7] = sim.send_ray_sensor( body_id = self.O[0], x=-1, y= 0, z=c.L + c.R, r1 = 1 , r2 = 0, r3 = 0)
##            self.S[8] = sim.send_ray_sensor( body_id = self.O[0], x=-1, y= 0, z=c.L + c.R, r1 = 1 , r2 = 1, r3 = 0)
##            self.S[9] = sim.send_ray_sensor( body_id = self.O[0], x=-1, y= 0, z=c.L + c.R, r1 = -1 , r2 = -1, r3 = 0)
##            self.S[10] = sim.send_ray_sensor( body_id = self.O[0], x=-1, y= 0, z=c.L + c.R, r1 = -1 , r2 = 1, r3 = 0)
##            self.S[11] = sim.send_ray_sensor( body_id = self.O[0], x=-1, y= 0, z=c.L + c.R, r1 = 1 , r2 = -1, r3 = 0)
##        else:
##            self.S[4] = sim.send_ray_sensor( body_id = self.O[0], x=1, y= 0, z=c.L + c.R, r1 = 0 , r2 = 1, r3 = 0)
##            self.S[5] = sim.send_ray_sensor( body_id = self.O[0], x=1, y= 0, z=c.L + c.R, r1 = 0 , r2 = -1, r3 = 0)
##            self.S[6] = sim.send_ray_sensor( body_id = self.O[0], x=1, y= 0, z=c.L + c.R, r1 = -1 , r2 = 0, r3 = 0)
##            self.S[7] = sim.send_ray_sensor( body_id = self.O[0], x=1, y= 0, z=c.L + c.R, r1 = 1 , r2 = 0, r3 = 0)
##            self.S[8] = sim.send_ray_sensor( body_id = self.O[0], x=1, y= 0, z=c.L + c.R, r1 = 1 , r2 = 1, r3 = 0)
##            self.S[9] = sim.send_ray_sensor( body_id = self.O[0], x=1, y= 0, z=c.L + c.R, r1 = -1 , r2 = -1, r3 = 0)
##            self.S[10] = sim.send_ray_sensor( body_id = self.O[0], x=1, y= 0, z=c.L + c.R, r1 = -1 , r2 = 1, r3 = 0)
##            self.S[11] = sim.send_ray_sensor( body_id = self.O[0], x=1, y= 0, z=c.L + c.R, r1 = 1 , r2 = -1, r3 = 0)

##            self.S[4] = sim.send_ray_sensor( body_id = self.O[1], x=1, y= 1.5*c.L+c.R, z=c.L + c.R, r1 = 0 , r2 = 1, r3 = 0)
##            self.S[5] = sim.send_ray_sensor( body_id = self.O[2], x=1+1.5*c.L+c.R, y= 0, z=c.L + c.R, r1 = 1 , r2 = 0, r3 = 0)
##            self.S[6] = sim.send_ray_sensor( body_id = self.O[3], x=1, y= -(1.5*c.L+c.R), z=c.L + c.R, r1 = 0 , r2 = -1, r3 = 0)
##            self.S[7] = sim.send_ray_sensor( body_id = self.O[4], x=1-1.5*c.L-c.R, y= 0, z=c.L + c.R, r1 = -1 , r2 = 0, r3 = 0)
