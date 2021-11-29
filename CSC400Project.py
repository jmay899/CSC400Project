import random

class Process:
	def __init__(self,prio,ioPrio):
		self.priority = prio
		self.ioPriority = ioPrio
		
	blockedTime = 0

def main():
	timeUnits = 0 #number of times units elapsed - stop after 10,000
	
	#dictionary for holding number of times a process with each priority (0-15) was scheduled
	numSchedules = dict([(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,0)])
	
	#initialize 40 processes with priority between 4 and 10, and I/O priority between 0 and .99999...
	processList = []
	for _ in range(40):
		processList.append(Process(int(random.randint(4,10)),random.random()))
	
	while(timeUnits<10000):
		#maxProcess = highest priority process that isn't blocked
		maxProcess = highestValidPriority(processList)
		numSchedules[maxProcess.priority] += 1
		
		#choose value between 0 and 1 to determine if process will run or block
		randomIo = random.random()
		if randomIo < maxProcess.ioPriority: #random is less than IO probability, block for random time, increase priority if possible
			maxProcess.blockedTime = int(random.randint(5,20))
			if maxProcess.priority < 15:
				maxProcess.priority += 1
		elif maxProcess.priority > 0: #random is greater than IO probability, decrease priority if possible
				maxProcess.priority -= 1
		timeUnits += 1
		
	printNumSchedules(numSchedules)	
		
		
#finds highest priority process that isn't blocked
def highestValidPriority(processList) -> Process:
	maxProcess = Process(0,0) #will hold highest priority process
	for pro in processList:
		if pro.blockedTime == 0:
			if pro.priority > maxProcess.priority:
				maxProcess = pro
		else: #if blocked reduce time they're blocked by 1
			pro.blockedTime -= 1
	return maxProcess
	
#how many times a process with each priority was scheduled	
def printNumSchedules(numSchedules):
	for p in numSchedules:
		print("Priority "+str(p)+" was scheduled "+str(numSchedules[p])+" times")
	
	
if __name__ == "__main__":
	main()