# Powered by Python 2.7

# run from stable. 
# we count the orgs with no partnership (degree zero in the stacked) and orgs with no stable partnership (degree zero in the stable)
# first, run Degree on stacked and store the result in the degreeStacked property
# next, run Degree on stable and store the result in the deepCollabDegree property 

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
	degreeStacked = graph.getDoubleProperty('degreeStacked')
	deepCollabDegree = graph.getDoubleProperty('deepCollabDegree')
	viewLayout = graph.getLayoutProperty("viewLayout")
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

	zeroPartners = 0
	zeroStablePartners = 0
	for n in graph.getNodes():
		if degreeStacked[n] == 0:
				zeroPartners += 1
		else:
			if deepCollabDegree[n] == 0:
				zeroStablePartners += 1
				
	print (str(zeroPartners) + ' orgs have no partners')
	print (str(zeroStablePartners) + ' orgs have no stable partners')

