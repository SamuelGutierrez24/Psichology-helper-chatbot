from experta import *
from .bayesianNetwork import defineModel
from pgmpy.inference import VariableElimination

class MentalHealthHelper(KnowledgeEngine):

  answers = set()

  def getAnswers(self):
    print(self.answers)
    return self.answers

  conds = list()

  def getConds(self):
    return self.conds
  
  lows = set()
  def getLows(self):
    return self.lows
  
  und = set()
  def getUnd(self):
    return self.und

  influence = 'Undetermined'
  def getInfluence(self):
    return self.influence

       
  @DefFacts()
  def _initial_ ( self ) :
    yield Fact(condition='Depression', cause='Traumatic event', recommendation='''La condicion puede estar causada por un evento traumático.
               Lamento mucho que hayas pasado por una situación así,me imagino que ha sido muy difícil para ti. Sería bueno que encontraras un espacio en el que te sientas segur@ para poder hablarlo con libertad, con alguien con quien te sientas cómod@. Mientras, recuerda que para aprender a sobrellevar este evento traumático toma tiempo, no trates de apresurarte o huir de este, es un proceso y requiere de mucha valentía para llevarlo a cabo.''')
   
    yield Fact(condition='Stress', cause='Too Much Work', recommendation='''La condicion puede estar causada por un exceso de trabajo.
               Debe de ser muy difícil, el ritmo de trabajo a veces supera nuestros tiempos. Es totalmente natural sentirnos cargados o estresados cuando vemos que algo nos supera. Llevar un manejo adecuado del tiempo por medio de un cronograma, priorizar labores y hacer listas de chequeos puede ayudarte a llevar a cabo tus funciones y facilitar la organización de los tiempos. Separar tus espacios de trabajo de lo personal y permitirte tomar pausas activas en el trabajo, en estas puedes realizar algunos ejercicios de respiración.''')
    
    yield Fact(condition='Stress', cause='Poor resource management', recommendation='''La condicion puede estar causada por una mala administración de recursos.
               Entiendo que esto puede generarte malestar (estrés), la administración de los recursos puede ser una labor que tome tiempo aprender a gestionar de forma efectiva. El manejo de recursos se puede llevar a cabo por medio de estrategias, ¿has oído hablar de la economía de fichas? Esta, es una herramienta donde según tu desempeño en metas personales obtienes recompensas.''')
    
    yield Fact(condition='Stress', cause='Self doubt', recommendation='''La condicion puede estar causada por dudas sobre ti mismo.
               Todos los seres humanos hemos sentido en algún momento que dudamos de nosotros mismos, de todo lo que somos capaces de realizar. Nosotros, como personas podemos tener infinidades de pensamientos que llegan de muchas partes, pues nuestra mente está constantemente recibiendo estímulos; aprender a diferenciar qué pensamientos ameritan tu atención es una forma de autocuidarnos. Tómate un tiempo para ti, frena y respira profundamente, Encontrar una forma que te ayude a liberar emociones, propicia el bienestar y puede ayudar a la recuperación, esto lo puedes hacer por medio de la expresión artística o simplemente conversando sobre tus sentimientos y emociones.''')
    
    yield Fact(condition='Anxiety', cause='Self doubt', recommendation='''La condicion puede estar causada por dudas sobre ti mismo.
               Todos los seres humanos hemos sentido en algún momento que dudamos de nosotros mismos, de todo lo que somos capaces de realizar. Nosotros, como personas podemos tener infinidades de pensamientos que llegan de muchas partes, pues nuestra mente está constantemente recibiendo estímulos; aprender a diferenciar qué pensamientos ameritan tu atención es una forma de autocuidarnos. Tómate un tiempo para ti, frena y respira profundamente, Encontrar una forma que te ayude a liberar emociones, propicia el bienestar y puede ayudar a la recuperación, esto lo puedes hacer por medio de la expresión artística o simplemente conversando sobre tus sentimientos y emociones.''')
    
    yield Fact(condition='Depression', cause='Reject', recommendation='''La condicion puede estar causada por un sentimiento de rechazo. Lamento mucho que te sientas de esta forma, a veces nos encontramos en el camino con personas que no ven nuestro potencial o nuestro valor, eso no significa que no esté en ti. La única persona que sabe que tanto ha hecho para llegar a donde está eres tú mism@, nadie más tiene el poder de vivir tu vida, solo tú. Reconocer tus méritos y tus logros puede ser una tarea que tome tiempo, pero está en ti hacerlo, no te apures en ello, empieza con pasos pequeños, apláudete. Por otro lado, sentirnos apoyados nos brinda más confianza, pero es fundamental acompañarnos de las personas que queremos, que nos aportan. Los comentarios negativos lamentablemente siempre estarán en nuestra vida, pero lo que hagas con ellos es lo que realmente importa ¿qué puedes aprender de estos?
               ¡Recuerda que una persona que te quiere jamás buscará hacerte daño! Estarán para ti, de formas distintas, pero estarán.''')
    
    yield Fact(condition='Anxiety', cause='Guilt', recommendation='''La condicion puede estar causada por un sentimiento de culpa.
               Comprendo lo duro que debe ser para ti sentirte de esta forma, la culpa es un sentimiento que nos carga muchas veces y no comprendemos que hacer con ella. Es bueno que entiendas que las situaciones de la vida se nos pueden salir de las manos, simplemente suceden. En nuestros caminos nos encontramos con situaciones muy variadas que enfrentaremos con las herramientas y conocimientos que dispongamos; no siempre saldrán de la forma que deseamos, pero otras veces sí. Lo importante es que sepas identificar lo que puede estar en tu control y lo que no. No está mal aceptar que no podemos con todo y que como personas, podemos cometer errores. Perdónate, perdona, busca si hay algo que puedes hacer ante esa situación, y si no, sigue, que de esta podrás aprender. ¡Probablemente a la próxima te sentirás y saldrá mejor!''')

    yield Fact(condition='Anxiety', cause= 'Phisical injury', recommendation='''La condicion puede estar causada por un daño físico.
                         Me imagino lo difícil que ha sido para ti vivir esta situación, no es nada fácil adaptarnos a los cambios. Aprender a vivir con una condición clínica toma tiempo, esta repercute en tus dinámicas y en tu estilo de vida. Eres muy valiente al afrontar esto; apóyate en tus personas de confianza y en los profesionales. Encontrar una forma que te ayude a liberar emociones, propicia el bienestar y puede ayudar a la recuperación, esto lo puedes hacer por medio de la expresión artística o simplemente conversando sobre tus sentimientos y emociones.''')
    

  symptoms = list()
  
  bNet = defineModel()

  def resetAns(self):
    self.answers = set()

  def resetCons(self):
    self.conds = list()

  def resetSym(self):
    self.symptoms = list()
  
  def trueReset(self):
    self.resetAns()
    self.resetCons()
    self.resetSym()
    self.reset()
    self.influence = 'Undetermined'

  @Rule(Fact(symptom=MATCH.a), salience=10)
  def addSymptom(self, a):
    #print(a)
    self.symptoms.append(a)

  @Rule(Fact(status='Done'), salience=1)
  def computeSymptoms(self):
    dSympt = {}
    for n in self.symptoms:
      #print(n)
      dSympt.update({n:0})
    print(dSympt)
    inference = VariableElimination(self.bNet)
    dep = inference.query(["Depression"], evidence=dSympt)
    print(dep)
    self.declare(Fact(depression=dep.values[0]))
    stress = inference.query(["Stress"], evidence=dSympt)
    print(stress)
    self.declare(Fact(stress=stress.values[0]))
    anx = inference.query(["Anxiety"], evidence=dSympt)
    print(anx)
    self.declare(Fact(anxiety=anx.values[0]))


  @Rule(Fact(depression=MATCH.a), TEST(lambda a: a>0.7))
  def hasDepression(self, a):
    self.declare(Fact(cond = 'Depression'))
    self.conds.append(['Depression', a])

  @Rule(Fact(stress=MATCH.a), TEST(lambda a: a>0.7))
  def hasStress(self, a):
    self.declare(Fact(cond = 'Stress'))
    self.conds.append(['Stress', a])

  @Rule(Fact(anxiety=MATCH.a), TEST(lambda a: a>0.7))
  def hasAnxiety(self, a):
    self.declare(Fact(cond = 'Anxiety'))
    self.conds.append(['Anxiety', a])

  @Rule(Fact(Hcond=MATCH.a),Fact(posCause=MATCH.b), Fact(condition=MATCH.a, cause=MATCH.b, recommendation= MATCH.c))
  def recommendation(self, c):
    self.answers.add(c)

  @Rule(Fact(depression=MATCH.a), TEST(lambda a: a<0.2))
  def hasDepressionLow(self):
    self.declare(Fact(low='Depression'))

  @Rule(Fact(stress=MATCH.a), TEST(lambda a: a<0.2))
  def hasStressLow(self):
    self.declare(Fact(low = 'Stress'))

  @Rule(Fact(anxiety=MATCH.a), TEST(lambda a: a<0.2))
  def hasAnxietyLow(self):
    self.declare(Fact(low = 'Anxiety'))

  @Rule(Fact(low = MATCH.a))
  def addLow(self, a):
    self.lows.add(a)

  @Rule(Fact(depression=MATCH.a), TEST(lambda a: a>0.2 and a<0.7))
  def hasDepressionUndefined(self):
    self.declare(Fact(undefined='Depression'))

  @Rule(Fact(stress=MATCH.a), TEST(lambda a: a>0.2 and a<0.7))
  def hasStressUndefined(self):
    self.declare(Fact(undefined = 'Stress'))

  @Rule(Fact(anxiety=MATCH.a), TEST(lambda a: a>0.2 and a<0.7))
  def hasAnxietyUndefined(self):    
    self.declare(Fact(undefined = 'Anxiety'))
  
  @Rule(Fact(undefined=MATCH.a))
  def addUndefinde(self, a):
    self.und.add(a)

  @Rule(OR(Fact(posCause='Traumatic event'),Fact(posCause='Too Much Work'),Fact(posCause='Poor resource management'), Fact(posCause='Phisical injury'), Fact(posCause='Reject')))
  def external(self):
    self.declare(Fact(influence='External'))
  
  @Rule(OR(Fact(posCause='Self doubt'),Fact(posCause='Guilt')))
  def internal(self):
    self.declare(Fact(influence='Internal'))
  
  @Rule(Fact(influence=MATCH.a))
  def addInfluence(self,a):
    self.influence = a
  
  @Rule(Fact(p1=MATCH.a), TEST(lambda a: a>=2))
  def p1(self):
    self.declare(Fact(posCause="Too Much Work"))
  
  @Rule(Fact(p2=MATCH.a), TEST(lambda a: a>=2))
  def p2(self):
    self.declare(Fact(posCause="Poor resource management"))
  
  @Rule(OR(AND(Fact(p3=MATCH.a), TEST(lambda a: a>=2)),AND(Fact(p5=MATCH.b), TEST(lambda b: b>=2))))
  def p3(self):
    self.declare(Fact(posCause="Self doubt"))
  
  @Rule(Fact(p4=MATCH.a), TEST(lambda a: a>=2))
  def p4(self):
    self.declare(Fact(posCause="Phisical injury"))
  
  @Rule(Fact(p6=MATCH.a), TEST(lambda a: a>=2))
  def p6(self):
    print('huh')
    self.declare(Fact(posCause="Traumatic event"))
  
  @Rule(Fact(p7=MATCH.a), TEST(lambda a: a>=2))
  def p7(self):
    self.declare(Fact(posCause="Reject"))
  
  @Rule(Fact(p8=MATCH.a), TEST(lambda a: a>=2))
  def p8(self):
    self.declare(Fact(posCause="Guilt"))



# es = MentalHealthHelper()

# es.reset()
# print('huh')
# es.declare(Fact(Hcond='Depression'))
# es.declare(Fact(posCause='Traumatic event'))
# print('wut')
# es.run()

# es.declare(Fact(Hcond='Stress'))
# es.declare(Fact(posCause='Too Much Work'))
# es.run()
# print(es.answers)