# Powered by Python 2.7

# this script stacks up parallel edges and quantifies the collaboration.
# run from the one-mode graph, not from the main. 

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

# start the clock
start_script = datetime.datetime.now()

def findEdge(node1, node2, graph, directed = False, create = True):
    '''
    finds an edge connected two given nodes if it exists,
    if not return a newly created edge unless stated otherwise
    deals with either directed or undirected graphs
    '''
    e = graph.existEdge(node1, node2)
    if e.isValid():
        return e
    else:
        if not directed:
            e = graph.existEdge(node2, node1)
            if e.isValid():
                return e
            else:
                if create:
                    e = graph.addEdge(node1, node2)
                    return e                        
        else:
            if create:    
                e = graph.addEdge(node1, node2)
                return e
            else:
                return None

def main(graph): 
  acronym = graph.getStringProperty("acronym")
  activityType = graph.getStringProperty("activityType")
  call = graph.getStringProperty("call")
  city = graph.getStringProperty("city")
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
  relationshipValue = graph.getDoubleProperty('relationshipValue')
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
  # initialize two new properties to represent collaboration
  projectsTogether = graph.getIntegerProperty('projectsTogether')
  moneyTogether = graph.getDoubleProperty('moneyTogether')
#  programmeVec = graph.getStringVectorProperty('programmeVec')
#  topicsVec = graph.getStringVectorProperty(topicsVec)
  
  stacked = graph.addSubGraph('stacked')
#  doubleStacked = graph.addSubGraph('doubleStacked')
  # add nodes in one pass
  for n in graph.getNodes():
    if projectNode[n] == False: # the stacked graph's nodes are only organizations
      addedNode = stacked.addNode(n)
#      otherAddedNode = doubleStacked.addNode(n)
  
  # add edges
  for e in graph.getEdges():
    source = graph.source(e)
    target = graph.target(e)
    stackedEdge = findEdge (source, target, stacked, False, True)
    # the last argument makes sure that an edge exists after the function call
    # we add the "stackable" information contained in e
    projectsTogether[stackedEdge] += 1
    moneyTogether[stackedEdge] += ecMaxContribution[e]
    
#    otherStackedEdge1 = findEdge (target, source, doubleStacked, True, True)
#    # reversing source and target to keep track of each org's share of money
#    relationshipValue[otherStackedEdge1] += e['ecContribution']
#    otherStackedEdge2 = findEdge (source, target, doubleStacked, True, True)
#    relationshipValue[otherStackedEdge2] += e['ecContribution']    

  end_script = datetime.datetime.now() 
  print ('Runtime: ' + str (end_script - start_script))

      
