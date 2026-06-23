# trackmania_rl/optimizer.py
import random

def tasConfig():

    gameInputs = [
        (0, "press u"),       
        (1200, "press r"),    
        (2500, "release r"),  
        (4000, "release u")   
    ]
    return gameInputs

def mutateConfig(baseInputs):
   
    mutatedInputs = []
    for timestampInMs, action in baseInputs:
        if timestampInMs == 0:
            mutatedInputs.append((timestampInMs, action))
        else:
            
            timeVariance = random.randint(-30, 30)
            mutatedInputs.append((timestampInMs + timeVariance, action))
            
    return mutatedInputs

if __name__ == "__main__":
    
    base = tasConfig()
    mutated = mutateConfig(base)
    print(f"Original: {base}")
    print(f"Mutated:  {mutated}")
