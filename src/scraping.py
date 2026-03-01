from google_play_scraper import reviews, Sort
import pandas as pd

app_id = 'id.co.bri.brimo'

print("Sedang mengambil data review BRImo...")

result, continuation_token = reviews(
    app_id,
    lang='id',        # Bahasa Indonesia
    country='id',     # Negara Indonesia
    sort=Sort.NEWEST, # Urutkan terbaru
    count=1000        # Jumlah review yang diambil
)

df = pd.DataFrame(result)

df = df[['userName', 'score', 'content', 'at']]

df.columns = ['user', 'rating', 'review', 'date']

df.to_csv('brimo_raw_reviews.csv', index=False)

print("Scraping selesai!")
print(f"Total data yang berhasil diambil: {len(df)} review")
print("File tersimpan sebagai: brimo_raw_reviews.csv")