import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout= 'wide')

# ----- Read Data -----
bank = pd.read_csv('data/BankChurners.csv')


## ----- Row 1 -----
# ----- Summary -----
st.write('# Credit Card Customer Segmentation')
st.write('''Analisis ini bertujuan untuk memanfaatkan data demografi pelanggan dan perilaku belanja untuk mengidentifikasi potensi risiko churn. 
         Dengan memprediksi attrisi pelanggan, perusahaan dapat mengembangkan strategi untuk mempertahankan pelanggan yang berharga dan meminimalkan perputaran pelanggan. 
         Dataset ini mencakup berbagai fitur yang terkait dengan demografi pelanggan dan kebiasaan belanja, 
         yang mencakup faktor-faktor seperti jenis kelamin, status perkawinan, tingkat pendidikan, golongan pendapatan, dan pola belanja.''')

## ----- Row 1.2 -----
### Input Slider Age
input_slider = st.slider(label= 'Select Age Range', 
                                   min_value= bank['Customer_Age'].min(), 
                                   max_value=bank['Customer_Age'].max(), 
                                   value=[26,73]
                                   )

min_slider = input_slider[0]
max_slider = input_slider[1]
# data: bar plot Age of Customer Vs Attrition_Flag 
bank_age = bank[bank['Customer_Age'].between(left=min_slider, right=max_slider)]

age_churn = pd.crosstab(index=bank_age['Customer_Age'],
            columns=bank_age['Attrition_Flag'],
            colnames=[None])

age_churn_melt = age_churn.melt(ignore_index=False, var_name='Attrition_Flag', value_name='num_people')

age_churn_melt = age_churn_melt.reset_index()

# plot: bar plot Age of Customer Vs Attrition_Flag 
plot_age_churn = px.bar(data_frame=age_churn_melt, 
                   x='Customer_Age', y='num_people', 
                   color='Attrition_Flag', barmode='group')

st.write('### Age of Customer Vs Attrition_Flag')
st.plotly_chart(plot_age_churn, use_container_width=True)
st.write('''Usia yang paling umum adalah 44 tahun, dengan 500 pelanggan memiliki usia tersebut, 
         sedangkan usia yang paling jarang adalah 67, 66, 68, 70, dan 73 tahun, masing-masing dengan hanya 1 pelanggan. 
         Usia dengan frekuensi tertinggi adalah antara 42 dan 54 tahun, dengan frekuensi menurun seiring bertambah atau berkurangnya usia dari rentang tersebut. 
         Usia dengan frekuensi terendah adalah di bawah 30 tahun dan di atas 65 tahun''')
st.write('''Insights yang dapat diperoleh untuk analisis data churn pelanggan berdasarkan usia:

Churn Rate menurut Usia Pelanggan:

- Terdapat perbedaan churn rate (tingkat berhenti berlangganan) menurut usia pelanggan.
- Plot menunjukkan distribusi churn rate pelanggan yang berbeda untuk kategori "Attrited Customer" (pelanggan yang berhenti berlangganan) dan "Existing Customer" (pelanggan yang masih berlangganan) di setiap kelompok usia.
- Secara umum, plot ini menunjukkan bahwa churn rate cenderung lebih tinggi pada pelanggan berusia 30-40 tahun dan 60-70 tahun.
- Secara umum, plot ini menunjukkan bahwa pelanggan dengan usia 40-55 tahun cenderung lebih loyal.

Implikasi untuk Analisis Data Churn:

Informasi mengenai churn rate pelanggan menurut usia dapat berguna untuk berbagai analisis data churn, seperti:

- Strategi Retensi Pelanggan: Mencegah churn rate yang tinggi pada kelompok usia tertentu dengan program atau penawaran khusus yang sesuai dengan kebutuhan mereka. Contohnya, program khusus untuk pelanggan berusia di atas 60 tahun yang mungkin membutuhkan layanan yang lebih mudah digunakan.
- Peningkatan Produk atau Layanan: Memahami alasan churn dari kelompok usia tertentu dapat membantu dalam perbaikan produk atau layanan yang sesuai dengan kebutuhan pelanggan.
- Kampanye Pemasaran Tertarget: Mengelompokkan calon pelanggan dan pelanggan berdasarkan usia untuk kampanye pemasaran yang lebih tertarget.''')


## ----- Row 2 -----
# ----- Visualization -----
col1, col2 = st.columns(2)

# data: bar plot Existing Customer VS. Attrited Customer
df_churn = pd.crosstab(index=bank.Attrition_Flag, columns="num_people", colnames=[None]) 

df_churn = df_churn.reset_index()

# plot: bar plot Existing Customer VS. Attrited Customer

# Define a dictionary mapping attrition flag to colors
color_dict = {'Attrited Customer': '#97a9c4', 'Existing Customer': '#2f5da8'}

plot_churn = px.bar(data_frame=df_churn, x = 'Attrition_Flag', y='num_people',
                    labels={'Attrition_Flag': 'Attrition Flag',
                            'num_people':'Customer Count'})

col1.write('### Existing Customer VS. Attrited Customer')
col1.plotly_chart(plot_churn, use_container_width=True)
col1.write('Terdapat 8500 pelanggan yang "existing" dan 1627 pelanggan yang "attrited". Kolom Attrition_Flag memberikan jumlah pelanggan di setiap kategori')


# data: bar plot Gender of Customer Vs Attrition_Flag  
gender_churn = pd.crosstab(index=bank['Gender'],
                           columns=bank['Attrition_Flag'],
                           colnames=[None])

gender_churn_melt = gender_churn.melt(ignore_index=False, var_name='Attrition_Flag', value_name='num_people')

gender_churn_melt = gender_churn_melt.reset_index()

# plot: bar plot Gender of Customer Vs Attrition_Flag  
#color_dict = {'M': '#97a9c4', 'F': '#2f5da8'}

plot_gender_churn = px.bar(data_frame=gender_churn_melt.sort_values(by='num_people'), 
                           x='num_people', y='Attrition_Flag', 
                           color='Gender', barmode='group' #,color_discrete_map=color_dict
                           )

col2.write('### Gender of Customer Vs Attrition_Flag')
col2.plotly_chart(plot_gender_churn, use_container_width=True)
col2.write('''Data menunjukkan bahwa 5358 pelanggan gender Female "F" dan 4769 pelanggan gender Male "M". Dari 
           semua kedua gender churn rate, "Female" memiliki jumlah pelanggan tertinggi, dan "Male" memiliki jumlah terendah.
           Plot menunjukkan bahwa Female memiliki churn rate yang lebih tinggi dibandingkan Male. 
           Hal ini perlu dipertimbangkan dalam analisis churn rate dan strategi untuk menguranginya. 
           Dan plot menunjukkan bahwa segmentasi pelanggan berdasarkan gender dapat bermanfaat dalam memahami dan menargetkan strategi pemasaran dan retensi pelanggan.''')


## ----- Row 3 -----
st.divider()
col3, col4 = st.columns(2)

### BarPlot
# data: barplot Marital Status Vs Attrition_Flag
marital_churn = pd.crosstab(index=bank['Marital_Status'],
                           columns=bank['Attrition_Flag'],
                           colnames=[None])

marital_churn_melt = marital_churn.melt(ignore_index=False, var_name='Attrition_Flag', value_name='num_people')

marital_churn_melt = marital_churn_melt.reset_index()

# plot: barplot Marital Status Vs Attrition_Flag
plot_marital_churn = px.bar(data_frame=marital_churn_melt.sort_values(by='num_people'), 
                            x='num_people', y='Marital_Status', 
                            color='Attrition_Flag', barmode='group' #,color_discrete_map=color_dict
                            )

col3.write('### Marital Status Vs Attrition_Flag')
col3.plotly_chart(plot_marital_churn, use_container_width=True)
col3.write('''Data menunjukkan bahwa 4687 pelanggan berstatus "married", 3943 berstatus "single", 749 tidak "unknown", dan 748 berstatus "divorced". 
           Dari semua status pernikahan, "Married" memiliki jumlah pelanggan tertinggi, dan "Divorced" memiliki jumlah terendah.
           Plot menunjukkan bahwa orang yang "Single" memiliki churn rate yang lebih tinggi dibandingkan dengan orang yang "Married" dan "Divorced." 
           Hal ini perlu dipertimbangkan dalam analisis churn rate dan strategi untuk menguranginya. 
           Dan plot menunjukkan bahwa segmentasi pelanggan berdasarkan status pernikahan dapat bermanfaat dalam memahami dan menargetkan strategi pemasaran dan retensi pelanggan.''')

### Multivariate
# data: barplot Type of Card Vs Attrition_Flag 
card_churn = pd.crosstab(index=bank['Card_Category'],
                        columns=bank['Attrition_Flag'],
                        colnames=[None])

card_churn_melt = card_churn.melt(ignore_index=False, var_name='Attrition_Flag', value_name='num_people')

card_churn_melt = card_churn_melt.reset_index()

# plot: barplot Type of Card Vs Attrition_Flag 
plot_card_churn = px.bar(data_frame=card_churn_melt.sort_values(by='num_people'), 
                        x='num_people', y='Card_Category', 
                        color='Attrition_Flag', barmode='group' #,color_discrete_map=color_dict
                        )

col4.write('### Type of Card Vs Attrition_Flag')
col4.plotly_chart(plot_card_churn, use_container_width=True)
col4.write('''Plot menunjukkan bahwa terdapat perbedaan distribusi kategori kartu pada kategori "Attrited Customer" dan "Existing Customer." 
           Orang dengan kategori "Blue Attrited Customer" dan "Silver Attrited Customer" memiliki churn rate yang lebih tinggi dibandingkan dengan orang dengan kategori "Blue Existing Customer" 
           dan "Platinum Existing Customer." Informasi ini dapat membantu dalam analisis data terkait churn rate dan customer segmentation.''')



## ----- Row 4 -----

### BarPlot
# data: barplot Customer Education level Vs Attrition Flag 
edu_churn = pd.crosstab(index=bank['Education_Level'],
                           columns=bank['Attrition_Flag'],
                           colnames=[None])

edu_churn_melt = edu_churn.melt(ignore_index=False, var_name='Attrition_Flag', value_name='num_people')

edu_churn_melt = edu_churn_melt.reset_index()

# plot: barplot Customer Education level Vs Attrition Flag 
plot_edu_churn = px.bar(data_frame=edu_churn_melt.sort_values(by='num_people',ascending=False), 
                        x='Education_Level', y='num_people', 
                        color='Attrition_Flag', barmode='group'#,color_discrete_map=color_dict
                        )

st.write('### Customer Education level Vs Attrition Flag ')
st.plotly_chart(plot_edu_churn, use_container_width=True)
st.write('''Plot menunjukkan bahwa orang dengan pendidikan "Post-graduate" dan "Doctorate" memiliki churn rate yang lebih tinggi dibandingkan dengan orang dengan pendidikan "College" dan "Educated." 
           Hal ini perlu dipertimbangkan dalam analisis churn rate dan strategi untuk menguranginya. 
           Dan plot menunjukkan bahwa segmentasi pelanggan berdasarkan pendidikan dapat bermanfaat dalam memahami dan menargetkan strategi pemasaran dan retensi pelanggan.''')

### Multivariate
# data: barplot Customer Education level Vs Attrition Flag 

# plot: barplot Customer Education level Vs Attrition Flag 


# col2.write('''Data''')

## ----- Row 5 -----
# col7, col8 = st.columns(2)

# data: barplot 
income_churn = pd.crosstab(index=bank['Income_Category'],
                        columns=bank['Attrition_Flag'],
                        colnames=[None])

income_churn_melt = income_churn.melt(ignore_index=False, var_name='Attrition_Flag', value_name='num_people')

income_churn_melt = income_churn_melt.reset_index()

# plot: barplot 
plot_income_churn = px.bar(data_frame=income_churn_melt.sort_values(by='num_people',ascending=False), 
                        x='Income_Category', y='num_people', 
                        color='Attrition_Flag', barmode='group' #,color_discrete_map=color_dict
                        )

st.write('### Type of Card Vs Attrition_Flag')
st.plotly_chart(plot_income_churn, use_container_width=True)
st.write('''Plot menunjukkan bahwa orang dengan gaji di bawah 40K dan di atas 120K memiliki churn rate yang lebih tinggi 
         dibandingkan dengan orang dengan gaji antara 40K dan 120K. 
         Hal ini perlu dipertimbangkan dalam analisis churn rate dan strategi untuk menguranginya.
         Dan plot menunjukkan bahwa segmentasi pelanggan berdasarkan gaji dapat bermanfaat dalam memahami 
         dan menargetkan strategi pemasaran dan retensi pelanggan.''')


## ----- Row 6 -----
# data: barplot 
creditLimit_sorted = pd.crosstab(index=bank.Credit_Limit, columns="count", colnames=[None]) 

creditLimit_sorted = creditLimit_sorted.reset_index()

# plot: barplot 
plot_credit_limit = px.histogram(creditLimit_sorted, x="Credit_Limit", y="count")

st.write('### Distribution of Credit Limit')
st.plotly_chart(plot_credit_limit, use_container_width=True)
st.write('''Plot menunjukkan distribusi kredit limit nasabah. Sebagian besar nasabah memiliki kredit limit yang berada di rentang nilai tertentu. Plot histogram ini tidak bisa secara langsung menunjukkan apakah kredit limit yang diberikan sudah sesuai atau belum. Analisis lebih lanjut diperlukan untuk mengetahui apakah kredit limit yang diberikan sesuai dengan kemampuan finansial nasabah dan riwayat kreditnya.

Informasi mengenai distribusi kredit limit nasabah dapat berguna untuk berbagai analisis data kredit, seperti:

- Analisis Risiko Kredit: Memahami distribusi kredit limit dapat membantu bank menilai risiko kredit secara keseluruhan. Kredit limit yang terlalu tinggi untuk nasabah tertentu dapat meningkatkan risiko kredit macet.
- Strategi Penetapan Kredit Limit: Bank dapat menggunakan informasi ini untuk membuat strategi penetapan kredit limit yang lebih baik, dengan mempertimbangkan karakteristik nasabah dan profil risiko kredit.
- Produk Kredit: Bank dapat mengembangkan produk kredit yang lebih sesuai dengan kebutuhan nasabah dengan segmentasi berdasarkan kredit limit.''')

## ----- Row 7 -----

# data: Total Revolving Balance vs. Average Open To Buy 

# plot: Total Revolving Balance vs. Average Open To Buy
plot_scatter = px.scatter(bank, x="Total_Revolving_Bal", y="Avg_Open_To_Buy") 

st.write('### Total Revolving Balance vs. Average Open To Buy')
st.plotly_chart(plot_scatter, use_container_width=True)
st.write('''Plot menunjukkan hubungan antara total revolving balance (sisa pinjaman) dan average open to buy ratio (rata-rata rasio kredit yang tersedia) untuk setiap nasabah. Karena tidak ada korelasi yang jelas, hubungan antara total revolving balance dan average open to buy ratio sulit ditentukan. Nasabah dengan total revolving balance yang tinggi bisa memiliki average open to buy ratio yang tinggi atau rendah, begitu juga sebaliknya.

Meskipun tidak ada korelasi yang jelas, ada beberapa kemungkinan interpretasi yang bisa dipertimbangkan:

- Nasabah dengan Utilization Rate Tinggi: Nasabah yang menggunakan sebagian besar kredit yang tersedia (high utilization rate) mungkin memiliki total revolving balance yang tinggi dan average open to buy ratio yang rendah.
- Nasabah dengan Kebiasaan Bayar yang Baik: Nasabah dengan kebiasaan membayar kredit yang baik mungkin memiliki total revolving balance yang bervariasi dan tetap memiliki average open to buy ratio yang tinggi karena bank memberi mereka kredit limit yang lebih besar.''')