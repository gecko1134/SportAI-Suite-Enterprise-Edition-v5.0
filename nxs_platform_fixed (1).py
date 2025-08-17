#!/usr/bin/env python3
"""
🏟️ NXS Sports AI Platform™ - Complete Enterprise Edition
© 2025 NXS Complex Solutions, LLC. All Rights Reserved.

Enterprise-Grade AI-Powered Sports Facility Management Platform
Licensed Software Solution for Multi-Facility Operations

TRADEMARK: NXS Sports AI Platform™
LICENSE: Commercial Enterprise License
VERSION: 4.0.0 Enterprise Edition
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import hashlib
import uuid
import time
import random
import sqlite3
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum

# Handle optional dependencies with fallbacks
try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# =============================================================================
# PLATFORM CONFIGURATION
# =============================================================================

class LicenseType(Enum):
    STARTER = "starter"
    PROFESSIONAL = "professional" 
    ENTERPRISE = "enterprise"

@dataclass
class LicenseInfo:
    license_key: str
    facility_name: str
    license_type: LicenseType
    max_users: int
    max_facilities: int
    expiry_date: datetime
    features_enabled: List[str]
    api_access: bool
    white_label: bool

class PlatformConfig:
    """Global platform configuration and licensing"""
    
    APP_NAME = "NXS Sports AI Platform™"
    VERSION = "4.0.0 Enterprise"
    COPYRIGHT = "© 2025 NXS Complex Solutions, LLC"
    TRADEMARK = "NXS Sports AI Platform™"
    
    FEATURE_MATRIX = {
        LicenseType.STARTER: {
            "max_users": 5,
            "max_facilities": 1,
            "ai_modules": False,
            "api_access": False,
            "white_label": False,
            "price_monthly": 99
        },
        LicenseType.PROFESSIONAL: {
            "max_users": 25,
            "max_facilities": 3,
            "ai_modules": True,
            "api_access": True,
            "white_label": True,
            "price_monthly": 299
        },
        LicenseType.ENTERPRISE: {
            "max_users": float('inf'),
            "max_facilities": float('inf'),
            "ai_modules": True,
            "api_access": True,
            "white_label": True,
            "price_monthly": "Custom"
        }
    }

# =============================================================================
# AUTHENTICATION & LICENSING
# =============================================================================

class LicenseManager:
    """Advanced licensing and subscription management"""
    
    def validate_license(self, license_key: str) -> Optional[LicenseInfo]:
        """Validate license and return license information"""
        try:
            if license_key == "DEMO-LICENSE-KEY":
                return LicenseInfo(
                    license_key="DEMO-LICENSE-KEY",
                    facility_name="NXS Sports Complex Demo",
                    license_type=LicenseType.ENTERPRISE,
                    max_users=100,
                    max_facilities=5,
                    expiry_date=datetime.now() + timedelta(days=30),
                    features_enabled=["all"],
                    api_access=True,
                    white_label=False
                )
            return None
        except Exception as e:
            st.error(f"License validation error: {str(e)}")
            return None

class AuthenticationManager:
    """Enterprise-grade authentication system"""
    
    def __init__(self, license_manager: LicenseManager):
        self.license_manager = license_manager
        
    def authenticate_user(self, email: str, password: str) -> bool:
        """Authenticate user credentials"""
        demo_users = {
            "admin@nxs.com": "admin123",
            "manager@nxs.com": "manager123",
            "coach@nxs.com": "coach123",
            "athlete@nxs.com": "athlete123"
        }
        return demo_users.get(email) == password

# =============================================================================
# AI ANALYTICS ENGINE
# =============================================================================

class AIAnalyticsEngine:
    """Real-time AI analytics and optimization engine"""
    
    def __init__(self):
        self.models_loaded = False
        
    def load_ai_models(self):
        """Load all AI models for real-time processing"""
        try:
            self.models = {
                'demand_forecasting': {
                    'name': 'Advanced Demand Forecasting',
                    'accuracy': 0.94,
                    'predictions_24h': self._generate_demand_predictions()
                },
                'revenue_optimization': {
                    'name': 'Dynamic Revenue Optimizer', 
                    'accuracy': 0.91,
                    'optimizations': self._generate_optimizations()
                }
            }
            self.models_loaded = True
        except Exception as e:
            st.error(f"Error loading AI models: {str(e)}")
            self.models = {}
    
    def _generate_demand_predictions(self):
        """Generate 24-hour demand predictions"""
        return [
            {
                'hour': hour,
                'predicted_occupancy': random.uniform(0.3, 0.95),
                'confidence': random.uniform(0.85, 0.98)
            }
            for hour in range(24)
        ]
    
    def _generate_optimizations(self):
        """Generate optimization suggestions"""
        return [
            {
                "type": "pricing",
                "suggestion": "Increase peak hour rates by 15%",
                "impact": "+$2,400/month",
                "confidence": 0.92
            }
        ]
    
    def get_real_time_metrics(self):
        """Get current real-time facility metrics"""
        try:
            return {
                'total_occupancy': random.uniform(0.65, 0.85),
                'revenue_today': random.uniform(8000, 12000),
                'energy_efficiency': random.uniform(0.88, 0.96),
                'member_satisfaction': random.uniform(4.2, 4.8)
            }
        except Exception as e:
            st.error(f"Error getting metrics: {str(e)}")
            return {
                'total_occupancy': 0.75,
                'revenue_today': 10000,
                'energy_efficiency': 0.90,
                'member_satisfaction': 4.5
            }

# =============================================================================
# DATA PROCESSING
# =============================================================================

class RealTimeDataProcessor:
    """Handles real-time data streams and processing"""
    
    def simulate_member_activity(self):
        """Simulate real-time member activity"""
        try:
            activities = ['basketball', 'soccer', 'fitness', 'swimming', 'tennis']
            return [
                {
                    'member_id': f'M{random.randint(1000, 9999)}',
                    'activity': random.choice(activities),
                    'duration_minutes': random.randint(30, 120),
                    'location': f'Area {random.randint(1, 5)}',
                    'timestamp': datetime.now() - timedelta(minutes=random.randint(0, 180))
                }
                for _ in range(random.randint(5, 15))
            ]
        except Exception as e:
            st.error(f"Error simulating activity: {str(e)}")
            return []
    
    def simulate_transactions(self):
        """Simulate real-time financial transactions"""
        try:
            transaction_types = ['membership', 'facility_booking', 'merchandise', 'concession']
            return [
                {
                    'transaction_id': str(uuid.uuid4())[:8],
                    'type': random.choice(transaction_types),
                    'amount': random.uniform(10, 200),
                    'payment_method': random.choice(['card', 'cash', 'mobile']),
                    'timestamp': datetime.now() - timedelta(minutes=random.randint(0, 60))
                }
                for _ in range(random.randint(3, 8))
            ]
        except Exception as e:
            st.error(f"Error simulating transactions: {str(e)}")
            return []

# =============================================================================
# CHART FUNCTIONS WITH FALLBACKS
# =============================================================================

def render_chart(data, x_col, y_col, title, chart_type="line"):
    """Render chart with fallback to streamlit native charts"""
    try:
        if PLOTLY_AVAILABLE and len(data) > 0:
            if chart_type == "line":
                fig = px.line(data, x=x_col, y=y_col, title=title)
            else:
                fig = px.bar(data, x=x_col, y=y_col, title=title)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.markdown(f"### {title}")
            if len(data) > 0:
                if chart_type == "line":
                    st.line_chart(data.set_index(x_col)[y_col])
                else:
                    st.bar_chart(data.set_index(x_col)[y_col])
            else:
                st.info("No data available for chart")
    except Exception as e:
        st.error(f"Error rendering chart: {str(e)}")
        st.info("Chart data temporarily unavailable")

# =============================================================================
# ENTERPRISE DASHBOARD
# =============================================================================

class EnterpriseDashboard:
    """Main enterprise dashboard with all modules"""
    
    def __init__(self, license_info: LicenseInfo, ai_engine: AIAnalyticsEngine):
        self.license_info = license_info
        self.ai_engine = ai_engine
        self.data_processor = RealTimeDataProcessor()
        
    def render_main_interface(self):
        """Render the main enterprise interface"""
        try:
            st.set_page_config(
                page_title=self.license_info.facility_name,
                page_icon="🏟️",
                layout="wide"
            )
            
            self._apply_styling()
            self._render_header()
            self._render_navigation()
        except Exception as e:
            st.error(f"Error rendering interface: {str(e)}")
            st.info("Please refresh the page or contact support")
    
    def _apply_styling(self):
        """Apply custom CSS styling"""
        
        st.markdown("""
        <style>
            .main-header {
                background: linear-gradient(135deg, #1f77b4, #ff7f0e);
                padding: 2rem;
                border-radius: 15px;
                margin-bottom: 2rem;
                color: white;
                text-align: center;
            }
            .metric-card {
                background: white;
                padding: 1.5rem;
                border-radius: 10px;
                border-left: 4px solid #1f77b4;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                margin-bottom: 1rem;
            }
            .status-active {
                color: #28a745;
                font-weight: bold;
                background: #d4edda;
                padding: 4px 8px;
                border-radius: 4px;
            }
            .status-warning {
                color: #856404;
                font-weight: bold;
                background: #fff3cd;
                padding: 4px 8px;
                border-radius: 4px;
            }
            .license-info {
                background: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 1rem;
                margin: 1rem 0;
                font-size: 0.9rem;
            }
        </style>
        """, unsafe_allow_html=True)
    
    def _render_header(self):
        """Render the main header"""
        try:
            st.markdown(f"""
            <div class="main-header">
                <h1>🏟️ {self.license_info.facility_name}</h1>
                <p>{PlatformConfig.APP_NAME} - Enterprise Management Platform</p>
                <p>License: {self.license_info.license_type.value.title()}</p>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error rendering header: {str(e)}")
    
    def _render_navigation(self):
        """Render main navigation"""
        try:
            # Get features with error handling
            features = self._get_license_features()
            
            available_modules = ["🏠 Real-Time Dashboard", "👥 Member Management", "🏟️ Facility Management"]
            
            if features.get("ai_modules", False):
                available_modules.append("🤖 AI Analytics")
            
            if features.get("api_access", False):
                available_modules.append("🔌 API Management")
            
            # Logout button
            if st.sidebar.button("🚪 Logout"):
                st.session_state.authenticated = False
                st.rerun()
            
            selected_module = st.sidebar.selectbox("🧭 Navigate Platform", available_modules)
            
            self._render_license_info()
            self._route_to_module(selected_module, features)
            
        except Exception as e:
            st.error(f"Navigation error: {str(e)}")
            # Fallback to basic interface
            st.markdown("## 🏠 Dashboard")
            st.info("Navigation temporarily unavailable. Showing basic dashboard.")
            self._render_basic_dashboard()
    
    def _get_license_features(self):
        """Get license features with error handling"""
        try:
            # Ensure license_type is correct type
            if hasattr(self.license_info, 'license_type'):
                license_type = self.license_info.license_type
                
                # Handle both enum and string types
                if isinstance(license_type, str):
                    # Convert string to enum
                    for enum_type in LicenseType:
                        if enum_type.value == license_type.lower():
                            license_type = enum_type
                            break
                    else:
                        # Default to ENTERPRISE if not found
                        license_type = LicenseType.ENTERPRISE
                
                return PlatformConfig.FEATURE_MATRIX.get(license_type, PlatformConfig.FEATURE_MATRIX[LicenseType.ENTERPRISE])
            else:
                # Fallback to enterprise features
                return PlatformConfig.FEATURE_MATRIX[LicenseType.ENTERPRISE]
                
        except Exception as e:
            st.error(f"Error getting license features: {str(e)}")
            # Return enterprise features as fallback
            return {
                "max_users": float('inf'),
                "max_facilities": float('inf'),
                "ai_modules": True,
                "api_access": True,
                "white_label": True,
                "price_monthly": "Custom"
            }
    
    def _render_license_info(self):
        """Render license information in sidebar"""
        try:
            st.sidebar.markdown("---")
            st.sidebar.markdown("### 📋 License Information")
            
            features = self._get_license_features()
            
            st.sidebar.markdown(f"""
            <div class="license-info">
                <strong>License:</strong> {self.license_info.license_type.value.title()}<br>
                <strong>Facility:</strong> {self.license_info.facility_name}<br>
                <strong>AI Modules:</strong> {'✅' if features.get('ai_modules', False) else '❌'}<br>
                <strong>API Access:</strong> {'✅' if features.get('api_access', False) else '❌'}<br>
                <strong>Price:</strong> ${features.get('price_monthly', 'N/A')}/month
            </div>
            """, unsafe_allow_html=True)
            
            st.sidebar.markdown(f"*{PlatformConfig.COPYRIGHT}*")
        except Exception as e:
            st.sidebar.error(f"License info error: {str(e)}")
    
    def _route_to_module(self, selected_module: str, features: Dict):
        """Route to the selected module"""
        try:
            if "Real-Time Dashboard" in selected_module:
                self._render_dashboard()
            elif "Member Management" in selected_module:
                self._render_member_management()
            elif "Facility Management" in selected_module:
                self._render_facility_management()
            elif "AI Analytics" in selected_module and features.get("ai_modules", False):
                self._render_ai_analytics()
            elif "API Management" in selected_module and features.get("api_access", False):
                self._render_api_management()
            else:
                st.info("🔒 This module requires a higher license tier")
        except Exception as e:
            st.error(f"Module routing error: {str(e)}")
            self._render_basic_dashboard()
    
    def _render_basic_dashboard(self):
        """Render basic dashboard as fallback"""
        st.markdown("## 📊 Basic Dashboard")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Facility Status", "Online", "✅ Active")
        with col2:
            st.metric("Current Time", datetime.now().strftime("%H:%M"))
        with col3:
            st.metric("License", "Valid", "✅ Active")
        with col4:
            st.metric("System", "Operational", "🟢 Good")
    
    def _render_dashboard(self):
        """Render the real-time dashboard"""
        try:
            st.markdown("## 📊 Real-Time Facility Overview")
            
            metrics = self.ai_engine.get_real_time_metrics()
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("🏟️ Facility Utilization", f"{metrics['total_occupancy']:.1%}", "+5.2%")
            
            with col2:
                st.metric("💰 Today's Revenue", f"${metrics['revenue_today']:,.0f}", "+12.1%")
            
            with col3:
                st.metric("⚡ Energy Efficiency", f"{metrics['energy_efficiency']:.1%}", "+3.4%")
            
            with col4:
                st.metric("😊 Member Satisfaction", f"{metrics['member_satisfaction']:.1f}/5.0", "+0.2")
            
            # AI Insights
            features = self._get_license_features()
            if features.get("ai_modules", False):
                st.markdown("### 🤖 AI-Powered Insights")
                
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown("#### 📈 Revenue Optimization Impact")
                    
                    hours = [f"{i:02d}:00" for i in range(6, 23)]
                    opt_data = pd.DataFrame({
                        'Hour': hours,
                        'Revenue_Impact': [random.uniform(5, 30) for _ in hours]
                    })
                    
                    render_chart(opt_data, 'Hour', 'Revenue_Impact', 'AI Revenue Optimization (%)', 'line')
                
                with col2:
                    st.markdown("#### 🎯 Smart Recommendations")
                    
                    with st.expander("🔴 High Priority - Peak Hour Pricing"):
                        st.write("**Suggestion:** Increase basketball court rates by 18%")
                        st.write("**Impact:** +$2,400/month")
                        st.write("**Confidence:** 94%")
                        
                        if st.button("✅ Implement"):
                            st.success("Recommendation implemented!")
            
            # Live Activity Feed
            st.markdown("### 🔄 Live Activity Feed")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("#### 🏃‍♂️ Current Member Activity")
                
                activities = self.data_processor.simulate_member_activity()
                recent = sorted(activities, key=lambda x: x['timestamp'], reverse=True)[:5]
                
                if recent:
                    for activity in recent:
                        time_ago = (datetime.now() - activity['timestamp']).seconds // 60
                        st.markdown(f"""
                        <div style="padding: 10px; border-left: 3px solid #1f77b4; margin: 5px 0; background: #f8f9fa;">
                            <strong>{activity['member_id']}</strong> - {activity['activity'].title()}<br>
                            <small>{activity['duration_minutes']} min @ {activity['location']} • {time_ago}m ago</small>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No recent activity data")
            
            with col2:
                st.markdown("#### 💳 Recent Transactions")
                
                transactions = self.data_processor.simulate_transactions()
                recent_txn = sorted(transactions, key=lambda x: x['timestamp'], reverse=True)[:5]
                
                if recent_txn:
                    total = sum(t['amount'] for t in recent_txn)
                    st.metric("Last Hour Revenue", f"${total:.2f}")
                    
                    for txn in recent_txn:
                        time_ago = (datetime.now() - txn['timestamp']).seconds // 60
                        st.markdown(f"""
                        <div style="padding: 8px; background: #e8f5e8; margin: 3px 0; border-radius: 5px;">
                            <strong>${txn['amount']:.2f}</strong> - {txn['type'].replace('_', ' ').title()}<br>
                            <small>{txn['payment_method'].title()} • {time_ago}m ago</small>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No recent transactions")
                    
        except Exception as e:
            st.error(f"Dashboard error: {str(e)}")
            self._render_basic_dashboard()
    
    def _render_member_management(self):
        """Render member management module"""
        try:
            st.markdown("## 👥 Member Management System")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Members", "1,247", "+23")
            with col2:
                st.metric("Active Today", "342", "+8%")
            with col3:
                st.metric("Retention Rate", "94.2%", "+2.1%")
            with col4:
                st.metric("Monthly Revenue", "$127", "+$12")
            
            tab1, tab2, tab3 = st.tabs(["📋 Member List", "📊 Analytics", "🎯 Retention"])
            
            with tab1:
                st.markdown("### 📋 Member Directory")
                
                # Generate sample member data
                members = []
                for i in range(20):
                    members.append({
                        "ID": f"M{1000+i:04d}",
                        "Name": f"{random.choice(['John', 'Sarah', 'Mike', 'Lisa'])} {random.choice(['Smith', 'Johnson', 'Brown'])}",
                        "Tier": random.choice(["Basic", "Premium", "Elite"]),
                        "Status": random.choice(["Active", "Active", "Inactive"]),
                        "Monthly Fee": random.choice([49, 89, 149])
                    })
                
                df = pd.DataFrame(members)
                st.dataframe(df, use_container_width=True)
                
                if st.button("📧 Send Newsletter"):
                    st.success("Newsletter sent to all members!")
            
            with tab2:
                st.markdown("### 📊 Member Analytics")
                
                # Member growth data
                dates = pd.date_range('2024-01-01', '2024-12-31', freq='M')
                growth_data = pd.DataFrame({
                    'Month': [d.strftime('%Y-%m') for d in dates],
                    'Members': [800 + i*30 + random.randint(-10, 20) for i in range(len(dates))]
                })
                
                render_chart(growth_data, 'Month', 'Members', 'Member Growth Over Time', 'line')
            
            with tab3:
                features = self._get_license_features()
                if features.get("ai_modules", False):
                    st.markdown("### 🎯 AI-Powered Retention")
                    
                    at_risk = [
                        {
                            "name": "Mike Davis",
                            "risk": 0.87,
                            "days": 12,
                            "action": "Personal outreach + 20% discount"
                        }
                    ]
                    
                    for member in at_risk:
                        with st.expander(f"🚨 {member['name']} - Risk: {member['risk']:.0%}"):
                            st.write(f"Days since visit: {member['days']}")
                            st.write(f"Recommendation: {member['action']}")
                            
                            if st.button(f"Contact {member['name'].split()[0]}"):
                                st.success(f"Retention specialist assigned!")
                else:
                    st.info("🔒 AI retention features require Professional+ license")
                    
        except Exception as e:
            st.error(f"Member management error: {str(e)}")
    
    def _render_facility_management(self):
        """Render facility management module"""
        try:
            st.markdown("## 🏟️ Facility Management System")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Facilities", "12", "+1")
            with col2:
                st.metric("Utilization", "78.4%", "+5.2%")
            with col3:
                st.metric("Maintenance Score", "94.2%", "+1.8%")
            with col4:
                st.metric("Energy Efficiency", "91.7%", "+3.1%")
            
            st.markdown("### 🏢 Facility Status")
            
            facilities = [
                {"name": "Basketball Court", "status": "Active", "occupancy": 0.85},
                {"name": "Soccer Field", "status": "Active", "occupancy": 0.45},
                {"name": "Swimming Pool", "status": "Maintenance", "occupancy": 0.0},
                {"name": "Fitness Center", "status": "Active", "occupancy": 0.92}
            ]
            
            for facility in facilities:
                occ_pct = facility["occupancy"] * 100
                status_class = "status-active" if facility["status"] == "Active" else "status-warning"
                
                st.markdown(f"""
                <div class="metric-card">
                    <h4>🏟️ {facility['name']}</h4>
                    <p><strong>Status:</strong> <span class="{status_class}">{facility['status']}</span></p>
                    <p><strong>Occupancy:</strong> {occ_pct:.0f}%</p>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Facility management error: {str(e)}")
    
    def _render_ai_analytics(self):
        """Render AI analytics module"""
        try:
            st.markdown("## 🤖 AI Analytics & Intelligence")
            
            if not self.ai_engine.models_loaded:
                with st.spinner("Loading AI models..."):
                    self.ai_engine.load_ai_models()
            
            st.markdown("### 🧠 AI Model Status")
            
            if hasattr(self.ai_engine, 'models') and self.ai_engine.models:
                for name, model in self.ai_engine.models.items():
                    st.markdown(f"""
                    <div class="metric-card">
                        <h4>{model['name']}</h4>
                        <p>Accuracy: {model['accuracy']*100:.1f}%</p>
                        <p>Status: <span class="status-active">Active</span></p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Predictions
                st.markdown("### 🔮 Predictions")
                
                if 'demand_forecasting' in self.ai_engine.models:
                    predictions = self.ai_engine.models['demand_forecasting']['predictions_24h']
                    pred_df = pd.DataFrame(predictions)
                    
                    render_chart(pred_df, 'hour', 'predicted_occupancy', '24-Hour Occupancy Forecast', 'line')
                else:
                    st.info("Demand forecasting model not available")
            else:
                st.warning("AI models not loaded. Please refresh the page.")
        except Exception as e:
            st.error(f"AI analytics error: {str(e)}")
    
    def _render_api_management(self):
        """Render API management module"""
        try:
            st.markdown("## 🔌 API Management")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("API Calls Today", "2,847", "+312")
            with col2:
                st.metric("Active Keys", "3", "+1")
            with col3:
                st.metric("Response Time", "127ms", "-23ms")
            with col4:
                st.metric("Success Rate", "99.7%", "+0.2%")
            
            st.markdown("### 🔑 API Keys")
            
            keys = [
                {"name": "Main App", "key": "nxs_live_abc123...xyz789", "calls": 2847, "status": "Active"}
            ]
            
            for key in keys:
                with st.expander(f"🔑 {key['name']} - {key['status']}"):
                    st.code(key['key'])
                    st.write(f"Calls today: {key['calls']:,}")
                    
                    if st.button("🔄 Regenerate", key=f"regen_{key['name']}"):
                        st.success("API key regenerated!")
        except Exception as e:
            st.error(f"API management error: {str(e)}")

# =============================================================================
# LOGIN INTERFACE
# =============================================================================

def render_login(auth_manager, license_manager):
    """Render login interface with error handling"""
    
    try:
        st.set_page_config(
            page_title="NXS Sports AI Platform™", 
            page_icon="🏟️", 
            layout="centered"
        )
        
        st.markdown("""
        <style>
            .login-header {
                text-align: center;
                padding: 2rem;
                background: linear-gradient(135deg, #1f77b4, #ff7f0e);
                color: white;
                border-radius: 15px;
                margin-bottom: 2rem;
            }
            .login-form {
                background: white;
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="login-header">
            <h1>🏟️ {PlatformConfig.APP_NAME}</h1>
            <p>Enterprise Sports Facility Management</p>
            <p>Version {PlatformConfig.VERSION}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown('<div class="login-form">', unsafe_allow_html=True)
            
            st.markdown("### 🔑 License Validation")
            license_key = st.text_input("License Key", value="DEMO-LICENSE-KEY")
            
            st.markdown("### 👤 User Authentication")
            email = st.text_input("Email", value="admin@nxs.com")
            password = st.text_input("Password", type="password", value="admin123")
            
            if st.button("🚀 Login to Platform", use_container_width=True):
                try:
                    # Validate license
                    license_info = license_manager.validate_license(license_key)
                    
                    if not license_info:
                        st.error("❌ Invalid license key")
                        return
                    
                    # Authenticate user
                    if auth_manager.authenticate_user(email, password):
                        # Store in session state
                        st.session_state.authenticated = True
                        st.session_state.license_info = license_info
                        st.session_state.user_info = {
                            "email": email,
                            "role": "admin" if "admin" in email else "manager",
                            "name": "Demo User",
                            "login_time": datetime.now()
                        }
                        
                        st.success("✅ Login successful!")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("❌ Invalid credentials")
                        
                except Exception as e:
                    st.error(f"Login error: {str(e)}")
                    st.info("Please try again or contact support")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Demo information
            with st.expander("🎭 Demo Accounts"):
                st.markdown("""
                **Admin:** admin@nxs.com / admin123
                **Manager:** manager@nxs.com / manager123
                **Coach:** coach@nxs.com / coach123
                **Athlete:** athlete@nxs.com / athlete123
                **License:** DEMO-LICENSE-KEY
                """)
            
            # Licensing information
            with st.expander("💼 Licensing Information"):
                st.markdown("""
                **Available License Types:**
                
                **Starter** - $99/month
                - 5 users, 1 facility
                - Basic features only
                
                **Professional** - $299/month  
                - 25 users, 3 facilities
                - AI modules included
                - API access
                
                **Enterprise** - Custom pricing
                - Unlimited users & facilities
                - All features included
                - Priority support
                """)
            
            # Support information
            with st.expander("🆘 Need Help?"):
                st.markdown("""
                **Common Issues:**
                - Make sure to use the demo license key: DEMO-LICENSE-KEY
                - Try refreshing the page if login fails
                - Contact support@nxssports.com for assistance
                
                **System Requirements:**
                - Modern web browser (Chrome, Firefox, Safari, Edge)
                - Internet connection
                - JavaScript enabled
                """)
            
            st.markdown("---")
            st.markdown(f"""
            <div style="text-align: center; color: #666; font-size: 0.8rem;">
                {PlatformConfig.COPYRIGHT}<br>
                {PlatformConfig.TRADEMARK} is a registered trademark.<br>
                All rights reserved. Patent pending.
            </div>
            """, unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"Login interface error: {str(e)}")
        st.markdown("## Emergency Login")
        st.info("Please contact support if you continue to experience issues")
        
        # Emergency login button
        if st.button("🚨 Emergency Access"):
            try:
                # Create emergency license
                emergency_license = LicenseInfo(
                    license_key="EMERGENCY",
                    facility_name="Emergency Access",
                    license_type=LicenseType.ENTERPRISE,
                    max_users=1,
                    max_facilities=1,
                    expiry_date=datetime.now() + timedelta(hours=1),
                    features_enabled=["basic"],
                    api_access=False,
                    white_label=False
                )
                
                st.session_state.authenticated = True
                st.session_state.license_info = emergency_license
                st.success("Emergency access granted for 1 hour")
                st.rerun()
                
            except Exception as emergency_error:
                st.error(f"Emergency access failed: {str(emergency_error)}")

# =============================================================================
# MAIN APPLICATION
# =============================================================================

def main():
    """Main application entry point with comprehensive error handling"""
    
    try:
        # Initialize managers with error handling
        license_manager = LicenseManager()
        auth_manager = AuthenticationManager(license_manager)
        ai_engine = AIAnalyticsEngine()
        
        # Initialize session state safely
        if 'authenticated' not in st.session_state:
            st.session_state.authenticated = False
        
        if 'license_info' not in st.session_state:
            st.session_state.license_info = None
        
        if not st.session_state.authenticated:
            render_login(auth_manager, license_manager)
            return
        
        # Validate license info exists
        if st.session_state.license_info is None:
            st.error("License information not found. Please log in again.")
            st.session_state.authenticated = False
            st.rerun()
            return
        
        license_info = st.session_state.license_info
        
        # Validate license_info has required attributes
        if not hasattr(license_info, 'license_type'):
            st.error("Invalid license information. Please log in again.")
            st.session_state.authenticated = False
            st.rerun()
            return
        
        # Create dashboard with error handling
        dashboard = EnterpriseDashboard(license_info, ai_engine)
        dashboard.render_main_interface()
        
    except Exception as e:
        st.error(f"Application error: {str(e)}")
        st.info("Please refresh the page. If the error persists, contact support.")
        
        # Provide basic functionality as fallback
        st.markdown("## 🏟️ NXS Sports AI Platform™")
        st.markdown("### Emergency Mode")
        
        if st.button("🔄 Reset Application"):
            # Clear session state and restart
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# =============================================================================
# APPLICATION STARTUP
# =============================================================================

if __name__ == "__main__":
    try:
        main()
    except Exception as startup_error:
        st.error(f"Startup error: {str(startup_error)}")
        st.markdown("## 🏟️ NXS Sports AI Platform™")
        st.error("The application encountered a startup error.")
        st.info("Please refresh the page or contact support@nxssports.com")
        
        # Show basic system info for debugging
        st.markdown("### System Information")
        st.write(f"**Time:** {datetime.now()}")
        st.write(f"**Python Version:** Available")
        st.write(f"**Streamlit Version:** Available") 
        st.write(f"**Error:** {str(startup_error)}")
        
        if st.button("🔄 Retry Application"):
            st.rerun()