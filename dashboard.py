import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data_day():
    day_df = pd.read_csv("Bike-sharing-dataset/day.csv")
    return day_df

def load_data_hour():
    hour_df = pd.read_csv("Bike-sharing-dataset/hour.csv")
    return hour_df

def create_by_season(df):
    return day_df.groupby(by="season").cnt.nunique().reset_index()


day_df = load_data_day()
hour_df = load_data_hour()

#TITLE
st.title('Bike Sharing Dashboard :sparkles:')

col1, col2 = st.columns(2)

#Menampilkan dataset
with col1:
  st.write('Daily')
  st.write(day_df.head())

with col2:
  st.write('Hourly')
  st.write(hour_df.head())

#Menampilkan informasi tentang jumlah rental sepeda berdasarkan musim
st.subheader("Rent's Number Based On Season")

fig, ax = plt.subplots(figsize=(16,8))
sns.barplot(data=day_df, x=day_df['season'], y=day_df['cnt'])
ax.set_xlabel("Season")
ax.set_ylabel("Count")
ax.set_title("The Number of Rent Based on Season")

st.pyplot(fig)

#Menampilkan Hubungan Antara Temperatur terhadap Jumlah Rental Sepeda
st.subheader("The Correlation Between Temperature and The Rent's Number")

fig, ax = plt.subplots(figsize=(16,8))
sns.scatterplot(data=day_df, x=day_df['temp'], y=day_df['cnt'])
sns.regplot(data=day_df, x=day_df['temp'], y=day_df['cnt'])
ax.set_xlabel("Temperature")
ax.set_ylabel("Count")
ax.set_title("The Correlation Between Temperature and The Rent's Number")

st.pyplot(fig)

#Menampilkan jumlah rental sepeda berdasarkan bulan
st.subheader("The Monthly Performance of Bike's Rent")

count_based_on_month = day_df.groupby(by="mnth").cnt.nunique()
fig, ax = plt.subplots(figsize=(16,8))
plt.plot(count_based_on_month)
ax.set_xlabel("Month")
ax.set_ylabel("Count")
ax.set_title("Monthly Performance of Bike's Rent")
ax.set_xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

st.pyplot(fig)


