import json
import requests

response = requests.get("http://numbersapi.com/42?json")

trivia = json.loads(response.content)

print(trivia)
print("\n")

print(type(trivia))
print("\n")

print(trivia["text"])
print("\n")

print(trivia["number"])
print("\n")

print(trivia)

""" 
1. What type is the “response” variable? How could you find out?
Ans: "dict" , print(type(trivia))

2. how we might just print the text of the trivia.
Ans: print(trivia["text"])

3. how we might print just the number of the trivia.
Ans: print(trivia["number"])

4. how we might do this for random trivia
Ans: response = requests.get("http://numbersapi.com/random?json") 

5. how we might print only the text, without the number, of the trivia """