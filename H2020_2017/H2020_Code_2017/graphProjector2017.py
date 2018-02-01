# Powered by Python 2.7

# This script projects a bipartite graph (orgs-to-projects) into a one-mode one (orgs-to-orgs). 

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

import datetime
from tulip import *

start_script = datetime.datetime.now()

# the updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# the pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# the runGraphScript(scriptFile, graph) function can be called to launch another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# the main(graph) function must be defined 
# to run the script on the current graph

def main(graph): 
  acronym = graph.getStringProperty("acronym")
  activityType = graph.getStringProperty("activityType")
  call = graph.getStringProperty("call")
  city = graph.getStringProperty("city")
  commDate = graph.getDoubleProperty("commDate")
  country = graph.getStringProperty("country")
  ecMaxContribution = graph.getDoubleProperty("ecMaxContribution")
  endDate = graph.getStringProperty("endDate")
  fundingScheme = graph.getStringProperty("fundingScheme")
  name = graph.getStringProperty("name")
  objective = graph.getStringProperty("objective")
  orgId = graph.getStringProperty("orgId")
  organizationUrl = graph.getStringProperty("organizationUrl")
  postCode = graph.getStringProperty("postCode")
  programme = graph.getStringProperty("programme")
  projectNode = graph.getBooleanProperty("projectNode")
  projectUrl = graph.getStringProperty("projectUrl")
  rcn = graph.getStringProperty("rcn")
  role = graph.getStringProperty("role")
  shortName = graph.getStringProperty("shortName")
  startDate = graph.getStringProperty("startDate")
  status = graph.getStringProperty("status")
  street = graph.getStringProperty("street")
  topics = graph.getStringProperty("topics")
  totalCost = graph.getDoubleProperty("totalCost")
  tentativeSIC = graph.getStringProperty('TentativeSIC')
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
  
  bipartite = graph.getSubGraph('bipartite')
  orgs2orgs = graph.addSubGraph('orgs2orgs')
  
  # add nodes first
  for p in bipartite.getNodes():
	  	if projectNode.getNodeValue(p) == False:
	  		orgs2orgs.addNode(p)
  
  for p in bipartite.getNodes(): # iterate over nodes...
		if projectNode.getNodeValue(p) == True: # only for project-type nodes
			projectAcronym = acronym.getNodeValue(p)
			participants = []
			for e in graph.getInEdges(p):
			  	participants.append(graph.source(e))
			for i in range (len(participants)):
				for j in range (i+1, len(participants)):
					newEdge = orgs2orgs.addEdge(participants[i], participants[j])
					acronym[newEdge] = acronym[p]
					call[newEdge] = call[p]
					totalCost[newEdge] = totalCost[p]
					ecMaxContribution[newEdge] = ecMaxContribution[p]
					programme[newEdge] = programme[p]
					startDate[newEdge] = startDate[p]
					endDate[newEdge] = endDate[p]
					topics[newEdge] = topics[p]
					tentativeSIC[newEdge] = tentativeSIC[p]
					
  end_script = datetime.datetime.now()
  
  print ('Runtime: ' + str (end_script - start_script))

					
