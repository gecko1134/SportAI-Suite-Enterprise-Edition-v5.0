"""
NXS Complete Fundraising & Investment Hub Module
Integrates Player Lab Investment Campaign, Bricks & Naming Campaign, and AI Grant Management
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date, timedelta
import json
from typing import Dict, List, Any, Optional
import random

class PlayerLabCampaign:
    """NXS Player Lab Investment Campaign Management"""
    
    def __init__(self):
        self.investment_tiers = {
            "player_lab_sponsor": {
                "name": "Player Lab Sponsor",
                "investment": 250000,
                "slots_total": 4,
                "slots_available": 2,
                "benefits": "10-year naming rights, branding, VIP access",
                "revenue_share": "Branding rights only"
            },
            "lab_operator": {
                "name": "Lab Operator", 
                "investment": 100000,
                "slots_total": 6,
                "slots_available": 3,
                "benefits": "Lease/own station, 70-80% net revenue",
                "revenue_share": "70-80% of generated revenue"
            },
            "equipment_co_owner": {
                "name": "Equipment Co-Owner",
                "investment": 25000,
                "slots_total": 10,
                "slots_available": 7,
                "benefits": "Quarterly revenue share based on usage",
                "revenue_share": "Quarterly % based on tracked usage"
            },
            "performance_donor": {
                "name": "Performance Donor",
                "investment": 10000,
                "slots_total": 20,
                "slots_available": 15,
                "benefits": "Recognition wall + member perks",
                "revenue_share": "Non-ownership with lifetime perks"
            }
        }
        
        self.target_businesses = {
            "batbox_valhalla": {
                "name": "Batbox/Valhalla",
                "description": "Hitting tunnels & LED reaction rings",
                "revenue_potential": "150-200/hour",
                "space_required": "500 sq ft"
            },
            "shoot_360": {
                "name": "Shoot 360/Noah", 
                "description": "Smart basketball shooting zones",
                "revenue_potential": "200/hour with 4-6 athletes",
                "space_required": "400 sq ft"
            },
            "exos_parisi": {
                "name": "EXOS/Parisi",
                "description": "Performance training tenants",
                "revenue_potential": "8K-12K/month per 1000 sq ft",
                "space_required": "1000+ sq ft"
            },
            "cryo_normatec": {
                "name": "Cryo/Normatec",
                "description": "Athlete recovery & wellness",
                "revenue_potential": "100-150/hour",
                "space_required": "300 sq ft"
            },
            "xp_league": {
                "name": "XP League/Film Stations",
                "description": "Esports & coaching stations",
                "revenue_potential": "50-100/hour",
                "space_required": "200 sq ft"
            }
        }
        
        self.phase_1_target = 2050000
        self.current_funding = 1230000
        
    def get_campaign_status(self) -> Dict[str, Any]:
        """Get current campaign status and metrics"""
        total_invested = sum([
            (tier["slots_total"] - tier["slots_available"]) * tier["investment"] 
            for tier in self.investment_tiers.values()
        ])
        
        return {
            "phase_1_target": self.phase_1_target,
            "current_funding": self.current_funding,
            "funding_percentage": (self.current_funding / self.phase_1_target) * 100,
            "slots_filled": sum([tier["slots_total"] - tier["slots_available"] for tier in self.investment_tiers.values()]),
            "total_slots": sum([tier["slots_total"] for tier in self.investment_tiers.values()]),
            "projected_monthly_revenue": random.randint(45000, 65000)
        }
    
    def calculate_revenue_projections(self) -> Dict[str, Any]:
        """Calculate revenue projections for different scenarios"""
        return {
            "conservative": {
                "monthly": 35000,
                "annual": 420000,
                "roi_percentage": 20.5
            },
            "moderate": {
                "monthly": 50000,
                "annual": 600000,
                "roi_percentage": 29.3
            },
            "optimistic": {
                "monthly": 72000,
                "annual": 864000,
                "roi_percentage": 42.1
            }
        }

class BricksNamingCampaign:
    """Legacy Bricks & Naming Campaign Management"""
    
    def __init__(self):
        self.brick_tiers = {
            "champion_brick": {
                "name": "Champion Brick",
                "price": 1000,
                "max_units": 100,
                "sold": 35,
                "placement": "Entry Plaza",
                "benefits": "Large engraved, central visibility"
            },
            "team_tile": {
                "name": "Team Tile",
                "price": 500,
                "max_units": 200,
                "sold": 78,
                "placement": "Trail/Wall Path",
                "benefits": "Team/group recognition"
            },
            "legacy_brick": {
                "name": "Legacy Brick", 
                "price": 250,
                "max_units": 500,
                "sold": 156,
                "placement": "Trail/Wall",
                "benefits": "Medium engraved brick"
            },
            "youth_tribute": {
                "name": "Youth Tribute",
                "price": 100,
                "max_units": 1000,
                "sold": 267,
                "placement": "Wall Base/Trail Edge",
                "benefits": "Affordable tribute"
            }
        }
        
        self.naming_zones = {
            "founding_city_sponsor": {
                "name": "Founding City Sponsor",
                "price": 150000,
                "status": "available",
                "term": "Lifetime"
            },
            "team_wall_sponsor": {
                "name": "Team Wall Sponsor",
                "price": 75000,
                "status": "sold",
                "term": "10 years"
            },
            "plaza_stone": {
                "name": "Plaza Stone",
                "price": 50000,
                "status": "available", 
                "term": "10 years"
            },
            "dedication_benches": {
                "name": "Dedication Benches",
                "price": 25000,
                "status": "available",
                "term": "10 years"
            },
            "honor_panels": {
                "name": "Honor Panels",
                "price": 15000,
                "status": "sold",
                "term": "10 years"
            }
        }
    
    def get_campaign_revenue(self) -> Dict[str, Any]:
        """Calculate total campaign revenue potential"""
        bricks_revenue = sum([
            tier["sold"] * tier["price"] for tier in self.brick_tiers.values()
        ])
        
        bricks_potential = sum([
            tier["max_units"] * tier["price"] for tier in self.brick_tiers.values()
        ])
        
        naming_revenue = sum([
            zone["price"] for zone in self.naming_zones.values() if zone["status"] == "sold"
        ])
        
        naming_potential = sum([zone["price"] for zone in self.naming_zones.values()])
        
        return {
            "bricks_current": bricks_revenue,
            "bricks_potential": bricks_potential,
            "naming_current": naming_revenue,
            "naming_potential": naming_potential,
            "total_current": bricks_revenue + naming_revenue,
            "total_potential": bricks_potential + naming_potential
        }

class GrantManagementSystem:
    """AI-Powered Grant Discovery and Management"""
    
    def __init__(self):
        self.grant_categories = {
            "youth_sports": {
                "name": "Youth Sports",
                "grants": [
                    {"name": "Play60 Foundation", "amount": 15000, "deadline": "2024-08-01"},
                    {"name": "Youth Activity Fund", "amount": 12000, "deadline": "2024-09-15"},
                    {"name": "Active Living Challenge", "amount": 8000, "deadline": "2024-10-30"}
                ]
            },
            "adaptive_access": {
                "name": "Adaptive Access",
                "grants": [
                    {"name": "Inclusive Rec Fund", "amount": 20000, "deadline": "2024-09-30"},
                    {"name": "Adaptive Athletics Fund", "amount": 18000, "deadline": "2024-11-15"}
                ]
            },
            "facility_expansion": {
                "name": "Facility Expansion",
                "grants": [
                    {"name": "State Infrastructure Bond", "amount": 100000, "deadline": "2024-12-01"},
                    {"name": "Tourism Grant Program", "amount": 35000, "deadline": "2024-07-15"}
                ]
            },
            "environment_trails": {
                "name": "Environment & Trails",
                "grants": [
                    {"name": "Green Recreation Fund", "amount": 25000, "deadline": "2025-01-15"},
                    {"name": "Trail Development Grant", "amount": 15000, "deadline": "2024-08-30"}
                ]
            }
        }
        
        self.active_applications = [
            {
                "name": "Play60 Foundation",
                "category": "Youth Sports",
                "amount": 15000,
                "status": "submitted",
                "deadline": "2024-08-01",
                "probability": 0.75
            },
            {
                "name": "Green Rec Fund",
                "category": "Environment & Trails", 
                "amount": 25000,
                "status": "approved",
                "deadline": "completed",
                "probability": 1.0
            },
            {
                "name": "Tourism Grant",
                "category": "Facility Expansion",
                "amount": 35000,
                "status": "draft",
                "deadline": "2024-07-15",
                "probability": 0.60
            }
        ]
    
    def generate_grant_narrative(self, program_name: str, amount: int, focus_area: str) -> str:
        """AI Grant Writer - Generate grant narrative"""
        today = date.today().strftime("%B %d, %Y")
        
        narrative = f"""
**Grant Narrative – {program_name}**

As of {today}, NXS Sports Complex seeks ${amount:,} in funding to support our mission in {focus_area.lower()} development. 

**Project Overview:**
This proposal supports the expansion of {program_name}, which directly serves our community's need for accessible, high-quality sports and recreation facilities. Our AI-powered facility management system ensures optimal resource allocation and measurable impact tracking.

**Community Impact:**
- Increased accessibility for underserved populations
- Enhanced youth development programming 
- Improved community health and wellness outcomes
- Economic development through sports tourism

**Measurable Outcomes:**
We will track participation rates, community engagement metrics, and economic impact through our integrated data management platform. Expected outcomes include:
- 25% increase in program participation
- Improved accessibility compliance
- Enhanced community partnerships
- Sustainable revenue growth

**Organizational Capacity:**
NXS Sports Complex operates with cutting-edge AI technology, comprehensive governance structure, and proven track record of community impact. Our board of directors brings expertise in healthcare, finance, legal affairs, and community development.

Thank you for your consideration of this proposal. We look forward to partnering with your foundation to create lasting positive impact in our community.

Sincerely,
NXS Sports Complex Development Team
        """
        
        return narrative.strip()
    
    def calculate_success_probability(self, grant_data: Dict[str, Any]) -> float:
        """Calculate grant success probability using AI modeling"""
        base_probability = 0.40  # Base 40% success rate
        
        # Adjust based on factors
        if grant_data.get("prior_relationship", False):
            base_probability += 0.20
        
        if grant_data.get("amount", 0) < 20000:
            base_probability += 0.15  # Smaller grants more likely
        
        if grant_data.get("category") == "Youth Sports":
            base_probability += 0.10  # High priority area
            
        if grant_data.get("matching_funds", False):
            base_probability += 0.25  # Matching funds boost success
        
        return min(base_probability, 0.95)  # Cap at 95%

class FundraisingInvestmentHub:
    """Main module class integrating all fundraising campaigns"""
    
    def __init__(self):
        self.player_lab = PlayerLabCampaign()
        self.bricks_naming = BricksNamingCampaign()
        self.grants = GrantManagementSystem()
        
    def run(self):
        """Main Streamlit interface"""
        st.set_page_config(
            page_title="🎯 NXS Fundraising & Investment Hub",
            page_icon="🎯",
            layout="wide"
        )
        
        st.title("🎯 NXS Complete Fundraising & Investment Hub")
        st.markdown("*Integrated campaign management for Player Lab, Legacy Bricks, and Grant opportunities*")
        
        # Main navigation tabs
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Campaign Overview", 
            "🏅 Player Lab Investment", 
            "🧱 Bricks & Naming Campaign", 
            "📝 Grant Management"
        ])
        
        with tab1:
            self._render_overview()
        
        with tab2:
            self._render_player_lab()
        
        with tab3:
            self._render_bricks_naming()
        
        with tab4:
            self._render_grants()
    
    def _render_overview(self):
        """Render campaign overview dashboard"""
        st.header("📊 Campaign Overview Dashboard")
        
        # Calculate totals
        player_lab_status = self.player_lab.get_campaign_status()
        bricks_revenue = self.bricks_naming.get_campaign_revenue()
        
        total_target = (player_lab_status["phase_1_target"] + 
                       bricks_revenue["total_potential"] + 195000)
        total_current = (player_lab_status["current_funding"] + 
                        bricks_revenue["total_current"] + 40000)
        
        # Top metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("💰 Total Campaign Target", f"${total_target/1000000:.1f}M")
        with col2:
            st.metric("✅ Current Funding", f"${total_current/1000000:.1f}M")
        with col3:
            st.metric("📈 Overall Progress", f"{(total_current/total_target)*100:.1f}%")
        with col4:
            st.metric("🎯 Active Campaigns", "3")
        
        # Progress visualization
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Campaign Revenue Breakdown")
            
            breakdown_data = pd.DataFrame({
                'Campaign': ['Player Lab', 'Bricks & Naming', 'Grants'],
                'Target': [2050000, 1007500, 195000],
                'Current': [1230000, 423000, 40000]
            })
            
            fig = px.bar(breakdown_data, x='Campaign', y=['Target', 'Current'],
                        title='Funding Progress by Campaign',
                        barmode='group',
                        color_discrete_map={'Target': '#E5E7EB', 'Current': '#10B981'})
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Investment Distribution")
            
            pie_data = pd.DataFrame({
                'Campaign': ['Player Lab', 'Bricks & Naming', 'Grants'],
                'Amount': [2050000, 1007500, 195000]
            })
            
            fig = px.pie(pie_data, values='Amount', names='Campaign',
                        title='Total Campaign Target Distribution')
            st.plotly_chart(fig, use_container_width=True)
        
        # Recent activity
        st.subheader("📅 Recent Campaign Activity")
        
        activity_data = pd.DataFrame({
            'Date': ['2024-06-15', '2024-06-12', '2024-06-10', '2024-06-08'],
            'Campaign': ['Player Lab', 'Bricks & Naming', 'Grants', 'Player Lab'],
            'Activity': ['New Lab Operator investment', 'Champion Brick sold', 'Green Rec Fund approved', 'Performance Donor added'],
            'Amount': ['$100,000', '$1,000', '$25,000', '$10,000']
        })
        
        st.dataframe(activity_data, use_container_width=True)
    
    def _render_player_lab(self):
        """Render Player Lab investment campaign"""
        st.header("🏅 NXS Player Lab Elite Training Hub")
        
        campaign_status = self.player_lab.get_campaign_status()
        
        # Campaign header with metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("💰 Funding Target", f"${campaign_status['phase_1_target']:,}")
        with col2:
            st.metric("✅ Current Funding", f"${campaign_status['current_funding']:,}")
        with col3:
            st.metric("📊 Progress", f"{campaign_status['funding_percentage']:.1f}%")
        with col4:
            st.metric("🎯 Slots Filled", f"{campaign_status['slots_filled']}/{campaign_status['total_slots']}")
        
        # Progress bar
        progress = campaign_status['funding_percentage'] / 100
        st.progress(progress)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("💼 Investment Tiers")
            
            for tier_key, tier in self.player_lab.investment_tiers.items():
                with st.expander(f"{tier['name']} - ${tier['investment']:,}"):
                    st.write(f"**Available Slots:** {tier['slots_available']} of {tier['slots_total']}")
                    st.write(f"**Benefits:** {tier['benefits']}")
                    st.write(f"**Revenue Share:** {tier['revenue_share']}")
                    
                    slots_filled = tier['slots_total'] - tier['slots_available']
                    slot_progress = slots_filled / tier['slots_total']
                    st.progress(slot_progress)
                    
                    if st.button(f"📋 Investment Details", key=f"details_{tier_key}"):
                        st.success(f"Investment packet generated for {tier['name']}")
        
        with col2:
            st.subheader("🏢 Target Training Businesses")
            
            for business_key, business in self.player_lab.target_businesses.items():
                st.markdown(f"""
                **{business['name']}**  
                {business['description']}  
                *Revenue: {business['revenue_potential']} | Space: {business['space_required']}*
                """)
                st.markdown("---")
            
            st.subheader("📈 Revenue Projections")
            projections = self.player_lab.calculate_revenue_projections()
            
            projection_df = pd.DataFrame({
                'Scenario': ['Conservative', 'Moderate', 'Optimistic'],
                'Monthly Revenue': [p['monthly'] for p in projections.values()],
                'Annual Revenue': [p['annual'] for p in projections.values()],
                'ROI %': [p['roi_percentage'] for p in projections.values()]
            })
            
            st.dataframe(projection_df, use_container_width=True)
    
    def _render_bricks_naming(self):
        """Render Bricks & Naming campaign"""
        st.header("🧱 Legacy Bricks & Naming Campaign")
        
        revenue_data = self.bricks_naming.get_campaign_revenue()
        
        # Campaign metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("🧱 Bricks Revenue", f"${revenue_data['bricks_current']:,}")
        with col2:
            st.metric("🏷️ Naming Revenue", f"${revenue_data['naming_current']:,}")
        with col3:
            st.metric("💰 Total Current", f"${revenue_data['total_current']:,}")
        with col4:
            st.metric("🎯 Total Potential", f"${revenue_data['total_potential']:,}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🧱 Brick & Tile Sales")
            
            for tier_key, tier in self.bricks_naming.brick_tiers.items():
                progress = tier['sold'] / tier['max_units']
                revenue = tier['sold'] * tier['price']
                
                st.markdown(f"**{tier['name']} - ${tier['price']}**")
                st.markdown(f"Sold: {tier['sold']} of {tier['max_units']} | Revenue: ${revenue:,}")
                st.markdown(f"Placement: {tier['placement']}")
                st.progress(progress)
                st.markdown("---")
        
        with col2:
            st.subheader("🏷️ Naming Zone Opportunities")
            
            for zone_key, zone in self.bricks_naming.naming_zones.items():
                status_color = "🟢" if zone['status'] == 'available' else "🔴"
                
                st.markdown(f"""
                {status_color} **{zone['name']}**  
                Price: ${zone['price']:,} | Term: {zone['term']}  
                Status: {zone['status'].title()}
                """)
                
                if zone['status'] == 'available':
                    if st.button(f"📋 Purchase Info", key=f"naming_{zone_key}"):
                        st.success(f"Information packet sent for {zone['name']}")
                
                st.markdown("---")
        
        # Sales chart
        st.subheader("📊 Sales Progress Visualization")
        
        brick_df = pd.DataFrame([
            {
                'Tier': tier['name'],
                'Sold': tier['sold'],
                'Available': tier['max_units'] - tier['sold'],
                'Revenue': tier['sold'] * tier['price']
            }
            for tier in self.bricks_naming.brick_tiers.values()
        ])
        
        fig = px.bar(brick_df, x='Tier', y=['Sold', 'Available'],
                    title='Brick Sales Progress by Tier',
                    color_discrete_map={'Sold': '#10B981', 'Available': '#E5E7EB'})
        st.plotly_chart(fig, use_container_width=True)
    
    def _render_grants(self):
        """Render Grant Management system"""
        st.header("📝 AI-Powered Grant Management Center")
        
        # Grant metrics
        total_potential = sum([
            sum([grant["amount"] for grant in category["grants"]])
            for category in self.grants.grant_categories.values()
        ])
        
        approved_amount = sum([
            app["amount"] for app in self.grants.active_applications 
            if app["status"] == "approved"
        ])
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("📝 Active Applications", len(self.grants.active_applications))
        with col2:
            st.metric("💰 Total Potential", f"${total_potential:,}")
        with col3:
            st.metric("✅ Approved Amount", f"${approved_amount:,}")
        with col4:
            st.metric("📊 Success Rate", "67%")
        
        # Grant tabs
        grant_tab1, grant_tab2, grant_tab3 = st.tabs([
            "📋 Active Applications", 
            "🤖 AI Grant Writer", 
            "🔍 Grant Discovery"
        ])
        
        with grant_tab1:
            st.subheader("📋 Grant Application Pipeline")
            
            app_df = pd.DataFrame(self.grants.active_applications)
            
            for _, app in app_df.iterrows():
                status_colors = {
                    'approved': '🟢',
                    'submitted': '🟡', 
                    'draft': '🔵',
                    'researching': '⚪'
                }
                
                status_color = status_colors.get(app['status'], '⚪')
                
                with st.expander(f"{status_color} {app['name']} - ${app['amount']:,}"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"**Category:** {app['category']}")
                        st.write(f"**Status:** {app['status'].title()}")
                        st.write(f"**Deadline:** {app['deadline']}")
                    
                    with col2:
                        st.write(f"**Success Probability:** {app['probability']:.1%}")
                        st.progress(app['probability'])
                    
                    if app['status'] == 'draft':
                        if st.button(f"📝 Complete Application", key=f"complete_{app['name']}"):
                            st.success(f"Application completion workflow started for {app['name']}")
        
        with grant_tab2:
            st.subheader("🤖 AI Grant Writing Assistant")
            
            col1, col2 = st.columns(2)
            
            with col1:
                program_name = st.text_input("Program Name", value="Youth Sports Access Program")
                funding_amount = st.number_input("Funding Request ($)", 1000, 200000, 25000)
                focus_area = st.selectbox("Focus Area", [
                    "Youth Development", "Adaptive Access", "Facility Expansion",
                    "Community Health", "Environmental Sustainability"
                ])
            
            with col2:
                if st.button("🎯 Generate Grant Narrative", use_container_width=True):
                    narrative = self.grants.generate_grant_narrative(
                        program_name, funding_amount, focus_area
                    )
                    
                    st.text_area("Generated Narrative", narrative, height=400)
                    
                    # Download button
                    st.download_button(
                        "📄 Download Narrative",
                        narrative,
                        file_name=f"{program_name.replace(' ', '_')}_grant_narrative.txt",
                        mime="text/plain"
                    )
        
        with grant_tab3:
            st.subheader("🔍 AI Grant Discovery & Matching")
            
            st.markdown("### Available Grant Opportunities by Category")
            
            for category_key, category in self.grants.grant_categories.items():
                with st.expander(f"📂 {category['name']} Grants"):
                    for grant in category['grants']:
                        probability = self.grants.calculate_success_probability({
                            'amount': grant['amount'],
                            'category': category['name']
                        })
                        
                        st.markdown(f"""
                        **{grant['name']}**  
                        Amount: ${grant['amount']:,} | Deadline: {grant['deadline']}  
                        Success Probability: {probability:.1%}
                        """)
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            if st.button(f"📋 Research Grant", key=f"research_{grant['name']}"):
                                st.success(f"Research initiated for {grant['name']}")
                        with col2:
                            if st.button(f"✍️ Start Application", key=f"apply_{grant['name']}"):
                                st.success(f"Application started for {grant['name']}")
                        
                        st.markdown("---")

# Main module function for integration
def run():
    """Main function to run the Fundraising & Investment Hub"""
    hub = FundraisingInvestmentHub()
    hub.run()

if __name__ == "__main__":
    run()
