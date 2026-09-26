# ✈️ Trip Pilot — Global Travel Guidance & AI Agent Web Application

**Trip Pilot** is a full-stack, responsive travel guidance web application built for travelers worldwide. It provides global access to **every country in the world**, featuring curated **Top 10 Places to Visit**, **Top 10 Places to Stay**, **Top 10 Places to Eat**, and **How to Travel & Transport Guidance**, along with a **responsive AI Travel Copilot** that converses with travelers in real time.

---

## ✨ Key Features

- **🌐 Worldwide Country Access**: Select or search from 195+ countries across all continents (Asia, Europe, North America, South America, Africa, Middle East, Oceania).
- **🏛️ Top 10 Places to Visit**: High-resolution attraction cards with star ratings, review counts, admission costs, category tags, addresses, and highlight summaries.
- **🏨 Top 10 Places to Stay**: Accommodations from luxury resorts and boutique hotels to heritage stays, eco-lodges, and budget hostels with price-per-night tiers and amenity chips.
- **🍽️ Top 10 Places to Eat**: Top restaurants, local food markets, signature dishes, cuisines, price levels, and dietary badges.
- **🚆 How to Travel & Transport Guide**: Country transit breakdown including train/subway advice, recommended transit passes, visa & entry rules, safety tips, and emergency contacts.
- **🤖 Workable & Responsive AI Copilot Agent**:
  - Embedded AI chat drawer aware of the active country, budget, and multi-turn conversation context.
  - Generates custom itineraries, budget travel hacks, accommodation picks, dining recommendations, and transit advice.
  - Interactive prompt suggestions & inline recommendation cards.
- **💰 Smart Budget Limit Filter**: Interactive budget slider ($10 – $500+ USD) that dynamically filters sights, stay rates, and meals.
- **🎨 Glassmorphism Responsive UI**: Built with HTML5, Tailwind CSS, FontAwesome, and vanilla JavaScript.

---

## 📁 Project Architecture

```
hime/
├── datasets/                 # Global Travel Datasets (JSON)
│   ├── countries.json        # 195+ Countries with capitals, flags, currencies, travel guides
│   ├── places.json           # Top places to visit with ratings, costs, highlights
│   ├── stays.json            # Top places to stay with nightly rates, amenities, types
│   └── food.json             # Top places to eat with signature dishes, cuisines, prices
├── backend/                  # Python FastAPI Backend
│   ├── __init__.py
│   ├── main.py               # REST API endpoints & static server
│   ├── models.py             # Pydantic data schemas
│   ├── data_loader.py        # Global dataset loader & dynamic 195-country knowledge engine
│   └── ai_assistant.py       # Trip Pilot AI Agent & conversational RAG engine
├── frontend/                 # Responsive Web Frontend SPA
│   ├── index.html            # Main HTML layout, 4-tab navigator, modal & AI Drawer
│   ├── styles.css            # Custom glassmorphism styles, glow effects & animations
│   └── app.js                # Frontend state management & API interaction
├── app.py                    # Application launch entry point
├── requirements.txt          # Python dependencies
└── README.md                 # Project Documentation
```

---

## 🚀 How to Run the Application

### 1. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 2. Start the Server
```bash
python app.py
```
Or run directly via Uvicorn:
```bash
python -m uvicorn backend.main:app --reload --port 8080
```

### 3. Open in Browser
- **Trip Pilot Web Application**: [http://127.0.0.1:8080](http://127.0.0.1:8080)
- **Interactive API Documentation (Swagger UI)**: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)

---

## 📡 REST API Documentation

| Endpoint | Method | Description |
|---|---|---|
| `/api/countries` | `GET` | Get list of all global countries (supports `continent` and `search` query parameters) |
| `/api/countries/{country_id}` | `GET` | Get details and travel transport guide for a specific country |
| `/api/places` | `GET` | Query Top 10 Places to Visit (`country_id`, `max_budget_usd`, `category`, `min_rating`, `search_term`) |
| `/api/stays` | `GET` | Query Top 10 Places to Stay (`country_id`, `max_budget_usd`, `stay_type`, `min_rating`, `search_term`) |
| `/api/food` | `GET` | Query Top 10 Places to Eat (`country_id`, `max_budget_usd`, `cuisine`, `min_rating`, `search_term`) |
| `/api/country-guide/{country_id}` | `GET` | Get complete country bundle: Top 10 Places, Top 10 Stays, Top 10 Food, and Travel Transport Guide |
| `/api/chat` | `POST` | Trip Pilot AI Copilot conversational chat endpoint |

---

## 🏆 Hackathon Highlights & Tech Stack

- **Backend**: Python 3, FastAPI, Uvicorn, Pydantic, JSON Datasets.
- **Frontend**: HTML5, Tailwind CSS, FontAwesome 6, Custom Glassmorphism CSS, Vanilla JS.
- **AI Agent**: Rule-assisted RAG (Retrieval-Augmented Generation) engine with intent classification, multi-turn history memory, and structured card returns.
