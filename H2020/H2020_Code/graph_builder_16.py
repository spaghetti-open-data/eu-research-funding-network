 # Powered by Python 2.7

# To cancel the modifications performed by the script
# on the current graph, click on the undo button.

# Some useful keyboards shortcuts : 
#   * Ctrl + D : comment selected lines.
#   * Ctrl + Shift + D  : uncomment selected lines.
#   * Ctrl + I : indent selected lines.
#   * Ctrl + Shift + I  : unindent selected lines.
#   * Ctrl + Return  : run script.
#   * Ctrl + F  : find selected text.
#   * Ctrl + R  : replace selected text.
#   * Ctrl + Space  : show auto-completion dialog.

import time
import datetime
import csv
from tulip import *

# the updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# the pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# the runGraphScript(scriptFile, graph) function can be called to launch another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# the main(graph) function must be defined 
# to run the script on the current graph

# start the clock
start_script = datetime.datetime.now()

# initialize variables

dirPath = '/Users/albertocottica/github/local/fp7-funding-network-analysis/CSV/'

def loadProjects():
	''' loads the projects CSV file and puts the results into a Dict'''
	projectsFile = dirPath + 'projects.csv'
	projects = csv.DictReader(open(projectsFile, 'rb'), delimiter='\t')
	projectsList = []
	for line in projects:
		projectsList.append(line)
	return projectsList
	
def loadOrgs():
	''' loads the orgs CSV file and puts the results into a Dict'''
	orgsFile = dirPath + 'unique_org.csv'
	orgs = csv.DictReader(open(orgsFile, 'rb'), delimiter=',') # in FP7 data it's comma separated
	orgsList = []
	for line in orgs:
		orgsList.append(line)
	return orgsList
	
def loadEdges():
	'''loads the edges file and puts the results into a dict'''
	edgesFile = dirPath + 'edges.csv'
	edges = csv.DictReader(open(edgesFile, 'rb'), delimiter = '\t')
	edgesList = []
	for edge in edges:
		edgesList.append(edge)
	return edgesList
	
def cleanAmount(dirtyString):
	'''
	(str) => float
	takes an amount given as a string in the CSV, cleans the string and
	converts it to float
	'''
	if dirtyString == '':
		print ('Missing value!')
		return 0
	else: 
		replaceComma = dirtyString.replace(',', '.', 1)
		stripEnd = replaceComma.strip('.')
		return float(stripEnd)
	
	
def main(graph): 
	viewBorderColor =  graph.getColorProperty("viewBorderColor")
	viewBorderWidth =  graph.getDoubleProperty("viewBorderWidth")
	viewColor =  graph.getColorProperty("viewColor")
	viewFont =  graph.getStringProperty("viewFont")
	viewFontSize =  graph.getIntegerProperty("viewFontSize")
	viewLabel =  graph.getStringProperty("viewLabel")
	viewLabelBorderColor =  graph.getColorProperty("viewLabelBorderColor")
	viewLabelBorderWidth =  graph.getDoubleProperty("viewLabelBorderWidth")
	viewLabelColor =  graph.getColorProperty("viewLabelColor")
	viewLabelPosition =  graph.getIntegerProperty("viewLabelPosition")
	viewLayout =  graph.getLayoutProperty("viewLayout")
	viewMetaGraph =  graph.getGraphProperty("viewMetaGraph")
	viewMetric =  graph.getDoubleProperty("viewMetric")
	viewRotation =  graph.getDoubleProperty("viewRotation")
	viewSelection =  graph.getBooleanProperty("viewSelection")
	viewShape =  graph.getIntegerProperty("viewShape")
	viewSize =  graph.getSizeProperty("viewSize")
	viewSrcAnchorShape =  graph.getIntegerProperty("viewSrcAnchorShape")
	viewSrcAnchorSize =  graph.getSizeProperty("viewSrcAnchorSize")
	viewTexture =  graph.getStringProperty("viewTexture")
	viewTgtAnchorShape =  graph.getIntegerProperty("viewTgtAnchorShape")
	viewTgtAnchorSize =  graph.getSizeProperty("viewTgtAnchorSize")

#	for n in graph.getNodes():
#		print n

	print ('Initializing graph...')
		
	projectNode = graph.getBooleanProperty('projectNode') # this property is common to both node types
	# create node properties: start with properties related to projects
	rcn = graph.getStringProperty('rcn')
	reference = graph.getStringProperty('reference')
	programmeCode = graph.getStringProperty('programme')
	topics = graph.getStringProperty('topics')
	subprogramme = graph.getStringProperty('subprogramme')
	title = graph.getStringProperty('acronym')
	startDate = graph.getStringProperty('startDate')
	endDate = graph.getStringProperty('endDate')
	totalCost = graph.getDoubleProperty('totalCost')
	ecMaxContribution = graph.getDoubleProperty('ecMaxContribution')
	call = graph.getStringProperty('call')
	fundingScheme = graph.getStringProperty('fundingScheme')
	coordinator = graph.getStringProperty('coordinator')
	coordinatorCountry = graph.getStringProperty('coordinatorCountry')
	
	# now create the properties of org-type nodes
	newOrgId = graph.getStringProperty('new_org_id')
	projectReference = graph.getStringProperty('projectReference')
	organisationName = graph.getStringProperty('name')
	organisationShortName = graph.getStringProperty('ShortName')
	organisationNameNormal = graph.getStringProperty('name_normal')
	organisationCountry = graph.getStringProperty('country')
	organisationNumProj = graph.getDoubleProperty('numProj')
	organisationTotalContribution = graph.getDoubleProperty('totContribution')
	
	# now create the properties of edges
#	isCoordinator = graph.getBooleanProperty('isCoordinator')
				
	projectsList = loadProjects() # we execute the functions to run the files
	orgsList = loadOrgs()
	edgesList = loadEdges()

	# add the projects as nodes from a list of projects, assigning their characteristics to node properties
	# requires plenty of OpenRefine
	# create project-type nodes and populate their properties
	
	print ('Adding project nodes...')

	p2n = {} # Ben's map trick. This maps the rcn property of projects to their node objects.
	counter = 0
	for p in projectsList:
		if p['startDate'] <= '2009-04-01': # we only include projects already started at the time of the last update of the dataset
			counter += 1
			# print ('Adding project ' + str(counter))
			n = graph.addNode()
			projectNode[n] = True # this is set to True for all projects!
			rcnCode = p['rcn']
			rcn[n] = rcnCode
			p2n[rcnCode] = n # update the map
			reference[n] = p['reference']
			programmeCode[n] = p['programme']
			title[n] = p['acronym']
			startDate[n] = p['startDate']
			endDate[n] = p['endDate']
			totalCost[n] = cleanAmount(p['totalCost'])
			ecMaxContribution[n] = cleanAmount(p['ecMaxContribution'])
			call[n] = p['call']
			fundingScheme[n] = p['fundingScheme']	
			coordinator[n] = p['coordinator']
			coordinatorCountry[n] = p['coordinatorCountry']
	
	
	# now add the org-type nodes and populate their properties
	print ('Adding organisation nodes...')
	counter = 0
	o2n = {} # Ben's map trick
	for o in orgsList:
		counter += 1
		# print ('Adding org ' + str(counter))
		# check that the organisation has not already been added
		oNewOrgId = o['new_org_id']
		oName = o['name']
		n = graph.addNode()
		projectNode[n] = False # Set to False for all orgs! 
		organisationName[n] = oName
		organisationShortName[n] = o['shortName']
		# organisationNameNormal[n] = o['name_normal'] missing in FP7 data
		organisationCountry[n] = o['country']
		organisationNumProj[n] = float(o['numProj'])
		# organisationTotalContribution[n] = cleanAmount(o['totContribution']) missing from FP7 data
		o2n[oNewOrgId] = n #update the map
			
	# create an edge		
	for e in edgesList:
		try: 
			source = o2n [e['new_org_id']]
			target = p2n [e['projectRcn']]
			newEdge = graph.addEdge(source, target)
			# isCoordinator[newEdge] = False
			# if o['organisationRole'] == coordinator:
			# 	isCoordinator[newEdge] = True
		except:
			print ('Could not add org ' + e['new_org_id'] + ' to project' + e['projectRcn'])

	end_script = datetime.datetime.now()
	running_time = end_script - start_script
	print ('Executed in ' + str(running_time))
