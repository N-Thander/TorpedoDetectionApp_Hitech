
from imports import *

def runScript():
    scriptPath = ""
    
    while True:
        process = subprocess.Popen(["python", scriptPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        try:
            for line in process.stdout:
                print(line.decode().strip())
            for line in process.stderr:
                print(line.decode().strip(), file=sys.stderr)
                
            process.wait()
            
            if process.returncode != 0:
                print()
        except KeyboardInterrupt:
            break
        
        finally:
            process.terminate()
            process.wait()
            
if __name__ == "__main__":
    runScript()