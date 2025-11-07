from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage


chat_template = ChatPromptTemplate(
    [
        ('system',"you are a {domain} expert"),
        ('human',"Explain in simple terms ,what is {topic}")
        # SystemMessage(content="you are a {domain} expert"),
        # HumanMessage(content = "Explain in simple terms ,what is {topic}") 
    ]
)
prompt = chat_template.invoke({'domain':'cricket','topic':'spinner'})

