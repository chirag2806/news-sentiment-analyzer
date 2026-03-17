# 🧠 News Sentiment Intelligence Dashboard

An AI-powered web application that analyzes real-time news articles and determines their sentiment using Natural Language Processing (NLP). Built with Streamlit, this project provides an interactive dashboard for visualizing news sentiment insights.

---

## 🚀 Features

* 🌍 **Auto Fetch News** using Google News RSS
* 🔍 **Keyword Filtering** for targeted analysis
* 🧠 **Sentiment Analysis** using VADER (NLP)
* 📊 **Interactive Dashboard** with charts
* 📈 **Trend Analysis over Time**
* 🧾 **AI-based Article Summaries**
* ⚠️ **Error Handling** for failed/unsupported URLs
* 📥 **Download Results as CSV**

---

## 🖥️ Tech Stack

* **Frontend/UI**: Streamlit
* **Backend**: Python
* **Web Scraping**: BeautifulSoup, Requests
* **NLP**: NLTK (VADER Sentiment Analyzer)
* **Data Handling**: Pandas
* **Visualization**: Matplotlib

---

## 📂 Project Structure

```
news-sentiment-analyzer/
│
├── app.py              # Main Streamlit application
├── scraper.py          # Web scraping logic
├── sentiment.py        # Sentiment analysis & summarization
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/your-username/news-sentiment-analyzer.git
cd news-sentiment-analyzer
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
streamlit run app.py
```

---

## 📊 How It Works

1. User inputs URLs or fetches news automatically
2. Articles are scraped using BeautifulSoup
3. Text is analyzed using VADER sentiment model
4. Results are visualized using charts
5. Users can filter, explore, and download insights

---

## ⚠️ Limitations

* Some websites (e.g., JavaScript-heavy pages) may block scraping
* Works best with static HTML news sources (BBC, CNN, Reuters)
* Sentiment analysis is rule-based (not deep learning)

---

## 💡 Future Improvements

* 🔥 Integrate News API for more reliable data
* 🤖 Upgrade to advanced AI models (BERT)
* 🔐 Add user authentication system
* 📊 Enhance UI with advanced dashboards

---

## 👨‍💻 Author

**Chirag Sindhu**
B.Tech CSE (AI & ML)

---

## 📌 License

This project is for educational and academic purposes.
