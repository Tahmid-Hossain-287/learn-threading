import threading
import time

def wakl_dog():
	time.sleep(5);
	print("walking the dog done")

def trash():
	time.sleep(3)
	print("throwing trash done")

def mail():
	time.sleep(2)
	print("mail check done")


walk_dog()
trash()
mail()