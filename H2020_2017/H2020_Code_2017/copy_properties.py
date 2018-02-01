# Powered by Python 2.7

# copy local properties into global ones


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
  partners = graph.getIntegerProperty('partners')
  projects = graph.getIntegerProperty('projects')
  allMyMoney = graph.getDoubleProperty('allMyMoney')
  TentativeSIC = graph.getStringProperty("TentativeSIC")
  acronym = graph.getStringProperty("acronym")
  activityType = graph.getStringProperty("activityType")
  birthDate = graph.getIntegerProperty("birthDate")
  call = graph.getStringProperty("call")
  city = graph.getStringProperty("city")
  commDate = graph.getDoubleProperty("commDate")
  country = graph.getStringProperty("country")
  ecContribution = graph.getDoubleProperty("ecContribution")
  ecMaxContribution = graph.getDoubleProperty("ecMaxContribution")
  endDate = graph.getStringProperty("endDate")
  endOfParticipation = graph.getBooleanProperty("endOfParticipation")
  fundingScheme = graph.getStringProperty("fundingScheme")
  intimacy = graph.getDoubleProperty("intimacy")
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
  
  bipartite = graph.getSubGraph('bipartite')
  orgs2orgs = graph.getSubGraph('orgs2orgs')
  stacked = orgs2orgs.getSubGraph('stacked')
  for n in graph.getNodes():
    if projectNode[n] == False:
      thisNode = orgId[n]
      for n1 in stacked.getNodes():
        if orgId[n1] == thisNode:
          partners[n] = numPartners.getNodeValue(n1)
      for n2 in bipartite.getNodes():
        if orgId[n2] == thisNode:
          projects[n] = numProjects[n2]
          allMyMoney[n] = myMoney[n2]
