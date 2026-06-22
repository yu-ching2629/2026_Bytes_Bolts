# for Unseen Track or test Seen
# No training required.Aims directly at the next Virtual Checkpoint (VCP).

import math

def getBestAction(carX, carY, carAngle, nextVcpX, nextVcpY):

    # Calculate angle to the next checkpoint
    angleToTarget = math.atan2(nextVcpY - carY, nextVcpX - carX)
    angleError = angleToTarget - carAngle
    
    # Normalize angle error between -pi and pi
    angleError = (angleError + math.pi) % (2 * math.pi) - math.pi
    
    # Simple rule-based discrete actions
    if angleError > 0.15:
        return {"forward": True, "backward": False, "left": False, "right": True}   # Turn Right
    elif angleError < -0.15:
        return {"forward": True, "backward": False, "left": True, "right": False}  # Turn Left
    else:
        return {"forward": True, "backward": False, "left": False, "right": False} # Drive Straight