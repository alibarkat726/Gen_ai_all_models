from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


document = [
    "hello how are you",
    "pakistan is abeautifull country",
    "i am a university student"
]
embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
result = embedding.embed_documents(document)
print(str(result))