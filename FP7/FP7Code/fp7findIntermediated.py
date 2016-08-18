# Powered by Python 2.7

# RUN THIS FROM GiantComp
# it finds the number of uniquely intermediated organizations by each organization.
# This is the number of orgs that are ONLY connected to the FP7 giant component by this org.

# Before running the script, run the degree algorithm on this graph. Assign the output to viewMetric, then copy viewMetric into 
# the deepCollabDegree property

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

from tulip import *

# the updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# the pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# the runGraphScript(scriptFile, graph) function can be called to launch another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# the main(graph) function must be defined 
# to run the script on the current graph

def main(graph): 
	deepCollabDegree = graph.getDoubleProperty('deepCollabDegree')
	ShortName = graph.getStringProperty("ShortName")
	acronym = graph.getStringProperty("acronym")
	call = graph.getStringProperty("call")
	coordinator = graph.getStringProperty("coordinator")
	coordinatorCountry = graph.getStringProperty("coordinatorCountry")
	country = graph.getStringProperty("country")
	degree = graph.getDoubleProperty("degree")
	ecMaxContribution = graph.getDoubleProperty("ecMaxContribution")
	endDate = graph.getStringProperty("endDate")
	fundingScheme = graph.getStringProperty("fundingScheme")
	moneyTogether = graph.getDoubleProperty("moneyTogether")
	name = graph.getStringProperty("name")
	name_normal = graph.getStringProperty("name_normal")
	new_org_id = graph.getStringProperty("new_org_id")
	numProj = graph.getDoubleProperty("numProj")
	programme = graph.getStringProperty("programme")
	projectNode = graph.getBooleanProperty("projectNode")
	projectReference = graph.getStringProperty("projectReference")
	projectUrl = graph.getStringProperty("projectUrl")
	projectsTogether = graph.getDoubleProperty("projectsTogether")
	rcn = graph.getStringProperty("rcn")
	reference = graph.getStringProperty("reference")
	sourceId = graph.getStringProperty("sourceId")
	startDate = graph.getStringProperty("startDate")
	subprogramme = graph.getStringProperty("subprogramme")
	targetId = graph.getStringProperty("targetId")
	topics = graph.getStringProperty("topics")
	totContribution = graph.getDoubleProperty("totContribution")
	totalCost = graph.getDoubleProperty("totalCost")
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

	# create two Booleans to store the property of being intermediated and intermediated
	intermediated = graph.getBooleanProperty('intermediated')
	intermediator = graph.getBooleanProperty('intermediator')
	# this is just for the visualization
	intermediateViz = graph.getIntegerProperty('intermediateViz')
	# create the property that stores the number of intermediated orgs
	intermediatedOrgs = graph.getIntegerProperty('intermediatedNodes')
	# store that number in a dictionary:{node: intermediatedOrgs}

	# set the default values
	for org in graph.getNodes():
		intermediated[org] = False
		intermediator[org] = False
		intermediateViz[org] = 1
	
	iO = {}
	numIntermediated = 0
	numIntermediaries = 0
	for org in graph.getNodes():
		if deepCollabDegree.getNodeValue(org) == 1: # neighbors of orgs with degree 1 are intermediaries
			intermediated[org] = True
			intermediateViz[org] = 0
			numIntermediated += 1
			for neighbor in graph.getInOutNodes(org): #neighbor is the intermediary
				if deepCollabDegree.getNodeValue(neighbor) == 2: # this condition means the intermediator is itself intermediated.
					intermediateViz[neighbor] = 2
					intermediator[neighbor] = True
				if neighbor in iO: # update the number of intermediated orgs in the dictionary
					iO[neighbor] += 1
				else:
					iO[neighbor] = 1
					
	print ('Intermediated: ' + str(numIntermediated))
	for org in graph.getNodes():
		if intermediator[org] == True:
			numIntermediaries += 1
	print ('Intermediaries: ' + str(numIntermediaries))
	
	for org in graph.getNodes():
		if org in iO:
			intermediatedOrgs[org] = iO[org]
