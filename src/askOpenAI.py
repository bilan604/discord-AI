import openai
import time


import openai
import time
#from dotenv import load_dotenv

#load_dotenv()


async def askOpenAI003(query):

    if type(query) != str:
        query = query.content

    if len(query) == 0:
        return "Empty Query Recieved"
    # Check if a command got passed in
    elif len(query) >= 1 and query[0] == "/":
        print("askOpenAI003(): command passed in as query")
        return ""

    message = "No Response"
    try:
        curr_temp = 0.32
        response = openai.Completion.create(model="text-davinci-003",
                                            prompt=query,
                                            temperature=curr_temp,
                                            max_tokens=1400)
        message = response.choices[0].text
    except Exception as e:
        print("Error on OpenAI API Call:", e)
    return message
