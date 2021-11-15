import pywhatkit as kit
import keyboard as keyb
import time
import pandas as pd

df = pd.read_excel("liste_rats.xlsx", dtype=str)
USERNAME = "Benjamin"
USERNUM = "+33675826399"
WAIT_TIME = 6  # time necessary to achieve connection to wa


def creer_message(rat, somme, message):
    if pd.isnull(message):
        message = """Bonjour, %s. Vous devez actuellement %s € à %s. \nVous êtes prié.e de bien vouloir le rembourser au plus vite. \
\nVous pouvez par exemple lui envoyez un lydia au %s. %s vous remercie d'avance! \nDes rappels vous seront envoyés quotidiennement \
jusqu'à ce que vous lui remboursiez vos dettes, énorme rat que vous êtes.\
\n\n[Message envoyé automatiquement grâce à Morora]""" % (rat, somme, USERNAME, USERNUM, USERNAME)
        return(message)
    else:
        return(str(message) + "\n[Message envoyé automatiquement grâce à Morora]")


def envoie_rappel(rat, num, somme, message):
    message = creer_message(rat, somme, message)
    kit.sendwhatmsg_instantly(num, message, WAIT_TIME, True, 2)


for i, row in df.iterrows():

    print("Message %d.\nNe pas toucher l'ordi pendant %d secondes" %
          (i, WAIT_TIME))
    envoie_rappel(row['Nom'], row['Numéro'], row['Somme due'], row["Message"])
