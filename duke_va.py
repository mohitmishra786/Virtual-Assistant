import wolframalpha    # To get the access from Wolfram Alpha for searching
import wikipedia       #To get all the access to wikipedia pages access
import PySimpleGUI as sg  # Used to make a popup so that we can search for our query
import pyttsx3        # We are using this for Text To Speech and by the way you can use any other too


#Here in the API ID put your own API id by making at Wolframalpha
client = wolframalpha.Client('API ID')




sg.theme('DarkBlue')    #Add a touch of color as you want

#All the stuff inside your window

layout = [[sg.Text('Search Anything'), sg.InputText()],
          [sg.Button("OK"),sg.Button('Cancel')]]

# Create the window
window = sg.Window("DuKe VA", layout) #Here in place of DuKe VA you can put your own window title as you want

# Create an event loop
# Here we created this loop tto process"events" and get the "values" of the inputs which we want
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event in (None, 'Cancel'):
        break
    engine = pyttsx3.init()
    try:
        wikiPd_res = wikipedia.summary(values[0], sentences=3)
        res = client.query(values[0])
        wolfram_res =next(res.results).text

        engine.say(wolfram_res) #For speaking the result that we will get from wolfram_res
        engine.say(wikiPd_res)  ##For speaking the result that we will get from wikiPd_res
        sg.PopupNonBlocking("Wolfram Alpha Result : "  + wolfram_res ,  "Wikipedia Result: " + wikiPd_res )  # Here we used PopupNonBlocking as we want speech and written text at the same time and if you dont want to listen and read  at the same time then you can use only popup

    except wikipedia.exceptions.DisambiguationError: # This DisambiguationError occurs when you ask any ambiguous Query so for not letting our program crash we will use except Here
        res = client.query(values[0])
        wolfram_res =next(res.results).text
        engine.say(wolfram_res) #For speaking the result that we will get from wolfram_res
        sg.PopupNonBlocking("Wolfram Alpha Result : "  + wolfram_res) # Here we only want the result of Wolframalpha


    except wikipedia.exceptions.PageError:  # This PageError occurs when you ask any Query that doesnt match with any of the pages present in Wikipedia so for not letting our program crash we will use except Here
        res = client.query(values[0])
        wolfram_res =next(res.results).text
        engine.say(wolfram_res) #For speaking the result that we will get from wolfram_res
        sg.PopupNonBlocking("Wolfram Alpha Result : "  + wolfram_res) # Here we only want the result of Wolframalpha

    except :  # We are using this except here as if there will not be any of the match results of our query in the Wolframalpha
        wikiPd_res = wikipedia.summary(values[0], sentences=3)

        engine.say(wikiPd_res)
        sg.PopupNonBlocking( "Wikipedia Result: " + wikiPd_res ) # Here we are only going to get the result of wikipedia



    engine.runAndWait()  # After speaking the text it will terminate automatically
    print(values[0])  # For printing the Query that you asked



window.close()
