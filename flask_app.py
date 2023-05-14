from flask import Flask, render_template,request, render_template_string, make_response
import openai
import os
import  markdown2
#from dotenv import load_dotenv, find_dotenv

# Lee local .env 
#_ = load_dotenv(find_dotenv()) 
openai.api_key  = "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"


# Abrir el archivo de miContexto y leerlo
miContexto = ''
try:
    with open('miContexto.txt', encoding='utf-8') as file:
        miContexto = file.read()
except FileNotFoundError:
    print('Error: El archivo miContexto.txt no se encuentra en el sistema de archivos.' )
    exit
#Añadimos miContexto al rol de sistema
context     = []
context     = [ {'role':'system', 'content': miContexto  } ]
conversations   = [] 

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.form['question']:
        #leemos la pregunta
        question =  request.form['question']
        
        context.append({'role':'user', 'content':f"{question}"})

        #Obtenemos la respuesta
        answer = (( get_completion_from_messages(context)))

        #Pasar respuesta Markdown a HTML
        answer_md = (markdown2.markdown( answer ))
        #print (answer_md)

        context.append({'role':'assistant', 'content': f"{answer_md}" })

        conversations.insert(0,{'tipo':0 , 'mostrar':answer_md})
        conversations.insert(0,{'tipo':1 , 'mostrar':question})

        return render_template('index.html', chat = conversations)
    
    else:
        return render_template('index.html')


@app.route('/diagrama', methods=['GET', 'POST'])
def diagrama():
    question = 'Diagrama de AgramDAO'
    context.append({'role':'user', 'content':f"{question}"})

    answer = "<a href='https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&layers=1&nav=1&title=ArbolFuncionesAgramDAO.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1fERRLli8_aIOAn4kBkJ-2koZAUTFuUTq%26export%3Ddownload' target='_blank'>Enlace al diagrama de bloques de AgramDAO: </a>\n"
    context.append({'role':'assistant', 'content': f"{answer}" })

    conversations.insert(0,{'tipo':0 , 'mostrar':answer})
    conversations.insert(0,{'tipo':1 , 'mostrar':question})    

    return render_template('index.html', chat = conversations)


@app.route('/video', methods=['GET', 'POST'])
def video():
    question = 'Vídeo sobre AgramDAO'
    context.append({'role':'user', 'content':f"{question}"})

    answer = "<a href='https://www.canva.com/design/DAFg6DXbMJc/wPAWPjxptgKjEzP6OeI-AA/watch?utm_content=DAFg6DXbMJc&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink' target='_blank'>Enlace al video explicando que es AgramDAO: </a>\n"
    context.append({'role':'assistant', 'content': f"{answer}" })

    conversations.insert(0,{'tipo':0 , 'mostrar':answer})
    conversations.insert(0,{'tipo':1 , 'mostrar':question})  

    return render_template('index.html', chat = conversations)

@app.route('/descargar', methods=['GET', 'POST'])
def descargar():
    textoHTML = ''
    for linea in conversations:
        textoHTML += linea['mostrar']
        if  linea['tipo'] == 0:
           textoHTML += '<hr>' 

    # Crear una respuesta con el contenido HTML
    respuesta = make_response(textoHTML)
    respuesta.headers['Content-Disposition'] = 'attachment; filename=miConsultaAgramDAO.html'
    respuesta.headers['Content-Type'] = 'text/html'

    return respuesta  


#Llamada a ChatGPT
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0.2):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
    )
    return response.choices[0].message["content"]


if __name__ == '__main__':

    # Abrir el archivo de miContexto y leerlo
    miContexto = ''
    try:
        with open('miContexto.txt', encoding='utf-8') as file:
            miContexto = file.read()

    except FileNotFoundError:
        print('Error: El archivo miContexto.txt no se encuentra en el sistema de archivos.' )
        exit

    #Añadimos miContexto al rol de sistema
    context     = []
    context     = [ {'role':'system', 'content': miContexto  } ]
    
    conversations   = []  
    
    app.run( port=5559 )