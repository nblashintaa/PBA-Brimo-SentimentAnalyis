import pandas as pd
import re
import string
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

print("Memulai preprocessing data...")

#Load dataset
df = pd.read_csv("brimo_raw_reviews.csv")

#Hapus review kosong
df = df.dropna(subset=['review'])

#Lowercase
df['clean_review'] = df['review'].str.lower()

#Hapus angka & simbol
df['clean_review'] = df['clean_review'].apply(
    lambda x: re.sub(r'[^a-zA-Z\s]', '', x)
)

#Stopword removal
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
df['clean_review'] = df['clean_review'].apply(lambda x: stopword.remove(x))

#Stemming
stem_factory = StemmerFactory()
stemmer = stem_factory.create_stemmer()
df['clean_review'] = df['clean_review'].apply(lambda x: stemmer.stem(x))

#Simpan hasil
df.to_csv("brimo_cleaned_reviews.csv", index=False)

print("Preprocessing selesai!")
print(f"Total data setelah dibersihkan: {len(df)}")
print("File tersimpan sebagai: brimo_cleaned_reviews.csv")