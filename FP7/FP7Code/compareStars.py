# Powered by Python 2.7

# compare the two deathStar lists.
#not using Tulip at all

import csv

dirPath = '/Users/albertocottica/github/local/eu-research-funding-network/'

def loadDeathStar(fileName):
	'''
	(str) => list of dicts
	loads the csv fileName and puts into a Python list of dicts
	'''
	csvFile = dirPath + fileName
	star = csv.DictReader(open(csvFile, 'rb'), delimiter =  ',')
	starList = []
	for line in star:
		starList.append(line)
	return starList
	
def main(graph):
	FP7Star = loadDeathStar('FP7/FP7Data/fp7deathstar.csv') # this list is the reference
	inFP7Only = loadDeathStar('FP7/FP7Data/fp7deathstar.csv') # this will later be tweaked
	H2020Star = loadDeathStar('H2020/H2020_Data/h2020deathstar.csv') # one more reference
	inH2020Only = loadDeathStar('H2020/H2020_Data/h2020deathstar.csv') # one more to be tweaked
	
	inBoth = []
	for org in inFP7Only:
		for org2 in H2020Star:
			if org['name'] == org2['name']:
				inFP7Only.remove(org)
				inBoth.append(org)
				break
			
	for org in inH2020Only:
		for or2 in FP7Star:
			if org['name'] == org2['name']:
				inH2020Only.remove(org)
				break
			
	print (str(len(inBoth)) + ' orgs in both')
	print (str(len(inFP7Only)) + 'orgs in FP7 only')
	print (str(len(inH2020Only)) + ' orgs in H2020 only')

	print ('In both FPs')
	for org in inBoth:
		print (org['name'])
	print ('-------------------------------------')
	print ('In FP7 only')
	for org in inFP7Only:
		print (org['name'])
		print ('-------------------------------------')
	print ('In H2020 only')
	for org in inH2020Only:
		print (org['name'])
