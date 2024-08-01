import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la   grabacion
        print("Ya puedes hablar")

        # guardar lo que escuche como audios
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-col")

            # prueba de que pudo ingresar
            print("Dijiste" + pedido)

            # devolver pedido
            return pedido

        # en caso de que  no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("Ups no  entendi")

            # devolver error
            return "Sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("Ups no hay servicio")

            # devolver error
            return "Sigo  esperando"

        # error  inesperado
        except:

            # prueba de que no comprendio el audio
            print("Ups algo ha salido mal")

            # devolver error
            return "Sigo esperando"


transformar_audio_en_texto()