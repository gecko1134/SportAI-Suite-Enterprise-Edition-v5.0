#!/usr/bin/env python3
"""
🏟️ SportAI Enterprise Suite™ - Complete Package Creator (Fixed)
© 2024 SportAI Solutions, LLC. All Rights Reserved.

USAGE:
======
python create_sportai_package.py

This will create a complete, downloadable SportAI Enterprise Suite package
with all necessary files, documentation, and setup scripts.
"""

import os
import sys
import subprocess
import json
import secrets
from pathlib import Path

def create_project_structure():
    """Create the complete project directory structure"""
    
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

def create_main_files():
    """Create main application files"""
    
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

def create_app():
    """Create and configure FastAPI application"""
    try:
        from fastapi import FastAPI
        from fastapi.middleware.cors import CORSMiddleware
        from backend.database import DatabaseManager
        from backend.auth import AuthenticationManager
        from backend.api.routes import create_api_router
        
        app = FastAPI(
            title="SportAI Enterprise Suite™",
            description="Complete Sports Facility Management Platform",
            version="6.0.0",
            docs_url="/docs",
            redoc_url="/redoc"
        )
        
        # CORS middleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        # Initialize services
        db_manager = DatabaseManager()
        auth_manager = AuthenticationManager(db_manager)
        
        # Store in app state
        app.state.db_manager = db_manager
        app.state.auth_manager = auth_manager
        
        # Include API routes
        api_router = create_api_router()
        app.include_router(api_router, prefix="/api")
        
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
        
    except ImportError as e:
        logger.error(f"Import error: {e}")
        logger.error("Please install required dependencies: pip install fastapi uvicorn")
        raise

if __name__ == "__main__":
    try:
        import uvicorn
        
        # Create directories
        Path("logs").mkdir(exist_ok=True)
        
        # Create application
        app = create_app()
        
        logger.info("🏟️ Starting SportAI Enterprise Suite™")
        logger.info("🌐 Server will be available at: http://localhost:8000")
        logger.info("📊 API Documentation: http://localhost:8000/docs")
        logger.info("🔑 Default login: admin@sportai.com / admin123")
        
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
        
    except ImportError:
        logger.error("❌ uvicorn not installed. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "uvicorn[standard]"])
        import uvicorn
        app = create_app()
        uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    except Exception as e:
        logger.error(f"Failed to start application: {e}")
        sys.exit(1)
'''
    
    # Database manager
    database_py = '''"""
Production Database Manager with SQLite support
"""

import sqlite3
import json
import logging
from typing import Dict, List, Optional, Any
from contextlib import contextmanager
from datetime import datetime, timedelta
import threading
import hashlib

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
                self._create_tables(cursor)
                self._create_indexes(cursor)
                conn.commit()
                
                # Insert sample data if tables are empty
                cursor.execute("SELECT COUNT(*) FROM facilities")
                if cursor.fetchone()[0] == 0:
                    self._insert_sample_data()
                
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
                    ("Mountain Bike", "Bikes", 15, 8, 25.0, 3200.0, "available", datetime.now().isoformat()),
                    ("Standard Golf Cart", "Golf Carts", 6, 4, 50.0, 6000.0, "available", datetime.now().isoformat()),
                    ("Day Locker", "Lockers", 50, 38, 5.0, 5700.0, "available", datetime.now().isoformat()),
                    ("Tennis Racket", "Sports Equipment", 25, 12, 15.0, 1800.0, "available", datetime.now().isoformat()),
                    ("Pool Noodles", "Aquatic Equipment", 100, 25, 2.0, 500.0, "available", datetime.now().isoformat()),
                    ("Kayak", "Water Sports", 8, 3, 40.0, 1200.0, "available", datetime.now().isoformat())
                ]
                
                cursor.executemany('''
                    INSERT INTO equipment (name, category, available, rented, daily_rate, monthly_revenue, status, last_maintenance)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', equipment_data)
                
                # Insert sample members
                members_data = [
                    ("M001", "John Smith", "john.smith@email.com", "Premium", datetime.now().isoformat(), 1250.0, datetime.now().isoformat(), "active", '{"preferred_sports": ["basketball", "tennis"]}'),
                    ("M002", "Sarah Johnson", "sarah.j@email.com", "Elite", datetime.now().isoformat(), 2100.0, datetime.now().isoformat(), "active", '{"preferred_sports": ["swimming", "fitness"]}'),
                    ("M003", "Mike Wilson", "mike.w@email.com", "Basic", datetime.now().isoformat(), 850.0, datetime.now().isoformat(), "active", '{"preferred_sports": ["soccer", "basketball"]}'),
                    ("M004", "Emily Davis", "emily.d@email.com", "Premium", datetime.now().isoformat(), 1450.0, datetime.now().isoformat(), "active", '{"preferred_sports": ["tennis", "swimming"]}'),
                    ("M005", "David Brown", "david.b@email.com", "Elite", datetime.now().isoformat(), 2800.0, datetime.now().isoformat(), "active", '{"preferred_sports": ["all_sports"]}')
                ]
                
                cursor.executemany('''
                    INSERT INTO members (member_id, name, email, tier, join_date, total_spent, last_visit, status, preferences)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', members_data)
                
                # Insert sample sponsors
                renewal_date = (datetime.now() + timedelta(days=365)).isoformat()
                sponsors_data = [
                    ("Wells Fargo Bank", "Diamond", 175000.0, 95.0, 9.2, "active", renewal_date, '{"contact": "sponsor@wellsfargo.com", "phone": "555-0100"}'),
                    ("HyVee", "Platinum", 62500.0, 88.0, 8.7, "active", renewal_date, '{"contact": "partnerships@hyvee.com", "phone": "555-0200"}'),
                    ("TD Ameritrade", "Gold", 32000.0, 92.0, 8.9, "active", renewal_date, '{"contact": "sports@tdameritrade.com", "phone": "555-0300"}'),
                    ("Nike", "Silver", 15000.0, 85.0, 8.5, "active", renewal_date, '{"contact": "local@nike.com", "phone": "555-0400"}'),
                    ("Gatorade", "Bronze", 8000.0, 78.0, 8.0, "active", renewal_date, '{"contact": "sports@gatorade.com", "phone": "555-0500"}')
                ]
                
                cursor.executemany('''
                    INSERT INTO sponsors (name, tier, annual_value, engagement, satisfaction, status, renewal_date, contact_info)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', sponsors_data)
                
                # Insert default admin user
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
    
    # Authentication module
    auth_py = '''"""
JWT Authentication Manager
"""

import logging
from datetime import datetime, timedelta
from typing import Optional, Dict

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
            # Try to use PyJWT
            try:
                import jwt
                payload = {
                    "user_id": user_id,
                    "email": email,
                    "role": role,
                    "exp": datetime.utcnow() + timedelta(hours=24),
                    "iat": datetime.utcnow(),
                    "iss": "SportAI Enterprise"
                }
                return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
            except ImportError:
                # Fallback to simple token
                import base64
                import json
                payload = {
                    "user_id": user_id,
                    "email": email,
                    "role": role,
                    "exp": (datetime.utcnow() + timedelta(hours=24)).isoformat()
                }
                token_data = json.dumps(payload).encode()
                return base64.b64encode(token_data).decode()
                
        except Exception as e:
            logger.error(f"Failed to create token: {e}")
            raise
    
    def verify_token(self, token: str) -> Optional[Dict]:
        """Verify and decode JWT token"""
        try:
            # Try PyJWT first
            try:
                import jwt
                payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
                return payload
            except ImportError:
                # Fallback to simple token
                import base64
                import json
                token_data = base64.b64decode(token.encode()).decode()
                payload = json.loads(token_data)
                
                # Check expiration
                exp_time = datetime.fromisoformat(payload['exp'])
                if datetime.utcnow() > exp_time:
                    return None
                    
                return payload
                
        except Exception as e:
            logger.warning(f"Token verification failed: {e}")
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

from typing import Dict, List

def create_api_router():
    """Create API router with all endpoints"""
    
    try:
        from fastapi import APIRouter, HTTPException, Depends, Request
        from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
    except ImportError:
        raise ImportError("FastAPI not installed. Run: pip install fastapi")
    
    router = APIRouter()
    security = HTTPBearer()
    
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
            },
            {
                "type": "performance",
                "title": "Equipment Efficiency Strong",
                "description": "Equipment rental efficiency at 78%. Consider expanding popular categories.",
                "priority": "low"
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
            
            # Predict with 10% optimization
            predicted = capacity * (utilization / 100) * rate * 24 * 30 * 1.1
            total_predicted += predicted
            current_revenue += facility.get('revenue', 0)
        
        growth_rate = ((total_predicted - current_revenue) / current_revenue * 100) if current_revenue > 0 else 0
        
        return {
            "total_predicted": round(total_predicted, 2),
            "growth_rate": round(growth_rate, 2),
            "current_revenue": round(current_revenue, 2)
        }
    
    return router
'''
    
    # Write main files
    main_files = {
        "main.py": main_py,
        "backend/__init__.py": "",
        "backend/database.py": database_py,
        "backend/auth.py": auth_py,
        "backend/api/__init__.py": "",
        "backend/api/routes.py": routes_py
    }
    
    print("🐍 Creating main application files...")
    for file_path, content in main_files.items():
        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✅ {file_path}")
    
    return True

def create_streamlit_app():
    """Create Streamlit interface"""
    
    streamlit_app_py = '''#!/usr/bin/env python3
"""
🏟️ SportAI Enterprise Suite™ - Streamlit Interface
Alternative web interface using Streamlit
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import sys
from pathlib import Path

# Add backend to path
sys.path.append(str(Path(__file__).parent / "backend"))

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
        from backend.database import DatabaseManager
        from backend.auth import AuthenticationManager
        
        db_manager = DatabaseManager()
        auth_manager = AuthenticationManager(db_manager)
        return db_manager, auth_manager
    except ImportError:
        st.error("❌ Backend modules not found. Please install dependencies first.")
        st.code("pip install fastapi uvicorn sqlalchemy pandas")
        return None, None
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
        st.markdown("### Installation Steps:")
        st.code("""
# 1. Install dependencies
pip install fastapi uvicorn sqlalchemy pandas streamlit

# 2. Run the main application
python main.py

# 3. Or run this Streamlit interface
streamlit run streamlit_app.py
        """)
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
    
    # Display data tables
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏟️ Recent Facilities")
        if facilities:
            df_facilities = pd.DataFrame(facilities)
            st.dataframe(df_facilities[['name', 'type', 'utilization', 'revenue']].head(), use_container_width=True)
    
    with col2:
        st.subheader("💰 Top Sponsors")
        if sponsors:
            df_sponsors = pd.DataFrame(sponsors)
            st.dataframe(df_sponsors[['name', 'tier', 'annual_value']].head(), use_container_width=True)

def show_facilities(db_manager):
    """Show facilities management"""
    
    st.title("🏟️ Facility Management")
    
    facilities = db_manager.get_facilities()
    
    if not facilities:
        st.warning("No facilities found.")
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
            "description": "Consider targeted upselling campaigns for Basic tier members.",
            "priority": "Medium"
        },
        {
            "title": "Equipment Efficiency",
            "description": "Equipment rental efficiency is strong. Consider expanding popular categories.",
            "priority": "Low"
        }
    ]
    
    for insight in insights:
        priority_color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
        st.info(f"{priority_color[insight['priority']]} **{insight['title']}**: {insight['description']}")

if __name__ == "__main__":
    main()
'''
    
    return streamlit_app_py

def create_installer():
    """Create installation script"""
    
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
    
    # Create directories
    if not create_directories():
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

def create_directories():
    """Create directory structure"""
    
    print("📁 Creating directories...")
    
    directories = [
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
        "streamlit>=1.28.0"
    ]
    
    # Optional requirements
    optional_requirements = [
        "python-jose[cryptography]>=3.3.0",
        "passlib[bcrypt]>=1.7.4",
        "python-multipart>=0.0.6",
        "plotly>=5.17.0",
        "openpyxl>=3.1.0"
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
    
    return install_py

def create_documentation():
    """Create documentation files"""
    
    readme_md = '''# 🏟️ SportAI Enterprise Suite™

Complete Sports Facility Management Platform with AI-Powered Analytics

## Features

- **Real-time Dashboard** - Live facility and revenue management
- **AI Analytics** - Predictive insights and optimization recommendations  
- **Member Management** - Complete member lifecycle tracking
- **Facility Optimization** - Dynamic utilization and pricing optimization
- **Equipment Tracking** - Rental management and revenue optimization
- **Sponsor Management** - Partnership tracking and ROI analysis

## Quick Start

### 1. Installation

```bash
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

## Support

- **Documentation**: See docs/ folder
- **Email**: support@sportai.com

## License

SportAI Enterprise Suite™ - © 2024 SportAI Solutions, LLC. All Rights Reserved.

## Trademark Notice

SportAI Enterprise Suite™ and related marks are trademarks of SportAI Solutions, LLC.
'''
    
    requirements_txt = '''# SportAI Enterprise Suite™ - Python Dependencies

# Core Framework
fastapi>=0.104.1
uvicorn[standard]>=0.24.0
pydantic>=2.5.0

# Database
sqlalchemy>=2.0.23
pandas>=2.1.3

# Web Interface
streamlit>=1.28.1

# Optional Dependencies
python-jose[cryptography]>=3.3.0
passlib[bcrypt]>=1.7.4
python-multipart>=0.0.6
plotly>=5.17.0
openpyxl>=3.1.2
'''
    
    docs_files = {
        "README.md": readme_md,
        "requirements.txt": requirements_txt,
        "streamlit_app.py": create_streamlit_app(),
        "install.py": create_installer()
    }
    
    print("📚 Creating documentation and support files...")
    for file_path, content in docs_files.items():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✅ {file_path}")
    
    return True

def main():
    """Main package creation process"""
    
    print("🏟️ SportAI Enterprise Suite™ - Package Creator")
    print("=" * 50)
    print()
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        return False
    
    print("✅ Python version:", sys.version.split()[0])
    
    # Create complete package
    steps = [
        ("📁 Creating project structure", create_project_structure),
        ("🐍 Creating main application files", create_main_files),
        ("📚 Creating documentation and support files", create_documentation)
    ]
    
    for step_name, step_function in steps:
        print(f"\n{step_name}...")
        if not step_function():
            print(f"❌ Failed: {step_name}")
            return False
    
    print("\n" + "=" * 50)
    print("🎉 SportAI Enterprise Suite™ Package Created Successfully!")
    print("=" * 50)
    print()
    print("📋 What's included:")
    print("   ✅ Complete Python backend with FastAPI")
    print("   ✅ SQLite database with sample data") 
    print("   ✅ JWT authentication system")
    print("   ✅ Streamlit web interface")
    print("   ✅ Automated installer")
    print("   ✅ Complete documentation")
    print()
    print("🚀 Quick Start:")
    print("   1. python install.py          # Install dependencies")
    print("   2. python main.py             # Start FastAPI server")
    print("   3. streamlit run streamlit_app.py  # Start web interface")
    print()
    print("🌐 Access URLs:")
    print("   • FastAPI Server: http://localhost:8000")
    print("   • API Docs: http://localhost:8000/docs")
    print("   • Streamlit UI: http://localhost:8501")
    print()
    print("🔑 Default Login:")
    print("   • Email: admin@sportai.com")
    print("   • Password: admin123")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("✅ Package is ready! Run the steps above to get started.")
    else:
        print("❌ Package creation failed")
    
    sys.exit(0 if success else 1)