DataQuery AI

**An intelligent SQL assistant with a beautiful, full-featured data editor.** Write, visualize, and manage SQL databases with natural language prompts, powerful query building, and real-time collaboration.

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

### Core Features
- **Natural Language to SQL** — Describe what you want in plain English, get SQL queries instantly
- **Multi-Method Query Building**
  - Chat interface with history and context awareness
  - Visual query builder for drag-and-drop SQL construction
  - Direct SQL editor with Monaco syntax highlighting
  - Schema browser with full table structure visualization

- **Advanced Data Management**
  - Table editor with inline cell editing and bulk operations
  - CSV/JSON import and export
  - Row duplication, copying as SQL/CSV/JSON
  - Saved filters for quick data queries
  - Full-text search across tables

### Analytics & Visualization
- **EDA (Exploratory Data Analysis)** — Auto-generate insights, correlations, and patterns
- **Interactive Dashboards** — Build custom dashboards with charts and saved queries
- **ER Diagrams** — Visualize table relationships
- **Query History** — Track and rerun previous queries
- **Alerts** — Set up monitoring for data changes

### Database Support
- SQLite (with file import)
- PostgreSQL
- MySQL
- Any SQLAlchemy-compatible database

### Developer Experience
- **Multi-tab SQL Editor** — Work on multiple queries simultaneously
- **Query Comparison** — Side-by-side SQL comparison
- **Keyboard Shortcuts** — Full hotkey support for power users
- **Theme & Accent Customization** — Light/dark modes + 6 accent colors
- **Responsive Design** — Works on desktop and tablet

---

## 🏗 Tech Stack

### Backend
- **Framework**: FastAPI (Python)
- **Database**: SQLite (default), extensible to any SQL DB via SQLAlchemy
- **AI/LLM**: Groq API (Llama 3.1 8B) or OpenAI
- **ORM**: SQLAlchemy
- **Server**: Uvicorn

### Frontend
- **Framework**: React 18 + TypeScript
- **Build**: Vite
- **UI**: Tailwind CSS + Framer Motion (animations)
- **Editor**: Monaco Editor (VS Code-like)
- **State**: Zustand + LocalStorage persistence
- **HTTP**: Axios with request/response interceptors
- **Charting**: Plotly.js

### DevOps
- Python 3.10+
- Node.js 18+

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd sql_chatbot
   ```

2. **Backend setup**
   ```bash
   # Create virtual environment
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt

   # Create .env file (see Configuration section)
   cp .env.example .env
   ```

3. **Frontend setup**
   ```bash
   cd frontend
   npm install
   ```

4. **Start backend** (from project root)
   ```bash
   python app.py
   ```
   Backend runs on `http://localhost:8000`

5. **Start frontend** (from `frontend/` directory)
   ```bash
   npm run dev
   ```
   Frontend runs on `http://localhost:5174`

6. **Open browser**
   ```
   http://localhost:5174
   ```

---

## ⚙️ Configuration

### Environment Variables (`.env`)

```env
# AI Model Configuration
OPENAI_API_KEY=sk_...          # OpenAI API key
OPENAI_MODEL=gpt-4o            # or use Groq instead
OLLAMA_URL=https://api.groq.com/openai/v1

# Default Groq (free, no API key needed for Llama 3.1)
# OLLAMA_URL=https://api.groq.com/openai/v1
# OPENAI_API_KEY=gsk_...  (get from https://console.groq.com)
```

### Optional: Authentication
To enable user authentication (email+password, OTP, Google OAuth):

```env
JWT_SECRET_KEY=<python -c "import secrets; print(secrets.token_hex(32))">
JWT_EXPIRE_MINUTES=10080
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REDIRECT_URI=http://localhost:5174/auth/callback
GMAIL_ADDRESS=
GMAIL_APP_PASSWORD=
```

---

## 📁 Project Structure

```
sql_chatbot/
├── backend/
│   ├── main.py                 # FastAPI app entry point
│   ├── auth_utils.py           # JWT, bcrypt, OTP utilities
│   ├── routers/
│   │   ├── connections.py      # Database connection management
│   │   ├── queries.py          # SQL execution
│   │   ├── ai.py               # NL2SQL, explain, fix features
│   │   ├── schema.py           # Database introspection
│   │   ├── dashboards.py       # Dashboard CRUD
│   │   ├── eda.py              # Statistical analysis
│   │   ├── alerts.py           # Data monitoring
│   │   └── ...
│   └── __init__.py
├── storage/
│   ├── app_db.py               # Database helpers & migrations
│   └── app_state.db            # SQLite database
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Home.tsx        # Landing page with animations
│   │   │   ├── Chat.tsx        # NL2SQL chat interface
│   │   │   ├── SQLEditorPage.tsx
│   │   │   ├── TableEditor.tsx
│   │   │   ├── Dashboard.tsx
│   │   │   ├── EDA.tsx
│   │   │   └── ...
│   │   ├── components/
│   │   │   ├── layout/
│   │   │   │   ├── Layout.tsx
│   │   │   │   └── Sidebar.tsx
│   │   │   └── ui/
│   │   ├── store/
│   │   │   └── useAppStore.ts  # Zustand state management
│   │   ├── utils/
│   │   │   ├── api.ts          # Axios instance + interceptors
│   │   │   └── exportData.ts
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.ts
│   └── tsconfig.json
├── requirements.txt
├── .env
└── README.md
```

---

## 🎯 Usage

### 1. Connect a Database
1. Click **"Connect a database"** in sidebar
2. Choose dialect (SQLite, PostgreSQL, MySQL)
3. Provide connection URI or upload SQLite file
4. Click **Test** → **Save**

### 2. Chat with Your Data
1. Go to **Chat** page
2. Type questions in natural English:
   - "Show me the top 10 customers by revenue"
   - "How many orders were placed last week?"
   - "Find customers with no purchases in 30 days"
3. System generates SQL and shows results instantly

### 3. Build Queries Visually
- **Query Builder**: Drag-and-drop table selection, filtering, sorting
- **SQL Editor**: Multi-tab editor with syntax highlighting
- **Schema Browser**: Explore table structures and relationships

### 4. Manage Data
- **Data Editor**: Click table row to edit inline
- **Bulk Operations**: Select multiple rows → delete/export
- **Import**: Upload CSV into any table
- **Saved Filters**: Name and reuse common WHERE clauses

### 5. Analyze & Visualize
- **EDA**: Auto-generate distributions, correlations, missing data report
- **Dashboards**: Create custom dashboards with multiple charts
- **ER Diagrams**: Visualize foreign key relationships

---

## 🔧 Development

### Running Tests
```bash
# Backend tests
pytest

# Frontend tests
cd frontend && npm run test
```

### Building for Production
```bash
# Frontend build
cd frontend && npm run build
# Output in frontend/dist/

# Backend uses gunicorn (install: pip install gunicorn)
gunicorn -w 4 -k uvicorn.workers.UvicornWorker backend.main:app
```

### Code Style
- Python: `black`, `flake8`
- TypeScript: `eslint`, `prettier`

---

## 📚 API Documentation

Once running, visit:
```
http://localhost:8000/docs
```

Interactive Swagger UI with all endpoints, request/response schemas, and try-it-out functionality.

### Main Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/connections/` | Create database connection |
| GET | `/api/schema/{conn_id}` | Get full schema |
| POST | `/api/queries/execute` | Execute SQL query |
| POST | `/api/queries/nl` | NL to SQL conversion |
| POST | `/api/ai/explain` | Explain SQL in plain English |
| POST | `/api/ai/fix` | Fix broken SQL with error context |
| POST | `/api/dashboards/` | Create dashboard |
| GET | `/api/alerts/` | List alerts |

---

## 🎨 Customization

### Theme
Go to **Settings** → **Appearance** to switch:
- Light/Dark mode
- 6 accent colors (blue, cyan, emerald, violet, amber, rose)

### Keyboard Shortcuts
Press `?` in the app to see all available shortcuts.

---

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check if port 8000 is in use
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process and restart
kill -9 <PID>
python app.py
```

### Frontend can't connect to backend
- Ensure backend is running on port 8000
- Check CORS is enabled (should be in `backend/main.py`)
- Browser console (F12) should show actual error

### Data not loading
1. Verify database connection in **Settings**
2. Check backend logs for SQL errors
3. Ensure tables have primary keys (needed for editing)

---

## 📄 License

MIT License — feel free to use for personal and commercial projects.

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📧 Support

For issues, questions, or feature requests:
- Open a GitHub Issue
- Email: support@example.com

---

## 🎓 Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [React Documentation](https://react.dev)
- [Tailwind CSS](https://tailwindcss.com)
- [SQLAlchemy](https://www.sqlalchemy.org)
- [Groq API](https://console.groq.com)
