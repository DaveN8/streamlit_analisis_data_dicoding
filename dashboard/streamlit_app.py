import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Membaca dataset
df1 = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv')
df2 = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Changping_20130301-20170228.csv')
df3 = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Dingling_20130301-20170228.csv')
df4 = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Dongsi_20130301-20170228.csv')
df5 = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Guanyuan_20130301-20170228.csv')
df6 = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Gucheng_20130301-20170228.csv')
df7 = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Huairou_20130301-20170228.csv')
df8 = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Nongzhanguan_20130301-20170228.csv')
df9 = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Shunyi_20130301-20170228.csv')
df10 = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Tiantan_20130301-20170228.csv')
df11 = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Wanliu_20130301-20170228.csv')
df12 = pd.read_csv('PRSA_Data_20130301-20170228/PRSA_Data_Wanshouxigong_20130301-20170228.csv')

# Menyatukan dataset
new_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12], axis=0, ignore_index=True)

# Menghapus data yang memiliki nilai null
new_df = new_df.dropna()

## Dashboard sederhana
st.title('Dashboard Sederhana Kualitas Udara')

st.subheader('Pertanyaan 1')

st.subheader('Distribusi Polutan Udara')
# Buat plot
fig1, ax1 = plt.subplots(figsize=(16, 8))
ax1.hist(new_df['PM2.5'], bins=50, alpha=0.5, label='PM2.5')
ax1.hist(new_df['PM10'], bins=50, alpha=0.5, label='PM10')
ax1.hist(new_df['SO2'], bins=50, alpha=0.5, label='SO2')
ax1.hist(new_df['NO2'], bins=50, alpha=0.5, label='NO2')
ax1.hist(new_df['CO'], bins=50, alpha=0.5, label='CO')
ax1.hist(new_df['O3'], bins=50, alpha=0.5, label='O3')
ax1.set_xlabel('Nilai dari Polutan Udara')
ax1.set_ylabel('Frekuensi Kemunculan')

# Tampilkan plot di Streamlit
st.pyplot(fig1)

st.subheader('Pertanyaan 2')

st.subheader('Perubahan Kualitas Udara')
# Buat plot
fig2, ax2 = plt.subplots(figsize=(16, 8))
ax2.hist(new_df['year'], bins=50, alpha=0.5, label='PM2.5')
ax2.hist(new_df['year'], bins=50, alpha=0.5, label='PM10')
ax2.hist(new_df['year'], bins=50, alpha=0.5, label='SO2')
ax2.hist(new_df['year'], bins=50, alpha=0.5, label='NO2')
ax2.hist(new_df['year'], bins=50, alpha=0.5, label='CO')
ax2.hist(new_df['year'], bins=50, alpha=0.5, label='O3')
ax2.set_xlabel('Tahun')
ax2.set_ylabel('Kualitas Udara')

st.pyplot(fig2)