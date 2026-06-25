import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Tech Salary Dashboard", layout="wide")
st.title("💻 Tech Salary Analytics Dashboard")
st.markdown("Dashboard Berdasarkan Data Hasil Survei Gaji Di Bidang Teknologi")

@st.cache_data
def load_data():
    return pd.read_csv("hasil_data_tech_salary.csv")
df = load_data()

col1, col2, col3 = st.columns(3)
col1.metric("Total Responden", f"{len(df):,}")
col2.metric("Rata-rata Gaji Tahunan", f"${df['annual_salary_usd'].mean():,.0f}")
col3.metric("Rata-rata Pengalaman", f"{df['experience_years_total'].mean():.1f} Tahun")

st.divider()

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Top 5 Bidang Teknologi (Gaji Tertinggi)", "Rata-rata Gaji vs Pendidikan", "Rata-rata Gaji vs Ukuran Perusahaan", "Top 5 Skill Utama (Gaji Tertinggi)", "Hubungan Pengalaman dan Gaji", "Top 5 Bidang Teknologi (Gaji Terendah)", "Insights & Kesimpulan"])

with tab1:
    st.subheader("1. Top 5 Bidang Teknologi (Gaji Tertinggi)")
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    top_fields = df.groupby('primary_tech_field')['annual_salary_usd'].mean().sort_values(ascending=False).head(5).reset_index()
    sns.barplot(data=top_fields, x='annual_salary_usd', y='primary_tech_field', palette='viridis', ax=ax1)
    ax1.set_xlabel('Gaji (USD)')
    ax1.set_ylabel('')
    st.pyplot(fig1)
    st.text("Blockchain & Web 3 adalah rata rata gaji tahunan dalam bentuk USD tertinggi")
    
with tab2:
    st.subheader("2. Rata-rata Gaji vs Pendidikan")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    order_edu = ["PhD", "Master's Degree", "Bachelor's Degree", "Associate's Degree", "Bootcamp", "High School"]
    edu_salary = df.groupby('education_level')['annual_salary_usd'].mean().reindex(order_edu).reset_index()
    sns.barplot(data=edu_salary, x='annual_salary_usd', y='education_level', palette='magma', ax=ax2)
    ax2.set_xlabel('Gaji (USD)')
    ax2.set_ylabel('')
    st.pyplot(fig2)
    st.text("PhD atau sudah lulus S3 memiliki rata rata gaji tertinggi, membuktikan bahwa pendidikan penting.")

with tab3:
    st.subheader("3. Rata-rata Gaji vs Ukuran Perusahaan")
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    order_comp = ["Startup (1-10)", "Small (11-50)", "Medium (51-200)", "Large (201-1000)", "Enterprise (1000+)"]
    comp_salary = df.groupby('company_size')['annual_salary_usd'].mean().reindex(order_comp).reset_index()
    sns.barplot(data=comp_salary, x='company_size', y='annual_salary_usd', palette='coolwarm', ax=ax3)
    ax3.set_xlabel('Ukuran Perusahaan')
    ax3.set_ylabel('')
    st.pyplot(fig3)
    st.text("Perusahaan startup memiliki rata rata gaji paling kecil dan perusahaan enterprise memiliki rata rata gaji paling besar.")

with tab4:
    st.subheader("4. Top 5 Skill Utama (Gaji Tertinggi)")
    fig4, ax4 = plt.subplots(figsize=(8, 4))
    top_skills = df.groupby('primary_skill')['annual_salary_usd'].mean().sort_values(ascending=False).head(5).reset_index()
    sns.barplot(data=top_skills, x='annual_salary_usd', y='primary_skill', palette='cubehelix', ax=ax4)
    ax4.set_xlabel('Gaji (USD)')
    ax4.set_ylabel('')
    st.pyplot(fig4)
    st.text("IPFS adalah Primary Skill Dengan Gaji tertinggi untuk saat ini")
    st.divider()

with tab5:
    st.subheader("5. Hubungan Pengalaman Kerja dan Gaji Tahunan")
    fig5, ax5 = plt.subplots(figsize=(10, 4))
    sns.regplot(data=df, x='experience_years_total', y='annual_salary_usd',
            scatter_kws={'alpha':0.3, 'color':'#2ca02c'}, line_kws={'color':'red'}, ax=ax5)
    ax5.set_xlabel('Total Pengalaman (Tahun)')
    ax5.set_ylabel('Gaji Tahunan (USD)')
    st.pyplot(fig5)
    st.text("Secara umum, semakin lama pengalaman seseorang, gajinya cenderung naik. Namun, karena angkanya bukan 1.0, ini membuktikan bahwa pengalaman bukan satu-satunya penentu gaji.")
    st.divider()

with tab6:
    st.subheader("6. Top 5 Bidang Teknologi (Gaji Terendah)")
    fig6, ax6 = plt.subplots(figsize=(10, 4))
    lowest_salary_fields = df.groupby('primary_tech_field')['annual_salary_usd'].mean().sort_values(ascending=True).head(5).reset_index()
    sns.barplot(data=lowest_salary_fields, x='annual_salary_usd', y='primary_tech_field', palette='coolwarm', ax=ax6)
    for p in ax6.patches:
        width = p.get_width()
        ax6.text(width + 2000, p.get_y() + p.get_height() / 2.,
            f"${width:,.0f}", ha="left", va="center", color='black', fontweight='bold')
    ax6.set_xlabel('Gaji (USD)')
    ax6.set_ylabel('')
    ax6.set_xlim(0, max(lowest_salary_fields['annual_salary_usd']) * 1.15)
    st.pyplot(fig6)
    st.text("QA & Testing Adalah pekerjaan di bidang teknologi dengan rata rata gaji terendah")
    
with tab7:
    st.subheader("7. Insights & Kesimpulan")
    st.markdown("""
    Ini adalah insight yang saya ambil dari data hasil survei gaji di bidang teknologi. Jika anda ingin memiliki gaji yang sangat tinggi,
    maka anda bisa ambil bidang Blockchain & Web 3, Lalu lulus pendidikan sampai S3, dan melatih terus pengalaman anda. Dan jika anda
    ingin tetap bekerja di bidang teknologi QA & testing memiliki gaji yang palling rendah, Jadi pilihlah bidang teknologi yang sesuai dengan passion anda, karena gaji bukan satu-satunya faktor yang menentukan kebahagiaan dalam bekerja.
    Kesimpulannya, Kita jadi tau mana bidang teknologi yang memiliki gaji tertinggi dan terendah, serta faktor-faktor yang mempengaruhi gaji di bidang teknologi.
    """)