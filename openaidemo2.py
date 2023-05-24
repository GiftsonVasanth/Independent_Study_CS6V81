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
conversation.append({'role': 'system', 'content': 'How may I help you?'})

conversation = chatgpt_conversation(conversation)
print(' {0} :  {1}'.format(conversation[-1]['role'], conversation[-1]['content']))

while True:
    prompt = input('User:')
    conversation.append({'role': 'user', 
                         'content' : prompt
                         })
    conversation = chatgpt_conversation(conversation)
    print(' {0} :  {1}'.format(conversation[-1]['role'], conversation[-1]['content']))




#role -> Input from user or system
# 3 roles : system, assistant, user

#database.



