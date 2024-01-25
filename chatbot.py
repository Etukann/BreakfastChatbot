import json, re , random
#Some recipies were gathered from https://www.bbc.co.uk/food
#Some of the bot code from https://www.youtube.com/watch?v=azP_d7SiRDg&t=199s&ab_channel=Indently

def json_load(file):
    with open(file) as responses:
        return json.load(responses)

responses_data = json_load("responses.json")

def recieve_response(input_str):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_str.lower())
    percentage_score = []

    for response in responses_data:
        response_score = 0
        score_required = 0
        words_required = response["words_required"]

        if words_required:
            for word in split_message:
                if word in words_required:
                    score_required +=1
        
        if score_required == len(words_required):
            for word in split_message:
                if word in response["input"]:
                    response_score +=1

        percentage_score.append(response_score)

    accurate_response = max(percentage_score)
    response_index = percentage_score.index(accurate_response)
    if input_str == "":
        return "Do you not wanna talk?"
    
    if accurate_response != 0:
        return responses_data[response_index]["responses"]

    else:
        random_ans = ["I'm afraid I don't understand what you mean.", "Sorry, I can't help you with that right now.", "Could you google that becuase I don't understand"]

        list_count = len(random_ans)
        random_item = random.randrange(list_count)

        return random_ans[random_item]

while True:
    user_input = input("You: ")
    print("Bot: ", recieve_response(user_input))
