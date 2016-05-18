# Powered by Python 2.7

# RUN THIS FROM THE SUPERGRAPH OF THE GRAPH YOU WANT TO STACK
# for the SOD16 hackathon we are interested in projects started in the first 28 months of FP7
# so we run from twoYrsEdges

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
from tulip import *

# the updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# the pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# the runGraphScript(scriptFile, graph) function can be called to launch another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# the main(graph) function must be defined 
# to run the script on the current graph

# run from the main

# start the clock
start_script = datetime.datetime.now()

def findEdge(node1, node2, graph1, directed = False, create = True):
	'''
   finds an edge connecting two given nodes if it exists,
   if not returns a newly created edge unless stated otherwise
   deals with either directed or undirected graphs
   '''
	e = graph1.existEdge(node1, node2)
	if e.isValid():
		return e
	else:
		if not directed:
			e = graph1.existEdge(node2, node1)
			if e.isValid():
				return e
			else:
				if create:
					e = graph1.addEdge(node1, node2)
					return e                        
		else:
			if create:    
				e = graph1.addEdge(node1, node2)
				return e
			else:
				return None

	
def main(graph): 
	projectsTogether =  graph.getDoubleProperty("projectsTogether")
	moneyTogether = graph.getDoubleProperty('moneyTogether')
	viewLayout =  graph.getLayoutProperty("viewLayout")
	ShortName =  graph.getStringProperty("ShortName")
	acronym =  graph.getStringProperty("acronym")
	call =  graph.getStringProperty("call")
	country =  graph.getStringProperty("country")
	ecMaxContribution =  graph.getDoubleProperty("ecMaxContribution")
	fundingScheme =  graph.getStringProperty("fundingScheme")
	name =  graph.getStringProperty("name")
	name_normal =  graph.getStringProperty("name_normal")
	new_org_id =  graph.getStringProperty("new_org_id")
	numProj =  graph.getDoubleProperty("numProj")
	programme =  graph.getStringProperty("programme")
	projectNode =  graph.getBooleanProperty("projectNode")
	projectReference =  graph.getStringProperty("projectReference")
	projectUrl =  graph.getStringProperty("projectUrl")
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

	# Add the new subgraph and grab the parallel edges graph
	stacked = graph.addSubGraph('twoYrsStacked')	
	nonStacked = graph.getSubGraph('twoYrsOrgsOnly')
	
	# add all nodes in graph1 to stacked
	for n in nonStacked.getNodes():
		stacked.addNode(n)
		
	# you go over all edges in graph1 and add only one edge to graph2
	# also collect the data you are interested in
	for edge in nonStacked.getEdges():
		source = nonStacked.source(edge)
		target = nonStacked.target(edge)
		# source and target are nodes connect
		subEdge = findEdge(source, target, stacked, False, True)
		if subEdge == None: # grph2 does not contain any edge between source and target
			subEdge = stacked.addEdge(source, target)
			projectsTogether[subEdge] = 1
			moneyTogether[subEdge] = totalCost(edge)		
		# else: grph2 already contains an edge - you do not need to include that case 
			# since you will have it in subEdge as a result of the call to findEdge
		projectsTogether[subEdge] += 1
		moneyTogether[subEdge] += totalCost[edge]
		
	end_script = datetime.datetime.now()
	running_time = end_script - start_script
	print ('Executed in ' + str(running_time))
