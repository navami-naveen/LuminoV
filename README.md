# LuminaV Career Guidance Platform

## 🚀 Quick Start Guide

### Step 1: Install Python Dependencies

Open a terminal/command prompt in the project folder and run:

```bash
pip install --user fastapi uvicorn python-multipart
```

### Step 2: Start the Backend Server

**Option A: Using Batch File (Easiest for Windows)**
- Double-click `start_backend.bat`

**Option B: Using PowerShell**
- Right-click `start_backend.ps1` → Run with PowerShell

**Option C: Manual Start**
```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

The server will start on `http://localhost:8000`

### Step 3: Open the Application

**Option A: Direct Open**
- Simply double-click `index.html` to open in your browser

**Option B: Test First**
- Open `test.html` in your browser to verify backend is running
- Then open `index.html`

---

## ⚠️ Troubleshooting

### Backend won't start
1. **Check Python version**: Run `python --version` (need 3.8+)
2. **Install dependencies**: Run `pip install --user -r requirements.txt`
3. **Port already in use**: Change port in backend/main.py

### Frontend can't connect
1. **Verify backend is running**: Open http://localhost:8000/api/questions in browser
2. **Check test page**: Open `test.html` to diagnose connection
3. **CORS errors**: Make sure you're not using `file://` protocol (use local server)

---

## 📁 Project Structure

```
hackher - Copy/
├── backend/
│   ├── main.py           # FastAPI backend server
│   └── data.py           # 500+ career database
├── index.html            # Main frontend application
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

---

## 🎯 Features

### 1. **RIASEC Personality Assessment**
- 6-question scientifically-based assessment
- Identifies personality type (Realistic, Investigative, Artistic, Social, Enterprising, Conventional)
- Provides match percentage

### 2. **Comprehensive Recommendations**
- Top 3 personalized career paths
- Relevant colleges (60+ institutions)
- Entrance exams with dates
- Required skills and technologies
- Learning resources

### 3. **Expanded Career Database**
- 500+ diverse career options
- Coverage across all RIASEC traits
- Emerging fields (AI Ethics, Space Mining, Climate Law, etc.)
- Traditional and modern career paths

---

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/questions` | GET | Fetch RIASEC assessment questions |
| `/api/evaluate` | POST | Evaluate quiz and generate recommendations |
| `/api/search-degree` | GET | Search Degree Dictionary for jargon |
| `/api/pivot/careers` | GET | List available careers for pivot analysis |
| `/api/pivot/calculate`| POST | Analyze skill gap between user and target career |

---

## 🎨 Technology Stack

**Backend:**
- FastAPI (Python web framework)
- Uvicorn (ASGI server)

**Frontend:**
- HTML5 (Semantic structure)
- Vanilla CSS (Glass-morphism design)
- Vanilla JavaScript (No frameworks)

---

## 📊 Usage Example

### Basic Flow:
1. **Home Page** → Click "Start Assessment"
2. **Assessment** → Select stream and marks
3. **Quiz** → Answer 6 personality questions
4. **Results** → View personalized recommendations

---

## 🔒 Security Notes

- **CORS**: Currently allows all origins (`*`) - restrict in production
- **Rate Limiting**: Consider adding for production deployment

---

## 📈 Performance

- **Load Time**: < 1 second
- **API Response**: < 1 second (typical)
- **Database**: 500+ courses loaded locally

---

## 🤝 Contributing

This is a hackathon project. For improvements:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📝 License

This project was created for educational purposes.

---

## 🙏 Acknowledgments

- **RIASEC Model**: John L. Holland's career theory
- **Design Inspiration**: Modern glass-morphism trends
- **Data Sources**: Compiled from various educational resources

---

## 📞 Support

For issues or questions:
1. Review the troubleshooting section above
2. Check backend console logs
3. Verify all dependencies are installed

---

**Happy Career Exploring! 🚀**
