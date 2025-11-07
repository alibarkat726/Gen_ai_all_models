from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from langchain_core.prompts import PromptTemplate,load_prompt



llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm  = llm)
paper_input = 'Attention is All you need'
style_input = 'Code_oriented'
length_input = "short(1-2 paragraph)"
template = load_prompt('template.json')

chain = template | model
result = chain.invoke(
     {
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    }
)
print(result.content)
