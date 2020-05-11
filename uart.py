import pygame
import serial


def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

pygame.init()
print ("Joystics No: ", pygame.joystick.get_count())
my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()
clock = pygame.time.Clock()
ser = serial.Serial('/dev/serial0', 115200)
while 1:
    for event in pygame.event.get():
        x=my_joystick.get_axis(0)
        y=my_joystick.get_axis(1)
        clock.tick(100)
        x=-1*(map(x, -1, 1, -1023, 1023))
        y=map(y, -1, 1, -1023, 1023)
        rval=0
        lval=0

        if(y>0): #above origin to move forward
            
            rval=map(y,0,1023,0,255)
            lval=map(y,0,1023,0,255)
        elif(y<0):
        
            rval=map(y,0,-1023,0,-255)
            lval=map(y,0,-1023,0,-255)
            
        else : #when at center
        
            rval=0
            lval=0
            
        #mapping xAxis to get exact analogWrite value

        if(x>0):
        
            xmapped=map(x,0,1023,0,255)
            rval=rval-xmapped
            lval=lval+xmapped
            
        if(lval>255):
          lval=255
        if(rval<-255):
          rval=-255
        elif(x<0):
            xmapped=map(x,0,-1023,0,255)
            rval=rval+xmapped
            lval=lval-xmapped
        if(rval>255):
          rval=255
        if(lval<-255):
         lval=-255
        l = 'l' if lval>= 0 else 'w'
        r = 'r' if rval>= 0 else 'w'
        packet = 's' + l + str(format(abs(lval), '03')) + r + str(format(abs(rval), '03')) + 'e'
        ser.write(packet.encode('utf-8'))
        print(packet)
        #print('Lval:',lval)
        #print('Rval:',rval)
        
        


        
