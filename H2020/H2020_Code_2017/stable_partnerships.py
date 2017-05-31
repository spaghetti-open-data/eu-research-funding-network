# Powered by Python 2.7

# Builds the stable parnership graph. Run from the stacked.

from tulip import tlp

# The updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# The pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# The runGraphScript(scriptFile, graph) function can be called to launch
# another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# The main(graph) function must be defined 
# to run the script on the current graph

def main(graph): 
  moneyTogether = graph.getDoubleProperty("moneyTogether")
  projectsTogether = graph.getIntegerProperty("projectsTogether")
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
  viewBorderColor = graph.getColorProperty("viewBorderColor")
  viewBorderWidth = graph.getDoubleProperty("viewBorderWidth")
  viewColor = graph.getColorProperty("viewColor")
  viewFont = graph.getStringProperty("viewFont")
  viewFontAwesomeIcon = graph.getStringProperty("viewFontAwesomeIcon")
  viewFontSize = graph.getIntegerProperty("viewFontSize")
  viewIcon = graph.getStringProperty("viewIcon")
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

  stable = graph.addSubGraph('stable') # creates the subgraph
  for n in graph.getNodes(): # all nodes are added in one pass
    newNode = stable.addNode(n)
    
  for e in graph.getEdges():
    if projectsTogether[e] > 1:
      stableEdge = stable.addEdge(e)
      
    
