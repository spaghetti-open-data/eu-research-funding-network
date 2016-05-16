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
	ShortName =  graph.getStringProperty("ShortName")
	acronym =  graph.getStringProperty("acronym")
	call =  graph.getStringProperty("call")
	coordinator =  graph.getStringProperty("coordinator")
	coordinatorCountry =  graph.getStringProperty("coordinatorCountry")
	country =  graph.getStringProperty("country")
	ecMaxContribution =  graph.getDoubleProperty("ecMaxContribution")
	endDate = graph.getStringProperty('endDate')
	fundingScheme =  graph.getStringProperty("fundingScheme")
	name =  graph.getStringProperty("name")
	name_normal =  graph.getStringProperty("name_normal")
	new_org_id =  graph.getStringProperty("new_org_id")
	numProj =  graph.getDoubleProperty("numProj")
	programme =  graph.getStringProperty("programme")
	projectNode =  graph.getBooleanProperty("projectNode")
	projectReference =  graph.getStringProperty("projectReference")
	rcn =  graph.getStringProperty("rcn")
	reference =  graph.getStringProperty("reference")
	startDate =  graph.getStringProperty("startDate")
	subprogramme =  graph.getStringProperty("subprogramme")
	topics =  graph.getStringProperty("topics")
	totContribution =  graph.getDoubleProperty("totContribution")
	totalCost =  graph.getDoubleProperty("totalCost")
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

	# before doing anything, run equalValue on the bipartite graph for projectNode
	# this gives two subgraphs, one of which contains only the organization-type nodes
	# use the Python shell to rename the graph for projectNode: False to orgsOnly
	
	# store the bipartite in a subgraph before adding any edges
	bipartite = graph.addSubGraph('bipartite')
	for n in graph.getNodes():
		bipartite.addNode(n)
	for e in graph.getEdges():
		bipartite.addEdge(e)
		

	# the graph
	onemode = graph.getSubGraph('orgsOnly')
	# initialize the property to store number of projects connecting two orgs
	projectsTogether = graph.getDoubleProperty('projectsTogether')

		
	
	for p in bipartite.getNodes(): # iterate over nodes...
		if projectNode.getNodeValue(p) == True: # .. only of the "project" type
			cost = totalCost.getNodeValue(p)
			sp = subprogramme.getNodeValue(p)
			participants = []
			for e in graph.getInEdges(p): 
				participants.append(graph.source(e))
			for i in range (len(participants)):
				for j in range (i+1, len(participants)):
					newEdge = onemode.addEdge(participants[i], participants[j])
					totalCost[newEdge] = cost
					subprogramme[newEdge] = sp
					startDate[newEdge] = startDate[p]
					endDate[newEdge] = endDate[p]
					
