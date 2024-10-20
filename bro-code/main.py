import threading
import time

def walk_dog():
	time.sleep(5);
	print("walking the dog done")

def trash():
	time.sleep(3)
	print("throwing trash done")

def mail():
	time.sleep(2)
	print("mail check done")

chore1 = threading.Thread(target = walk_dog)
chore2 = threading.Thread(target = trash)
chore3 = threading.Thread(target = mail)

chore1.start()
chore2.start()
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")