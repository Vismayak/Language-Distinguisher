import bigrams 
import dicts
from math import log 
from math import exp

if __name__ == '__main__':

	filename = "LangId.train.English"
	Enbdict = bigrams.file2bigrams(filename)

	for i in Enbdict.keys():
		total = 0
		for j in Enbdict[i].keys():
			total +=  Enbdict[i][j]

		for j in Enbdict[i].keys():
			Enbdict[i][j] = (1.0 * Enbdict[i][j]+1)/(total+ len(Enbdict)) 
		Enbdict['!0']=1.0/len(Enbdict)

	
	filename = "LangId.train.French"
	Frbdict = bigrams.file2bigrams(filename)

	for i in Frbdict.keys():
		total = 0
		for j in Frbdict[i].keys():
			total +=  Frbdict[i][j]

		for j in Frbdict[i].keys():
			Frbdict[i][j] = (1.0 * Frbdict[i][j]+1)/(total+ len(Frbdict)) 
		Frbdict['!0']=1.0/len(Frbdict)

	filename = "LangId.train.Italian"
	Itbdict = bigrams.file2bigrams(filename)

	for i in Itbdict.keys():
		total = 0
		for j in Itbdict[i].keys():
			total +=  Itbdict[i][j]

		for j in Itbdict[i].keys():
			Itbdict[i][j] = (1.0 * Itbdict[i][j]+1)/(total+ len(Itbdict)) 
		Itbdict['!0']=1.0/len(Itbdict)

	filename = "LangId.test"
	input_file=open(filename)
	filename = "wordLangId.out"
	output_file = open(filename,"w")
	counter = 1
	for i in input_file.readlines():
		words = i.split()
		words = words +[None]
		probeng = 0 
		probfr  = 0 
		probit  = 0 
		for i in range(len(words)-1):
			if(words[i] in Enbdict):
				if(words[i+1] in Enbdict[words[i]]):
					probeng = probeng + log(Enbdict[words[i]][words[i+1]])
				else:
					probeng += log(Enbdict['!0'])
			else:
				probeng += log(Enbdict['!0'])
			
			if(words[i] in Frbdict):
				if(words[i+1] in Frbdict[words[i]]):
					probfr =  probfr + log(Frbdict[words[i]][words[i+1]])
				else:
					probfr += log(Frbdict['!0'])
			else:
				probfr += log(Frbdict['!0'])
			
			if(words[i] in Itbdict):
				if(words[i+1] in Itbdict[words[i]]):
					probit =  probit + log(Itbdict[words[i]][words[i+1]])
				else:
					probit += log(Itbdict['!0'])
			else:
				probit += log(Itbdict['!0'])

		if probfr > probit and probfr > probeng:
			output_file.write(str(counter)+' French\n')
		elif probeng > probit:
			output_file.write (str(counter)+' English\n')
		else:
			output_file.write (str(counter)+' Italian\n')
		
		counter += 1
		
