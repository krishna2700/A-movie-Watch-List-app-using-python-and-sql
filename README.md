# मूवी वॉचलिस्ट ऐप

यह एक कमांड-लाइन आधारित मूवी वॉचलिस्ट एप्लिकेशन है जो Python और SQLite पर बना है। इससे आप फिल्मों को ट्रैक कर सकते हैं, यूज़र्स मैनेज कर सकते हैं, और यह रिकॉर्ड रख सकते हैं कि आपने कौन-सी फिल्में देखीं।

## फीचर्स

- **फिल्म जोड़ें** — रिलीज़ डेट के साथ नई फिल्म स्टोर करें
- **आगामी फिल्में देखें** — भविष्य की रिलीज़ डेट वाली फिल्मों की सूची देखें
- **सभी फिल्में देखें** — पूरी मूवी कैटलॉग ब्राउज़ करें
- **देखी गई फिल्में मार्क करें** — किस यूज़र ने कौन-सी फिल्म देखी, ट्रैक करें
- **यूज़र मैनेजमेंट** — नए यूज़र जोड़ें
- **खोज** — आंशिक शीर्षक से फिल्म खोजें

## आवश्यकताएँ

- Python 3.8+ (क्योंकि `app.py` में `:=` ऑपरेटर का उपयोग है)

कोई बाहरी डिपेंडेंसी नहीं चाहिए। ऐप Python के बिल्ट-इन `sqlite3` मॉड्यूल का उपयोग करता है।

## शुरू करें

1. **रिपॉजिटरी क्लोन करें**

   ```bash
   git clone <repository-url>
   cd A-movie-Watch-List-app-using-python-and-sql
   ```

2. **ऐप चलाएँ**

   ```bash
   python3 app.py
   ```

   पहली बार रन पर `data.db` फाइल अपने आप बन जाती है।

## उपयोग

ऐप शुरू करने पर आपको यह इंटरैक्टिव मेन्यू दिखेगा:

```
Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.
```

| विकल्प | विवरण |
|--------|-------|
| **1** | फिल्म का शीर्षक और रिलीज़ डेट (`dd-mm-YYYY`) देकर नई फिल्म जोड़ें। अगर तारीख खाली है तो आज की तारीख ली जाएगी। |
| **2** | भविष्य में रिलीज़ होने वाली फिल्मों की सूची देखें। |
| **3** | डेटाबेस में मौजूद सभी फिल्मों की सूची देखें। |
| **4** | यूज़रनेम और मूवी ID देकर फिल्म को वॉच्ड मार्क करें। |
| **5** | किसी यूज़र द्वारा देखी गई फिल्मों की सूची देखें। |
| **6** | नया यूज़र रजिस्टर करें। |
| **7** | आंशिक शीर्षक से फिल्म खोजें। |
| **8** | ऐप से बाहर निकलें। |

## डेटाबेस स्कीमा

ऐप `data.db` में तीन टेबल बनाता है:

### `movies`

| कॉलम | टाइप | विवरण |
|------|------|-------|
| `id` | INTEGER (PK) | ऑटो-इन्क्रिमेंट मूवी ID |
| `title` | TEXT | फिल्म का शीर्षक |
| `release_timestamp` | REAL | रिलीज़ डेट (Unix टाइमस्टैम्प) |

### `users`

| कॉलम | टाइप | विवरण |
|------|------|-------|
| `username` | TEXT (PK) | यूनिक यूज़रनेम |

### `watched`

| कॉलम | टाइप | विवरण |
|------|------|-------|
| `user_username` | TEXT (FK → users) | देखने वाले यूज़र का नाम |
| `movie_id` | INTEGER (FK → movies) | देखी गई फिल्म की ID |

आने वाली फिल्मों के लिए `movies.release_timestamp` पर `movies_release_idx` इंडेक्स बनाया जाता है।

## प्रोजेक्ट स्ट्रक्चर

```
.
├── app.py          # CLI इंटरफेस और मेन्यू लॉजिक
├── database.py     # SQLite क्वेरी और कनेक्शन
├── data.db         # SQLite डेटाबेस (ऑटो-क्रिएटेड)
└── README.md
```

## उदाहरण सत्र

```
Welcome to the watchlist app!

Please select one of the following options:
...
Your selection: 6
Username: alice

Your selection: 1
Movie title: Inception
Release date (dd-mm-YYYY): 16-07-2010

Your selection: 1
Movie title: Dune Part Three
Release date (dd-mm-YYYY): 15-03-2026

Your selection: 3
-- All movies --
1: Inception (on Jul 16 2010)
2: Dune Part Three (on Mar 15 2026)
----

Your selection: 4
Username: alice
Movie ID: 1

Your selection: 5
Username: alice
-- Watched movies --
1: Inception (on Jul 16 2010)
----

Your selection: 7
Enter partial movie title: dune
-- Movies found movies --
2: Dune Part Three (on Mar 15 2026)
----

Your selection: 8
```

## सीमाएँ / भविष्य के सुधार

- **Python संस्करण** — `:=` ऑपरेटर के कारण Python 3.8+ जरूरी है।
- **इनपुट वैलिडेशन नहीं** — गलत तारीख, गलत यूज़र या गलत ID पर एरर आ सकते हैं।
- **डिलीट/एडिट सपोर्ट नहीं** — मूवी और यूज़र अपडेट या हटाए नहीं जा सकते।
- **डुप्लिकेट वॉच रिकॉर्ड** — एक ही फिल्म को कई बार वॉच्ड मार्क किया जा सकता है।
- **Foreign key enforcement** — SQLite में foreign keys रनटाइम पर एनेबल नहीं हैं।
- **पेजिनेशन नहीं** — लंबी मूवी लिस्ट पूरी छपती है।
- **हार्डकोडेड DB पाथ** — `data.db` हमेशा करंट डायरेक्टरी में रहता है।
- **टेस्ट नहीं** — अभी कोई ऑटोमेटेड टेस्ट नहीं है।

## योगदान

1. रिपॉजिटरी fork करें।
2. एक फीचर ब्रांच बनाएं (`git checkout -b feature/my-feature`).
3. बदलाव commit करें (`git commit -m "Add my feature"`).
4. ब्रांच push करें (`git push origin feature/my-feature`).
5. Pull Request खोलें।

## लाइसेंस

यह प्रोजेक्ट अभी किसी विशेष लाइसेंस के अंतर्गत प्रकाशित नहीं है। डिस्ट्रीब्यूशन टर्म्स तय करने के लिए `LICENSE` फाइल जोड़ें।
