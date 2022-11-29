import sys;
import subprocess;
import threading;

# Edit this to add each python file you wish to use

#start_files = [
#    "./Bot1/main.py",
#    "./Bot2/main.py"
#];

start_files = [
    "./discordBot.py",
    "./altereal_guilded.py"
];



# Do not edit below this line

print("[Loader]Loading "+str(len(start_files))+" files");

def runfile(name):
    print("[Loader]Opening file "+name);
    working_dir = "/".join(name.split("/")[:-1]);
    subprocess.call([ sys.executable, '-u', name ]);
    print("[Loader]File "+name+" stopped");

threads = []

for f in start_files:
    thread = threading.Thread(target=runfile, args=(f,));
    thread.start();


# Wait for each thread to finish
for thread in threads:
    thread.join();

print("[Loader]All files have exited, quitting.");