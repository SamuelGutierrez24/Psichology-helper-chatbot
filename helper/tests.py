from django.test import TestCase
from .views.chat_view import processFirstQuestionSet, processSecondQuestionSet
from helper.models import diagnosis


class UtilsTestCase(TestCase):

    
    def test_ProcessFirstQuestionSetDepression(self):

        result1 = processFirstQuestionSet(['si', 'no', 'no', 'no','no', 'no', 'no', 'no','si', 'si', 'si',
                                              'no','no', 'no', 'no', 'si','no', 'si', 'no'])

        result2= processFirstQuestionSet(['si', 'si', 'si', 'si','si', 'si', 'si', 'si','si', 'si', 'si',
                                              'si','si', 'no', 'si', 'si','si', 'si', 'si'])
        
        result3= processFirstQuestionSet(['no', 'si', 'si', 'si','no', 'si', 'no', 'si','si', 'no', 'si',
                                              'si','no', 'si', 'si', 'si','si', 'si', 'si'])
        
        self.assertEqual(result1, "Depression")
        self.assertEqual(result2, "Depression")
        self.assertEqual(result3, "Depression")
    
    
    
    def test_ProcessFirstQuestionSetAnxiety(self):

        result1 = processFirstQuestionSet(['si', 'si', 'si', 'si','si', 'si', 'no', 'no','no', 'no', 'no',
                                              'no','no', 'no', 'no', 'si','no', 'si', 'no'])

        result2= processFirstQuestionSet(['si', 'si', 'si', 'si','si', 'no', 'no', 'si','no', 'no', 'si',
                                              'si','no', 'no', 'si', 'si','si', 'no', 'no'])
        
        result3= processFirstQuestionSet(['no', 'si', 'si', 'si','no', 'si', 'no', 'no','no', 'no', 'no',
                                              'no','no', 'no', 'no', 'no','no', 'no', 'no'])
        
        self.assertEqual(result1, "Anxiety")
        self.assertEqual(result2, "Anxiety")
        self.assertEqual(result3, "Anxiety")


    def test_ProcessFirstQuestionSetStress(self):

        result1 = processFirstQuestionSet(['no', 'no', 'no', 'no','si', 'si', 'si', 'si','si', 'si', 'si',
                                              'no','no', 'no', 'no', 'no','no', 'no', 'no'])

        result2= processFirstQuestionSet(['no', 'si', 'no', 'no','si', 'si', 'si', 'si','no', 'si', 'si',
                                              'no','no', 'si', 'no', 'no','si', 'no', 'no'])
        
        result3= processFirstQuestionSet(['no', 'si', 'no', 'no','si', 'no', 'no', 'si','no', 'si', 'si',
                                              'no','no', 'si', 'no', 'no','no', 'si', 'no'])
        
        self.assertEqual(result1, "Stress")
        self.assertEqual(result2, "Stress")
        self.assertEqual(result3, "Stress")

    

    def test_ProcessSecondQuestionSetDepression(self):

        result1=processSecondQuestionSet(['si', 'si', 'no', 'no','no'], "Depression")
        result2=processSecondQuestionSet(['no', 'no', 'si', 'si','si'], "Depression")

        self.assertEqual(result1, '''La condicion puede estar causada por un evento traumático.
               Lamento mucho que hayas pasado por una situación así,me imagino que ha sido muy difícil para ti. Sería bueno que encontraras un espacio en el que te sientas segur@ para poder hablarlo con libertad, con alguien con quien te sientas cómod@. Mientras, recuerda que para aprender a sobrellevar este evento traumático toma tiempo, no trates de apresurarte o huir de este, es un proceso y requiere de mucha valentía para llevarlo a cabo.\n\n\n''')
   
        self.assertEqual(result2, '''La condicion puede estar causada por un sentimiento de rechazo. Lamento mucho que te sientas de esta forma, a veces nos encontramos en el camino con personas que no ven nuestro potencial o nuestro valor, eso no significa que no esté en ti. La única persona que sabe que tanto ha hecho para llegar a donde está eres tú mism@, nadie más tiene el poder de vivir tu vida, solo tú. Reconocer tus méritos y tus logros puede ser una tarea que tome tiempo, pero está en ti hacerlo, no te apures en ello, empieza con pasos pequeños, apláudete. Por otro lado, sentirnos apoyados nos brinda más confianza, pero es fundamental acompañarnos de las personas que queremos, que nos aportan. Los comentarios negativos lamentablemente siempre estarán en nuestra vida, pero lo que hagas con ellos es lo que realmente importa ¿qué puedes aprender de estos?
               ¡Recuerda que una persona que te quiere jamás buscará hacerte daño! Estarán para ti, de formas distintas, pero estarán.\n\n\n''')
    
    
    def test_ProcessSecondQuestionSetStress(self):

        result1=processSecondQuestionSet(['si', 'si', 'no', 'si','no','no','si','no','no'], "Stress")
        result2=processSecondQuestionSet(['si', 'si', 'no', 'si','si','si','si','no','no'], "Stress")
        result3=processSecondQuestionSet(['no', 'si', 'no', 'si','no','no','si','si','no'], "Stress")

        self.assertEqual(result1, '''La condicion puede estar causada por un exceso de trabajo.
               Debe de ser muy difícil, el ritmo de trabajo a veces supera nuestros tiempos. Es totalmente natural sentirnos cargados o estresados cuando vemos que algo nos supera. Llevar un manejo adecuado del tiempo por medio de un cronograma, priorizar labores y hacer listas de chequeos puede ayudarte a llevar a cabo tus funciones y facilitar la organización de los tiempos. Separar tus espacios de trabajo de lo personal y permitirte tomar pausas activas en el trabajo, en estas puedes realizar algunos ejercicios de respiración.\n\n\n''')
    
        self.assertEqual(result2, '''La condicion puede estar causada por una mala administración de recursos.
               Entiendo que esto puede generarte malestar (estrés), la administración de los recursos puede ser una labor que tome tiempo aprender a gestionar de forma efectiva. El manejo de recursos se puede llevar a cabo por medio de estrategias, ¿has oído hablar de la economía de fichas? Esta, es una herramienta donde según tu desempeño en metas personales obtienes recompensas.\n\n\n''')
    
        self.assertEqual(result3,'''La condicion puede estar causada por dudas sobre ti mismo.
               Todos los seres humanos hemos sentido en algún momento que dudamos de nosotros mismos, de todo lo que somos capaces de realizar. Nosotros, como personas podemos tener infinidades de pensamientos que llegan de muchas partes, pues nuestra mente está constantemente recibiendo estímulos; aprender a diferenciar qué pensamientos ameritan tu atención es una forma de autocuidarnos. Tómate un tiempo para ti, frena y respira profundamente, Encontrar una forma que te ayude a liberar emociones, propicia el bienestar y puede ayudar a la recuperación, esto lo puedes hacer por medio de la expresión artística o simplemente conversando sobre tus sentimientos y emociones.\n\n\n''')
    
    
    def test_ProcessSecondQuestionSetAnxiety(self):

        result1=processSecondQuestionSet(['si', 'si', 'si', 'no','no','no','no','no'], "Anxiety")
        result2=processSecondQuestionSet(['no', 'no', 'no', 'si','si','no','no','no'], "Anxiety")
        result3=processSecondQuestionSet(['no', 'no', 'no', 'no','no','si','si','si'], "Anxiety")

        self.assertEqual(result1, '''La condicion puede estar causada por un sentimiento de culpa.
               Comprendo lo duro que debe ser para ti sentirte de esta forma, la culpa es un sentimiento que nos carga muchas veces y no comprendemos que hacer con ella. Es bueno que entiendas que las situaciones de la vida se nos pueden salir de las manos, simplemente suceden. En nuestros caminos nos encontramos con situaciones muy variadas que enfrentaremos con las herramientas y conocimientos que dispongamos; no siempre saldrán de la forma que deseamos, pero otras veces sí. Lo importante es que sepas identificar lo que puede estar en tu control y lo que no. No está mal aceptar que no podemos con todo y que como personas, podemos cometer errores. Perdónate, perdona, busca si hay algo que puedes hacer ante esa situación, y si no, sigue, que de esta podrás aprender. ¡Probablemente a la próxima te sentirás y saldrá mejor!\n\n\n''')
  
        self.assertEqual(result2, '''La condicion puede estar causada por un daño físico.
                         Me imagino lo difícil que ha sido para ti vivir esta situación, no es nada fácil adaptarnos a los cambios. Aprender a vivir con una condición clínica toma tiempo, esta repercute en tus dinámicas y en tu estilo de vida. Eres muy valiente al afrontar esto; apóyate en tus personas de confianza y en los profesionales. Encontrar una forma que te ayude a liberar emociones, propicia el bienestar y puede ayudar a la recuperación, esto lo puedes hacer por medio de la expresión artística o simplemente conversando sobre tus sentimientos y emociones.\n\n\n''')
    
        self.assertEqual(result3,'''La condicion puede estar causada por dudas sobre ti mismo.
               Todos los seres humanos hemos sentido en algún momento que dudamos de nosotros mismos, de todo lo que somos capaces de realizar. Nosotros, como personas podemos tener infinidades de pensamientos que llegan de muchas partes, pues nuestra mente está constantemente recibiendo estímulos; aprender a diferenciar qué pensamientos ameritan tu atención es una forma de autocuidarnos. Tómate un tiempo para ti, frena y respira profundamente, Encontrar una forma que te ayude a liberar emociones, propicia el bienestar y puede ayudar a la recuperación, esto lo puedes hacer por medio de la expresión artística o simplemente conversando sobre tus sentimientos y emociones.\n\n\n''')
    

    def test_ProcessSecondQuestionSetStress(self):
            result2= processFirstQuestionSet(['no', 'si', 'no', 'no','si', 'si', 'si', 'si','no', 'si', 'si',
                                            'no','no', 'no', 'no', 'no','no', 'no', 'no'])
            result1=processSecondQuestionSet(['si', 'si', 'no', 'si','no','no','si','no','no'], "Stress")
