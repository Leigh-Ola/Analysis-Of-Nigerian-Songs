#pylint:disable=W0621
#pylint:disable=W0312


def parse(fName):
	import csv
	import re

	rowNum, colNum = 0,0
	obj = {}
	maxOcc = 0
	sortedObj = {}

	def extractWords(lyrics):
		lyricsList = re.split("[,\'\s\(\)\n\[\]\.\?!]", lyrics)
		maxO = 0
		for l in lyricsList:
			if l != "":
				word = str(l).strip().lower()
				if word in obj:
					obj[word]+=1
					maxO = maxO if (maxO > obj[word]) else (obj[word])
				else:
					obj[word] = 1
		maxO = maxO if (maxO>maxOcc) else maxOcc
		return maxO
		
	def countWords():
		for o in obj:
			if str(obj[o]) not in sortedObj:
				sortedObj[str(obj[o])] = []
			sortedObj[str(obj[o])].append(o)
		

	with open(fName, "r") as file:
		fileData = csv.reader(file, delimiter=",")
		for r in fileData:
			rowNum+=1
			for c in r:
				colNum+=1
				if colNum==3:
					maxOcc = extractWords(c)
			colNum=0
			if rowNum>=5000:
				break
		countWords()
	
	#print(obj,"\n\n")
	return {"sorted" : sortedObj, "max" : maxOcc}

def summarize(data):
	obj, maxO = data["sorted"], data["max"]
	s, total = "",0
	for o in range(1, maxO+1):
		if str(o) in obj:
			l = len(obj[str(o)])
			s+= " {} appeared {} times.\n".format("~ {} words".format(l) if (l>1) else obj[str(o)][0], o)
			total+=l
	s+="\n\nTotal of {} words.".format(total)
	print(s)

obj = parse("data.csv")
summarize(obj)

#print(obj["sorted"]["5"]," : ",obj["max"])

