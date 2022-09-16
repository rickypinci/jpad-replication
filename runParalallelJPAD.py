import sys
import os
import threading
import time
import queue

def worker():
    while True:
        exec_str = q.get()
        os.system(exec_str)
        q.task_done()



#class MyThread(threading.Thread):
#	def __init__(self, threadID, folderName, load, duration, system):
#		threading.Thread.__init__(self)
#		self.threadID = threadID
#		self.folderName = folderName
#		self.load = str(load)
#		self.duration = str(duration)
#		self.system = system
#	def run(self):
#		exec_str = 'java -jar train-ticket-analysis/javaAP_terminal_TrainTicket_v1.jar ' + self.folderName + ' ' + self.load + ' ' + self.duration + ' ' + self.system
#		subprocess.call(exec_str, shell=True)





NUM_THREADS = 16
FOLDER = '/home/pinciroli/javaAntipatterns-dir/reading_files/original/'
RESULTS_DIR = FOLDER + str(int(time.time()))
LOADS = [25, 50, 75, 100]
DURATIONS = [3, 6, 12]
SYSTEMS = [
#'broadleaf',
#'openmrs',
#'petclinic',
#'trainticket',
#'webgoat'
'teastore'
]


q = queue.Queue()
threads = []
thID = 0
for load in LOADS:
	for duration in DURATIONS:
		for system in SYSTEMS:
			exec_str = 'java -jar JPAD-0.0.1-cli.jar ' + FOLDER + ' ' + str(load) + ' ' + str(duration) + ' ' + system
			q.put(exec_str)
#			threads.append(MyThread(thID, FOLDER, load, duration, system))
#			thID += 1

#for th in threads:
#	th.start()

#for th in threads:
#	th.join()

for idx in range(NUM_THREADS):
    threading.Thread(target=worker, daemon=True).start()

q.join()

os.system('mkdir ' + RESULTS_DIR)
os.system('mv ' + FOLDER + '*.csv ' + RESULTS_DIR)
