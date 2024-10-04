
from imports import *

def run_script(script_name):
    script_path = os.path.join("app", script_name)
    
    while True:
        process = subprocess.Popen(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        try: 
            for line in process.stdout:
                print(line.decode().strip())
            for line in process.stderr:
                print(line.decode().strip, file=sys.stderr)
                
            process.wait()
            if process.returncode != 0:
                print(f"Script {script_name} excited with error code {process.returncode}")
        
        except KeyboardInterrupt:
            print(f"Wrapper script interrupted for {script_name}. Exiting ...")
            break
    
        finally:
            process.terminate()
            process.wait()
            

def run_all_scripts():
    # add all the script name here 
    scripts = []
    
    processes = []
    
    try:
        for script in scripts:
            p = subprocess.Popen(["python", os.path.join("TorpdeoDetectionApp", "app", script)],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            processes.append((script, p))
            print(f"Started {script}")
            
        while True:
            for script, process in processes:
                retcode = process.poll()
                if retcode is not None:
                    print(f"{script} exited with code {retcode}, Restarting ...")
                    process.remove((script, process))
                    
                    p = subprocess.Popen(["python", os.path.join("TorpdeoDetectionApp", "app", script)],
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    
                    process.append((script, p))
                    print(f"Resarted {script}")
            time.sleep(5)
    
    except KeyboardInterrupt:
        print("Wrapper script interrupted. Exiting...")
    finally:
        for script, process in process:
            process.terminate()
            process.wait()
            print(f"Terminated {script}")
                    
                    
if __name__ == "__main__":
    run_all_scripts()