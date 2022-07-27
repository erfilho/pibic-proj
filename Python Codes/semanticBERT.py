from sentence_transformers import SentenceTransformer
from tqdm import tqdm
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

documents = [
    "Vodafone wins 20.000 Y Crore Tax Arbitration Case Against Government",
    "Voda Idea shares jump nearly 15% as Vodafone wins retro tax case in Hague",
    "Gold prices today fall for 4th time in 5 days, down 6500 Y from last month high",
    "Silver futures slip 0.36% to RS 59.415 per kg, down over 12% this week",
    "Amazon unveils drone that films inside your gome. What could go wrong?",
    "Iphone 12 mini performance mat disappoint due to the apple b14 chip",
    "Delhi Capitals vs Chennai Super Kings: Ptithvi Shaw shines as DC beat CSK to post second consecutive win in IPL",
    "French Open 2020: Rafael Nadal handed touch draw in bid for record-equaling 20th Grand Slam"
]

model = SentenceTransformer('bert-base-nli-mean-tokens')

text_embeddings = model.encode(documents, batch_size = 8, show_progress_bar = True)

np.shape(text_embeddings)

similarity = cosine_similarity(text_embeddings)
print(f'pairwise dense output:\n{similarity}')

sort_similarity = similarity.argsort()

id_1 = []
id_2 = []
score = []

for index, array in enumerate(sort_similarity):
    id_1.append(index)
    id_2.append(array[-2])
    score.append(similarity[index][array[-2]])

index_df = pd.DataFrame({
                        'id_1': id_1,
                        'id_2': id_2,
                        'score': score
                        })