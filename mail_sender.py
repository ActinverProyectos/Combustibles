#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 


# In[ ]:


def send_mail(destinatario_ : str):

    # Iniciamos los parámetros del script
    remitente = 'actinverdc@gmail.com'
    destinatarios = [destinatario_]
    asunto = 'Información de gasolinas diarias'
    cuerpo = ''
    ruta_adjunto = 'D:\\ACTINVER\\Proyectos actinver\\Z Info Combustibles\\InfoGas.csv'
    nombre_adjunto = 'InfoGas.csv'

    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()

    # Establecemos los atributos del mensaje
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto

    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Abrimos el archivo que vamos a adjuntar
    archivo_adjunto = open(ruta_adjunto, 'rb')

    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    mensaje.attach(adjunto_MIME)

    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)

    # Ciframos la conexión
    sesion_smtp.starttls()

    # Iniciamos sesión en el servidor
    sesion_smtp.login('actinverdc@gmail.com','Actinver2021')

    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()

    # Enviamos el mensaje
    sesion_smtp.sendmail(remitente, destinatarios, texto)

    # Cerramos la conexión
    sesion_smtp.quit()


# In[ ]:


#Aklgoritmo de implementacion
#Guardar el archivo en el mismo directorio
#extraer fdatos y actualizar el archivo
#Leer el archivo desde el mismo directorio
#Enviar archivo
#Agregar como titulo al fecha y tambien en el cuerpo del correo
#Cambiar el correo 

