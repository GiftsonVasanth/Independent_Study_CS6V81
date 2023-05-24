import openai


#API Key to connect to API
API_KEY = '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'
openai.api_key = API_KEY

#Giving model to use
model_id = 'gpt-3.5-turbo'

#Function to use libraries.

# def chatgpt_conversation(conversation):
#     response = openai.ChatCompletion.create(
#         model = model_id
#         messages = conversation
#     )

conversation = []
conversation.append({'role': 'system', 'content': 'Who is the president of the US?'})

#role -> Input from user or system
# 3 roles : system, assistant, user

response = openai.ChatCompletion.create(
        model = model_id,
        messages = conversation
    )


#print(response)
print(response.choices[0].message.content)


"""
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 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" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Who is the president of the US? "}],
   }'


"""
