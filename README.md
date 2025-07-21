# 🔗 URL Shortener App (Flask)

A clean and mobile-friendly URL shortener built with **Flask** and **pyshorteners**. Supports multiple shortening services like TinyURL, Is.gd, Clck.ru, and more.

---

## 🚀 Features

- Paste any long URL and get a shortened version
- Choose from multiple shortening services
- Copy shortened URL to clipboard with one click
- Clean, modern, mobile-responsive UI
- No database or login required

---

## 🛠️ Tech Stack

- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Library:** pyshorteners

---

## 📦 Installation

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
pip install -r requirements.txt
python app.py
````
### 📝 Requirements
Create a requirements.txt
````flask
pyshorteners
````

### 💡 How It Works
1. User pastes a long URL

2. Chooses a service (TinyURL, Is.gd, etc.)

3. App sends a request to Flask backend

4. Flask uses pyshorteners to generate short link

5. Short link is returned and shown in the UI


### 📂 Folder Structure
```
url-shortener/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
```
### 🤝 Contributing
Pull requests and stars are welcome. Feel free to fork and improve it.

### 📄 License
MIT License © 2025 