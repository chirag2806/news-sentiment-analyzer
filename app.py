import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from scraper import scrape_text
from sentiment import analyze_sentiment, summarize_text

# ================= PAGE CONFIG =================
st.set_page_config(page_title="News Sentiment AI", layout="wide")

# ================= LIGHT UI =================
st.markdown("""
<style>
body {
    background-color: #F7F9FC;
}
.card {
    background: white;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 0px 2px 12px rgba(0,0,0,0.08);
    text-align: center;
}
.news-card {
    background: white;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 12px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.title("🧠 News Sentiment Intelligence")
st.markdown("AI-powered news analytics dashboard")
st.markdown("---")

# ================= GOOGLE NEWS =================
def fetch_google_news(keyword):
    try:
        url = f"https://news.google.com/rss/search?q={keyword}&hl=en-IN&gl=IN&ceid=IN:en"
        headers = {"User-Agent": "Mozilla/5.0"}

        page = requests.get(url, headers=headers, timeout=10)

        from xml.etree import ElementTree as ET

        root = ET.fromstring(page.content)

        links = []

        for item in root.findall(".//item"):
            link = item.find("link").text
            links.append(link)

        return links[:10]  # limit

    except Exception as e:
        print(e)
        return []

# ================= SIDEBAR =================
st.sidebar.header("⚙️ Controls")

urls_input = st.sidebar.text_area("Paste URLs (comma separated)")
keyword = st.sidebar.text_input("🔍 Filter keyword")
auto_keyword = st.sidebar.text_input("🌍 Auto Fetch News")

fetch_btn = st.sidebar.button("Fetch")
analyze_btn = st.sidebar.button("🚀 Analyze")

urls = []

if fetch_btn and auto_keyword:
    urls = fetch_google_news(auto_keyword)
    st.sidebar.success(f"{len(urls)} articles fetched")

if urls_input:
    urls.extend([u.strip() for u in urls_input.split(",") if u.strip()])

# ================= MAIN =================
if analyze_btn:

    if not urls:
        st.warning("Enter URLs or fetch news")
        st.stop()

    results = []
    failed_urls = []

    progress = st.progress(0)
    status = st.empty()

    total_urls = len(urls)

    for i, url in enumerate(urls):
        status.text(f"Processing {i+1}/{total_urls}")

        text = scrape_text(url)

        if "Error" in text or not text.strip():
            failed_urls.append(url)
            continue

        if keyword and keyword.lower() not in text.lower():
            failed_urls.append(url)
            continue

        label, score = analyze_sentiment(text)
        summary = summarize_text(text)

        results.append({
            "Source": url,
            "Sentiment": label,
            "Confidence": round(score, 3),
            "Summary": summary
        })

        progress.progress((i + 1) / total_urls)

    status.text("✅ Analysis Complete")

    # ================= HANDLE NO RESULTS =================
    if not results:
        st.error("❌ No articles could be analyzed")

        if failed_urls:
            st.subheader("⚠️ Failed URLs")
            for url in failed_urls:
                st.write(url)

        st.stop()

    df = pd.DataFrame(results)
    df["Time"] = pd.date_range(end=pd.Timestamp.now(), periods=len(df))

    # ================= KPI =================
    st.subheader("📊 Overview")

    total = len(urls)
    success = len(results)
    failed = len(failed_urls)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total URLs", total)
    col2.metric("Analyzed", success)
    col3.metric("Failed", failed)
    col4.metric("Success Rate", f"{(success/total)*100:.1f}%")

    st.markdown("---")

    # ================= TABLE =================
    st.dataframe(df, use_container_width=True)

    # ================= FAILED =================
    if failed_urls:
        st.subheader("⚠️ Failed / Skipped Articles")
        for url in failed_urls:
            st.write(f"❌ {url}")

    st.markdown("---")

    # ================= CHARTS =================
    st.subheader("📈 Analytics")

    colA, colB = st.columns(2)

    # DONUT
    with colA:
        fig1, ax1 = plt.subplots(figsize=(4, 4))
        counts = df["Sentiment"].value_counts()

        ax1.pie(
            counts,
            labels=counts.index,
            autopct='%1.1f%%',
            colors=["#22C55E", "#EF4444", "#FACC15"],
            wedgeprops={'width': 0.4}
        )

        plt.tight_layout()
        st.pyplot(fig1)

    # BAR
    with colB:
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        sentiments = df.groupby("Sentiment")["Confidence"].mean()

        ax2.bar(
            sentiments.index,
            sentiments.values,
            color=["#22C55E", "#EF4444", "#FACC15"]
        )

        ax2.set_title("Confidence Analysis")
        plt.tight_layout()

        st.pyplot(fig2)

    # ================= TREND =================
    st.subheader("📊 Trend")

    fig3, ax3 = plt.subplots(figsize=(7, 3))
    df_sorted = df.sort_values("Time")

    ax3.plot(df_sorted["Time"], df_sorted["Confidence"], marker='o')

    plt.xticks(rotation=30)
    plt.tight_layout()

    st.pyplot(fig3)

    st.markdown("---")

    # ================= AI CARDS =================
    st.subheader("🧠 Insights")

    for _, row in df.iterrows():
        st.markdown(f"""
        <div class="news-card">
            <b>{row['Sentiment']}</b> | Confidence: {row['Confidence']} <br><br>
            {row['Summary']}<br><br>
            <a href="{row['Source']}" target="_blank">Read Article</a>
        </div>
        """, unsafe_allow_html=True)

    # ================= DOWNLOAD =================
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Report",
        csv,
        "report.csv",
        "text/csv"
    )