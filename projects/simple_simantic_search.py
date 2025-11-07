from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import numpy as np
load_dotenv()

documnent = [
    "Babar Azam is a great batsman and former captain of Pakistan.",
    "Shaheen Afridi is a fast bowler who swings the new ball beautifully.",
    "Mohammad Rizwan is a hardworking wicketkeeper and consistent opener.",
    "Shadab Khan is an excellent all-rounder and a sharp fielder.",
    "Fakhar Zaman is an aggressive opening batsman with match-winning ability.",
]
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
query = "who is babar azam"

doc_embed = embedding.embed_documents(documnent)
query_embed = embedding.embed_query(query)

scores = cosine_similarity([query_embed],doc_embed)[0]

index,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(query)
print(documnent[index])
print("similarity score : ",score)