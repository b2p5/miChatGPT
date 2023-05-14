# miChatGPT

## Creación de un ChatBot de ChatGPT con temática personal  

### Descripción

Mediante este programa podrá generar un ChatBot que conteste a las preguntas sobre un tema particular. 
Para conseguir esto es necesario que modifique el fichero **miContexto.txt** aportando información sobre el tema 
que quiera tratar, dicha información servirá para decirle a ChatGPT cual es el roll de su sistema ( cual es el foco
de su conocimiento ).

### Instalación

* Descargue el programa
* Darse de alta en OpenAI y consiga una API_KEY en la página de OpenAI: 
    * <code> https://platform.openai.com/account/api-keys </code> 
* Grabar dicha clave en el fichero .env 

* Este programa corre en Python y necesita instalar las siguientes librerías:
    * openai
    * flask
    * markdown
    * dotenv
    * os

* Ejecute main.py  

    * <code> python main.py </code> 

* Abrir la dirección de enlace que proporciona Flask ( http://127.0.0.1/5559 )


Debe aparecerle la siguiente pantalla en el navegador:

![Pantalla principal de miChatGPT](https://github.com/b2p5/miChatGPT/blob/master/static/images/PantallaChatAgramDAO.png)


### Funcionamiento

Este Bot, con cada pregunta, en primer lugar tratará de resolverla mediante el contexto que le damos en el fichero
**miContexto.txt**, si no encuentra la respuesta dentro del mismo irá a buscar en ChatGPT.

Los cuatro iconos que aparecen debajo de la línea de texto proporcionan funcionalidades particulares para AgramDAO:
* Diagrama de bloques de AgramDAO
* Vídeo sobre el funcionamiento deAgramDAO
* Ir a la Web de AgramDAO
* Descargar todas las consultas que se han realizado.   


