import requests
import json

def getRatings():
    response = requests.get("http://212.101.137.104:8000/ratings")
    ratings = response.json()

    badwords = ['sranje', 'drek']

    for rating in ratings:
        textArr = []
        init = 0
        text = rating["comment"]

        for i, char in enumerate(text):
            if char == ' ' or char == '.' or char == ',' or char == '!' or char == '?' or char == ':' or char == ';':
                if init == 0:
                    textArr.append(text[init : i])
                    init = i          
                else:
                    textArr.append(text[(init + 1) : i])
                    init = i 
            
            elif i == (len(text) - 1):
                textArr.append(text[init : (i + 1)])
                init = i  

        for badword in badwords:
            for word in textArr:
                if word == badword:
                    comment = "Comment was deleted for inappropriateness."

                    id = rating["id"]
                    update = requests.put(f"http://212.101.137.104:8000/rating/update/{id}?comment={comment}") 
                else:
                    update = ratings
    
    return update


def handle(req):
    try:
        ratings = getRatings()
        return json.dumps({"status": "success", "ratings": ratings})
    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)})
