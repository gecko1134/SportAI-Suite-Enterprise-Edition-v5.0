"""
🏟️ SportAI Enterprise Suite - Unified Heatmap & Sponsorship Integration
Module to integrate into existing SportAI main app

Add this file as: unified_heatmap_sponsorship.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import random
from typing import Dict, List, Any, Optional

def run_unified_heatmap_sponsorship():
    """Main function to run the unified heatmap and sponsorship system"""
    
    # Initialize session state
    if 'unified_current_module' not in st.session_state:
        st.session_state.unified_current_module = 'dashboard'
    if 'unified_sponsor_data' not in st.session_state:
        initialize_unified_data()
    
    # CSS Styling
    st.markdown("""
    <style>
    .unified-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    .unified-metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2a5298;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .unified-facility-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 3px 12px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="unified-header">
        <h1>🏟️ NXS Unified Analytics Center</h1>
        <h2>Real-time Heatmap & Sponsorship Management</h2>
        <p>📊 Live Facility Analytics | 🤝 Sponsor Relationship Management | 💰 Revenue Optimization</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🏠 Dashboard", use_container_width=True, 
                    type="primary" if st.session_state.unified_current_module == 'dashboard' else "secondary"):
            st.session_state.unified_current_module = 'dashboard'
    
    with col2:
        if st.button("🔥 Usage Heatmap", use_container_width=True,
                    type="primary" if st.session_state.unified_current_module == 'heatmap' else "secondary"):
            st.session_state.unified_current_module = 'heatmap'
    
    with col3:
        if st.button("🤝 Sponsorship Center", use_container_width=True,
                    type="primary" if st.session_state.unified_current_module == 'sponsorship' else "secondary"):
            st.session_state.unified_current_module = 'sponsorship'
    
    with col4:
        if st.button("📊 Analytics Hub", use_container_width=True,
                    type="primary" if st.session_state.unified_current_module == 'analytics' else "secondary"):
            st.session_state.unified_current_module = 'analytics'
    
    st.markdown("---")
    
    # Route to selected module
    if st.session_state.unified_current_module == 'dashboard':
        render_unified_dashboard()
    elif st.session_state.unified_current_module == 'heatmap':
        render_heatmap_module()
    elif st.session_state.unified_current_module == 'sponsorship':
        render_sponsorship_module()
    elif st.session_state.unified_current_module == 'analytics':
        render_analytics_module()

def initialize_unified_data():
    """Initialize all data for the unified system"""
    
    # Sponsor data
    st.session_state.unified_sponsor_data = [
        {
            'id': 1,
            'name': 'Wells Fargo Bank',
            'tier': 'Diamond',
            'value': 1750000,
            'status': 'Active',
            'renewal': '2024-12-31',
            'contact': {
                'primary': 'Sarah Johnson',
                'email': 'sarah.johnson@wellsfargo.com',
                'phone': '555-0123',
                'title': 'Marketing Director'
            },
            'fulfillment': {'overall': 95, 'signage': 98, 'digital': 92, 'events': 97},
            'performance': {'exposureValue': 3200000, 'digitalImpressions': 2500000, 'leadGeneration': 340},
            'satisfaction': {'score': 9.2}
        },
        {
            'id': 2,
            'name': 'HyVee',
            'tier': 'Platinum',
            'value': 625000,
            'status': 'Active',
            'renewal': '2024-09-30',
            'contact': {
                'primary': 'Mike Chen',
                'email': 'mike.chen@hy-vee.com',
                'phone': '555-0456',
                'title': 'Community Relations Manager'
            },
            'fulfillment': {'overall': 88, 'signage': 85, 'digital': 90, 'events': 92},
            'performance': {'exposureValue': 1800000, 'digitalImpressions': 1200000, 'leadGeneration': 185},
            'satisfaction': {'score': 8.7}
        },
        {
            'id': 3,
            'name': 'TD Ameritrade',
            'tier': 'Gold',
            'value': 320000,
            'status': 'Active',
            'renewal': '2024-06-30',
            'contact': {
                'primary': 'Jennifer Liu',
                'email': 'j.liu@tdameritrade.com',
                'phone': '555-0789',
                'title': 'Sponsorship Manager'
            },
            'fulfillment': {'overall': 92, 'signage': 95, 'digital': 88, 'events': 94},
            'performance': {'exposureValue': 950000, 'digitalImpressions': 800000, 'leadGeneration': 95},
            'satisfaction': {'score': 8.9}
        }
    ]
    
    # Heatmap data for facilities
    facilities = [
        'Main Dome', 'Basketball Court 1', 'Basketball Court 2', 'Basketball Court 3', 'Basketball Court 4',
        'Outdoor Field A', 'Outdoor Field B', 'Outdoor Field C', 'Outdoor Field D',
        'Walking Track', 'Wellness Center', 'Esports Arena'
    ]
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    hours = list(range(6, 23))  # 6 AM to 10 PM
    
    heatmap_data = []
    for day_idx, day in enumerate(days):
        for hour in hours:
            for facility in facilities:
                # Generate realistic usage patterns
                base_usage = 30
                
                # Peak times boost
                if (hour >= 17 and hour <= 21) or (hour >= 7 and hour <= 9):
                    base_usage += 40
                
                # Weekend boost
                if day_idx >= 5:
                    base_usage += 20
                
                # Facility-specific patterns
                if 'Basketball' in facility:
                    base_usage += 30 if (hour >= 18 and hour <= 21) else 0
                elif 'Field' in facility:
                    base_usage += 25 if (hour >= 16 and hour <= 20) else 0
                elif 'Dome' in facility:
                    base_usage += 35 if (hour >= 17 and hour <= 20) else 0
                
                usage = min(100, max(10, base_usage + random.uniform(-15, 15)))
                revenue = usage * random.uniform(25, 75)
                
                heatmap_data.append({
                    'day': day,
                    'day_idx': day_idx,
                    'hour': hour,
                    'facility': facility,
                    'usage': round(usage),
                    'revenue': round(revenue),
                    'is_prime_time': (hour >= 17 and hour <= 21) or (hour >= 7 and hour <= 9),
                    'is_weekend': day_idx >= 5
                })
    
    st.session_state.unified_heatmap_data = heatmap_data
    
    # Performance metrics
    st.session_state.unified_metrics = {
        'total_revenue': 2695000,
        'sponsor_retention': 96.8,
        'facility_utilization': 78.4,
        'customer_satisfaction': 8.93,
        'active_sponsors': len(st.session_state.unified_sponsor_data),
        'pipeline_value': 450000
    }

def render_unified_dashboard():
    """Render the main dashboard with overview metrics"""
    
    st.markdown("## 📊 Unified Performance Dashboard")
    
    metrics = st.session_state.unified_metrics
    sponsors = st.session_state.unified_sponsor_data
    heatmap_data = st.session_state.unified_heatmap_data
    
    # Key Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "💰 Total Revenue", 
            f"${metrics['total_revenue']:,}", 
            "+15.3% YoY"
        )
    
    with col2:
        st.metric(
            "🤝 Active Sponsors", 
            metrics['active_sponsors'],
            "+2 new this year"
        )
    
    with col3:
        st.metric(
            "🏟️ Facility Usage", 
            f"{metrics['facility_utilization']:.1f}%",
            "+5.2% vs last month"
        )
    
    with col4:
        st.metric(
            "⭐ Satisfaction", 
            f"{metrics['customer_satisfaction']:.1f}/10",
            "+0.3 improvement"
        )
    
    # Quick Overview Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔥 Real-time Facility Usage")
        
        # Current usage by facility
        current_hour = datetime.now().hour
        current_usage = []
        
        for facility in ['Main Dome', 'Basketball Court 1', 'Basketball Court 2', 'Basketball Court 3', 'Basketball Court 4']:
            facility_data = [d for d in heatmap_data if d['facility'] == facility and d['hour'] == current_hour]
            if facility_data:
                current_usage.append({
                    'Facility': facility,
                    'Usage': facility_data[0]['usage']
                })
        
        if current_usage:
            usage_df = pd.DataFrame(current_usage)
            fig = px.bar(usage_df, x='Facility', y='Usage', 
                        title=f"Current Usage ({current_hour}:00)",
                        color='Usage',
                        color_continuous_scale='viridis')
            fig.update_xaxis(tickangle=45)
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 💰 Sponsorship Portfolio")
        
        # Sponsor value distribution
        sponsor_values = [{'Sponsor': s['name'], 'Value': s['value']} for s in sponsors]
        sponsor_df = pd.DataFrame(sponsor_values)
        
        fig = px.pie(sponsor_df, values='Value', names='Sponsor',
                    title="Revenue Distribution by Sponsor")
        st.plotly_chart(fig, use_container_width=True)
    
    # Live Activity Feed
    st.markdown("### 📢 Live System Activity")
    
    activities = [
        {
            'time': '2 minutes ago',
            'type': '🔥',
            'message': 'Main Dome usage spike detected - 94% capacity',
            'status': 'info'
        },
        {
            'time': '5 minutes ago',
            'type': '🤝',
            'message': 'Wells Fargo sponsorship fulfillment updated to 95%',
            'status': 'success'
        },
        {
            'time': '12 minutes ago',
            'type': '💰',
            'message': 'Revenue optimization AI increased Basketball Court rates by 8%',
            'status': 'success'
        },
        {
            'time': '18 minutes ago',
            'type': '⚠️',
            'message': 'TD Ameritrade contract renewal reminder sent (90 days)',
            'status': 'warning'
        }
    ]
    
    for activity in activities:
        status_color = {
            'success': '#28a745',
            'warning': '#ffc107', 
            'info': '#17a2b8',
            'danger': '#dc3545'
        }.get(activity['status'], '#6c757d')
        
        st.markdown(f"""
        <div style="border-left: 4px solid {status_color}; background: #f8f9fa; padding: 1rem; margin: 0.5rem 0; border-radius: 4px;">
            <div style="display: flex; justify-content: between; align-items: center;">
                <span style="font-size: 1.2em;">{activity['type']}</span>
                <span style="margin-left: 10px;">{activity['message']}</span>
                <span style="margin-left: auto; color: #6c757d; font-size: 0.9em;">{activity['time']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_heatmap_module():
    """Render the enhanced heatmap module"""
    
    st.markdown("## 🔥 Enhanced Usage Heatmap Analytics")
    
    heatmap_data = st.session_state.unified_heatmap_data
    
    # Heatmap Controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        view_type = st.selectbox("📊 View Type", ["Usage %", "Revenue $", "Efficiency"])
    
    with col2:
        time_filter = st.selectbox("⏰ Time Filter", ["All Hours", "Peak Hours", "Off-Peak"])
    
    with col3:
        facility_filter = st.selectbox("🏟️ Facility Filter", 
                                     ["All Facilities"] + list(set([d['facility'] for d in heatmap_data])))
    
    # Filter data based on selections
    filtered_data = heatmap_data.copy()
    
    if time_filter == "Peak Hours":
        filtered_data = [d for d in filtered_data if d['is_prime_time']]
    elif time_filter == "Off-Peak":
        filtered_data = [d for d in filtered_data if not d['is_prime_time']]
    
    if facility_filter != "All Facilities":
        filtered_data = [d for d in filtered_data if d['facility'] == facility_filter]
    
    # Overview Metrics
    if filtered_data:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            avg_usage = sum(d['usage'] for d in filtered_data) / len(filtered_data)
            st.metric("📊 Average Usage", f"{avg_usage:.1f}%")
        
        with col2:
            total_revenue = sum(d['revenue'] for d in filtered_data)
            st.metric("💰 Total Revenue", f"${total_revenue:,.0f}")
        
        with col3:
            peak_usage = max(d['usage'] for d in filtered_data)
            st.metric("🔝 Peak Usage", f"{peak_usage}%")
        
        with col4:
            active_facilities = len(set(d['facility'] for d in filtered_data))
            st.metric("🏟️ Active Facilities", active_facilities)
    
    # Main Heatmap Visualization
    if filtered_data:
        # Create hourly usage chart
        hourly_data = {}
        for d in filtered_data:
            hour = d['hour']
            if hour not in hourly_data:
                hourly_data[hour] = {'usage': [], 'revenue': []}
            hourly_data[hour]['usage'].append(d['usage'])
            hourly_data[hour]['revenue'].append(d['revenue'])
        
        hourly_avg = []
        for hour in sorted(hourly_data.keys()):
            hourly_avg.append({
                'Hour': f"{hour}:00",
                'Usage': sum(hourly_data[hour]['usage']) / len(hourly_data[hour]['usage']),
                'Revenue': sum(hourly_data[hour]['revenue']) / len(hourly_data[hour]['revenue'])
            })
        
        if hourly_avg:
            hourly_df = pd.DataFrame(hourly_avg)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = px.line(hourly_df, x='Hour', y='Usage', 
                             title="📈 Hourly Usage Patterns",
                             markers=True)
                fig.update_layout(yaxis_title="Usage %", xaxis_title="Time of Day")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = px.bar(hourly_df, x='Hour', y='Revenue',
                            title="💰 Hourly Revenue Generation",
                            color='Revenue',
                            color_continuous_scale='viridis')
                fig.update_layout(yaxis_title="Revenue ($)", xaxis_title="Time of Day")
                st.plotly_chart(fig, use_container_width=True)
    
    # Facility Performance Grid
    st.markdown("### 🏟️ Live Facility Status")
    
    facilities = list(set([d['facility'] for d in heatmap_data]))
    
    # Create facility performance cards
    cols = st.columns(3)
    
    for i, facility in enumerate(facilities):
        facility_data = [d for d in heatmap_data if d['facility'] == facility]
        avg_usage = sum(d['usage'] for d in facility_data) / len(facility_data) if facility_data else 0
        avg_revenue = sum(d['revenue'] for d in facility_data) / len(facility_data) if facility_data else 0
        
        with cols[i % 3]:
            usage_color = "🟢" if avg_usage >= 70 else "🟡" if avg_usage >= 50 else "🔴"
            
            st.markdown(f"""
            <div class="unified-facility-card">
                <h4>{usage_color} {facility}</h4>
                <p><strong>Usage:</strong> {avg_usage:.1f}%</p>
                <p><strong>Revenue:</strong> ${avg_revenue:.0f}</p>
                <p><strong>Status:</strong> {'High Demand' if avg_usage >= 70 else 'Moderate' if avg_usage >= 50 else 'Available'}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # AI Insights
    st.markdown("### 🤖 AI-Powered Insights")
    
    insights = [
        "🔥 **Peak Optimization**: Main Dome showing 94% utilization during 6-8 PM - consider dynamic pricing",
        "💡 **Revenue Opportunity**: Walking Track has 40% unused capacity during afternoons - promote wellness programs", 
        "⚡ **Efficiency Boost**: Basketball courts could increase revenue by 15% with optimized scheduling",
        "📈 **Growth Potential**: Weekend programming could add $25K monthly revenue across outdoor fields"
    ]
    
    for insight in insights:
        st.markdown(insight)

def render_sponsorship_module():
    """Render the sponsorship management module"""
    
    st.markdown("## 🤝 NXS Sponsorship Command Center")
    
    sponsors = st.session_state.unified_sponsor_data
    
    # Sponsorship Overview
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_value = sum(s['value'] for s in sponsors)
        st.metric("💰 Portfolio Value", f"${total_value:,}")
    
    with col2:
        active_sponsors = len([s for s in sponsors if s['status'] == 'Active'])
        st.metric("🤝 Active Sponsors", active_sponsors)
    
    with col3:
        avg_fulfillment = sum(s['fulfillment']['overall'] for s in sponsors) / len(sponsors)
        st.metric("📊 Avg Fulfillment", f"{avg_fulfillment:.1f}%")
    
    with col4:
        avg_satisfaction = sum(s['satisfaction']['score'] for s in sponsors) / len(sponsors)
        st.metric("⭐ Satisfaction", f"{avg_satisfaction:.1f}/10")
    
    # Sponsor Cards
    st.markdown("### 🏢 Active Sponsors")
    
    for sponsor in sponsors:
        with st.expander(f"🏆 {sponsor['name']} - {sponsor['tier']} Tier"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**📋 Contract Details:**")
                st.markdown(f"- **Value:** ${sponsor['value']:,}")
                st.markdown(f"- **Tier:** {sponsor['tier']}")
                st.markdown(f"- **Status:** {sponsor['status']}")
                st.markdown(f"- **Renewal:** {sponsor['renewal']}")
                
                st.markdown("**👤 Contact Information:**")
                st.markdown(f"- **Primary:** {sponsor['contact']['primary']}")
                st.markdown(f"- **Title:** {sponsor['contact']['title']}")
                st.markdown(f"- **Email:** {sponsor['contact']['email']}")
                st.markdown(f"- **Phone:** {sponsor['contact']['phone']}")
            
            with col2:
                st.markdown("**📈 Performance Metrics:**")
                
                # Fulfillment Progress
                fulfillment = sponsor['fulfillment']['overall']
                st.progress(fulfillment / 100)
                st.caption(f"Overall Fulfillment: {fulfillment}%")
                
                # Key metrics
                perf = sponsor['performance']
                st.markdown(f"- **Exposure Value:** ${perf['exposureValue']:,}")
                st.markdown(f"- **Digital Impressions:** {perf['digitalImpressions']:,}")
                st.markdown(f"- **Lead Generation:** {perf['leadGeneration']}")
                
                # ROI Calculation
                roi = (perf['exposureValue'] / sponsor['value']) * 100
                st.markdown(f"- **ROI:** {roi:.0f}%")
                
                st.markdown(f"**😊 Satisfaction Score:** {sponsor['satisfaction']['score']}/10")
            
            # Action buttons
            col_a, col_b, col_c = st.columns(3)
            
            with col_a:
                if st.button(f"📧 Contact {sponsor['name']}", key=f"contact_{sponsor['id']}"):
                    st.success(f"Opening email to {sponsor['contact']['email']}")
            
            with col_b:
                if st.button(f"📊 Generate Report", key=f"report_{sponsor['id']}"):
                    st.success(f"Performance report generated for {sponsor['name']}")
            
            with col_c:
                if st.button(f"📅 Schedule Meeting", key=f"meeting_{sponsor['id']}"):
                    st.success(f"Meeting scheduled with {sponsor['contact']['primary']}")
    
    # Sponsorship Analytics
    st.markdown("### 📊 Sponsorship Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Tier distribution
        tier_data = {}
        for sponsor in sponsors:
            tier = sponsor['tier']
            tier_data[tier] = tier_data.get(tier, 0) + 1
        
        tier_df = pd.DataFrame(list(tier_data.items()), columns=['Tier', 'Count'])
        fig = px.pie(tier_df, values='Count', names='Tier',
                    title="Sponsors by Tier")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Performance comparison
        perf_data = []
        for sponsor in sponsors:
            perf_data.append({
                'Sponsor': sponsor['name'],
                'Fulfillment': sponsor['fulfillment']['overall'],
                'Satisfaction': sponsor['satisfaction']['score'] * 10,  # Scale to 100
                'ROI': (sponsor['performance']['exposureValue'] / sponsor['value']) * 100
            })
        
        perf_df = pd.DataFrame(perf_data)
        fig = px.bar(perf_df, x='Sponsor', y=['Fulfillment', 'Satisfaction'],
                    title="Performance Comparison",
                    barmode='group')
        fig.update_xaxis(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

def render_analytics_module():
    """Render the advanced analytics module"""
    
    st.markdown("## 📊 Advanced Analytics Hub")
    
    sponsors = st.session_state.unified_sponsor_data
    heatmap_data = st.session_state.unified_heatmap_data
    metrics = st.session_state.unified_metrics
    
    # Integrated Performance Dashboard
    st.markdown("### 🎯 Integrated Performance Analysis")
    
    # Create correlation analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 💰 Revenue vs Utilization Correlation")
        
        # Calculate facility utilization vs sponsor satisfaction
        facility_usage = {}
        for d in heatmap_data:
            facility = d['facility']
            if facility not in facility_usage:
                facility_usage[facility] = []
            facility_usage[facility].append(d['usage'])
        
        # Average usage per facility
        avg_facility_usage = {f: sum(usage)/len(usage) for f, usage in facility_usage.items()}
        
        # Correlation data
        correlation_data = []
        for sponsor in sponsors:
            correlation_data.append({
                'Sponsor': sponsor['name'],
                'Fulfillment': sponsor['fulfillment']['overall'],
                'Satisfaction': sponsor['satisfaction']['score'],
                'Revenue': sponsor['value'] / 1000000,  # In millions
                'ROI': (sponsor['performance']['exposureValue'] / sponsor['value']) * 100
            })
        
        corr_df = pd.DataFrame(correlation_data)
        
        fig = px.scatter(corr_df, x='Fulfillment', y='Satisfaction',
                        size='Revenue', color='ROI',
                        hover_name='Sponsor',
                        title="Sponsor Performance Matrix",
                        labels={'Fulfillment': 'Fulfillment %', 'Satisfaction': 'Satisfaction Score'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 🔥 Facility Performance Rankings")
        
        facility_performance = []
        for facility, usage_list in facility_usage.items():
            avg_usage = sum(usage_list) / len(usage_list)
            facility_revenue = sum(d['revenue'] for d in heatmap_data if d['facility'] == facility)
            
            facility_performance.append({
                'Facility': facility,
                'Avg_Usage': avg_usage,
                'Total_Revenue': facility_revenue,
                'Efficiency_Score': (avg_usage * facility_revenue) / 10000  # Normalized score
            })
        
        facility_df = pd.DataFrame(facility_performance)
        facility_df = facility_df.sort_values('Efficiency_Score', ascending=False)
        
        fig = px.bar(facility_df.head(8), x='Facility', y='Efficiency_Score',
                    title="Top Performing Facilities",
                    color='Efficiency_Score',
                    color_continuous_scale='viridis')
        fig.update_xaxis(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)
    
    # Performance Summary Table
    st.markdown("### 📋 Comprehensive Performance Summary")
    
    summary_data = []
    for sponsor in sponsors:
        # Calculate days until renewal
        renewal_date = datetime.strptime(sponsor['renewal'], '%Y-%m-%d')
        days_until_renewal = (renewal_date - datetime.now()).days
        
        summary_data.append({
            'Sponsor': sponsor['name'],
            'Tier': sponsor['tier'],
            'Contract Value': f"${sponsor['value']:,}",
            'Fulfillment %': f"{sponsor['fulfillment']['overall']}%",
            'Satisfaction': f"{sponsor['satisfaction']['score']}/10",
            'ROI': f"{(sponsor['performance']['exposureValue'] / sponsor['value']) * 100:.0f}%",
            'Days to Renewal': days_until_renewal,
            'Status': sponsor['status']
        })
    
    summary_df = pd.DataFrame(summary_data)
    st.dataframe(summary_df, use_container_width=True)
    
    # Export Options
    st.markdown("### 📤 Export & Reporting")
    
    col1, col2, col3 = st.columns(3)
    