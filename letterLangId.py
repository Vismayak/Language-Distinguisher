import bigrams 
import dicts
from math import log 
from math import exp

if __name__ == '__main__':

	input_file = open("LangId.train.English",'r')
	words=[]
	for i in input_file.readlines():
		words += list(i)
	
	Enbdict = bigrams.bigrams(words)

	for i in Enbdict.keys():
		total = 0
		for j in Enbdict[i].keys():
			total +=  Enbdict[i][j]

		for j in Enbdict[i].keys():
			Enbdict[i][j] = 1.0 * Enbdict[i][j]/total 


	input_file = open("LangId.train.French",'r')
	words=[]
	for i in input_file.readlines():
		words += list(i)
	
	Frbdict = bigrams.bigrams(words)

	for i in Frbdict.keys():
		total = 0
		for j in Frbdict[i].keys():
			total +=  Frbdict[i][j]

		for j in Frbdict[i].keys():
			Frbdict[i][j] = 1.0 * Frbdict[i][j]/total 

	
	input_file = open("LangId.train.Italian",'r')
	words=[]
	for i in input_file.readlines():
		words += list(i)
	
	Itbdict = bigrams.bigrams(words)



	for i in Itbdict.keys():
		total = 0
		for j in Itbdict[i].keys():
			total +=  Itbdict[i][j]

		for j in Itbdict[i].keys():
			Itbdict[i][j] = 1.0 * Itbdict[i][j]/total 

	

	filename = "LangId.test"
	input_file=open(filename)
	filename = "letterLangId.out"
	output_file = open(filename,"w")
	counter = 1
	for i in input_file.readlines():
		words = list(i)
		words = words +[None]
		#print words
		probeng = 0 
		probfr  = 0 
		probit  = 0 
		for i in range(len(words)-1):
			if(words[i] in Enbdict):
				if(words[i+1] in Enbdict[words[i]]):
					probeng = probeng + log(Enbdict[words[i]][words[i+1]])
			if(words[i] in Frbdict):
				if(words[i+1] in Frbdict[words[i]]):
					probfr =  probfr + log(Frbdict[words[i]][words[i+1]])
			if(words[i] in Itbdict):
				if(words[i+1] in Itbdict[words[i]]):
					probit =  probit + log(Itbdict[words[i]][words[i+1]])


		if probfr > probit and probfr > probeng:
			output_file.write(str(counter)+' French\n')
		elif probeng > probit:
			output_file.write (str(counter)+' English\n')
		else:
			output_file.write (str(counter)+' Italian\n')
		
		counter += 1
		
