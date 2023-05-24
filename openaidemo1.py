import openai


#API Key to connect to API
API_KEY = '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'
openai.api_key = API_KEY

#Giving model to use
model_id = 'gpt-3.5-turbo'

#Function to use libraries.

def chatgpt_conversation(conversation):
    response = openai.ChatCompletion.create(
        model = model_id,
        messages = conversation
    )
    conversation.append({'role' : response.choices[0].message.role, 'content' : response.choices[0].message.content})
    return conversation
   
conversation = []
conversation.append({'role': 'system', 'content': 'Who is the president of the US?'})

conversation = chatgpt_conversation(conversation)
print('Role : {0}; Content: {1}'.format(conversation[-1]['role'], conversation[-1]['content']))

conversation.append({'role': 'user', 'content': 'Who is the first president of the US?'})
conversation = chatgpt_conversation(conversation)

print('Role : {0}; Content: {1}'.format(conversation[-1]['role'], conversation[-1]['content']))


#role -> Input from user or system
# 3 roles : system, assistant, user

