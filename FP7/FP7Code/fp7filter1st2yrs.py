# Powered by Python 2.7

# RUN THIS FROM orgsOnly

# this script filters FP7 partnership to only those related to projects that started before April 15th 2009.
# this is to compare the first 28 months of FP7 to the first 28 months of H2020

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
	degree = graph.getDoubleProperty('degree') # need this to filter out orgs not active in the first two years
	ShortName = graph.getStringProperty("ShortName")
	acronym = graph.getStringProperty("acronym")
	call = graph.getStringProperty("call")
	coordinator = graph.getStringProperty("coordinator")
	coordinatorCountry = graph.getStringProperty("coordinatorCountry")
	country = graph.getStringProperty("country")
	ecMaxContribution = graph.getDoubleProperty("ecMaxContribution")
	endDate = graph.getStringProperty("endDate")
	fundingScheme = graph.getStringProperty("fundingScheme")
	name = graph.getStringProperty("name")
	name_normal = graph.getStringProperty("name_normal")
	new_org_id = graph.getStringProperty("new_org_id")
	numProj = graph.getDoubleProperty("numProj")
	programme = graph.getStringProperty("programme")
	projectNode = graph.getBooleanProperty("projectNode")
	projectReference = graph.getStringProperty("projectReference")
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
	
	twoYrsEdges = graph.addSubGraph('twoYrsEdges')
	for n in graph.getNodes():
		twoYrsEdges.addNode(n)
	for e in graph.getEdges():
		if startDate[e] < '2009-04-15':
			twoYrsEdges.addEdge(e)
	
	
