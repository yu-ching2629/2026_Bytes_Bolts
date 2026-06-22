import os

def tasConfig():
    # TODO: Connect optimization loop/algorithm here later to mutate timestamps
    # Key mapping for TMAS: u=Up, d=Down, l=Left, r=Right
    gameInputs = [
        (0, "press u"),       
        (1200, "press r"),    
        (2500, "release r"),  
        (4000, "release u")   
    ]
    
    # Format to TMAS text specs
    scriptContent = ""
    for timestampInMs, action in gameInputs:
        scriptContent += f"{timestampInMs}ms {action}\n"
        
    # Export for Windows testing node
    outputFilename = "first_run.txt"
    with open(outputFilename, "w") as f:
        f.write(scriptContent)
    
    print(f"[SUCCESS] {outputFilename} ready for TMAS injection.")

if __name__ == "__main__":
    tasConfig()