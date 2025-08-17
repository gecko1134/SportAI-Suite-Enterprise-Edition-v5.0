                        "Recommended Action": "Class recommendation + free session",
                        "Value at Risk": "$1,788"
                    }
                ]
                
                for member in at_risk_members:
                    with st.expander(f"🚨 {member['Name']} - Risk Score: {member['Risk Score']:.0%}"):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.write(f"**Days Since Last Visit:** {member['Days Since Visit']}")
                            st.write(f"**Usage Trend:** {member['Decline Trend']}")
                            st.write(f"**Revenue at Risk:** {member['Value at Risk']}")
                        
                        with col2:
                            st.write(f"**AI Recommendation:** {member['Recommended Action']}")
                            
                            if st.button(f"📞 Contact {member['Name'].split()[0]}", key=f"contact_{member['Name']}"):
                                st.success(f"Retention specialist assigned to {member['Name']}")
                            
                            if st.button(f"🎁 Send Offer", key=f"offer_{member['Name']}"):
                                st.success(f"Personalized offer sent to {member['Name']}")
            else:
                st.info("🔒 AI-powered retention features available in Professional+ licenses")
    
    def _render_facility_management(self):
        """Render facility management module"""
        
        st.markdown("## 🏟️ Facility Management System")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Facilities", "12", delta="+1 new")
        with col2:
            st.metric("Current Utilization", "78.4%", delta="+5.2%")
        with col3:
            st.metric("Maintenance Score", "94.2%", delta="+1.8%")
        with col4:
            st.metric("Energy Efficiency", "91.7%", delta="+3.1%")
        
        # Facility management tabs
        tab1, tab2, tab3 = st.tabs(["🏢 Facility Overview", "📅 Booking Management", "🔧 Maintenance"])
        
        with tab1:
            st.markdown("### 🏢 Facility Status Overview")
            
            facilities = [
                {"name": "Main Basketball Court", "type": "Court", "capacity": 200, "status": "Active", "occupancy": 0.85},
                {"name": "Soccer Field A", "type": "Field", "capacity": 22, "status": "Active", "occupancy": 0.45},
                {"name": "Tennis Courts 1-4", "type": "Courts", "capacity": 8, "status": "Active", "occupancy": 0.75},
                {"name": "Swimming Pool", "type": "Pool", "capacity": 50, "status": "Maintenance", "occupancy": 0.0},
                {"name": "Fitness Center", "type": "Gym", "capacity": 80, "status": "Active", "occupancy": 0.92},
                {"name": "Volleyball Courts", "type": "Courts", "capacity": 12, "status": "Active", "occupancy": 0.33}
            ]
            
            # Display facilities in a grid
            cols = st.columns(2)
            
            for i, facility in enumerate(facilities):
                col = cols[i % 2]
                
                with col:
                    occupancy_pct = facility["occupancy"] * 100
                    
                    if facility["status"] == "Active":
                        status_class = "status-active"
                    elif facility["status"] == "Maintenance":
                        status_class = "status-warning"
                    else:
                        status_class = "status-warning"
                    
                    st.markdown(f"""
                    <div class="metric-card">
                        <h4>🏟️ {facility['name']}</h4>
                        <p><strong>Type:</strong> {facility['type']} | <strong>Capacity:</strong> {facility['capacity']}</p>
                        <p><strong>Status:</strong> <span class="{status_class}">{facility['status']}</span></p>
                        <p><strong>Current Occupancy:</strong> {occupancy_pct:.0f}%</p>
                        <div style="background: #e0e0e0; height: 10px; border-radius: 5px; margin: 5px 0;">
                            <div style="background: {'#28a745' if occupancy_pct < 80 else '#ffc107' if occupancy_pct < 95 else '#dc3545'}; 
                                        height: 100%; width: {occupancy_pct}%; border-radius: 5px;"></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Quick actions
            st.markdown("### 🎛️ Quick Controls")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                if st.button("🔄 Refresh All Status"):
                    st.success("All facility statuses updated!")
            
            with col2:
                if st.button("🚨 Emergency Mode"):
                    st.warning("Emergency protocols activated!")
            
            with col3:
                if st.button("🌙 Night Mode Setup"):
                    st.info("Facilities prepared for night mode")
            
            with col4:
                if st.button("📊 Generate Report"):
                    st.success("Facility report generated and sent to management")
        
        with tab2:
            st.markdown("### 📅 Booking Management System")
            
            # Booking overview
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Today's Bookings", "47", delta="+8")
            with col2:
                st.metric("Booking Rate", "89.2%", delta="+5.3%")
            with col3:
                st.metric("Revenue from Bookings", "$3,247", delta="+12.1%")
            
            # Recent bookings
            st.markdown("#### 📋 Recent Bookings")
            
            bookings_data = []
            for i in range(10):
                booking = {
                    "Time": f"{random.randint(6, 22):02d}:{random.choice(['00', '30'])}",
                    "Facility": random.choice(["Basketball Court", "Soccer Field", "Tennis Court", "Pool"]),
                    "Member": f"{random.choice(['John', 'Sarah', 'Mike', 'Lisa'])} {random.choice(['Smith', 'Johnson', 'Williams'])}",
                    "Duration": f"{random.choice([60, 90, 120])} min",
                    "Status": random.choice(["Confirmed", "Confirmed", "Pending", "Completed"]),
                    "Revenue": f"${random.randint(25, 150)}"
                }
                bookings_data.append(booking)
            
            df_bookings = pd.DataFrame(bookings_data)
            st.dataframe(df_bookings, use_container_width=True)
            
            # Booking actions
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("➕ New Booking"):
                    st.success("New booking form opened!")
            
            with col2:
                if st.button("📊 Booking Analytics"):
                    st.info("Detailed booking analytics displayed")
            
            with col3:
                if st.button("📧 Send Confirmations"):
                    st.success("Booking confirmations sent to all members")
        
        with tab3:
            st.markdown("### 🔧 Maintenance Management")
            
            # Maintenance overview
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Pending Tasks", "12", delta="+3")
            with col2:
                st.metric("Completed This Week", "28", delta="+5")
            with col3:
                st.metric("Maintenance Budget", "$15,400", delta="-8.2%")
            with col4:
                st.metric("Equipment Uptime", "96.8%", delta="+1.2%")
            
            # Maintenance tasks
            st.markdown("#### 🛠️ Active Maintenance Tasks")
            
            maintenance_tasks = [
                {
                    "Priority": "🔴 High",
                    "Task": "HVAC System Zone 3 - Filter Replacement",
                    "Facility": "Fitness Center",
                    "Assigned To": "Mike Johnson",
                    "Due Date": "2024-02-18",
                    "Estimated Cost": "$245"
                },
                {
                    "Priority": "🟡 Medium",
                    "Task": "Basketball Hoop Height Adjustment",
                    "Facility": "Main Court",
                    "Assigned To": "Sarah Wilson",
                    "Due Date": "2024-02-20",
                    "Estimated Cost": "$85"
                },
                {
                    "Priority": "🟢 Low",
                    "Task": "Pool Chemical Balance Check",
                    "Facility": "Swimming Pool",
                    "Assigned To": "David Brown",
                    "Due Date": "2024-02-22",
                    "Estimated Cost": "$35"
                }
            ]
            
            for task in maintenance_tasks:
                with st.expander(f"{task['Priority']} - {task['Task']}"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"**Facility:** {task['Facility']}")
                        st.write(f"**Assigned To:** {task['Assigned To']}")
                        st.write(f"**Due Date:** {task['Due Date']}")
                        st.write(f"**Estimated Cost:** {task['Estimated Cost']}")
                    
                    with col2:
                        if st.button(f"✅ Mark Complete", key=f"complete_{task['Task']}"):
                            st.success("Task marked as completed!")
                        
                        if st.button(f"📞 Contact Assignee", key=f"contact_{task['Task']}"):
                            st.info(f"Message sent to {task['Assigned To']}")
    
    def _render_ai_analytics(self):
        """Render AI analytics module"""
        
        st.markdown("## 🤖 AI Analytics & Intelligence")
        
        if not self.ai_engine.models_loaded:
            with st.spinner("Loading AI models..."):
                self.ai_engine.load_ai_models()
        
        st.markdown("### 🧠 AI Model Status")
        
        models = self.ai_engine.models
        
        col1, col2, col3 = st.columns(3)
        model_cols = [col1, col2, col3]
        
        for i, (model_name, model_data) in enumerate(models.items()):
            col = model_cols[i % 3]
            
            with col:
                st.markdown(f"""
                <div class="metric-card">
                    <h4>{model_data['name']}</h4>
                    <p><strong>Accuracy:</strong> {model_data.get('accuracy', 0.9)*100:.1f}%</p>
                    <p><strong>Status:</strong> <span class="status-active">Active</span></p>
                    <p><strong>Last Updated:</strong> {model_data.get('last_trained', datetime.now()).strftime('%Y-%m-%d')}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # AI analytics tabs
        tab1, tab2, tab3 = st.tabs(["🔮 Predictions", "🎯 Optimization", "⚠️ Alerts"])
        
        with tab1:
            st.markdown("### 🔮 AI Predictions Dashboard")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 📈 24-Hour Demand Forecast")
                
                predictions = models['demand_forecasting']['predictions_24h']
                forecast_df = pd.DataFrame(predictions)
                
                fig = create_line_chart(forecast_df, 'hour', 'predicted_occupancy', '24-Hour Facility Occupancy Forecast')
                render_chart(fig, forecast_df, 'hour', 'predicted_occupancy', 'line')
            
            with col2:
                st.markdown("#### 💰 Revenue Predictions")
                
                # Generate revenue prediction data
                hours = list(range(24))
                revenue_predictions = []
                
                for hour in hours:
                    if 17 <= hour <= 21:  # Peak hours
                        base_revenue = random.uniform(400, 600)
                    elif 6 <= hour <= 9:   # Morning
                        base_revenue = random.uniform(200, 300)
                    else:
                        base_revenue = random.uniform(50, 150)
                    
                    revenue_predictions.append({
                        'hour': hour,
                        'predicted_revenue': base_revenue
                    })
                
                revenue_df = pd.DataFrame(revenue_predictions)
                
                fig = create_bar_chart(revenue_df, 'hour', 'predicted_revenue', 'Hourly Revenue Predictions')
                render_chart(fig, revenue_df, 'hour', 'predicted_revenue', 'bar')
        
        with tab2:
            st.markdown("### 🎯 AI Optimization Recommendations")
            
            optimizations = models['revenue_optimization']['current_optimizations']
            
            for opt in optimizations:
                with st.expander(f"💡 {opt['type'].title()} Optimization"):
                    st.write(f"**Suggestion:** {opt['suggestion']}")
                    st.write(f"**Expected Impact:** {opt['impact']}")
                    st.write(f"**AI Confidence:** {opt['confidence']:.0%}")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if st.button(f"✅ Implement", key=f"opt_{opt['type']}"):
                            st.success("Optimization implemented successfully!")
                    
                    with col2:
                        if st.button(f"📊 View Details", key=f"details_{opt['type']}"):
                            st.info("Detailed analysis opened in new tab")
            
            # AI Performance Metrics
            st.markdown("### 📊 AI Performance Impact")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Revenue Increase", "+18.3%", delta="vs pre-AI period")
            with col2:
                st.metric("Cost Reduction", "-12.7%", delta="through optimization")
            with col3:
                st.metric("Efficiency Gain", "+24.1%", delta="operational improvement")
        
        with tab3:
            st.markdown("### ⚠️ AI-Powered Alerts & Maintenance")
            
            # Generate AI alerts
            ai_alerts = [
                {
                    "type": "maintenance",
                    "priority": "High",
                    "title": "HVAC Zone 3 - Predictive Alert",
                    "description": "AI detected unusual vibration patterns. Recommend inspection within 7 days.",
                    "confidence": 0.89,
                    "potential_cost": "$8,500"
                },
                {
                    "type": "revenue",
                    "priority": "Medium", 
                    "title": "Peak Hour Optimization",
                    "description": "AI identified opportunity to increase tennis court rates by 12% during 6-8 PM.",
                    "confidence": 0.94,
                    "potential_gain": "$1,200/month"
                },
                {
                    "type": "member",
                    "priority": "Medium",
                    "title": "Churn Risk Alert",
                    "description": "15 members showing early churn indicators. Intervention recommended.",
                    "confidence": 0.76,
                    "potential_loss": "$4,500"
                }
            ]
            
            for alert in ai_alerts:
                priority_color = "🔴" if alert['priority'] == 'High' else "🟡"
                
                with st.expander(f"{priority_color} {alert['title']} - {alert['confidence']:.0%} Confidence"):
                    st.write(f"**Type:** {alert['type'].title()}")
                    st.write(f"**Description:** {alert['description']}")
                    st.write(f"**AI Confidence:** {alert['confidence']:.0%}")
                    
                    if 'potential_cost' in alert:
                        st.write(f"**Potential Cost if Ignored:** {alert['potential_cost']}")
                    if 'potential_gain' in alert:
                        st.write(f"**Potential Gain:** {alert['potential_gain']}")
                    if 'potential_loss' in alert:
                        st.write(f"**Potential Revenue Loss:** {alert['potential_loss']}")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if st.button(f"🚀 Take Action", key=f"action_{alert['title']}"):
                            st.success("Action initiated based on AI recommendation!")
                    
                    with col2:
                        if st.button(f"📋 Create Task", key=f"task_{alert['title']}"):
                            st.info("Task created and assigned to appropriate team member")
    
    def _render_api_management(self):
        """Render API management module"""
        
        st.markdown("## 🔌 API Management & Integrations")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("API Calls Today", "2,847", delta="+312")
        with col2:
            st.metric("Active Integrations", "12", delta="+2")
        with col3:
            st.metric("Response Time", "127ms", delta="-23ms")
        with col4:
            st.metric("Success Rate", "99.7%", delta="+0.2%")
        
        # API management tabs
        tab1, tab2, tab3 = st.tabs(["🔑 API Keys", "📊 Usage Analytics", "🔗 Integrations"])
        
        with tab1:
            st.markdown("### 🔑 API Key Management")
            
            api_keys = [
                {
                    "name": "Main Application", 
                    "key": "nxs_live_abc123...xyz789",
                    "created": "2024-01-15",
                    "last_used": "2 minutes ago",
                    "calls_today": 2847,
                    "status": "Active"
                },
                {
                    "name": "Mobile App",
                    "key": "nxs_mobile_def456...uvw012",
                    "created": "2024-02-01", 
                    "last_used": "5 minutes ago",
                    "calls_today": 1205,
                    "status": "Active"
                }
            ]
            
            for key_info in api_keys:
                with st.expander(f"🔑 {key_info['name']} - {key_info['status']}"):
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.code(key_info['key'])
                        st.write(f"**Created:** {key_info['created']}")
                        st.write(f"**Last Used:** {key_info['last_used']}")
                        st.write(f"**Calls Today:** {key_info['calls_today']:,}")
                    
                    with col2:
                        if st.button("🔄 Regenerate", key=f"regen_{key_info['name']}"):
                            st.success("API key regenerated!")
                        
                        if st.button("📋 Copy", key=f"copy_{key_info['name']}"):
                            st.success("API key copied to clipboard!")
                        
                        if st.button("⏸️ Disable", key=f"disable_{key_info['name']}"):
                            st.warning("API key disabled")
            
            # Create new API key
            st.markdown("#### ➕ Create New API Key")
            
            with st.form("new_api_key"):
                key_name = st.text_input("Key Name", placeholder="e.g., Third-party Integration")
                permissions = st.multiselect("Permissions", [
                    "Read Members", "Write Members", "Read Bookings", "Write Bookings",
                    "Read Analytics", "Read Facilities"
                ])
                
                if st.form_submit_button("🔐 Generate API Key"):
                    if key_name:
                        new_key = f"nxs_live_{uuid.uuid4().hex[:16]}"
                        st.success(f"New API key created: `{new_key}`")
                        st.info("Store this key securely - it won't be shown again!")
        
        with tab2:
            st.markdown("### 📊 API Usage Analytics")
            
            # Generate sample API usage data
            dates = pd.date_range(start='2024-01-01', end='2024-02-15', freq='D')
            api_data = []
            
            for date in dates:
                calls = random.randint(1500, 4000)
                api_data.append({
                    'Date': date,
                    'API_Calls': calls,
                    'Success_Rate': random.uniform(98, 100)
                })
            
            df_api = pd.DataFrame(api_data)
            
            # API usage chart
            fig = create_line_chart(df_api, 'Date', 'API_Calls', 'Daily API Usage')
            render_chart(fig, df_api, 'Date', 'API_Calls', 'line')
            
            # API endpoints usage
            st.markdown("#### 🎯 Most Popular Endpoints")
            
            endpoints_data = [
                {"Endpoint": "/api/members", "Calls": 1247, "Avg Response": "89ms"},
                {"Endpoint": "/api/facilities", "Calls": 892, "Avg Response": "156ms"},
                {"Endpoint": "/api/bookings", "Calls": 634, "Avg Response": "203ms"},
                {"Endpoint": "/api/analytics", "Calls": 445, "Avg Response": "412ms"}
            ]
            
            df_endpoints = pd.DataFrame(endpoints_data)
            st.dataframe(df_endpoints, use_container_width=True)
        
        with tab3:
            st.markdown("### 🔗 Active Integrations")
            
            integrations = [
                {
                    "name": "Payment Gateway - Stripe",
                    "type": "Payment Processing",
                    "status": "Connected",
                    "last_sync": "2 minutes ago"
                },
                {
                    "name": "Email Service - SendGrid", 
                    "type": "Communication",
                    "status": "Connected",
                    "last_sync": "5 minutes ago"
                },
                {
                    "name": "Calendar - Google Calendar",
                    "type": "Scheduling",
                    "status": "Connected",
                    "last_sync": "1 hour ago"
                },
                {
                    "name": "Analytics - Google Analytics",
                    "type": "Web Analytics", 
                    "status": "Pending",
                    "last_sync": "Never"
                }
            ]
            
            for integration in integrations:
                status_class = "status-active" if integration['status'] == 'Connected' else "status-warning"
                
                with st.expander(f"🔗 {integration['name']} - {integration['status']}"):
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.write(f"**Type:** {integration['type']}")
                        st.write(f"**Status:** {integration['status']}")
                        st.write(f"**Last Sync:** {integration['last_sync']}")
                    
                    with col2:
                        if integration['status'] == 'Connected':
                            if st.button("🔄 Refresh", key=f"refresh_{integration['name']}"):
                                st.success("Integration refreshed!")
                        else:
                            if st.button("🔗 Connect", key=f"connect_{integration['name']}"):
                                st.success("Integration connected!")
    
    def _render_module_placeholder(self, module_name: str):
        """Render placeholder for unimplemented modules"""
        
        st.markdown(f"## {module_name}")
        
        st.info(f"""
        🚧 **Module Under Development**
        
        The {module_name.split(' ', 1)[1]} module is currently being developed and will be available in the next release.
        
        **Expected Features:**
        - Real-time data processing
        - Advanced analytics and reporting
        - AI-powered insights and recommendations
        - Mobile-responsive interface
        - API integration support
        
        **Release Timeline:** Q2 2025
        """)
        
        # Demo contact form
        st.markdown("### 💬 Request Early Access")
        
        with st.form(f"early_access_{module_name}"):
            email = st.text_input("Email Address")
            message = st.text_area("What features are you most interested in?")
            submitted = st.form_submit_button("Request Access")
            
            if submitted and email:
                st.success("Thank you! We'll contact you when this module is available.")

# =============================================================================
# MAIN APPLICATION
# =============================================================================

def main():
    """Main application entry point"""
    
    license_manager = LicenseManager()
    auth_manager = AuthenticationManager(license_manager)
    ai_engine = AIAnalyticsEngine()
    
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.license_info = None
    
    if not st.session_state.authenticated:
        render_login_interface(auth_manager, license_manager)
        return
    
    license_info = st.session_state.license_info
    dashboard = EnterpriseDashboard(license_info, ai_engine)
    dashboard.render_main_interface()

def render_login_interface(auth_manager: AuthenticationManager, license_manager: LicenseManager):
    """Render login interface"""
    
    st.set_page_config(
        page_title="NXS Sports AI Platform™ - Login",
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
    
    # Header
    st.markdown(f"""
    <div class="login-header">
        <h1>🏟️ {PlatformConfig.APP_NAME}</h1>
        <p>Enterprise Sports Facility Management</p>
        <p><em>Version {PlatformConfig.VERSION}</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Login form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="login-form">', unsafe_allow_html=True)
        
        # License key input
        st.markdown("### 🔑 License Validation")
        license_key = st.text_input(
            "License Key",
            value="DEMO-LICENSE-KEY",
            help="Enter your facility's license key"
        )
        
        # User credentials
        st.markdown("### 👤 User Authentication")
        email = st.text_input("Email", value="admin@nxs.com")
        password = st.text_input("Password", type="password", value="admin123")
        
        # Login button
        if st.button("🚀 Login to Platform", use_container_width=True):
            
            # Validate license first
            license_info = license_manager.validate_license(license_key)
            
            if not license_info:
                st.error("❌ Invalid or expired license key")
                return
            
            # Authenticate user
            if auth_manager.authenticate_user(email, password):
                st.session_state.authenticated = True
                st.session_state.license_info = license_info
                st.session_state.user_info = {
                    "email": email,
                    "role": "admin" if "admin" in email else "manager",
                    "name": "Demo User",
                    "login_time": datetime.now()
                }
                st.success("✅ Login successful! Redirecting...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("❌ Invalid credentials")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Demo information
        with st.expander("🎭 Demo Accounts"):
            st.markdown("""
            **Administrator Access:**
            - Email: admin@nxs.com
            - Password: admin123
            
            **Manager Access:**
            - Email: manager@nxs.com  
            - Password: manager123
            
            **Coach Access:**
            - Email: coach@nxs.com
            - Password: coach123
            
            **Athlete Access:**
            - Email: athlete@nxs.com
            - Password: athlete123
            
            **License Key:** DEMO-LICENSE-KEY
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
        
        # Copyright notice
        st.markdown("---")
        st.markdown(f"""
        <div style="text-align: center; color: #666; font-size: 0.8rem;">
            {PlatformConfig.COPYRIGHT}<br>
            {PlatformConfig.TRADEMARK} is a registered trademark.<br>
            All rights reserved. Patent pending.
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()#!/usr/bin/env python3
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
    st.warning("⚠️ Plotly not available. Using basic charts.")

# =============================================================================
# PLATFORM CONFIGURATION
# =============================================================================

class LicenseType(Enum):
    STARTER = "starter"
    PROFESSIONAL = "professional"
    ENTERPRISE = "enterprise"
    WHITE_LABEL = "white_label"

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
            "real_time_analytics": False,
            "advanced_reporting": False,
            "price_monthly": 99
        },
        LicenseType.PROFESSIONAL: {
            "max_users": 25,
            "max_facilities": 3,
            "ai_modules": True,
            "api_access": True,
            "white_label": True,
            "real_time_analytics": True,
            "advanced_reporting": True,
            "price_monthly": 299
        },
        LicenseType.ENTERPRISE: {
            "max_users": float('inf'),
            "max_facilities": float('inf'),
            "ai_modules": True,
            "api_access": True,
            "white_label": True,
            "real_time_analytics": True,
            "advanced_reporting": True,
            "price_monthly": "Custom"
        }
    }

# =============================================================================
# AUTHENTICATION & LICENSING
# =============================================================================

class LicenseManager:
    """Advanced licensing and subscription management"""
    
    def __init__(self):
        pass
        
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
        except Exception:
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
        self.models = {
            'demand_forecasting': {
                'name': 'Advanced Demand Forecasting',
                'accuracy': 0.94,
                'last_trained': datetime.now() - timedelta(days=1),
                'predictions_24h': self._generate_demand_predictions()
            },
            'revenue_optimization': {
                'name': 'Dynamic Revenue Optimizer',
                'accuracy': 0.91,
                'current_optimizations': self._generate_revenue_optimizations()
            },
            'churn_prediction': {
                'name': 'Member Retention AI',
                'accuracy': 0.88,
                'at_risk_members': self._identify_at_risk_members()
            }
        }
        self.models_loaded = True
    
    def _generate_demand_predictions(self):
        """Generate 24-hour demand predictions"""
        hours = range(24)
        return [
            {
                'hour': hour,
                'predicted_occupancy': random.uniform(0.3, 0.95),
                'confidence': random.uniform(0.85, 0.98)
            }
            for hour in hours
        ]
    
    def _generate_revenue_optimizations(self):
        """Generate revenue optimization suggestions"""
        return [
            {
                "type": "pricing",
                "suggestion": "Increase peak hour rates by 15%",
                "impact": "+$2,400/month",
                "confidence": 0.92
            }
        ]
    
    def _identify_at_risk_members(self):
        """Identify members at risk of churning"""
        return [
            {
                "name": "Mike Davis",
                "risk_score": 0.87,
                "days_since_visit": 12,
                "recommended_action": "Personal outreach + 20% discount"
            }
        ]
    
    def get_real_time_metrics(self):
        """Get current real-time facility metrics"""
        return {
            'total_occupancy': random.uniform(0.65, 0.85),
            'revenue_today': random.uniform(8000, 12000),
            'energy_efficiency': random.uniform(0.88, 0.96),
            'member_satisfaction': random.uniform(4.2, 4.8),
            'last_updated': datetime.now()
        }

# =============================================================================
# DATA PROCESSING
# =============================================================================

class RealTimeDataProcessor:
    """Handles real-time data streams and processing"""
    
    def __init__(self):
        pass
        
    def start_data_streams(self):
        """Initialize all real-time data streams"""
        pass
    
    def _simulate_member_activity(self):
        """Simulate real-time member activity"""
        activities = ['basketball', 'soccer', 'fitness', 'swimming', 'tennis']
        return [
            {
                'member_id': f'M{random.randint(1000, 9999)}',
                'activity': random.choice(activities),
                'duration_minutes': random.randint(30, 120),
                'location': f'Area {random.randint(1, 5)}',
                'timestamp': datetime.now() - timedelta(minutes=random.randint(0, 180))
            }
            for _ in range(random.randint(15, 35))
        ]
    
    def _simulate_transactions(self):
        """Simulate real-time financial transactions"""
        transaction_types = ['membership', 'facility_booking', 'merchandise', 'concession']
        return [
            {
                'transaction_id': str(uuid.uuid4())[:8],
                'type': random.choice(transaction_types),
                'amount': random.uniform(10, 200),
                'payment_method': random.choice(['card', 'cash', 'mobile']),
                'timestamp': datetime.now() - timedelta(minutes=random.randint(0, 60))
            }
            for _ in range(random.randint(5, 15))
        ]

# =============================================================================
# CHART FUNCTIONS WITH FALLBACKS
# =============================================================================

def create_line_chart(data, x_col, y_col, title):
    """Create line chart with plotly or fallback to streamlit"""
    if PLOTLY_AVAILABLE:
        fig = px.line(data, x=x_col, y=y_col, title=title)
        return fig
    else:
        return None

def create_bar_chart(data, x_col, y_col, title):
    """Create bar chart with plotly or fallback to streamlit"""
    if PLOTLY_AVAILABLE:
        fig = px.bar(data, x=x_col, y=y_col, title=title)
        return fig
    else:
        return None

def render_chart(fig, data, x_col, y_col, chart_type="line"):
    """Render chart with fallback to streamlit native charts"""
    if PLOTLY_AVAILABLE and fig is not None:
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.markdown(f"### {chart_type.title()} Chart")
        if chart_type == "line":
            st.line_chart(data.set_index(x_col)[y_col])
        elif chart_type == "bar":
            st.bar_chart(data.set_index(x_col)[y_col])
        else:
            st.dataframe(data)

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
        
        st.set_page_config(
            page_title=self.license_info.facility_name,
            page_icon="🏟️",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        self._apply_custom_styling()
        self._render_header()
        self._render_navigation()
    
    def _apply_custom_styling(self):
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
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            }
            
            .main-header h1 {
                margin: 0;
                font-size: 3rem;
                font-weight: 700;
            }
            
            .metric-card {
                background: white;
                padding: 2rem;
                border-radius: 12px;
                border-left: 5px solid #1f77b4;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                margin-bottom: 1.5rem;
            }
            
            .status-active {
                color: #28a745;
                font-weight: bold;
                background: #d4edda;
                padding: 4px 8px;
                border-radius: 6px;
            }
            
            .status-warning {
                color: #856404;
                font-weight: bold;
                background: #fff3cd;
                padding: 4px 8px;
                border-radius: 6px;
            }
            
            .license-info {
                background: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 1rem;
                margin: 1rem 0;
                font-size: 0.9rem;
            }
            
            .ai-badge {
                background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
                color: white;
                padding: 5px 10px;
                border-radius: 15px;
                font-size: 12px;
                font-weight: bold;
                text-transform: uppercase;
            }
        </style>
        """, unsafe_allow_html=True)
    
    def _render_header(self):
        """Render the main header"""
        
        st.markdown(f"""
        <div class="main-header">
            <h1>🏟️ {self.license_info.facility_name}</h1>
            <p>{PlatformConfig.APP_NAME} - Enterprise Sports Management Platform</p>
            <div style="margin-top: 1rem;">
                <strong>LIVE SYSTEM</strong> | 
                License: {self.license_info.license_type.value.title()}
                {' | <span class="ai-badge">AI Powered</span>' if PlatformConfig.FEATURE_MATRIX[self.license_info.license_type]["ai_modules"] else ''}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def _render_navigation(self):
        """Render main navigation"""
        
        features = PlatformConfig.FEATURE_MATRIX[self.license_info.license_type]
        
        available_modules = ["🏠 Real-Time Dashboard"]
        available_modules.extend([
            "👥 Member Management",
            "🏟️ Facility Management", 
            "💰 Revenue Management"
        ])
        
        if features["ai_modules"]:
            available_modules.extend([
                "🤖 AI Analytics",
                "🔮 Predictive Intelligence"
            ])
        
        if features["api_access"]:
            available_modules.extend([
                "🔌 API Management"
            ])
        
        # Add logout button
        if st.sidebar.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()
        
        selected_module = st.sidebar.selectbox(
            "🧭 Navigate Platform",
            available_modules
        )
        
        self._render_license_info()
        self._route_to_module(selected_module, features)
    
    def _render_license_info(self):
        """Render license information in sidebar"""
        
        st.sidebar.markdown("---")
        st.sidebar.markdown("### 📋 License Information")
        
        license_features = PlatformConfig.FEATURE_MATRIX[self.license_info.license_type]
        
        st.sidebar.markdown(f"""
        <div class="license-info">
            <strong>License:</strong> {self.license_info.license_type.value.title()}<br>
            <strong>Facility:</strong> {self.license_info.facility_name}<br>
            <strong>Expires:</strong> {self.license_info.expiry_date.strftime('%Y-%m-%d')}<br>
            <strong>AI Modules:</strong> {'✅' if license_features['ai_modules'] else '❌'}<br>
            <strong>API Access:</strong> {'✅' if license_features['api_access'] else '❌'}<br>
            <strong>Price:</strong> ${license_features['price_monthly']}/month
        </div>
        """, unsafe_allow_html=True)
        
        st.sidebar.markdown(f"*{PlatformConfig.COPYRIGHT}*")
        
        # Upgrade prompt for non-enterprise licenses
        if self.license_info.license_type != LicenseType.ENTERPRISE:
            st.sidebar.markdown("---")
            st.sidebar.markdown("### 🚀 Upgrade License")
            st.sidebar.info("Unlock more features with Enterprise license!")
            if st.sidebar.button("📞 Contact Sales"):
                st.sidebar.success("Sales team will contact you within 24 hours!")
    
    def _route_to_module(self, selected_module: str, features: Dict):
        """Route to the selected module"""
        
        if "Real-Time Dashboard" in selected_module:
            self._render_realtime_dashboard()
        elif "Member Management" in selected_module:
            self._render_member_management()
        elif "Facility Management" in selected_module:
            self._render_facility_management()
        elif "AI Analytics" in selected_module and features["ai_modules"]:
            self._render_ai_analytics()
        elif "API Management" in selected_module and features["api_access"]:
            self._render_api_management()
        else:
            self._render_module_placeholder(selected_module)
    
    def _render_realtime_dashboard(self):
        """Render the real-time dashboard"""
        
        st.markdown("## 📊 Real-Time Facility Overview")
        
        metrics = self.ai_engine.get_real_time_metrics()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric(
                "🏟️ Facility Utilization",
                f"{metrics['total_occupancy']:.1%}",
                delta=f"+{random.uniform(2, 8):.1f}% vs yesterday"
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric(
                "💰 Today's Revenue", 
                f"${metrics['revenue_today']:,.0f}",
                delta=f"+{random.uniform(5, 15):.1f}% vs avg"
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric(
                "⚡ Energy Efficiency",
                f"{metrics['energy_efficiency']:.1%}",
                delta=f"+{random.uniform(1, 4):.1f}% vs last week"
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col4:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric(
                "😊 Member Satisfaction",
                f"{metrics['member_satisfaction']:.1f}/5.0",
                delta=f"+{random.uniform(0.1, 0.3):.1f} vs last month"
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        # AI Insights Section
        if PlatformConfig.FEATURE_MATRIX[self.license_info.license_type]["ai_modules"]:
            st.markdown("### 🤖 AI-Powered Insights")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("#### 📈 Revenue Optimization Impact")
                
                # Generate sample optimization data
                hours = [f"{i:02d}:00" for i in range(6, 23)]
                optimization_data = []
                
                for hour in hours:
                    impact = random.uniform(5, 30)
                    optimization_data.append({
                        'Hour': hour,
                        'Revenue_Impact': impact
                    })
                
                df_opt = pd.DataFrame(optimization_data)
                
                # Use fallback chart rendering
                fig = create_line_chart(df_opt, 'Hour', 'Revenue_Impact', 'AI Revenue Optimization Impact (%)')
                render_chart(fig, df_opt, 'Hour', 'Revenue_Impact', 'line')
            
            with col2:
                st.markdown("#### 🎯 Smart Recommendations")
                
                recommendations = [
                    {
                        "priority": "🔴 High",
                        "title": "Peak Hour Pricing",
                        "description": "Increase basketball court rates by 18% during 7-9 PM",
                        "impact": "+$2,400/month",
                        "confidence": "94%"
                    },
                    {
                        "priority": "🟡 Medium",
                        "title": "Equipment Maintenance", 
                        "description": "Schedule HVAC maintenance for Zone 3 within 10 days",
                        "impact": "Prevent $8,500 repair",
                        "confidence": "87%"
                    }
                ]
                
                for i, rec in enumerate(recommendations):
                    with st.expander(f"{rec['priority']} - {rec['title']}"):
                        st.write(rec['description'])
                        st.write(f"**Impact:** {rec['impact']}")
                        st.write(f"**Confidence:** {rec['confidence']}")
                        
                        col_a, col_b = st.columns(2)
                        with col_a:
                            if st.button(f"✅ Implement", key=f"impl_{i}"):
                                st.success("Recommendation implemented!")
                        with col_b:
                            if st.button(f"⏰ Remind Later", key=f"remind_{i}"):
                                st.info("Reminder set for tomorrow")
        
        # Live Activity Feed
        st.markdown("### 🔄 Live Activity Feed")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("#### 🏃‍♂️ Current Member Activity")
            
            member_activities = self.data_processor._simulate_member_activity()
            recent_activities = sorted(member_activities, key=lambda x: x['timestamp'], reverse=True)[:5]
            
            for activity in recent_activities:
                time_ago = (datetime.now() - activity['timestamp']).seconds // 60
                st.markdown(f"""
                <div style="padding: 10px; border-left: 3px solid #1f77b4; margin: 5px 0; background: #f8f9fa;">
                    <strong>{activity['member_id']}</strong> - {activity['activity'].title()} 
                    <span style="color: #666;">({activity['duration_minutes']} min @ {activity['location']})</span><br>
                    <small style="color: #999;">{time_ago} minutes ago</small>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### 💳 Recent Transactions")
            
            transactions = self.data_processor._simulate_transactions()
            recent_transactions = sorted(transactions, key=lambda x: x['timestamp'], reverse=True)[:5]
            
            total_recent = sum(t['amount'] for t in recent_transactions)
            st.metric("Last Hour Revenue", f"${total_recent:.2f}")
            
            for txn in recent_transactions:
                time_ago = (datetime.now() - txn['timestamp']).seconds // 60
                st.markdown(f"""
                <div style="padding: 8px; border-radius: 5px; margin: 3px 0; background: #e8f5e8;">
                    <strong>${txn['amount']:.2f}</strong> - {txn['type'].replace('_', ' ').title()}<br>
                    <small>{txn['payment_method'].title()} • {time_ago}m ago</small>
                </div>
                """, unsafe_allow_html=True)
        
        # Real-time refresh
        if st.button("🔄 Refresh Data"):
            st.rerun()
    
    def _render_member_management(self):
        """Render member management module"""
        
        st.markdown("## 👥 Member Management System")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Members", "1,247", delta="+23 this week")
        with col2:
            st.metric("Active Today", "342", delta="+8%")
        with col3:
            st.metric("Retention Rate", "94.2%", delta="+2.1%")
        with col4:
            st.metric("Avg. Monthly Revenue", "$127", delta="+$12")
        
        # Create tabs properly indented
        tab1, tab2, tab3 = st.tabs(["📋 Member List", "📊 Analytics", "🎯 Retention"])
        
        with tab1:
            st.markdown("### 📋 Member Directory")
            
            # Search and filter controls
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                search_term = st.text_input("🔍 Search members", placeholder="Name, email, or member ID")
            
            with col2:
                status_filter = st.selectbox("Status", ["All", "Active", "Inactive", "At Risk"])
            
            with col3:
                tier_filter = st.selectbox("Membership Tier", ["All", "Basic", "Premium", "Elite", "VIP"])
            
            # Generate sample member data
            members_data = []
            for i in range(20):
                member = {
                    "ID": f"M{1000 + i:04d}",
                    "Name": f"{random.choice(['John', 'Sarah', 'Mike', 'Lisa', 'David', 'Emma'])} {random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Davis', 'Wilson'])}",
                    "Email": f"member{i}@email.com",
                    "Tier": random.choice(["Basic", "Premium", "Elite", "VIP"]),
                    "Status": random.choice(["Active", "Active", "Active", "Inactive", "At Risk"]),
                    "Join Date": (datetime.now() - timedelta(days=random.randint(30, 1000))).strftime("%Y-%m-%d"),
                    "Monthly Fee": random.choice([49, 89, 149, 249]),
                    "Total Visits": random.randint(5, 300)
                }
                members_data.append(member)
            
            # Apply filters
            filtered_members = members_data
            
            if search_term:
                filtered_members = [m for m in filtered_members if search_term.lower() in m["Name"].lower()]
            
            if status_filter != "All":
                filtered_members = [m for m in filtered_members if m["Status"] == status_filter]
            
            if tier_filter != "All":
                filtered_members = [m for m in filtered_members if m["Tier"] == tier_filter]
            
            st.markdown(f"**Showing {len(filtered_members)} members**")
            
            df_members = pd.DataFrame(filtered_members)
            st.dataframe(df_members, use_container_width=True)
            
            # Bulk actions
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("📧 Send Newsletter"):
                    st.success(f"Newsletter sent to {len(filtered_members)} members!")
            
            with col2:
                if st.button("📊 Export Data"):
                    csv = df_members.to_csv(index=False)
                    st.download_button("📥 Download CSV", csv, "members.csv", "text/csv")
            
            with col3:
                if st.button("🎯 Create Campaign"):
                    st.info("Campaign creation wizard opened!")
        
        with tab2:
            st.markdown("### 📊 Member Analytics Dashboard")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 📈 Member Growth Trend")
                
                # Generate member growth data
                dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
                growth_data = []
                base_members = 800
                
                for i, date in enumerate(dates):
                    growth = base_members + i * 30 + random.randint(-10, 20)
                    growth_data.append({
                        'Month': date.strftime('%Y-%m'),
                        'Total_Members': growth
                    })
                
                df_growth = pd.DataFrame(growth_data)
                
                # Use fallback chart rendering
                fig = create_line_chart(df_growth, 'Month', 'Total_Members', 'Member Growth Over Time')
                render_chart(fig, df_growth, 'Month', 'Total_Members', 'line')
            
            with col2:
                st.markdown("#### 🎯 Membership Tier Distribution")
                
                tier_data = pd.DataFrame({
                    'Tier': ['Basic', 'Premium', 'Elite', 'VIP'],
                    'Count': [420, 380, 280, 167]
                })
                
                st.bar_chart(tier_data.set_index('Tier')['Count'])
        
        with tab3:
            if PlatformConfig.FEATURE_MATRIX[self.license_info.license_type]["ai_modules"]:
                st.markdown("### 🎯 AI-Powered Member Retention")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("High Risk Members", "23", delta="-5 vs last week")
                with col2:
                    st.metric("Predicted Churn Rate", "4.2%", delta="-1.1%")
                with col3:
                    st.metric("Retention Actions", "18", delta="+8")
                
                st.markdown("#### ⚠️ Members at Risk of Churning")
                
                at_risk_members = [
                    {
                        "Name": "Mike Davis",
                        "Risk Score": 0.87,
                        "Days Since Visit": 12,
                        "Decline Trend": "📉 -40% visits",
                        "Recommended Action": "Personal outreach + 20% discount",
                        "Value at Risk": "$588"
                    },
                    {
                        "Name": "Lisa Chen",
                        "Risk Score": 0.73,
                        "Days Since Visit": 8,
                        "Decline Trend": "📉 -25% visits