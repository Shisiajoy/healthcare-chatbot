import json                #import json module
import re                 #import regex
import random_responses   #import random responses created
    
#function to load json data used 
def load_json(file):
    with open(file) as bot_responses:
       # print(f"loaded '{file}' successfully!")
        return json.load(bot_responses)


responses_data = load_json("responses.json") #load data into a variable response_data

#print(responses_data)

 #function to get response based on user input
def get_responses(input_string):
    split_message = re.split(r"\s+|[,;?!.-]\s* " , input_string.lower())  #regex patteern from google used to deconstruct the input string with pattern provided
    score_list = []  #initialize an empty list tostore scores for each respose

    for response in responses_data["responses"]:
        response_score = 0  #how many required word are present in json file
        required_words = response["required_words"] #response index at reqiured word
           
           #check if the list of required words is not empty,if empty there are no required words for this response,
        if required_words:   
            for word in split_message:
                if word in required_words:
                    required_score += 1   #required score should match  required words

        if required_score == len(required_words):  #if amount ofitems in required words = required score
            response_score = 0 #reset response_score for each response 
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1 


        score_list.append(response_score)

    best_response = max(score_list)
    response_index = score_list.index(best_response)
    
        #check ifinput string is empty
    if input_string == "":
        return "please type something to chat :) "

    if best_response != 0:
        return responses_data[response_index]["bot_response"]

    #return random_responses.random_string()


#creating the main function
while True:
    user_input = input("you :")
    print ("Bot:" , get_responses(user_input))      #loops creating a chat effect






