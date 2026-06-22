# trackmania_rl/reward_shaping.py

def computeMiniRaceReward(velocity, deviationFromRef, hitWall):
    """
    Reward function based on Linesight's 7-second mini-race trick.
    """
    if hitWall:
        return -500.0  # Massive penalty to kill bad trajectories early
    
    # Reward high velocity but penalize drifting too far from the reference line
    reward = (velocity * 0.2) - (deviationFromRef * 0.5)
    return reward