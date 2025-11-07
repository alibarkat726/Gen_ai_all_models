from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


chat_template = ChatPromptTemplate([
    ("system","you are a helpfull customer support agent"),
    MessagesPlaceholder('chat_history'),
    ('human','{query}')
])
chat_history=[]
with open('history.txt') as f:
    chat_history.append(f.readlines())

print(chat_history)

prompt = chat_template.invoke({'chat_history':chat_history,'query':"where is my refund"})
print(prompt)