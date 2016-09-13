# Powered by Python 2.7

# Export the graph as a JSON object 
# Run from the graph you want to export

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
import json

# the updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# the pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# the runGraphScript(scriptFile, graph) function can be called to launch another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# the main(graph) function must be defined 
# to run the script on the current graph

def main(graph): 
	ShortName = graph.getStringProperty("ShortName")
	acronym = graph.getStringProperty("acronym")
	call = graph.getStringProperty("call")
	constraints = graph.getStringProperty("constraints")
	coordinator = graph.getStringProperty("coordinator")
	coordinatorCountry = graph.getStringProperty("coordinatorCountry")
	country = graph.getStringProperty("country")
	deepCollabDegree = graph.getDoubleProperty("deepCollabDegree")
	degree = graph.getDoubleProperty("degree")
	degreeStacked = graph.getDoubleProperty("degreeStacked")
	ecMaxContribution = graph.getDoubleProperty("ecMaxContribution")
	endDate = graph.getStringProperty("endDate")
	fundingScheme = graph.getStringProperty("fundingScheme")
	intermediateViz = graph.getIntegerProperty("intermediateViz")
	intermediated = graph.getBooleanProperty("intermediated")
	intermediatedNodes = graph.getIntegerProperty("intermediatedNodes")
	intermediator = graph.getBooleanProperty("intermediator")
	kCore = graph.getDoubleProperty("kCore")
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
	totCollaborators = graph.getDoubleProperty('totCollaborators')
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

	allData = {}
	allData['nodes'] = []
	allData['edges'] = []
	for n in graph.getNodes():
		thisNodeProperties = {}
		thisNodeProperties['ID'] = new_org_id[n]
		thisNodeProperties['name'] = name[n]
		thisNodeProperties['ShortName'] = ShortName[n]
		thisNodeProperties['numProj'] = numProj[n]
		thisNodeProperties['country'] = country[n]
		thisNodeProperties['dependentOrgs'] = intermediatedNodes[n]
		thisNodeProperties['collaborators'] = totCollaborators[n]
		allData['nodes'].append(thisNodeProperties)
	for e in graph.getEdges():

		thisEdgeProperties = {}
		thisEdgeProperties ['source'] = new_org_id [graph.source(e) ]
		thisEdgeProperties ['target'] = new_org_id [graph.target(e) ]
		thisEdgeProperties ['collaborations'] = projectsTogether[e]
		thisEdgeProperties ['collBudget'] = moneyTogether[e]
		allData ['edges'].append(thisEdgeProperties)
		
	dirPath = '/Users/albertocottica/github/local/eu-research-funding-network/H2020/H2020_Data/'
	with open (dirPath + 'H2020DeathStar.json', 'w') as jsonFile:
		json.dump(allData, jsonFile)
		
			
		
		
