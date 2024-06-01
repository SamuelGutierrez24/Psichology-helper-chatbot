from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from PsychologyHelper.logic.expertSystem import MentalHealthHelper
from experta import *
import json
from collections import Counter

from helper.models import Message
from helper.models import diagnosis
import copy


expert_system = MentalHealthHelper()

unde=[]
diag=[]
low=[]
influ=""
#Hola buenas tardes

preguntas = [
  "¿Sientes que no te puedes relajar?",
  "¿Sientes que no te puedes quedar quieto?",
  "¿Sientes temor de forma irracional?", 
  "¿Te sientes preocupado todo el tiempo?",
  "¿Sientes que no puedes controlar tus preocupaciones?",
  "¿Te sientes irritable?",
  "¿Te sientes nervioso?",
  "¿Te sientes molesto por situaciones inesperadas?",
  "¿Sientes que las cosas no te han salido bien últimamente?",
  "¿Sientes que no tienes el control de tu vida?",
  "¿Te sientes abrumado?",
  "¿Te sientes desinteresado?",
  "¿Te sientes desesperanzado?",
  "¿Te sientes falto de energía?",
  "¿Sientes que te desconcentras fácilmente?",
  "¿Sientes mucho o muy poco apetito?",
  "¿Sientes que caminas muy rápido o muy lento?",
  "¿Duermes mucho o muy poco?",
  "¿Tienes pensamientos de autolesión?"
]


#trabajo(3)-recursos(3)-duda(3)
preguntas_estres= ["¿Sientes que tu trabajo requiere más tiempo y energía de lo que puedes proporcionar sin comprometer tu bienestar?",
"¿Te resulta difícil desconectarte de tus responsabilidades laborales incluso cuando no estás trabajando?",
"¿Sientes que las expectativas de tu rendimiento laboral son poco claras o demasiado exigentes?",
"¿Te preocupas constantemente por no tener suficiente dinero para cubrir tus gastos básicos o emergencias?",
"¿Describirías como buena tu habilidad para administrar tus finanzas personales en términos de planificación y ahorro?",
"¿El estrés financiero te ha llevado a tomar decisiones que afectan negativamente tu calidad de vida o bienestar emocional?",
"¿Te sientes frecuentemente insatisfecho con tus logros debido a la inseguridad en tus habilidades?",
"Cuando las cosas no salen como esperabas, ¿tus primeros pensamientos son críticos hacia tus capacidades?",
"¿Con frecuencia te encuentras dudando de tus habilidades antes de comenzar una actividad importante?"]

#Culpa(3)-daño(2)-duda(3)
preguntas_ansiedad= ["¿Te encuentras constantemente pensando en un error que cometiste y deseando haber actuado de manera diferente?",
                        "Cuando cometes un error, ¿se ve afectada tu autoestima y a tu percepción sobre ti mismo?",
                        "¿Tienes dificultades para perdonarte a ti mismo después de cometer errores, incluso cuando otros han aceptado tus disculpas o reparaciones?",
                        "Después de un accidente o diagnóstico de una enfermedad, ¿te sientes constantemente preocupado por tu salud física o por sufrir más daño?",
                        "¿Encuentras que tu mente está frecuentemente ocupada con pensamientos sobre posibles futuros problemas de salud o accidentes?",
                        "¿Con frecuencia te cuestionas a ti mismo sobre tu capacidad para manejar tareas cotidianas o desafíos?",
                        "¿Tus dudas sobre tus habilidades te impiden tomar iniciativas o probar nuevas experiencias?",
                        "Cuando enfrentas un fracaso o un retroceso, ¿se ve impactada la creencia en tus propias habilidades?" ]

#evento(2)-rechazo(3)
preguntas_depresion= ["¿Has tenido dificultades para dormir o te sobresaltas fácilmente por un evento que te haya ocurrido?",
                        "¿Te encuentras evitando lugares, personas o actividades que te recuerdan a algun evento traumático?",
                        "¿Te has sentido excluido por las personas con las que compartes frecuentemente?",
                        "¿El miedo al rechazo te impide participar en actividades sociales o nuevas experiencias?",
                        "¿Te afecta emocionalmente cuando sientes que otros te han rechazado o excluido?"]

@csrf_exempt  # Aplicar directamente para funciones de vista
def chat(request):
    dict = {"Stress" : preguntas_estres, 
           "Anxiety" : preguntas_ansiedad, 
           "Depression" : preguntas_depresion}
    
    translateDict = {"Stress" : "Estres", 
           "Anxiety" : "Ansiedad", 
           "Depression" : "Depresión"}

    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data['message']
        u_name = request.session.get('user_name')

        preQuestions=0

        if (diagnosis.objects.filter(user_name = u_name).count() == 0):
            listQuestions=preguntas
        else:
            listQuestions=dict[diagnosis.objects.filter(user_name=u_name).values_list('text', flat=True).first()]
            preQuestions=19

        total_mensajes_usuario = Message.objects.filter(user_name = u_name).count()
        print(total_mensajes_usuario)

        if ( total_mensajes_usuario < (len(listQuestions)-1)+preQuestions):
            question = listQuestions[total_mensajes_usuario - preQuestions]
            next_question = listQuestions[(total_mensajes_usuario +1 ) - preQuestions]
            Message.objects.create(text=user_message, question= question, user_name = u_name, number = total_mensajes_usuario)
        else:
            try:
                question = listQuestions[total_mensajes_usuario-preQuestions]
                Message.objects.create(text=user_message, question= question, user_name = u_name, number = total_mensajes_usuario)

                next_question= ""
                respuestas = list(Message.objects.filter(user_name = u_name).values_list('text', flat=True))

                if (diagnosis.objects.filter(user_name = u_name).count() == 0):

                    answer = processFirstQuestionSet(respuestas)

                    #print(diag)

                    next_question= next_question + "\n Tu condición puede ser: " + translateDict[answer] + ".\n" + dict[answer][0]
                    diagnosis.objects.create(text=answer, user_name = u_name, number =0)

                else:
                    respuestas = list(Message.objects.filter(user_name=u_name, number__gt=18).values_list('text', flat=True))
                    answer = processSecondQuestionSet(respuestas, diagnosis.objects.filter(user_name=u_name).values_list('text', flat=True).first())
                    next_question= [next_question + "\n " + answer]

                    if unde:
                        out=""
                        for i in unde:
                            out+= " " + i
                        next_question.append(out)

                    if low:
                        out=""
                        for i in low:
                            out+= " " + i
                        next_question.append(out)

                    if  influ != "":
                        next_question.append(influ)


                    next_question.append( "Escribe otro mensaje para reiniciar el chat")
                    diagnosis.objects.create(text=answer, user_name = u_name, number =1)

            except:
                next_question = ''
                if (diagnosis.objects.filter(user_name = u_name).count() == 0):
                    next_question= next_question + "\n No pude encontrar una condicion que se asocie a tus problemas actuales, si aun tienes dudas, te recomiendo que busques ayuda psicologica profesional. \n\n"
                Message.objects.filter(user_name = u_name).delete()
                diagnosis.objects.filter(user_name = u_name).delete()
                next_question += preguntas[0] if preguntas else None


        respuestas = list(Message.objects.filter(user_name = u_name).values_list('text', flat=True))

        print(respuestas)


        return JsonResponse({'user_message': user_message, 'bot_message': next_question})
    else:
        introduccion = '''Bienvenid@ al chatbot de ayuda psicologica, a continuación te haré unas preguntas para determinar
        cual es el mejor consejo que puedo darte dependiendo de tu situacion. Ten en cuenta que este chatbot está pensado como
        una primera ayuda y de ninguna manera es comparable con la opinion de un psicologo.
        
        
        '''
        u_name = request.session.get('user_name')

        total_mensajes_usuario = Message.objects.filter(user_name = u_name).count()

        preQuestions=0

        if (diagnosis.objects.filter(user_name = u_name).count() == 0):
            listQuestions=preguntas
        else:
            listQuestions=dict[diagnosis.objects.filter(user_name=u_name).values_list('text', flat=True).first()]
            preQuestions=19     

        messages = Message.objects.all().values('text')
        try:
            pregunta_inicial = [introduccion,listQuestions[total_mensajes_usuario-preQuestions]] if listQuestions else None
        except:
            Message.objects.filter(user_name = u_name).delete()
            diagnosis.objects.filter(user_name = u_name).delete()
            pregunta_inicial = [introduccion,preguntas[0]] if preguntas else None
        return render(request, 'chatbot.html', {'messages': list(messages),'pregunta_inicial': pregunta_inicial, 'name': u_name})
    

def processFirstQuestionSet(list):

    expert_system = MentalHealthHelper()

    questionslist=['Cannot relax','Cannot stand still','Dreadfull','Worried all the time', 'Cannot control worries', 'Irritable', 
                   'Nervous' , 'Upset from unexpected situation', "Hasn't felt things going their way", 'Inability to control things in life',
                    'Overwhelmed','Uninterested', 'Hopeless','Low energy', 'Low concentration', 'Too much/too little apetite', 'Move too slow/too fast',
                    'Too much/too little sleep', 'Self harm thoughts'
                ]
    
    #'Traumatic Events', 'Abusive Relationships', 'Too Much Work', 'Poor resource management', 'Self doubt', 'Phisical injury', 'Guilt','Depression', 'Stress', 'Anxiety',    

    expert_system.trueReset()
    count=0

    #print (expert_system.facts)
    

    for i in list:

        if (i=="si"):

            kwargs = {
            "symptom": questionslist[count],
            }
            expert_system.declare(Fact(**kwargs))

        count+=1

    expert_system.declare(Fact(status='Done'))

    expert_system.run()


    answerList= expert_system.getConds()

    answer= max(answerList, key=lambda x: x[1])

    #print(answer[0])

    print(answerList)

    low=expert_system.getLows()
  
    unde=expert_system.getUnd()
    

    print(low)
    print(unde)

    return answer[0]



def processSecondQuestionSet(list, condition):

    stressdict = {0 : "p1",  #work
           1 : "p1", 
           2: "p1",
           3:"p2", #resources
           4: "p2",
           5:"p2",
           6:"p3", #doubt
           7:"p3",
           8:"p3"}
    
    anxietydict = {0 : "p8",  #guilt
           1 : "p8", 
           2: "p8",
           3:"p4", #injury
           4: "p4",
           5:"p5",#doubt
           6:"p5", 
           7:"p5"}
    
    depressiondict = {0 : "p6",  #envent
           1 : "p6", 
           2: "p7", #reject
           3:"p7", 
           4: "p7"}


    if (condition=="Depression"):
        questionDict= depressiondict
        
    elif (condition=="Anxiety"):
        questionDict= anxietydict

    elif (condition=="Stress"):
        questionDict = stressdict

    expert_system.trueReset()

    expert_system.declare(Fact(Hcond=condition))


    count=0
    questionList=[]

    for i in list:

        if (i=="si"):

            questionList.append(questionDict[count])

        count+=1

    if questionList:

        mostCommonElement, mostCommonCount = mostFrequentElement(questionList)


        #print(mostCommonElement, mostCommonCount)

        for i in mostCommonElement:
            kwargs = {
                    i: mostCommonCount,
                    }
            expert_system.declare(Fact(**kwargs))

        #print (expert_system.facts)

        expert_system.run()

        answerList= expert_system.getAnswers()
        #print(answerList)
        
        answer=""

        if len(answerList) == 0:
            answer='''Lo lamento mucho pero no he podido identificar la causa específica de tu condición. 
            Cada persona es única y, a veces, las razones detrás de estos sentimientos requieren una 
            exploración más profunda de lo que podemos alcanzar en este chat. Te animo a que busques el apoyo de un profesional de la salud mental, 
            como un psicólogo, que pueda ofrecerte una guía más personalizada y efectiva. Es importante cuidar de tu salud mental y 
            gracias por confiar en chatbot-helper.'''
        else:
            for i in answerList:
                answer+=i + '\n\n\n'

        #print(answer)
    else:
        answer='''Lo lamento mucho pero no he podido identificar la causa específica de tu condición. 
            Cada persona es única y, a veces, las razones detrás de estos sentimientos requieren una 
            exploración más profunda de lo que podemos alcanzar en este chat. Te animo a que busques el apoyo de un profesional de la salud mental, 
            como un psicólogo, que pueda ofrecerte una guía más personalizada y efectiva. Es importante cuidar de tu salud mental y 
            gracias por confiar en chatbot-helper.'''
        


    influ= expert_system.getInfluence()
    print(influ)
   
    return answer



def mostFrequentElement(lst):

    counter = Counter(lst)
    max_count = max(counter.values())
    most_common_elements = [elem for elem, count in counter.items() if count == max_count]
    
    return lst, max_count