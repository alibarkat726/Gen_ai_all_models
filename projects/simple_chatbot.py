from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm  = llm)

messages = [
    SystemMessage("You are a Genai proffessor"),
    
]


while True:
    
    user_input = input('you: ')
    messages.append(HumanMessage(content=user_input))
    if user_input =='exit':
        break
    result = model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print("Ai: ",result.content)

print (messages)