from UDPComms import Publisher
import time 
# look into joystickinterface.py for control outputs
# drive_pub = Publisher(8830) = controls movement of pupper (basically mode 1)
# arm_pub = Publisher(8410) = controls more movements of upper (mode 2)
# mode 2 is what you can do when pupper is not in trot mode when using a controller.
drive_pub = Publisher(8830)
arm_pub = Publisher(8410)
# L1 = activate/disactivate
# R1 = transition between Rest mode and Trot mode.
# circle = dance or hold for 3 seconds to turn off system
# trinagle  = NOTHING 
# X = jump
# L2 = nothing
# R2 = Nothing
# ly = forward or backwards
# lx = left or right
# rx = turn left or right (pitch)
# ry = pitches the robot forward
def activate():
    drive_pub.send({"L1": 1, 
            "R1": 0, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0, 
            "lx": 0, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})

def trot():
    drive_pub.send({"L1": 0, 
            "R1": 1, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": 0, 
            "lx": 0, 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})
    
    
def move_forward():
    drive_pub.send({"L1": 0, 
            "R1": 0, 
            "x": 0, 
            "circle": 0, 
            "triangle": 0, 
            "L2": 0, 
            "R2": 0, 
            "ly": [0.1, 0], 
            "lx": [0, 0], 
            "rx": 0, 
            "message_rate": 20, 
            "ry": 0, 
            "dpady": 0, 
            "dpadx": 0})
    
if __name__ == "__main__":
    activate()
    # trot()
    time.sleep(1)
    trot()
    print("moving forward")
    time.sleep(5)
    a = True
    while a:
        move_forward()
    # trot_stop()
    # activate_stop()