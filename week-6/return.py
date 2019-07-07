# ask a name and a language
# say hello following the language choice

name = input("enter your name: ")
lang = input("choose a language (en, fr or de): ")

def hello (lang):
    if lang == "en":
        return ("goodmorning")
    elif lang == "fr":
        return ("bonjour")
    elif lang == "de":
        return ("Guten Tag")


print (hello(lang),name)