# Powered by Python 2.7

# run from stable to get to the number of "one-offers"

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
	deepCollabDegree = graph.getDoubleProperty("deepCollabDegree")
	sourceId = graph.getStringProperty("sourceId")
	targetId = graph.getStringProperty("targetId")
	viewLayout = graph.getLayoutProperty("viewLayout")
	viewMetric = graph.getDoubleProperty("viewMetric")
	ShortName = graph.getStringProperty("ShortName")
	acronym = graph.getStringProperty("acronym")
	call = graph.getStringProperty("call")
	coordinator = graph.getStringProperty("coordinator")
	coordinatorCountry = graph.getStringProperty("coordinatorCountry")
	country = graph.getStringProperty("country")
	degree = graph.getDoubleProperty("degree")
	degreeStacked = graph.getDoubleProperty("degreeStacked")
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
	startDate = graph.getStringProperty("startDate")
	subprogramme = graph.getStringProperty("subprogramme")
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
	viewRotation = graph.getDoubleProperty("viewRotation")
	viewSelection = graph.getBooleanProperty("viewSelection")
	viewShape = graph.getIntegerProperty("viewShape")
	viewSize = graph.getSizeProperty("viewSize")
	viewSrcAnchorShape = graph.getIntegerProperty("viewSrcAnchorShape")
	viewSrcAnchorSize = graph.getSizeProperty("viewSrcAnchorSize")
	viewTexture = graph.getStringProperty("viewTexture")
	viewTgtAnchorShape = graph.getIntegerProperty("viewTgtAnchorShape")
	viewTgtAnchorSize = graph.getSizeProperty("viewTgtAnchorSize")
	
	oneOffers = 0
	for n in graph.getNodes():
		if degreeStacked [n] > 0: 
			if deepCollabDegree [n] == 0:
				oneOffers += 1
			
	print ('One-offers: ' + str (oneOffers))
	
			
			
		
