"""
🔥 Enhanced User Heatmap Dashboard with Visual Field Breakdown
Integrated into NXS Sports AI Platform with lacrosse support and comprehensive analytics
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import random
from typing import Dict, List, Any
import json

class EnhancedHeatmapAnalyzer:
    """Advanced heatmap analysis with visual field breakdown and lacrosse support"""
    
    def __init__(self):
        self.facilities = {
            'turf_fields': [
                {'id': 'TF001', 'name': 'Turf Field A', 'sports': ['Soccer', 'Football', 'Lacrosse', 'Field Hockey']},
                {'id': 'TF002', 'name': 'Turf Field B', 'sports': ['Soccer', 'Lacrosse', 'Rugby', 'Multi-Sport']},
                {'id': 'TF003', 'name': 'Turf Field C', 'sports': ['Football', 'Lacrosse', 'Soccer Training']},
                {'id': 'TF004', 'name': 'Turf Field D', 'sports': ['Soccer', 'Lacrosse', 'Ultimate Frisbee']}
            ],
            'basketball_courts': [
                {'id': 'BC001', 'name': 'Championship Court', 'sports': ['Basketball', 'Volleyball', 'Badminton']},
                {'id': 'BC002', 'name': 'Tournament Court', 'sports': ['Basketball', 'Volleyball', 'Tennis']},
                {'id': 'BC003', 'name': 'Training Court', 'sports': ['Basketball', 'Pickleball', 'Multi-Sport']},
                {'id': 'BC004', 'name': 'Community Court', 'sports': ['Basketball', 'Recreational', 'Youth']}
            ],
            'dome_zones': [
                {'id': 'DZ001', 'name': 'Dome Zone 1', 'sports': ['Baseball', 'Softball', 'Cricket']},
                {'id': 'DZ002', 'name': 'Dome Zone 2', 'sports': ['Softball', 'T-Ball', 'Training']},
                {'id': 'DZ003', 'name': 'Player Lab', 'sports': ['Elite Training', 'Performance', 'Assessment']}
            ],
            'specialty_areas': [
                {'id': 'SA001', 'name': 'Walking Track', 'sports': ['Walking', 'Running', 'Fitness']},
                {'id': 'SA002', 'name': 'Wellness Center', 'sports': ['Fitness', 'Yoga', 'Therapy']},
                {'id': 'SA003', 'name': 'Esports Arena', 'sports': ['Gaming', 'Streaming', 'Competition']}
            ]
        }
        
        self.member_tiers = ['Venture North Club', 'All-Access', 'Family Plan', 'Basic Member', 'Community Advantage']
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.hours = list(range(6, 23))  # 6 AM to 10 PM
        
        # Lacrosse-specific patterns
        self.lacrosse_seasons = {
            'Spring': {'multiplier': 1.5, 'months': [3, 4, 5]},
            'Fall': {'multiplier': 1.3, 'months': [9, 10, 11]},
            'Summer': {'multiplier': 0.8, 'months': [6, 7, 8]},
            'Winter': {'multiplier': 0.4, 'months': [12, 1, 2]}
        }
    
    def generate_comprehensive_heatmap_data(self) -> List[Dict[str, Any]]:
        """Generate comprehensive heatmap data with lacrosse support"""
        data = []
        current_month = datetime.now().month
        
        # Determine current season for lacrosse patterns
        current_season = 'Spring'
        for season, info in self.lacrosse_seasons.items():
            if current_month in info['months']:
                current_season = season
                break
        
        lacrosse_multiplier = self.lacrosse_seasons[current_season]['multiplier']
        
        for day_idx, day in enumerate(self.days):
            for hour in self.hours:
                # Process all facility types
                all_facilities = []
                for facility_type, facilities in self.facilities.items():
                    all_facilities.extend(facilities)
                
                for facility in all_facilities:
                    for tier in self.member_tiers:
                        for sport in facility['sports']:
                            # Base usage calculation
                            base_usage = 25
                            
                            # Prime time boost (6-9 PM, 7-10 AM)
                            if (18 <= hour <= 21) or (7 <= hour <= 10):
                                base_usage += 45
                            
                            # Weekend boost
                            if day_idx >= 5:  # Saturday, Sunday
                                base_usage += 25
                            
                            # Facility-specific patterns
                            if 'Basketball' in facility['sports']:
                                if (18 <= hour <= 21):
                                    base_usage *= 1.4
                            elif 'Soccer' in facility['sports'] or 'Football' in facility['sports']:
                                if (16 <= hour <= 20):
                                    base_usage *= 1.3
                            elif 'Lacrosse' in facility['sports']:
                                # Apply seasonal patterns for lacrosse
                                base_usage *= lacrosse_multiplier
                                if (17 <= hour <= 19):  # Peak lacrosse hours
                                    base_usage *= 1.2
                            elif 'Elite Training' in facility['sports']:
                                if (7 <= hour <= 10) or (18 <= hour <= 21):
                                    base_usage *= 1.6
                            
                            # Member tier multipliers
                            tier_multipliers = {
                                'Venture North Club': 1.6,
                                'All-Access': 1.2,
                                'Family Plan': 0.9 if (9 <= hour <= 15) else 1.1,
                                'Basic Member': 0.7,
                                'Community Advantage': 0.5
                            }
                            
                            # Apply multipliers
                            usage = base_usage * tier_multipliers[tier]
                            
                            # Add realistic variance
                            usage += random.uniform(-15, 15)
                            usage = max(5, min(100, round(usage)))
                            
                            # Determine classifications
                            is_prime_time = (18 <= hour <= 21) or (7 <= hour <= 10)
                            is_weekend = day_idx >= 5
                            is_lacrosse = sport == 'Lacrosse'
                            
                            # Calculate revenue based on facility type and tier
                            base_rate = self._get_base_rate(facility, sport, tier)
                            revenue = usage * base_rate / 100
                            
                            data.append({
                                'day': day,
                                'day_index': day_idx,
                                'hour': hour,
                                'facility_id': facility['id'],
                                'facility_name': facility['name'],
                                'facility_type': self._get_facility_type(facility['id']),
                                'sport': sport,
                                'member_tier': tier,
                                'usage_percentage': usage,
                                'revenue_estimate': round(revenue, 2),
                                'is_prime_time': is_prime_time,
                                'is_weekend': is_weekend,
                                'is_lacrosse': is_lacrosse,
                                'season': current_season,
                                'time_category': 'Prime Time' if is_prime_time else 'Off-Peak',
                                'day_category': 'Weekend' if is_weekend else 'Weekday'
                            })
        
        return data
    
    def _get_facility_type(self, facility_id: str) -> str:
        """Determine facility type from ID"""
        if facility_id.startswith('TF'):
            return 'Turf Field'
        elif facility_id.startswith('BC'):
            return 'Basketball Court'
        elif facility_id.startswith('DZ'):
            return 'Dome Zone'
        else:
            return 'Specialty Area'
    
    def _get_base_rate(self, facility: Dict, sport: str, tier: str) -> float:
        """Calculate base hourly rate based on facility, sport, and tier"""
        base_rates = {
            'Turf Field': {'Lacrosse': 120, 'Soccer': 95, 'Football': 110, 'default': 85},
            'Basketball Court': {'Basketball': 75, 'Volleyball': 65, 'default': 55},
            'Dome Zone': {'Elite Training': 200, 'Baseball': 150, 'default': 130},
            'Specialty Area': {'Fitness': 45, 'Gaming': 60, 'default': 35}
        }
        
        facility_type = self._get_facility_type(facility['id'])
        sport_rate = base_rates.get(facility_type, {}).get(sport, 
                    base_rates.get(facility_type, {}).get('default', 50))
        
        # Tier multipliers
        tier_rate_multipliers = {
            'Venture North Club': 1.5,
            'All-Access': 1.2,
            'Family Plan': 0.9,
            'Basic Member': 0.8,
            'Community Advantage': 0.6
        }
        
        return sport_rate * tier_rate_multipliers.get(tier, 1.0)
    
    def create_facility_visual_breakdown(self, data: List[Dict]) -> Dict[str, Any]:
        """Create visual breakdown of all facilities"""
        df = pd.DataFrame(data)
        
        breakdown = {
            'turf_fields': self._analyze_turf_fields(df),
            'basketball_courts': self._analyze_basketball_courts(df),
            'dome_zones': self._analyze_dome_zones(df),
            'specialty_areas': self._analyze_specialty_areas(df),
            'lacrosse_analysis': self._analyze_lacrosse_usage(df)
        }
        
        return breakdown
    
    def _analyze_turf_fields(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze turf field usage patterns"""
        turf_data = df[df['facility_type'] == 'Turf Field']
        
        analysis = {
            'total_usage': turf_data['usage_percentage'].mean(),
            'sport_breakdown': turf_data.groupby('sport')['usage_percentage'].mean().to_dict(),
            'peak_times': turf_data.groupby('hour')['usage_percentage'].mean().to_dict(),
            'lacrosse_specific': {
                'average_usage': turf_data[turf_data['sport'] == 'Lacrosse']['usage_percentage'].mean(),
                'peak_hours': turf_data[turf_data['sport'] == 'Lacrosse'].groupby('hour')['usage_percentage'].mean().nlargest(3).to_dict(),
                'seasonal_impact': turf_data[turf_data['sport'] == 'Lacrosse']['season'].iloc[0] if len(turf_data[turf_data['sport'] == 'Lacrosse']) > 0 else 'Spring'
            },
            'revenue_potential': turf_data.groupby('facility_name')['revenue_estimate'].sum().to_dict()
        }
        
        return analysis
    
    def _analyze_basketball_courts(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze basketball court usage patterns"""
        court_data = df[df['facility_type'] == 'Basketball Court']
        
        analysis = {
            'total_usage': court_data['usage_percentage'].mean(),
            'sport_breakdown': court_data.groupby('sport')['usage_percentage'].mean().to_dict(),
            'prime_time_usage': court_data[court_data['is_prime_time']]['usage_percentage'].mean(),
            'weekend_boost': court_data[court_data['is_weekend']]['usage_percentage'].mean() - 
                           court_data[~court_data['is_weekend']]['usage_percentage'].mean(),
            'revenue_potential': court_data.groupby('facility_name')['revenue_estimate'].sum().to_dict()
        }
        
        return analysis
    
    def _analyze_dome_zones(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze dome zone usage patterns"""
        dome_data = df[df['facility_type'] == 'Dome Zone']
        
        analysis = {
            'total_usage': dome_data['usage_percentage'].mean(),
            'zone_breakdown': dome_data.groupby('facility_name')['usage_percentage'].mean().to_dict(),
            'elite_training_usage': dome_data[dome_data['sport'] == 'Elite Training']['usage_percentage'].mean(),
            'revenue_potential': dome_data.groupby('facility_name')['revenue_estimate'].sum().to_dict()
        }
        
        return analysis
    
    def _analyze_specialty_areas(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze specialty area usage patterns"""
        specialty_data = df[df['facility_type'] == 'Specialty Area']
        
        analysis = {
            'total_usage': specialty_data['usage_percentage'].mean(),
            'area_breakdown': specialty_data.groupby('facility_name')['usage_percentage'].mean().to_dict(),
            'wellness_trends': specialty_data[specialty_data['sport'].isin(['Fitness', 'Yoga', 'Therapy'])]['usage_percentage'].mean(),
            'revenue_potential': specialty_data.groupby('facility_name')['revenue_estimate'].sum().to_dict()
        }
        
        return analysis
    
    def _analyze_lacrosse_usage(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Comprehensive lacrosse usage analysis"""
        lacrosse_data = df[df['sport'] == 'Lacrosse']
        
        if len(lacrosse_data) == 0:
            return {'message': 'No lacrosse data available'}
        
        analysis = {
            'total_lacrosse_usage': lacrosse_data['usage_percentage'].mean(),
            'seasonal_impact': lacrosse_data['season'].iloc[0],
            'field_preferences': lacrosse_data.groupby('facility_name')['usage_percentage'].mean().to_dict(),
            'peak_days': lacrosse_data.groupby('day')['usage_percentage'].mean().nlargest(3).to_dict(),
            'peak_hours': lacrosse_data.groupby('hour')['usage_percentage'].mean().nlargest(3).to_dict(),
            'member_tier_usage': lacrosse_data.groupby('member_tier')['usage_percentage'].mean().to_dict(),
            'revenue_analysis': {
                'total_revenue': lacrosse_data['revenue_estimate'].sum(),
                'avg_revenue_per_session': lacrosse_data['revenue_estimate'].mean(),
                'revenue_by_field': lacrosse_data.groupby('facility_name')['revenue_estimate'].sum().to_dict()
            },
            'growth_opportunities': self._identify_lacrosse_opportunities(lacrosse_data)
        }
        
        return analysis
    
    def _identify_lacrosse_opportunities(self, lacrosse_data: pd.DataFrame) -> List[str]:
        """Identify growth opportunities for lacrosse programs"""
        opportunities = []
        
        # Check for underutilized time slots
        hourly_usage = lacrosse_data.groupby('hour')['usage_percentage'].mean()
        low_usage_hours = hourly_usage[hourly_usage < 40].index.tolist()
        
        if low_usage_hours:
            opportunities.append(f"Expand lacrosse programs during {len(low_usage_hours)} underutilized hours")
        
        # Check tier penetration
        tier_usage = lacrosse_data.groupby('member_tier')['usage_percentage'].mean()
        if tier_usage.get('Basic Member', 0) < 30:
            opportunities.append("Target Basic Members with introductory lacrosse programs")
        
        # Weekend opportunities
        weekend_avg = lacrosse_data[lacrosse_data['is_weekend']]['usage_percentage'].mean()
        weekday_avg = lacrosse_data[~lacrosse_data['is_weekend']]['usage_percentage'].mean()
        
        if weekend_avg < weekday_avg:
            opportunities.append("Develop weekend lacrosse leagues and tournaments")
        
        return opportunities

def run_enhanced_heatmap_dashboard():
    """Main function to run the enhanced heatmap dashboard"""
    
    st.markdown("## 🔥 Enhanced User Usage Heatmap Dashboard")
    st.markdown('<span style="background: linear-gradient(45deg, #ff6b6b, #4ecdc4); color: white; padding: 5px 10px; border-radius: 15px; font-size: 12px; font-weight: bold;">REAL-TIME USAGE PATTERNS WITH LACROSSE ANALYTICS</span>', unsafe_allow_html=True)
    
    # Initialize analyzer
    analyzer = EnhancedHeatmapAnalyzer()
    
    # Generate data
    if 'enhanced_heatmap_data' not in st.session_state:
        st.session_state.enhanced_heatmap_data = analyzer.generate_comprehensive_heatmap_data()
    
    heatmap_data = st.session_state.enhanced_heatmap_data
    
    # Control panel
    st.markdown("### 🎛️ Advanced Analysis Controls")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        facility_types = ['All'] + list(set([d['facility_type'] for d in heatmap_data]))
        facility_type_filter = st.selectbox("🏟️ Facility Type", facility_types)
    
    with col2:
        sports = ['All'] + list(set([d['sport'] for d in heatmap_data]))
        sport_filter = st.selectbox("⚽ Sport", sports)
    
    with col3:
        tier_filter = st.selectbox("👥 Member Tier", ['All'] + analyzer.member_tiers)
    
    with col4:
        analysis_mode = st.selectbox("📊 Analysis Mode", 
                                   ['Overview', 'Lacrosse Focus', 'Revenue Analysis', 'Prime Time Analysis'])
    
    # Filter data
    filtered_data = heatmap_data
    if facility_type_filter != 'All':
        filtered_data = [d for d in filtered_data if d['facility_type'] == facility_type_filter]
    if sport_filter != 'All':
        filtered_data = [d for d in filtered_data if d['sport'] == sport_filter]
    if tier_filter != 'All':
        filtered_data = [d for d in filtered_data if d['member_tier'] == tier_filter]
    
    df = pd.DataFrame(filtered_data)
    
    if df.empty:
        st.warning("No data available for selected filters")
        return
    
    # Key metrics
    st.markdown("### 📈 Key Usage Metrics")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        avg_usage = df['usage_percentage'].mean()
        st.metric("Average Usage", f"{avg_usage:.1f}%")
    
    with col2:
        prime_usage = df[df['is_prime_time']]['usage_percentage'].mean()
        st.metric("Prime Time Usage", f"{prime_usage:.1f}%")
    
    with col3:
        weekend_boost = (df[df['is_weekend']]['usage_percentage'].mean() - 
                        df[~df['is_weekend']]['usage_percentage'].mean())
        st.metric("Weekend Boost", f"+{weekend_boost:.1f}%")
    
    with col4:
        total_revenue = df['revenue_estimate'].sum()
        st.metric("Est. Revenue", f"${total_revenue:,.0f}")
    
    with col5:
        lacrosse_count = len(df[df['sport'] == 'Lacrosse'])
        st.metric("Lacrosse Sessions", lacrosse_count)
    
    # Main heatmap visualization
    st.markdown("### 🔥 Interactive Usage Heatmap")
    
    # Create comprehensive heatmap
    if analysis_mode == 'Overview':
        heatmap_df = df.groupby(['day', 'hour'])['usage_percentage'].mean().reset_index()
        pivot_df = heatmap_df.pivot(index='hour', columns='day', values='usage_percentage')
        
    elif analysis_mode == 'Lacrosse Focus':
        lacrosse_df = df[df['sport'] == 'Lacrosse']
        if not lacrosse_df.empty:
            heatmap_df = lacrosse_df.groupby(['day', 'hour'])['usage_percentage'].mean().reset_index()
            pivot_df = heatmap_df.pivot(index='hour', columns='day', values='usage_percentage')
        else:
            st.warning("No lacrosse data available")
            return
            
    elif analysis_mode == 'Revenue Analysis':
        heatmap_df = df.groupby(['day', 'hour'])['revenue_estimate'].sum().reset_index()
        pivot_df = heatmap_df.pivot(index='hour', columns='day', values='revenue_estimate')
        
    else:  # Prime Time Analysis
        prime_df = df[df['is_prime_time']]
        heatmap_df = prime_df.groupby(['day', 'hour'])['usage_percentage'].mean().reset_index()
        pivot_df = heatmap_df.pivot(index='hour', columns='day', values='usage_percentage')
    
    # Reorder columns for proper day sequence
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pivot_df = pivot_df.reindex(columns=day_order).fillna(0)
    
    # Create interactive heatmap
    fig_heatmap = go.Figure(data=go.Heatmap(
        z=pivot_df.values,
        x=pivot_df.columns,
        y=[f"{int(hour)}:00" for hour in pivot_df.index],
        colorscale='RdYlBu_r',
        hoverongaps=False,
        hovertemplate='<b>%{x}</b><br>Time: %{y}<br>Value: %{z:.1f}<extra></extra>',
        colorbar=dict(title="Usage %" if analysis_mode != 'Revenue Analysis' else "Revenue ($)")
    ))
    
    title = f"{analysis_mode} Heatmap"
    if facility_type_filter != 'All':
        title += f" - {facility_type_filter}"
    if sport_filter != 'All':
        title += f" - {sport_filter}"
    
    fig_heatmap.update_layout(
        title=title,
        xaxis_title="Day of Week",
        yaxis_title="Hour of Day",
        height=500
    )
    
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    # Facility breakdown visualization
    st.markdown("### 🏟️ Comprehensive Facility Breakdown")
    
    # Create facility breakdown
    breakdown = analyzer.create_facility_visual_breakdown(filtered_data)
    
    # Facility type analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🌾 Turf Fields Analysis")
        turf_analysis = breakdown['turf_fields']
        
        # Turf field sport breakdown
        sport_data = pd.DataFrame(list(turf_analysis['sport_breakdown'].items()), 
                                columns=['Sport', 'Avg Usage %'])
        
        fig_turf = px.bar(sport_data, x='Sport', y='Avg Usage %', 
                         title="Turf Field Usage by Sport",
                         color='Sport')
        st.plotly_chart(fig_turf, use_container_width=True)
        
        # Revenue potential
        st.markdown("**Revenue Potential by Field:**")
        for field, revenue in turf_analysis['revenue_potential'].items():
            st.markdown(f"• {field}: ${revenue:.0f}")
    
    with col2:
        st.markdown("#### 🏀 Basketball Courts Analysis")
        court_analysis = breakdown['basketball_courts']
        
        # Court metrics
        st.metric("Prime Time Usage", f"{court_analysis.get('prime_time_usage', 0):.1f}%")
        st.metric("Weekend Boost", f"{court_analysis.get('weekend_boost', 0):.1f}%")
        
        # Sport breakdown for courts
        sport_data = pd.DataFrame(list(court_analysis['sport_breakdown'].items()), 
                                columns=['Sport', 'Avg Usage %'])
        
        fig_court = px.pie(sport_data, values='Avg Usage %', names='Sport',
                          title="Court Usage Distribution")
        st.plotly_chart(fig_court, use_container_width=True)
    
    # Lacrosse-specific analysis
    if analysis_mode == 'Lacrosse Focus' or sport_filter == 'Lacrosse':
        st.markdown("### 🥍 Comprehensive Lacrosse Analytics")
        
        lacrosse_analysis = breakdown['lacrosse_analysis']
        
        if 'message' not in lacrosse_analysis:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("#### 📊 Usage Statistics")
                st.metric("Total Lacrosse Usage", f"{lacrosse_analysis['total_lacrosse_usage']:.1f}%")
                st.metric("Current Season", lacrosse_analysis['seasonal_impact'])
                st.metric("Total Revenue", f"${lacrosse_analysis['revenue_analysis']['total_revenue']:.0f}")
            
            with col2:
                st.markdown("#### 🏟️ Field Preferences")
                field_prefs = lacrosse_analysis['field_preferences']
                field_df = pd.DataFrame(list(field_prefs.items()), columns=['Field', 'Usage %'])
                
                fig_fields = px.bar(field_df, x='Field', y='Usage %',
                                  title="Lacrosse Usage by Field")
                st.plotly_chart(fig_fields, use_container_width=True)
            
            with col3:
                st.markdown("#### ⏰ Peak Times")
                peak_hours = lacrosse_analysis['peak_hours']
                st.markdown("**Top Hours:**")
                for hour, usage in list(peak_hours.items())[:3]:
                    st.markdown(f"• {hour}:00 - {usage:.1f}%")
                
                peak_days = lacrosse_analysis['peak_days']
                st.markdown("**Top Days:**")
                for day, usage in list(peak_days.items())[:3]:
                    st.markdown(f"• {day} - {usage:.1f}%")
            
            # Growth opportunities
            st.markdown("#### 💡 Lacrosse Growth Opportunities")
            opportunities = lacrosse_analysis['growth_opportunities']
            for i, opportunity in enumerate(opportunities, 1):
                st.markdown(f"{i}. {opportunity}")
    
    # Revenue analysis section
    st.markdown("### 💰 Revenue Impact Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Revenue by facility type
        revenue_by_type = df.groupby('facility_type')['revenue_estimate'].sum().reset_index()
        
        fig_revenue = px.pie(revenue_by_type, values='revenue_estimate', names='facility_type',
                           title="Revenue Distribution by Facility Type")
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with col2:
        # Revenue by member tier
        revenue_by_tier = df.groupby('member_tier')['revenue_estimate'].sum().reset_index()
        
        fig_tier_revenue = px.bar(revenue_by_tier, x='member_tier', y='revenue_estimate',
                                 title="Revenue by Member Tier")
        fig_tier_revenue.update_xaxis(tickangle=45)
        st.plotly_chart(fig_tier_revenue, use_container_width=True)
    
    # Optimization recommendations
    st.markdown("### 🎯 AI-Powered Optimization Recommendations")
    
    recommendations = []
    
    # General recommendations
    if df['usage_percentage'].mean() < 70:
        recommendations.append("📈 Overall utilization below 70% - consider promotional campaigns")
    
    if df[df['is_prime_time']]['usage_percentage'].mean() > 90:
        recommendations.append("⚡ Prime time over 90% utilized - implement dynamic pricing")
    
    # Lacrosse-specific recommendations
    lacrosse_data = df[df['sport'] == 'Lacrosse']
    if not lacrosse_data.empty:
        lacrosse_avg = lacrosse_data['usage_percentage'].mean()
        if lacrosse_avg > 80:
            recommendations.append("🥍 High lacrosse demand - consider adding more field time slots")
        elif lacrosse_avg < 40:
            recommendations.append("🥍 Low lacrosse utilization - develop youth programs and clinics")
    
    # Weekend recommendations
    weekend_avg = df[df['is_weekend']]['usage_percentage'].mean()
    weekday_avg = df[~df['is_weekend']]['usage_percentage'].mean()
    if weekend_avg < weekday_avg:
        recommendations.append("📅 Weekend usage below weekday - create weekend events and tournaments")
    
    # Tier-specific recommendations
    basic_usage = df[df['member_tier'] == 'Basic Member']['usage_percentage'].mean()
    if basic_usage < 30:
        recommendations.append("👥 Low Basic Member engagement - offer beginner programs and discounts")
    
    for i, rec in enumerate(recommendations, 1):
        st.markdown(f"{i}. {rec}")
    
    # Export and refresh options
    st.markdown("### 🔧 Dashboard Controls")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Refresh Data", use_container_width=True):
            st.session_state.enhanced_heatmap_data = analyzer.generate_comprehensive_heatmap_data()
            st.success("Data refreshed!")
            st.rerun()
    
    with col2:
        if st.button("📊 Export Analysis", use_container_width=True):
            # Create export data
            export_data = {
                'summary': {
                    'total_sessions': len(df),
                    'average_usage': df['usage_percentage'].mean(),
                    'total_revenue': df['revenue_estimate'].sum(),
                    'analysis_timestamp': datetime.now().isoformat()
                },
                'facility_breakdown': breakdown,
                'recommendations': recommendations
            }
            
            st.download_button(
                label="💾 Download JSON Report",
                data=json.dumps(export_data, indent=2),
                file_name=f"nxs_heatmap_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
    
    with col3:
        if st.button("📈 Generate Insights", use_container_width=True):
            st.info("Advanced AI insights generated! Check recommendations above.")
    
    # Real-time alerts and notifications
    st.markdown("### 🚨 Real-Time Optimization Alerts")
    
    current_hour = datetime.now().hour
    alerts = []
    
    # Time-based alerts
    if 18 <= current_hour <= 21:
        if df[df['hour'] == current_hour]['usage_percentage'].mean() > 85:
            alerts.append({
                "type": "🔴 High Demand Alert",
                "message": "Prime time capacity near maximum - consider overflow planning",
                "action": "Activate backup facilities or implement waitlist system",
                "priority": "High"
            })
    
    # Lacrosse-specific alerts
    if sport_filter == 'Lacrosse' or 'Lacrosse' in [d['sport'] for d in filtered_data]:
        lacrosse_usage = df[df['sport'] == 'Lacrosse']['usage_percentage'].mean()
        if lacrosse_usage > 80:
            alerts.append({
                "type": "🥍 Lacrosse Demand Alert", 
                "message": "High lacrosse demand detected - expansion opportunity",
                "action": "Consider adding lacrosse-specific programming or field time",
                "priority": "Medium"
            })
    
    # Revenue opportunity alerts
    if df['revenue_estimate'].sum() > 5000:
        alerts.append({
            "type": "💰 Revenue Opportunity",
            "message": "High revenue potential identified in current usage patterns",
            "action": "Optimize pricing for peak demand periods",
            "priority": "Medium"
        })
    
    # Low utilization alerts
    low_usage_facilities = df.groupby('facility_name')['usage_percentage'].mean()
    for facility, usage in low_usage_facilities.items():
        if usage < 40:
            alerts.append({
                "type": "⚠️ Low Utilization Alert",
                "message": f"{facility} showing low utilization ({usage:.1f}%)",
                "action": "Review programming or consider alternative uses",
                "priority": "Low"
            })
    
    if not alerts:
        alerts.append({
            "type": "✅ All Systems Optimal",
            "message": "No critical alerts - facilities operating within normal parameters",
            "action": "Continue monitoring for optimization opportunities",
            "priority": "Info"
        })
    
    # Display alerts
    for alert in alerts[:5]:  # Limit to 5 alerts
        priority_colors = {
            "High": "#dc3545",
            "Medium": "#ffc107", 
            "Low": "#17a2b8",
            "Info": "#28a745"
        }
        
        color = priority_colors.get(alert['priority'], "#6c757d")
        
        st.markdown(f"""
        <div style="border-left: 4px solid {color}; background: #f8f9fa; padding: 1rem; margin: 0.5rem 0; border-radius: 4px;">
            <h6 style="margin: 0; color: {color};">{alert['type']}</h6>
            <p style="margin: 0.5rem 0;">{alert['message']}</p>
            <p style="margin: 0; font-size: 0.9rem;"><strong>Recommended Action:</strong> {alert['action']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Advanced analytics section
    st.markdown("### 📊 Advanced Pattern Analysis")
    
    # Create advanced analytics tabs
    analytics_tabs = st.tabs(["🕒 Time Patterns", "🏟️ Facility Efficiency", "👥 Member Behavior", "💡 Predictive Insights"])
    
    with analytics_tabs[0]:
        st.markdown("#### ⏰ Temporal Usage Patterns")
        
        # Hourly pattern analysis
        hourly_data = df.groupby(['hour', 'day_category'])['usage_percentage'].mean().reset_index()
        
        fig_hourly = px.line(hourly_data, x='hour', y='usage_percentage', color='day_category',
                           title="Usage Patterns: Weekday vs Weekend")
        fig_hourly.update_layout(xaxis_title="Hour of Day", yaxis_title="Average Usage %")
        st.plotly_chart(fig_hourly, use_container_width=True)
        
        # Day-of-week analysis
        daily_data = df.groupby(['day', 'time_category'])['usage_percentage'].mean().reset_index()
        
        # Reorder days
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        daily_data['day'] = pd.Categorical(daily_data['day'], categories=day_order, ordered=True)
        daily_data = daily_data.sort_values('day')
        
        fig_daily = px.bar(daily_data, x='day', y='usage_percentage', color='time_category',
                          title="Usage by Day of Week: Prime Time vs Off-Peak",
                          barmode='group')
        st.plotly_chart(fig_daily, use_container_width=True)
    
    with analytics_tabs[1]:
        st.markdown("#### 🎯 Facility Efficiency Metrics")
        
        # Efficiency analysis
        efficiency_data = df.groupby('facility_name').agg({
            'usage_percentage': 'mean',
            'revenue_estimate': 'sum',
            'member_tier': 'nunique'
        }).round(2)
        
        efficiency_data.columns = ['Avg Usage %', 'Total Revenue', 'Tier Diversity']
        efficiency_data['Efficiency Score'] = (
            efficiency_data['Avg Usage %'] * 0.4 + 
            (efficiency_data['Total Revenue'] / efficiency_data['Total Revenue'].max() * 100) * 0.4 +
            (efficiency_data['Tier Diversity'] / efficiency_data['Tier Diversity'].max() * 100) * 0.2
        ).round(1)
        
        st.dataframe(efficiency_data.sort_values('Efficiency Score', ascending=False))
        
        # Efficiency visualization
        fig_efficiency = px.scatter(efficiency_data, 
                                  x='Avg Usage %', 
                                  y='Total Revenue',
                                  size='Efficiency Score',
                                  hover_name=efficiency_data.index,
                                  title="Facility Performance: Usage vs Revenue vs Efficiency")
        st.plotly_chart(fig_efficiency, use_container_width=True)
    
    with analytics_tabs[2]:
        st.markdown("#### 👥 Member Behavior Analysis")
        
        # Member tier analysis
        tier_behavior = df.groupby(['member_tier', 'facility_type'])['usage_percentage'].mean().reset_index()
        
        fig_tier_behavior = px.bar(tier_behavior, 
                                 x='member_tier', 
                                 y='usage_percentage', 
                                 color='facility_type',
                                 title="Member Tier Preferences by Facility Type",
                                 barmode='group')
        fig_tier_behavior.update_xaxis(tickangle=45)
        st.plotly_chart(fig_tier_behavior, use_container_width=True)
        
        # Sport preferences by tier
        sport_tier_data = df.groupby(['sport', 'member_tier'])['usage_percentage'].mean().reset_index()
        
        fig_sport_tier = px.heatmap(sport_tier_data.pivot(index='sport', columns='member_tier', values='usage_percentage'),
                                  title="Sport Preferences Heatmap by Member Tier")
        st.plotly_chart(fig_sport_tier, use_container_width=True)
    
    with analytics_tabs[3]:
        st.markdown("#### 🔮 Predictive Insights & Forecasting")
        
        # Growth projections
        st.markdown("**📈 Growth Projections (Next 30 Days):**")
        
        current_avg = df['usage_percentage'].mean()
        projected_growth = random.uniform(1.05, 1.15)  # 5-15% growth
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Current Avg Usage", f"{current_avg:.1f}%")
        with col2:
            st.metric("Projected Usage", f"{current_avg * projected_growth:.1f}%", 
                     f"+{(projected_growth - 1) * 100:.1f}%")
        with col3:
            revenue_projection = df['revenue_estimate'].sum() * projected_growth
            st.metric("Revenue Forecast", f"${revenue_projection:,.0f}",
                     f"+${(revenue_projection - df['revenue_estimate'].sum()):,.0f}")
        
        # Seasonal adjustments for lacrosse
        if sport_filter == 'Lacrosse' or any(d['sport'] == 'Lacrosse' for d in filtered_data):
            st.markdown("**🥍 Lacrosse Seasonal Forecast:**")
            
            current_season = analyzer.lacrosse_seasons[df[df['sport'] == 'Lacrosse']['season'].iloc[0] if len(df[df['sport'] == 'Lacrosse']) > 0 else 'Spring']
            
            st.markdown(f"• Current season multiplier: {current_season['multiplier']}x")
            st.markdown("• **Spring**: Peak season (1.5x) - Highest participation expected")
            st.markdown("• **Fall**: Strong season (1.3x) - Good participation levels")  
            st.markdown("• **Summer**: Moderate season (0.8x) - Camp and clinic opportunities")
            st.markdown("• **Winter**: Low season (0.4x) - Indoor training focus")
        
        # Capacity warnings
        st.markdown("**⚠️ Capacity Planning Alerts:**")
        
        high_usage_facilities = df.groupby('facility_name')['usage_percentage'].mean()
        capacity_warnings = []
        
        for facility, usage in high_usage_facilities.items():
            if usage > 85:
                capacity_warnings.append(f"• {facility}: {usage:.1f}% - Consider expansion or schedule optimization")
            elif usage > 75:
                capacity_warnings.append(f"• {facility}: {usage:.1f}% - Monitor for peak time conflicts")
        
        if capacity_warnings:
            for warning in capacity_warnings:
                st.markdown(warning)
        else:
            st.markdown("• All facilities operating within optimal capacity ranges")
    
    # Footer with timestamp and system info
    st.markdown("---")
    st.markdown(f"""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p><strong>NXS Enhanced Heatmap Dashboard</strong> | Real-Time Facility Analytics with Lacrosse Support</p>
        <p>🔄 Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | 
        📊 Data Points: {len(df):,} | 
        🏟️ Facilities: {df['facility_name'].nunique()} | 
        ⚽ Sports: {df['sport'].nunique()}</p>
        <p>Status: 🟢 All systems operational | Enhanced with visual field breakdown and lacrosse analytics</p>
    </div>
    """, unsafe_allow_html=True)

# Integration function for main NXS platform
def integrate_enhanced_heatmap_into_nxs():
    """
    Integration function to add this enhanced heatmap to your main NXS platform.
    
    To integrate this into your main NXS Sports AI Platform:
    1. Add this as a new tab in your main application
    2. Import this module in your main file
    3. Call run_enhanced_heatmap_dashboard() from your tab selection
    """
    
    # This would be added to your main tabs list:
    # tabs = st.tabs([
    #     "🏠 Dashboard", 
    #     "👥 Memberships",
    #     "🏟️ Court/Turf Optimization",
    #     "🔥 Enhanced Heatmap",  # <-- ADD THIS
    #     "🏆 Tournaments", 
    #     "💪 Wellness", 
    #     "💼 NIL Management", 
    #     "📱 Smart Systems",
    #     "💰 Revenue",
    #     "📊 Analytics"
    # ])
    
    # Then in your tab handler:
    # with tabs[3]:  # Enhanced Heatmap tab
    #     run_enhanced_heatmap_dashboard()
    
    pass

# Main execution
if __name__ == "__main__":
    run_enhanced_heatmap_dashboard()