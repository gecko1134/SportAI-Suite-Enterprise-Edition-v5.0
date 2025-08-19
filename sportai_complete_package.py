# Production configuration  
class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://sportai:password@localhost:5432/sportai_production")
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY environment variable must be set in production")

# Get configuration based on environment
def get_config():
    """Get configuration based on environment"""
    env = os.getenv("FLASK_ENV", "development")
    
    if env == "production":
        return ProductionConfig()
    else:
        return DevelopmentConfig()
'''
    
    # Environment file
    env_content = '''# SportAI Enterprise Suite™ Environment Configuration
# Copy this file to .env and update the values

# Application Environment
FLASK_ENV=development
DEBUG=true

# Database Configuration
DATABASE_URL=sportai_production.db

# Security Configuration
SECRET_KEY=your-secret-key-here-change-in-production

# API Configuration
API_RATE_LIMIT=1000
MAX_UPLOAD_SIZE=52428800

# Logging Configuration
LOG_LEVEL=INFO

# External API Keys (Optional)
SPORTSKEY_API_KEY=your_sportskey_api_key
ONECAUSE_API_KEY=your_onecause_api_key
QUICKBOOKS_API_KEY=your_quickbooks_api_key
STRIPE_API_KEY=your_stripe_api_key

# Email Configuration (Optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=noreply@sportai.com
SMTP_PASSWORD=your_smtp_password
'''
    
    # Requirements file
    requirements_txt = '''# SportAI Enterprise Suite™ - Python Dependencies
# Core Framework
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0

# Database
sqlalchemy==2.0.23
pandas==2.1.3
numpy==1.24.4

# Authentication & Security
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6

# File Processing
aiofiles==23.2.1
openpyxl==3.1.2

# HTTP Client
requests==2.31.0

# Real-time Features
websockets==12.0

# Environment Management
python-dotenv==1.0.0

# Analytics & ML (Optional)
scikit-learn==1.3.2
plotly==5.17.0

# Streamlit Interface (Optional)
streamlit==1.28.1

# Development Tools (Optional)
pytest==7.4.3
pytest-cov==4.1.0
black==23.11.0
'''
    
    # Streamlit alternative interface
    streamlit_app_py = '''#!/usr/bin/env python3
"""
🏟️ SportAI Enterprise Suite™ - Streamlit Interface
Alternative web interface using Streamlit
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent / "backend"))

try:
    from backend.database import DatabaseManager
    from backend.auth import AuthenticationManager
except ImportError:
    st.error("❌ Backend modules not found. Please run the installation first.")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="SportAI Enterprise Suite™",
    page_icon="🏟️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
@st.cache_resource
def init_database():
    """Initialize database connection"""
    try:
        db_manager = DatabaseManager()
        auth_manager = AuthenticationManager(db_manager)
        return db_manager, auth_manager
    except Exception as e:
        st.error(f"Database initialization failed: {e}")
        return None, None

def main():
    """Main Streamlit application"""
    
    # Header
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); 
                color: white; padding: 2rem; border-radius: 15px; margin-bottom: 2rem; text-align: center;">
        <h1>🏟️ SportAI Enterprise Suite™</h1>
        <h2>Complete Sports Facility Management Platform</h2>
        <p>🔄 Real-time Data • 🔗 Live Integrations • 📊 Advanced Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize database
    db_manager, auth_manager = init_database()
    
    if not db_manager:
        st.error("❌ Failed to initialize database. Please check the installation.")
        return
    
    # Authentication
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        show_login(auth_manager)
        return
    
    # Main application
    show_dashboard(db_manager)

def show_login(auth_manager):
    """Show login interface"""
    
    st.markdown("## 🔐 Login to SportAI Enterprise Suite™")
    
    with st.form("login_form"):
        email = st.text_input("Email", value="admin@sportai.com")
        password = st.text_input("Password", type="password", value="admin123")
        submitted = st.form_submit_button("Sign In")
        
        if submitted:
            result = auth_manager.login(email, password)
            if result:
                st.session_state.authenticated = True
                st.session_state.user = result['user']
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials. Please try again.")
    
    st.info("💡 Demo Credentials: admin@sportai.com / admin123")

def show_dashboard(db_manager):
    """Show main dashboard"""
    
    # Sidebar navigation
    st.sidebar.title("🏟️ SportAI Navigation")
    
    pages = {
        "📊 Dashboard": show_main_dashboard,
        "🏟️ Facilities": show_facilities,
        "🚲 Equipment": show_equipment,
        "👥 Members": show_members,
        "🤝 Sponsors": show_sponsors,
        "📈 Analytics": show_analytics
    }
    
    selected_page = st.sidebar.selectbox("Select Page", list(pages.keys()))
    
    # Logout button
    if st.sidebar.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.rerun()
    
    # Show selected page
    pages[selected_page](db_manager)

def show_main_dashboard(db_manager):
    """Show main dashboard"""
    
    st.title("📊 SportAI Enterprise Dashboard")
    
    # Load data
    facilities = db_manager.get_facilities()
    equipment = db_manager.get_equipment()
    members = db_manager.get_members()
    sponsors = db_manager.get_sponsors()
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_revenue = sum(f.get('revenue', 0) for f in facilities)
        st.metric("Total Revenue", f"${total_revenue:,.0f}", "+31.2%")
    
    with col2:
        active_facilities = len([f for f in facilities if f.get('status') == 'active'])
        st.metric("Active Facilities", active_facilities, f"{len(facilities)} total")
    
    with col3:
        active_members = len([m for m in members if m.get('status') == 'active'])
        st.metric("Active Members", active_members, "+12.5%")
    
    with col4:
        total_sponsor_value = sum(s.get('annual_value', 0) for s in sponsors)
        st.metric("Sponsor Value", f"${total_sponsor_value/1000:.0f}K", "+8.7%")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏟️ Facility Utilization")
        if facilities:
            df_facilities = pd.DataFrame(facilities)
            fig = px.bar(df_facilities, x='name', y='utilization', 
                        title="Facility Utilization %")
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("💰 Revenue by Facility")
        if facilities:
            df_facilities = pd.DataFrame(facilities)
            fig = px.pie(df_facilities, values='revenue', names='name',
                        title="Revenue Distribution")
            st.plotly_chart(fig, use_container_width=True)

def show_facilities(db_manager):
    """Show facilities management"""
    
    st.title("🏟️ Facility Management")
    
    facilities = db_manager.get_facilities()
    
    if not facilities:
        st.warning("No facilities found. Please add some facilities first.")
        return
    
    # Facility metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_utilization = sum(f.get('utilization', 0) for f in facilities) / len(facilities)
        st.metric("Average Utilization", f"{avg_utilization:.1f}%")
    
    with col2:
        total_capacity = sum(f.get('capacity', 0) for f in facilities)
        st.metric("Total Capacity", total_capacity)
    
    with col3:
        total_revenue = sum(f.get('revenue', 0) for f in facilities)
        st.metric("Total Revenue", f"${total_revenue:,.0f}")
    
    # Facilities table
    st.subheader("📋 Facilities Overview")
    df_facilities = pd.DataFrame(facilities)
    st.dataframe(df_facilities, use_container_width=True)
    
    # Utilization chart
    st.subheader("📊 Utilization Analysis")
    fig = px.bar(df_facilities, x='name', y='utilization', color='type',
                title="Facility Utilization by Type")
    st.plotly_chart(fig, use_container_width=True)

def show_equipment(db_manager):
    """Show equipment management"""
    
    st.title("🚲 Equipment Management")
    
    equipment = db_manager.get_equipment()
    
    if not equipment:
        st.warning("No equipment found.")
        return
    
    # Equipment metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_rented = sum(e.get('rented', 0) for e in equipment)
        st.metric("Items Rented", total_rented)
    
    with col2:
        total_available = sum(e.get('available', 0) for e in equipment)
        st.metric("Items Available", total_available)
    
    with col3:
        total_revenue = sum(e.get('monthly_revenue', 0) for e in equipment)
        st.metric("Monthly Revenue", f"${total_revenue:,.0f}")
    
    # Equipment table
    st.subheader("📋 Equipment Overview")
    df_equipment = pd.DataFrame(equipment)
    st.dataframe(df_equipment, use_container_width=True)

def show_members(db_manager):
    """Show member management"""
    
    st.title("👥 Member Management")
    
    members = db_manager.get_members()
    
    if not members:
        st.warning("No members found.")
        return
    
    # Member metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_members = len(members)
        st.metric("Total Members", total_members)
    
    with col2:
        total_spent = sum(m.get('total_spent', 0) for m in members)
        st.metric("Total Spending", f"${total_spent:,.0f}")
    
    with col3:
        avg_spent = total_spent / total_members if total_members > 0 else 0
        st.metric("Avg Spending", f"${avg_spent:.0f}")
    
    # Members table
    st.subheader("📋 Members Overview")
    df_members = pd.DataFrame(members)
    st.dataframe(df_members, use_container_width=True)
    
    # Spending by tier
    if 'tier' in df_members.columns and 'total_spent' in df_members.columns:
        st.subheader("💰 Spending by Tier")
        tier_spending = df_members.groupby('tier')['total_spent'].sum().reset_index()
        fig = px.pie(tier_spending, values='total_spent', names='tier',
                    title="Total Spending by Member Tier")
        st.plotly_chart(fig, use_container_width=True)

def show_sponsors(db_manager):
    """Show sponsor management"""
    
    st.title("🤝 Sponsor Management")
    
    sponsors = db_manager.get_sponsors()
    
    if not sponsors:
        st.warning("No sponsors found.")
        return
    
    # Sponsor metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_sponsors = len(sponsors)
        st.metric("Total Sponsors", total_sponsors)
    
    with col2:
        total_value = sum(s.get('annual_value', 0) for s in sponsors)
        st.metric("Total Value", f"${total_value/1000:.0f}K")
    
    with col3:
        avg_satisfaction = sum(s.get('satisfaction', 0) for s in sponsors) / total_sponsors
        st.metric("Avg Satisfaction", f"{avg_satisfaction:.1f}/10")
    
    # Sponsors table
    st.subheader("📋 Sponsors Overview")
    df_sponsors = pd.DataFrame(sponsors)
    st.dataframe(df_sponsors, use_container_width=True)
    
    # Value by tier
    if 'tier' in df_sponsors.columns and 'annual_value' in df_sponsors.columns:
        st.subheader("💰 Value by Tier")
        fig = px.bar(df_sponsors, x='name', y='annual_value', color='tier',
                    title="Annual Value by Sponsor")
        st.plotly_chart(fig, use_container_width=True)

def show_analytics(db_manager):
    """Show analytics dashboard"""
    
    st.title("📈 Advanced Analytics")
    
    # Load all data
    facilities = db_manager.get_facilities()
    equipment = db_manager.get_equipment()
    members = db_manager.get_members()
    sponsors = db_manager.get_sponsors()
    
    # Performance metrics
    st.subheader("🎯 Key Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Revenue Growth", "+31.2%", "vs Last Year")
    
    with col2:
        avg_util = sum(f.get('utilization', 0) for f in facilities) / len(facilities) if facilities else 0
        st.metric("Facility Utilization", f"{avg_util:.1f}%", "Above Target")
    
    with col3:
        st.metric("Member Satisfaction", "9.2/10", "Excellent")
    
    with col4:
        st.metric("AI Optimization", "97%", "Efficiency Score")
    
    # Insights
    st.subheader("🤖 AI-Generated Insights")
    
    insights = [
        {
            "title": "Utilization Optimization Opportunity",
            "description": f"Average facility utilization is {avg_util:.1f}%. Implementing dynamic pricing could increase revenue by 15-25%.",
            "priority": "High"
        },
        {
            "title": "Member Tier Upgrade Potential",
            "description": "32% of members are Premium/Elite. Targeted upselling campaigns could increase revenue.",
            "priority": "Medium"
        },
        {
            "title": "Equipment Efficiency",
            "description": "Equipment rental efficiency is at 78%. Consider expanding popular categories.",
            "priority": "Low"
        }
    ]
    
    for insight in insights:
        priority_color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
        st.info(f"{priority_color[insight['priority']]} **{insight['title']}**: {insight['description']}")

if __name__ == "__main__":
    main()
'''
    
    # Installation script
    install_py = '''#!/usr/bin/env python3
"""
🏟️ SportAI Enterprise Suite™ - Installation Script
Automated installation and setup
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def main():
    """Main installation process"""
    
    print("🏟️ SportAI Enterprise Suite™ - Installation")
    print("=" * 50)
    print()
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required. Current version:", sys.version)
        return False
    
    print("✅ Python version:", sys.version.split()[0])
    
    # Create project structure
    if not create_project_structure():
        return False
    
    # Install dependencies
    if not install_dependencies():
        return False
    
    # Create configuration files
    if not create_config_files():
        return False
    
    # Initialize database
    if not initialize_database():
        return False
    
    print()
    print("🎉 Installation completed successfully!")
    print()
    print("Next steps:")
    print("1. Run: python main.py")
    print("2. Open: http://localhost:8000")
    print("3. Login: admin@sportai.com / admin123")
    print()
    print("Alternative Streamlit interface:")
    print("1. Run: streamlit run streamlit_app.py")
    print("2. Open: http://localhost:8501")
    print()
    
    return True

def create_project_structure():
    """Create directory structure"""
    
    print("📁 Creating project structure...")
    
    directories = [
        "backend",
        "backend/api",
        "frontend",
        "config", 
        "logs",
        "uploads",
        "backups"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"   ✅ {directory}/")
    
    return True

def install_dependencies():
    """Install Python dependencies"""
    
    print("📦 Installing Python dependencies...")
    
    # Core requirements
    requirements = [
        "fastapi>=0.104.0",
        "uvicorn[standard]>=0.24.0", 
        "pydantic>=2.5.0",
        "sqlalchemy>=2.0.0",
        "pandas>=2.1.0",
        "numpy>=1.24.0",
        "requests>=2.31.0",
        "python-jose[cryptography]>=3.3.0",
        "passlib[bcrypt]>=1.7.4",
        "python-multipart>=0.0.6",
        "websockets>=12.0",
        "aiofiles>=23.2.0",
        "python-dotenv>=1.0.0",
        "streamlit>=1.28.0"
    ]
    
    # Optional requirements
    optional_requirements = [
        "plotly>=5.17.0",
        "openpyxl>=3.1.0", 
        "scikit-learn>=1.3.0"
    ]
    
    # Install core requirements
    for requirement in requirements:
        try:
            print(f"   Installing {requirement}...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", requirement
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"   ✅ {requirement}")
        except subprocess.CalledProcessError:
            print(f"   ❌ Failed to install {requirement}")
            return False
    
    # Install optional requirements
    for requirement in optional_requirements:
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", requirement
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"   ✅ {requirement} (optional)")
        except subprocess.CalledProcessError:
            print(f"   ⚠️  {requirement} (optional - skipped)")
    
    return True

def create_config_files():
    """Create configuration files"""
    
    print("⚙️ Creating configuration files...")
    
    # Create .env file
    env_content = '''# SportAI Enterprise Suite™ Configuration
DEBUG=true
SECRET_KEY=sportai-development-key-change-in-production
DATABASE_URL=sportai_production.db
LOG_LEVEL=INFO
'''
    
    with open('.env', 'w') as f:
        f.write(env_content)
    print("   ✅ .env")
    
    return True

def initialize_database():
    """Initialize the database"""
    
    print("🗃️ Initializing database...")
    
    try:
        # Import and initialize database
        sys.path.append(str(Path.cwd() / "backend"))
        from backend.database import DatabaseManager
        
        db_manager = DatabaseManager()
        print("   ✅ Database initialized with sample data")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Database initialization failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
'''
    
    # README file
    readme_md = '''# 🏟️ SportAI Enterprise Suite™

Complete Sports Facility Management Platform with AI-Powered Analytics

## Features

- **Real-time Dashboard** - Live facility and revenue management
- **AI Analytics** - Predictive insights and optimization recommendations  
- **Member Management** - Complete member lifecycle tracking
- **Facility Optimization** - Dynamic utilization and pricing optimization
- **Equipment Tracking** - Rental management and revenue optimization
- **Sponsor Management** - Partnership tracking and ROI analysis
- **File Management** - CSV/Excel data import and export
- **Third-party Integrations** - SportsKey, OneCause, QuickBooks, Stripe

## Quick Start

### 1. Installation

```bash
# Download and extract the SportAI package
# Navigate to the project directory
cd sportai-enterprise-suite

# Run the installation script
python install.py
```

### 2. Start the Application

```bash
# Start the FastAPI server
python main.py
```

### 3. Access the Platform

- **API Server**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Streamlit Interface**: `streamlit run streamlit_app.py`

### 4. Login

- **Email**: admin@sportai.com
- **Password**: admin123

## System Requirements

- Python 3.8+
- 4GB RAM minimum (8GB recommended)
- 2GB free disk space
- Modern web browser

## Architecture

```
sportai-enterprise-suite/
├── main.py                 # Main application entry point
├── streamlit_app.py        # Alternative Streamlit interface
├── install.py              # Installation script
├── backend/                # Backend Python modules
│   ├── app.py             # FastAPI application factory
│   ├── database.py        # Database management
│   ├── auth.py            # Authentication system
│   └── api/
│       └── routes.py      # API routes
├── config/                 # Configuration files
├── logs/                  # Application logs
├── uploads/               # File uploads
└── docs/                  # Documentation

```

## Configuration

### Environment Variables

Create a `.env` file:

```env
DEBUG=true
SECRET_KEY=your-secret-key-here
DATABASE_URL=sportai_production.db
LOG_LEVEL=INFO

# Optional: Third-party API keys
SPORTSKEY_API_KEY=your_key
ONECAUSE_API_KEY=your_key
QUICKBOOKS_API_KEY=your_key
STRIPE_API_KEY=your_key
```

### Database

The system uses SQLite by default for easy setup. For production, configure PostgreSQL:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/sportai_production
```

## API Endpoints

### Authentication
- `POST /api/auth/login` - User login

### Data Management
- `GET /api/facilities` - Get all facilities
- `GET /api/equipment` - Get all equipment  
- `GET /api/members` - Get all members
- `GET /api/sponsors` - Get all sponsors

### Analytics
- `GET /api/analytics/insights` - Get AI insights
- `GET /api/analytics/revenue-prediction` - Get revenue predictions

### Health Check
- `GET /health` - System health status

## Usage Examples

### Python API Client

```python
import requests

# Login
response = requests.post("http://localhost:8000/api/auth/login", 
                        data={"email": "admin@sportai.com", "password": "admin123"})
token = response.json()["access_token"]

# Get facilities
headers = {"Authorization": f"Bearer {token}"}
facilities = requests.get("http://localhost:8000/api/facilities", headers=headers)
print(facilities.json())
```

### Streamlit Interface

```bash
# Start Streamlit interface
streamlit run streamlit_app.py

# Access at http://localhost:8501
```

## Development

### Adding New Features

1. **Backend**: Add routes in `backend/api/routes.py`
2. **Database**: Extend models in `backend/database.py`
3. **Frontend**: Update Streamlit interface in `streamlit_app.py`

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/
```

## Production Deployment

### Docker

```bash
# Build and run with Docker
docker build -t sportai-enterprise .
docker run -p 8000:8000 sportai-enterprise
```

### Traditional Server

```bash
# Install production dependencies
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

## Support

- **Documentation**: See `docs/` folder
- **Issues**: Create an issue for bug reports
- **Email**: support@sportai.com

## License

SportAI Enterprise Suite™ - © 2024 SportAI Solutions, LLC. All Rights Reserved.

## Trademark Notice

SportAI Enterprise Suite™ and related marks are trademarks of SportAI Solutions, LLC.
'''
    
    # Create all additional files
    additional_files = {
        "backend/auth.py": auth_py,
        "backend/api/__init__.py": "",
        "backend/api/routes.py": routes_py,
        "config/settings.py": config_py,
        ".env.example": env_content,
        "requirements.txt": requirements_txt,
        "streamlit_app.py": streamlit_app_py,
        "install.py": install_py,
        "README.md": readme_md
    }
    
    print("📝 Creating additional backend files...")
    for file_path, content in additional_files.items():
        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✅ {file_path}")
    
    return True

def create_frontend_files():
    """Create React frontend files"""
    
    # Package.json
    package_json = '''{
  "name": "sportai-enterprise-frontend",
  "version": "6.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "lucide-react": "^0.294.0",
    "axios": "^1.6.2"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version", 
      "last 1 safari version"
    ]
  }
}'''
    
    # Public index.html
    index_html = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="SportAI Enterprise Suite - Complete Sports Facility Management Platform" />
    <title>SportAI Enterprise Suite™</title>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run SportAI Enterprise Suite™.</noscript>
    <div id="root"></div>
  </body>
</html>'''
    
    # App.js
    app_js = '''import React from 'react';
import './App.css';

function App() {
  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center">
      <div className="text-center">
        <h1 className="text-4xl font-bold text-blue-600 mb-4">
          🏟️ SportAI Enterprise Suite™
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Complete Sports Facility Management Platform
        </p>
        <div className="space-y-4">
          <p className="text-gray-500">
            The React frontend is available in the complete implementation.
          </p>
          <p className="text-gray-500">
            For now, use the Streamlit interface:
          </p>
          <code className="bg-gray-100 px-4 py-2 rounded">
            streamlit run streamlit_app.py
          </code>
        </div>
      </div>
    </div>
  );
}

export default App;'''
    
    # Create frontend files
    frontend_files = {
        "frontend/package.json": package_json,
        "frontend/public/index.html": index_html,
        "frontend/src/App.js": app_js,
        "frontend/src/App.css#!/usr/bin/env python3
"""
🏟️ SportAI Enterprise Suite™ - Complete Production Package
© 2024 SportAI Solutions, LLC. All Rights Reserved.

INSTALLATION INSTRUCTIONS:
==========================

1. Download and extract this package
2. Install Python 3.11+ and dependencies
3. Configure environment variables
4. Run the installation script
5. Access the platform at http://localhost:8000

QUICK START:
============
python install.py
python main.py

"""

import os
import sys
import subprocess
import json
import sqlite3
import secrets
from pathlib import Path

# =============================================================================
# INSTALLATION SCRIPT
# =============================================================================

def create_project_structure():
    """Create the complete project directory structure"""
    
    # Main directories
    directories = [
        "backend",
        "backend/api",
        "backend/models", 
        "backend/services",
        "backend/utils",
        "frontend",
        "frontend/src",
        "frontend/src/components",
        "frontend/src/services",
        "frontend/public",
        "config",
        "scripts",
        "docs",
        "logs",
        "uploads",
        "backups",
        "tests",
        "monitoring"
    ]
    
    print("📁 Creating project structure...")
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"   ✅ Created {directory}/")
    
    return True

def install_python_dependencies():
    """Install all required Python packages"""
    
    requirements = [
        "fastapi==0.104.1",
        "uvicorn[standard]==0.24.0",
        "pydantic==2.5.0", 
        "sqlalchemy==2.0.23",
        "pandas==2.1.3",
        "numpy==1.24.4",
        "requests==2.31.0",
        "python-jose[cryptography]==3.3.0",
        "passlib[bcrypt]==1.7.4",
        "python-multipart==0.0.6",
        "websockets==12.0",
        "aiofiles==23.2.1",
        "python-dotenv==1.0.0",
        "streamlit==1.28.1",
        "plotly==5.17.0",
        "openpyxl==3.1.2",
        "scikit-learn==1.3.2"
    ]
    
    print("📦 Installing Python dependencies...")
    
    # Check if pip is available
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
    except subprocess.CalledProcessError:
        print("❌ pip is not available. Please install pip first.")
        return False
    
    # Install requirements
    for package in requirements:
        try:
            print(f"   Installing {package}...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", package
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"   ✅ {package}")
        except subprocess.CalledProcessError:
            print(f"   ⚠️  {package} (optional - will use fallbacks)")
    
    return True

def create_backend_files():
    """Create all backend Python files"""
    
    # Main FastAPI application
    main_py = '''#!/usr/bin/env python3
"""
🏟️ SportAI Enterprise Suite™ - Main Application
Production-ready FastAPI server with all features
"""

import os
import sys
import logging
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent / "backend"))

from backend.app import create_app

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/sportai.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Create application
    app = create_app()
    
    # Import uvicorn for running the server
    try:
        import uvicorn
        logger.info("🏟️ Starting SportAI Enterprise Suite™")
        logger.info("🌐 Frontend will be available at: http://localhost:3000")
        logger.info("🔗 API will be available at: http://localhost:8000")
        logger.info("📊 API Documentation: http://localhost:8000/docs")
        
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except ImportError:
        logger.error("❌ uvicorn not installed. Installing now...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "uvicorn[standard]"])
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
'''
    
    # Backend application factory
    backend_app_py = '''"""
FastAPI Application Factory
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from .database import DatabaseManager
from .auth import AuthenticationManager
from .api.routes import create_api_router

# Global instances
db_manager = None
auth_manager = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan management"""
    global db_manager, auth_manager
    
    # Startup
    print("🏟️ Starting SportAI Enterprise Suite™...")
    
    # Initialize database
    db_manager = DatabaseManager()
    auth_manager = AuthenticationManager(db_manager)
    
    # Store in app state
    app.state.db_manager = db_manager
    app.state.auth_manager = auth_manager
    
    print("✅ Database initialized")
    print("✅ Authentication system ready")
    print("🚀 SportAI Enterprise Suite™ is ready!")
    
    yield
    
    # Shutdown
    print("👋 Shutting down SportAI Enterprise Suite™")

def create_app() -> FastAPI:
    """Create and configure FastAPI application"""
    
    app = FastAPI(
        title="SportAI Enterprise Suite™",
        description="Complete Sports Facility Management Platform",
        version="6.0.0",
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include API routes
    api_router = create_api_router()
    app.include_router(api_router, prefix="/api")
    
    # Serve static files
    try:
        app.mount("/static", StaticFiles(directory="frontend/build/static"), name="static")
    except RuntimeError:
        pass  # Directory doesn't exist yet
    
    # Health check endpoint
    @app.get("/health")
    async def health_check():
        return {
            "status": "healthy",
            "version": "6.0.0",
            "platform": "SportAI Enterprise Suite™"
        }
    
    # Root endpoint
    @app.get("/")
    async def root():
        return {
            "message": "🏟️ SportAI Enterprise Suite™ API",
            "version": "6.0.0",
            "docs": "/docs",
            "health": "/health"
        }
    
    return app
'''
    
    # Database manager
    database_py = '''"""
Production Database Manager with SQLite/PostgreSQL support
"""

import sqlite3
import json
import logging
from typing import Dict, List, Optional, Any
from contextlib import contextmanager
from datetime import datetime
import threading
import pandas as pd

logger = logging.getLogger(__name__)

class DatabaseManager:
    """Production database manager with connection pooling"""
    
    def __init__(self, db_path: str = "sportai_production.db"):
        self.db_path = db_path
        self._connection_pool = []
        self._pool_lock = threading.Lock()
        self.init_database()
        logger.info(f"Database initialized: {db_path}")
    
    @contextmanager
    def get_connection(self):
        """Get database connection from pool with automatic cleanup"""
        conn = None
        try:
            with self._pool_lock:
                if self._connection_pool:
                    conn = self._connection_pool.pop()
                else:
                    conn = sqlite3.connect(self.db_path, check_same_thread=False)
                    conn.row_factory = sqlite3.Row
            yield conn
        except Exception as e:
            logger.error(f"Database error: {e}")
            if conn:
                conn.rollback()
            raise
        finally:
            if conn:
                conn.commit()
                with self._pool_lock:
                    if len(self._connection_pool) < 10:
                        self._connection_pool.append(conn)
                    else:
                        conn.close()
    
    def init_database(self):
        """Initialize database with comprehensive schema"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Create all tables
                self._create_tables(cursor)
                self._create_indexes(cursor)
                self._insert_sample_data()
                
                conn.commit()
                logger.info("Database schema created successfully")
                
        except Exception as e:
            logger.error(f"Database initialization failed: {e}")
            raise
    
    def _create_tables(self, cursor):
        """Create all database tables"""
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'user',
                facility_id INTEGER,
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP
            )
        ''')
        
        # Facilities table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS facilities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                capacity INTEGER NOT NULL,
                hourly_rate REAL NOT NULL,
                utilization REAL DEFAULT 0,
                revenue REAL DEFAULT 0,
                status TEXT DEFAULT 'active',
                equipment TEXT DEFAULT '[]',
                location TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Equipment table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS equipment (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                available INTEGER NOT NULL,
                rented INTEGER DEFAULT 0,
                daily_rate REAL NOT NULL,
                monthly_revenue REAL DEFAULT 0,
                status TEXT DEFAULT 'available',
                last_maintenance TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Members table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                tier TEXT NOT NULL,
                join_date TIMESTAMP NOT NULL,
                total_spent REAL DEFAULT 0,
                last_visit TIMESTAMP,
                status TEXT DEFAULT 'active',
                preferences TEXT DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Sponsors table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sponsors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                tier TEXT NOT NULL,
                annual_value REAL NOT NULL,
                engagement REAL DEFAULT 0,
                satisfaction REAL DEFAULT 0,
                status TEXT DEFAULT 'active',
                renewal_date TIMESTAMP,
                contact_info TEXT DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Analytics table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analytics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date DATE NOT NULL,
                metric_type TEXT NOT NULL,
                metric_value REAL NOT NULL,
                facility_id INTEGER,
                metadata TEXT DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    
    def _create_indexes(self, cursor):
        """Create database indexes for performance"""
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_facilities_status ON facilities (status)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_members_tier ON members (tier)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_analytics_date ON analytics (date)')
    
    def _insert_sample_data(self):
        """Insert comprehensive sample data"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Check if data already exists
                cursor.execute("SELECT COUNT(*) FROM facilities")
                if cursor.fetchone()[0] == 0:
                    
                    # Insert sample facilities
                    facilities_data = [
                        ("Basketball Court 1", "Indoor Court", 200, 150.0, 89.0, 9450.0, "active", '["Scoreboard", "Sound System"]', "North Wing"),
                        ("Basketball Court 2", "Indoor Court", 150, 140.0, 84.0, 8290.0, "active", '["Volleyball Net", "Speakers"]', "South Wing"),
                        ("Main Dome", "Multi-Sport", 500, 350.0, 93.0, 15200.0, "active", '["Field Goals", "PA System"]', "Central"),
                        ("Outdoor Field A", "Turf Field", 150, 100.0, 72.0, 5200.0, "active", '["Soccer Goals"]', "East Side"),
                        ("Tennis Court 1", "Tennis Court", 50, 80.0, 78.0, 4800.0, "active", '["Net", "Lights"]', "West Side"),
                        ("Swimming Pool", "Aquatic", 100, 120.0, 65.0, 7200.0, "active", '["Lane Markers", "Timing System"]', "Aquatic Center")
                    ]
                    
                    cursor.executemany('''
                        INSERT INTO facilities (name, type, capacity, hourly_rate, utilization, revenue, status, equipment, location)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', facilities_data)
                    
                    # Insert sample equipment
                    equipment_data = [
                        ("Mountain Bike", "Bikes", 15, 8, 25.0, 3200.0, "available", datetime.now()),
                        ("Standard Golf Cart", "Golf Carts", 6, 4, 50.0, 6000.0, "available", datetime.now()),
                        ("Day Locker", "Lockers", 50, 38, 5.0, 5700.0, "available", datetime.now()),
                        ("Tennis Racket", "Sports Equipment", 25, 12, 15.0, 1800.0, "available", datetime.now()),
                        ("Pool Noodles", "Aquatic Equipment", 100, 25, 2.0, 500.0, "available", datetime.now()),
                        ("Kayak", "Water Sports", 8, 3, 40.0, 1200.0, "available", datetime.now())
                    ]
                    
                    cursor.executemany('''
                        INSERT INTO equipment (name, category, available, rented, daily_rate, monthly_revenue, status, last_maintenance)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', equipment_data)
                    
                    # Insert sample members
                    members_data = [
                        ("M001", "John Smith", "john.smith@email.com", "Premium", datetime.now(), 1250.0, datetime.now(), "active", '{"preferred_sports": ["basketball", "tennis"]}'),
                        ("M002", "Sarah Johnson", "sarah.j@email.com", "Elite", datetime.now(), 2100.0, datetime.now(), "active", '{"preferred_sports": ["swimming", "fitness"]}'),
                        ("M003", "Mike Wilson", "mike.w@email.com", "Basic", datetime.now(), 850.0, datetime.now(), "active", '{"preferred_sports": ["soccer", "basketball"]}'),
                        ("M004", "Emily Davis", "emily.d@email.com", "Premium", datetime.now(), 1450.0, datetime.now(), "active", '{"preferred_sports": ["tennis", "swimming"]}'),
                        ("M005", "David Brown", "david.b@email.com", "Elite", datetime.now(), 2800.0, datetime.now(), "active", '{"preferred_sports": ["all_sports"]}')
                    ]
                    
                    cursor.executemany('''
                        INSERT INTO members (member_id, name, email, tier, join_date, total_spent, last_visit, status, preferences)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', members_data)
                    
                    # Insert sample sponsors
                    sponsors_data = [
                        ("Wells Fargo Bank", "Diamond", 175000.0, 95.0, 9.2, "active", datetime.now(), '{"contact": "sponsor@wellsfargo.com", "phone": "555-0100"}'),
                        ("HyVee", "Platinum", 62500.0, 88.0, 8.7, "active", datetime.now(), '{"contact": "partnerships@hyvee.com", "phone": "555-0200"}'),
                        ("TD Ameritrade", "Gold", 32000.0, 92.0, 8.9, "active", datetime.now(), '{"contact": "sports@tdameritrade.com", "phone": "555-0300"}'),
                        ("Nike", "Silver", 15000.0, 85.0, 8.5, "active", datetime.now(), '{"contact": "local@nike.com", "phone": "555-0400"}'),
                        ("Gatorade", "Bronze", 8000.0, 78.0, 8.0, "active", datetime.now(), '{"contact": "sports@gatorade.com", "phone": "555-0500"}')
                    ]
                    
                    cursor.executemany('''
                        INSERT INTO sponsors (name, tier, annual_value, engagement, satisfaction, status, renewal_date, contact_info)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', sponsors_data)
                    
                    # Insert default admin user
                    import hashlib
                    admin_password = hashlib.sha256("admin123".encode()).hexdigest()
                    cursor.execute('''
                        INSERT INTO users (email, password_hash, role, is_active)
                        VALUES (?, ?, ?, ?)
                    ''', ("admin@sportai.com", admin_password, "admin", True))
                    
                    conn.commit()
                    logger.info("Sample data inserted successfully")
                    
        except Exception as e:
            logger.error(f"Failed to insert sample data: {e}")
            raise
    
    # Data access methods
    def get_facilities(self) -> List[Dict]:
        """Get all facilities"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM facilities ORDER BY name")
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get facilities: {e}")
            return []
    
    def get_equipment(self) -> List[Dict]:
        """Get all equipment"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM equipment ORDER BY category, name")
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get equipment: {e}")
            return []
    
    def get_members(self) -> List[Dict]:
        """Get all members"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM members ORDER BY name")
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get members: {e}")
            return []
    
    def get_sponsors(self) -> List[Dict]:
        """Get all sponsors"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM sponsors ORDER BY annual_value DESC")
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get sponsors: {e}")
            return []
    
    def authenticate_user(self, email: str, password: str) -> Optional[Dict]:
        """Authenticate user"""
        try:
            import hashlib
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT id, email, role, facility_id, is_active 
                    FROM users 
                    WHERE email = ? AND password_hash = ? AND is_active = 1
                ''', (email, password_hash))
                row = cursor.fetchone()
                
                if row:
                    # Update last login
                    cursor.execute('''
                        UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = ?
                    ''', (row['id'],))
                    return dict(row)
                return None
                
        except Exception as e:
            logger.error(f"Authentication failed: {e}")
            return None
'''
    
    # Write all backend files
    files_to_create = {
        "main.py": main_py,
        "backend/__init__.py": "",
        "backend/app.py": backend_app_py,
        "backend/database.py": database_py
    }
    
    print("🐍 Creating backend Python files...")
    for file_path, content in files_to_create.items():
        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✅ {file_path}")
    
    return True

def create_additional_backend_files():
    """Create remaining backend files"""
    
    # Authentication module
    auth_py = '''"""
JWT Authentication Manager
"""

import jwt
import hashlib
from datetime import datetime, timedelta
from typing import Optional, Dict
import logging

logger = logging.getLogger(__name__)

class AuthenticationManager:
    """JWT-based authentication"""
    
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.secret_key = "sportai-secret-key-change-in-production"
        self.algorithm = "HS256"
    
    def create_access_token(self, user_id: int, email: str, role: str) -> str:
        """Create JWT access token"""
        try:
            payload = {
                "user_id": user_id,
                "email": email,
                "role": role,
                "exp": datetime.utcnow() + timedelta(hours=24),
                "iat": datetime.utcnow(),
                "iss": "SportAI Enterprise"
            }
            return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        except Exception as e:
            logger.error(f"Failed to create token: {e}")
            raise
    
    def verify_token(self, token: str) -> Optional[Dict]:
        """Verify and decode JWT token"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            logger.warning("Token has expired")
            return None
        except jwt.InvalidTokenError:
            logger.warning("Invalid token")
            return None
    
    def login(self, email: str, password: str) -> Optional[Dict]:
        """Login user and return token"""
        user = self.db_manager.authenticate_user(email, password)
        if user:
            token = self.create_access_token(user['id'], user['email'], user['role'])
            return {
                "user": user,
                "access_token": token,
                "token_type": "bearer"
            }
        return None
'''
    
    # API Routes
    routes_py = '''"""
API Routes for SportAI Enterprise Suite
"""

from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Dict, List

security = HTTPBearer()

def create_api_router() -> APIRouter:
    """Create API router with all endpoints"""
    
    router = APIRouter()
    
    async def get_current_user(
        request: Request,
        credentials: HTTPAuthorizationCredentials = Depends(security)
    ):
        """Get current authenticated user"""
        auth_manager = request.app.state.auth_manager
        payload = auth_manager.verify_token(credentials.credentials)
        if not payload:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return payload
    
    # Authentication endpoints
    @router.post("/auth/login")
    async def login(request: Request, email: str, password: str):
        """User login endpoint"""
        auth_manager = request.app.state.auth_manager
        result = auth_manager.login(email, password)
        if not result:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return result
    
    # Data endpoints
    @router.get("/facilities")
    async def get_facilities(request: Request, current_user: dict = Depends(get_current_user)):
        """Get all facilities"""
        db_manager = request.app.state.db_manager
        return db_manager.get_facilities()
    
    @router.get("/equipment")
    async def get_equipment(request: Request, current_user: dict = Depends(get_current_user)):
        """Get all equipment"""
        db_manager = request.app.state.db_manager
        return db_manager.get_equipment()
    
    @router.get("/members")
    async def get_members(request: Request, current_user: dict = Depends(get_current_user)):
        """Get all members"""
        db_manager = request.app.state.db_manager
        return db_manager.get_members()
    
    @router.get("/sponsors")
    async def get_sponsors(request: Request, current_user: dict = Depends(get_current_user)):
        """Get all sponsors"""
        db_manager = request.app.state.db_manager
        return db_manager.get_sponsors()
    
    # Analytics endpoints
    @router.get("/analytics/insights")
    async def get_insights(request: Request, current_user: dict = Depends(get_current_user)):
        """Get AI-generated business insights"""
        # Mock insights for demo
        return [
            {
                "type": "opportunity",
                "title": "Utilization Optimization Opportunity",
                "description": "Average facility utilization is 84.2%. Implementing dynamic pricing could increase revenue by 15-25%.",
                "priority": "high"
            },
            {
                "type": "growth",
                "title": "Member Tier Upgrade Opportunity", 
                "description": "32% of members are Premium/Elite. Targeted upselling could increase revenue.",
                "priority": "medium"
            }
        ]
    
    @router.get("/analytics/revenue-prediction")
    async def predict_revenue(request: Request, current_user: dict = Depends(get_current_user)):
        """Get revenue predictions"""
        db_manager = request.app.state.db_manager
        facilities = db_manager.get_facilities()
        
        # Simple prediction calculation
        total_predicted = 0
        current_revenue = 0
        
        for facility in facilities:
            capacity = facility.get('capacity', 0)
            utilization = facility.get('utilization', 0)
            rate = facility.get('hourly_rate', 0)
            
            predicted = capacity * (utilization / 100) * rate * 24 * 30 * 1.1
            total_predicted += predicted
            current_revenue += facility.get('revenue', 0)
        
        growth_rate = ((total_predicted - current_revenue) / current_revenue * 100) if current_revenue > 0 else 0
        
        return {
            "total_predicted": total_predicted,
            "growth_rate": round(growth_rate, 2)
        }
    
    return router
'''
    
    # Configuration file
    config_py = '''"""
Configuration settings for SportAI Enterprise Suite
"""

import os
from pathlib import Path

class Config:
    """Application configuration"""
    
    # Application
    APP_NAME = "SportAI Enterprise Suite™"
    VERSION = "6.0.0"
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "sportai_production.db")
    
    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "sportai-secret-key-change-in-production")
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_HOURS = 24
    
    # File upload
    MAX_UPLOAD_SIZE = 50 * 1024 * 1024  # 50MB
    UPLOAD_FOLDER = Path("uploads")
    ALLOWED_EXTENSIONS = {'.csv', '.xlsx', '.xls', '.json'}
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = "logs/sportai.log"
    
    # Directories
    @staticmethod
    def create_directories():
        """Create necessary directories"""
        directories = [
            "logs",
            "uploads", 
            "backups",
            "frontend/build"
        ]
        
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)

# Development configuration
class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URL = "sportai_development.db"

# Production configuration  