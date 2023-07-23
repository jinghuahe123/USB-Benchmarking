import os, shutil, datetime, logging

file_exists = os.path.exists("debug.log")

if (file_exists == True):
  with open('debug.log', 'r') as f:
    for line in f:
      pass
    last_line = line
    cycle = last_line[32:-5]
    cycle = int(cycle) + int(1)
else:
  cycle = 1

logging.basicConfig(filename='debug.log', filemode='a', format='%(asctime)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

print("PLEASE READ:")
print(" This is a python program designed to stress test a drive by repeatedly copying and deleting files.")
print(" This program will not show the speeds of the specified drive.")
print(" You will not be able to write directly to a drive, so please make sure to enter a folder name after the drive letter.")
print(" This does not have to be an existing folder as this program will create it automatically.")
print(" Please do not enter a folder name that is already in use as the contents will be deleted.")
print(" Use at your own risk. I will not be responsible for broken drives.")
print(" Enjoy, Jinghua.\n")
print("Program Start Time: ", datetime.datetime.now(), "\n")
if (cycle == 1):
  logging.info("Program Started")
else:
  logging.info("Program Restarted")


src = input("Source (Must Exist): ")
dest = input("Destination (Must NOT Exist): ")
print("\n")

dir = os.path.join(dest)
if not os.path.exists(dir):
  os.mkdir(dir)

while True:
  shutil.rmtree(dest)
  destination = shutil.copytree(src, dest) 
  print("Cycle ", cycle, " OK - ", datetime.datetime.now())
  logging.info("Cycle %s OK.", cycle)
  cycle = cycle + 1
