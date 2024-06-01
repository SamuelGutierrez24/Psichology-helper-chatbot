from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

from pgmpy.factors.discrete import TabularCPD
def defineModel():
  psycologyModel = BayesianModel()

  psycologyModel.add_nodes_from(['Traumatic Events', 'Rejection', 'Too Much Work', 'Poor resource management', 'Self doubt', 'Phisical injury', 'Guilt',
                                'Depression', 'Stress', 'Anxiety', 'Uninterested', 'Low energy', 'Low concentration', 'Hopeless', 'Too much/too little apetite',
                                'Move too slow/too fast', 'Too much/too little sleep', 'Self harm thoughts', 'Inability to control things in life', 'Overwhelmed',
                                'Upset from unexpected situation', "Hasn't felt things going their way", 'Irritable', 'Nervous', 'Cannot control worries', 'Cannot relax',
                                'Worried all the time', 'Cannot stand still', 'Dreadfull'])



  #Edges

  psycologyModel.add_edge('Traumatic Events', 'Depression')
  psycologyModel.add_edge('Rejection', 'Depression')
  psycologyModel.add_edge('Rejection', 'Stress')
  psycologyModel.add_edge('Too Much Work', 'Stress')
  psycologyModel.add_edge('Poor resource management', 'Stress')
  psycologyModel.add_edge('Self doubt', 'Stress')
  psycologyModel.add_edge('Self doubt', 'Anxiety')
  psycologyModel.add_edge('Phisical injury', 'Anxiety')
  psycologyModel.add_edge('Guilt', 'Anxiety')
  psycologyModel.add_edge('Anxiety', 'Dreadfull')
  psycologyModel.add_edge('Anxiety', 'Cannot stand still')
  psycologyModel.add_edge('Anxiety', 'Worried all the time')
  psycologyModel.add_edge('Anxiety', 'Cannot relax')
  psycologyModel.add_edge('Anxiety', 'Cannot control worries')
  psycologyModel.add_edge('Anxiety', 'Nervous')
  psycologyModel.add_edge('Anxiety', 'Irritable')
  psycologyModel.add_edge('Stress', 'Cannot control worries')
  psycologyModel.add_edge('Stress', 'Nervous')
  psycologyModel.add_edge('Stress', 'Irritable')
  psycologyModel.add_edge('Stress', "Hasn't felt things going their way")
  psycologyModel.add_edge('Stress', 'Upset from unexpected situation')
  psycologyModel.add_edge('Stress', 'Overwhelmed')
  psycologyModel.add_edge('Stress', 'Inability to control things in life')
  psycologyModel.add_edge('Depression', 'Inability to control things in life')
  psycologyModel.add_edge('Depression', 'Self harm thoughts')
  psycologyModel.add_edge('Depression', 'Too much/too little sleep')
  psycologyModel.add_edge('Depression', 'Move too slow/too fast')
  psycologyModel.add_edge('Depression', 'Too much/too little apetite')
  psycologyModel.add_edge('Depression', 'Hopeless')
  psycologyModel.add_edge('Depression', 'Low concentration')
  psycologyModel.add_edge('Depression', 'Low energy')
  psycologyModel.add_edge('Depression', 'Uninterested')


  cpd_TraumaticEvents = TabularCPD('Traumatic Events', variable_card=2, values=[[0.08],[0.92]])
  cpd_AbusiveRelationships = TabularCPD('Rejection', variable_card=2, values=[[0.14],[0.86]])
  cpd_TooMuchWork= TabularCPD('Too Much Work', variable_card=2, values=[[0.19],[0.81]])
  cpd_poorResourceManagement = TabularCPD('Poor resource management', variable_card=2, values=[[0.08],[0.92]])
  cpd_SelfDoubt = TabularCPD('Self doubt', variable_card=2, values=[[0.09],[0.91]])
  cpd_PhisicalInjury = TabularCPD('Phisical injury', variable_card=2, values=[[0.02],[0.98]])
  cpd_Guilt = TabularCPD('Guilt', variable_card=2, values=[[0.1],[0.9]])



  cpd_Anxiety = TabularCPD(
      'Anxiety',
      variable_card=2,
      values=[
          [0.79,0.39,0.49,0.22,0.2,0.03,0.06,0.01],
          [0.21,0.61,0.51,0.78,0.8,0.97,0.94,0.99]
      ],
      evidence=['Self doubt', 'Phisical injury', 'Guilt'],
      evidence_card=[2,2,2]
  )

  cpd_Stress = TabularCPD(
      'Stress',
      variable_card=2,
      values=[
          [0.8,0.43,0.42,0.35,0.38,0.2,0.15,0.09,0.45,0.4,0.3,0.2,0.19,0.15,0.03,0.01],
          [0.2,0.57,0.58,0.65,0.62,0.8,0.85,0.91,0.55,0.6,0.7,0.8,0.81,0.85,0.97,0.99]
      ],
      evidence=['Rejection', 'Too Much Work', 'Poor resource management', 'Self doubt'],
      evidence_card=[2,2,2,2]
  )

  cpd_Depression = TabularCPD(
      'Depression',
      variable_card=2,
      values=[
          [0.87, 0.45, 0.35, 0.01],
          [0.13, 0.55, 0.65, 0.99]
      ],
      evidence=['Traumatic Events', 'Rejection'],
      evidence_card=[2,2]
  )


  cpd_Uninterested = TabularCPD(
  "Uninterested",
  variable_card=2,
  values=[
  [0.46, 0.16],
  [0.54, 0.84]
  ],
  evidence=["Depression"],
  evidence_card=[2])

  cpd_LowEnergy = TabularCPD(
  "Low energy",
  variable_card=2,
  values=[
  [0.34, 0.06],
  [0.66, 0.94]
  ],
  evidence=["Depression"],
  evidence_card=[2])

  cpd_LowConcentration = TabularCPD(
  "Low concentration",
  variable_card=2,
  values=[
  [0.42, 0.27],
  [0.58, 0.73]
  ],
  evidence=["Depression"],
  evidence_card=[2])

  cpd_Hopeless = TabularCPD(
  "Hopeless",
  variable_card=2,
  values=[
  [0.45, 0.16],
  [0.55, 0.84]
  ],
  evidence=["Depression"],
  evidence_card=[2])

  cpd_TMTLApetite = TabularCPD(
  "Too much/too little apetite",
  variable_card=2,
  values=[
  [0.25, 0.11],
  [0.75, 0.89]
  ],
  evidence=["Depression"],
  evidence_card=[2])

  cpd_MoveTSTF = TabularCPD(
  "Move too slow/too fast",
  variable_card=2,
  values=[
  [0.23, 0.18],
  [0.77, 0.82]
  ],
  evidence=["Depression"],
  evidence_card=[2])

  cpd_TMTLSleep = TabularCPD(
  "Too much/too little sleep",
  variable_card=2,
  values=[
  [0.36, 0.19],
  [0.64, 0.81]
  ],
  evidence=["Depression"],
  evidence_card=[2])

  cpd_SelfHarmThoughts = TabularCPD(
  "Self harm thoughts",
  variable_card=2,
  values=[
  [0.7, 0.25],
  [0.3, 0.75]
  ],
  evidence=["Depression"],
  evidence_card=[2])

  cpd_InavilityToControl = TabularCPD(
  "Inability to control things in life",
  variable_card=2,
  values=[
  [0.32, 0.24, 0.12,0.01],
  [0.68, 0.76, 0.88, 0.99]
  ],
  evidence=["Depression", 'Stress'],
  evidence_card=[2,2])



  cpd_Overwhelmed = TabularCPD(
  "Overwhelmed",
  variable_card=2,
  values=[
  [0.5, 0.15],
  [0.5, 0.85]
  ],
  evidence=["Stress"],
  evidence_card=[2])

  cpd_Upset = TabularCPD(
  "Upset from unexpected situation",
  variable_card=2,
  values=[
  [0.25, 0.14],
  [0.75, 0.86]
  ],
  evidence=["Stress"],
  evidence_card=[2])

  cpd_TheirWay = TabularCPD(
  "Hasn't felt things going their way",
  variable_card=2,
  values=[
  [0.31, 0.14],
  [0.69, 0.86]
  ],
  evidence=["Stress"],
  evidence_card=[2])

  cpd_Irritable = TabularCPD(
  "Irritable",
  variable_card=2,
  values=[
  [0.45, 0.35, 0.36, 0.01],
  [0.55, 0.65, 0.64, 0.99]
  ],
  evidence=['Anxiety', "Stress"],
  evidence_card=[2,2])

  cpd_Nervous = TabularCPD(
  "Nervous",
  variable_card=2,
  values=[
  [0.3, 0.42, 0.26, 0.01],
  [0.7, 0.58, 0.74, 0.99]
  ],
  evidence=['Anxiety', "Stress"],
  evidence_card=[2,2])

  cpd_CannotControlWorries = TabularCPD(
  "Cannot control worries",
  variable_card=2,
  values=[
  [0.24, 0.34, 0.42, 0.01],
  [0.76, 0.66, 0.58, 0.99]
  ],
  evidence=['Anxiety', "Stress"],
  evidence_card=[2,2])

  cpd_WorriedAllTheTime = TabularCPD(
  "Worried all the time",
  variable_card=2,
  values=[
  [0.37, 0.16],
  [0.63, 0.84]
  ],
  evidence=["Anxiety"],
  evidence_card=[2])


  cpd_CannotRelax = TabularCPD(
  "Cannot relax",
  variable_card=2,
  values=[
  [0.21, 0.11],
  [0.79, 0.89]
  ],
  evidence=["Anxiety"],
  evidence_card=[2])

  cpd_CannotStandStill = TabularCPD(
  "Cannot stand still",
  variable_card=2,
  values=[
  [0.3, 0.12],
  [0.7, 0.88]
  ],
  evidence=["Anxiety"],
  evidence_card=[2])

  cpd_Dreadfull = TabularCPD(
  "Dreadfull",
  variable_card=2,
  values=[
  [0.35, 0.04],
  [0.65, 0.96]
  ],
  evidence=["Anxiety"],
  evidence_card=[2])


  psycologyModel.add_cpds(cpd_TraumaticEvents, cpd_AbusiveRelationships, cpd_TooMuchWork, cpd_poorResourceManagement, cpd_SelfDoubt,
                          cpd_PhisicalInjury, cpd_Guilt, cpd_Anxiety, cpd_Stress, cpd_Depression, cpd_Uninterested, cpd_LowEnergy,
                          cpd_LowConcentration, cpd_Hopeless, cpd_TMTLApetite, cpd_MoveTSTF, cpd_TMTLSleep, cpd_SelfHarmThoughts,
                          cpd_InavilityToControl, cpd_Overwhelmed, cpd_Upset, cpd_TheirWay, cpd_Irritable, cpd_Nervous, cpd_CannotControlWorries,
                          cpd_WorriedAllTheTime, cpd_CannotRelax, cpd_CannotStandStill, cpd_Dreadfull)
  
  return psycologyModel