# This script builds the main graph and the bipartite orgs-to-project file starting from the .tsv files

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

# start the clock
start_script = datetime.datetime.now()

# initialize variables
dirPath = '/Users/albertocottica/github/local/eu-research-funding-network/H2020/H2020_Data_2017/'

def loadProjects():
	''' loads the projects CSV file and puts the results into a Dict'''
	projectsFile = dirPath + 'cordis-h2020projects.tsv'
	projects = csv.DictReader(open(projectsFile, 'rb'), delimiter='\t')
	projectsList = []
	for line in projects:
		projectsList.append(line)
	return projectsList
	
def loadEdges():
	'''
	Loads the orgs file and puts the results into a dict.
	The orgs file in 2017 has a new structure: each line is a relationship between one project and one organisation.
	Projects with n partners map onto n lines of the file.
	'''
	edgesFile = dirPath + 'cordis-h2020organizations.tsv'
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


# the updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# the pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# the runGraphScript(scriptFile, graph) function can be called to launch another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# the main(graph) function must be defined 
# to run the script on the current graph

def main(graph): 
  viewBorderColor = graph.getColorProperty("viewBorderColor")
  viewBorderWidth = graph.getDoubleProperty("viewBorderWidth")
  viewColor = graph.getColorProperty("viewColor")
  viewFont = graph.getStringProperty("viewFont")
  viewFontAwesomeIcon = graph.getStringProperty("viewFontAwesomeIcon")
  viewFontSize = graph.getIntegerProperty("viewFontSize")
  viewLabel = graph.getStringProperty("viewLabel")
  viewLabelBorderColor = graph.getColorProperty("viewLabelBorderColor")
  viewLabelBorderWidth = graph.getDoubleProperty("viewLabelBorderWidth")
  viewLabelColor = graph.getColorProperty("viewLabelColor")
  viewLabelPosition = graph.getIntegerProperty("viewLabelPosition")
  viewLayout = graph.getLayoutProperty("viewLayout")
  viewMetric = graph.getDoubleProperty("viewMetric")
  viewRotation = graph.getDoubleProperty("viewRotation")
  viewSelection = graph.getBooleanProperty("viewSelection")
  viewShape = graph.getIntegerProperty("viewShape")
  viewSize = graph.getSizeProperty("viewSize")
  viewSrcAnchorShape = graph.getIntegerProperty("viewSrcAnchorShape")
  viewSrcAnchorSize = graph.getSizeProperty("viewSrcAnchorSize")
  viewTexture = graph.getStringProperty("viewTexture")
  viewTgtAnchorShape = graph.getIntegerProperty("viewTgtAnchorShape")
  viewTgtAnchorSize = graph.getSizeProperty("viewTgtAnchorSize")
  
  print ('Initializing graph...')
	
	# create node properties: start with properties related to projects
  projectNode = graph.getBooleanProperty('projectNode') # this property is common to both node types
  rcn = graph.getStringProperty('rcn') # also a property of edges
  acronym = graph.getStringProperty('acronym')
  status = graph.getStringProperty('status')
  programme = graph.getStringProperty('programme')	
  topics = graph.getStringProperty('topics')
  title = graph.getStringProperty('acronym')
  startDate = graph.getStringProperty('startDate')
  endDate = graph.getStringProperty('endDate')
  projectUrl = graph.getStringProperty('projectUrl')
  objective = graph.getStringProperty('objective')
  totalCost = graph.getDoubleProperty('totalCost')
  ecMaxContribution = graph.getDoubleProperty('ecMaxContribution')
  call = graph.getStringProperty('call')
  fundingScheme = graph.getStringProperty('fundingScheme')
  
  # now create the properties of org-type nodes
  orgId = graph.getStringProperty('orgId') # also a property of edges
  name = graph.getStringProperty('name')
  shortName = graph.getStringProperty('shortName')
  activityType = graph.getStringProperty('activityType')
  country = graph.getStringProperty('country')
  street = graph.getStringProperty('street')
  city = graph.getStringProperty('city')
  postCode = graph.getStringProperty('postCode')
  organizationUrl = graph.getStringProperty('organizationUrl')
  
  # properties of edges
  role = graph.getStringProperty('role')
  
  graph.setName('main graph') # this is just to store stuff, it has no economic or social interpretation
  bipartite = graph.addSubGraph('bipartite') # create the bipartite orgs-to-projects graph.
  
  
  # !!! Here we go !!!
  projectsList = loadProjects()
  edgesList = loadEdges()
  
  print ('Adding project nodes...')
  
  p2n = {} # Ben's map trick. This maps the rcn property of projects to their node objects.
  counter = 0 
  for p in projectsList:
    counter += 1 
    n = bipartite.addNode()
    projectNode[n] = True # this is set to True for all projects!
    rcnCode = p['rcn']
    rcn[n] = rcnCode
    p2n[rcnCode] = n #update the map
    acronym[n] = p['acronym']
    status[n] = p['status']
    programme[n] = p['programme']
    topics[n] = p['topics'] # there is alway only one topic
    title[n] = p['title']
    startDate[n] = p['startDate']
    endDate[n] = p['endDate']
    projectUrl[n] = p['projectUrl']
    objective[n] = p['objective']
    totalCost[n] = cleanAmount(p['totalCost'])
    ecMaxContribution[n] = cleanAmount (p['ecMaxContribution'])
    call[n] = p['call']
    fundingScheme[n] = p['fundingScheme']    
  print (str(counter) + ' projects added')
   
  print ('Adding organizations and edges...')
  o2n = {} # mapping from org ID to org-type node
  counter = 0
  for e in edgesList:
    thisOrgId = e['id']
    if thisOrgId not in o2n: # If we have not already added this organization, we do it here
      counter += 1
      o = bipartite.addNode()
      o2n[thisOrgId] = o # update the map
      # fill the new node's properties
      orgId[o] = thisOrgId
      projectNode[o] = False 
      name[o] = e['name']
      shortName[o] = e['shortName']
      activityType[o] = e['activityType']
      country[o] = e['country']
      street[o] = e['street']
      city[o] = e['city']
      
    else: # If we already have, we grab it from the o2n map 
      o = o2n[thisOrgId] 
      
    # create the edge from the same line in edgesList
    thisEdgeProject = p2n[e['projectRcn']]
    newEdge = bipartite.addEdge(o, thisEdgeProject)
    role[newEdge] = e['role']
  print (str(counter) + ' organizations added.')
  
  end_script = datetime.datetime.now()
  
  print ('Runtime: ' + str (end_script - start_script))
  
