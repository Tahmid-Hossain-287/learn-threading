import threading
import time

ls = []

def count(n):
	for i in range(1, n+1):
		ls.append(i)
		time.sleep(0.1)

def count2(n):
	for i in range(1, n+1):
		ls.append(i)
		time.sleep(0.3)

x = threading.Thread(target = count, args=(10,))
x.start()

y = threading.Thread(target = count2, args=(10,))
y.start()

x.join()
y.join()

print(ls)