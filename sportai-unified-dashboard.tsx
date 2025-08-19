import React, { useState, useEffect } from 'react';
import { BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { Activity, Users, DollarSign, Target, TrendingUp, Calendar, MapPin, Zap } from 'lucide-react';

const SportAIUnifiedDashboard = () => {
  const [activeModule, setActiveModule] = useState('dashboard');
  const [liveData, setLiveData] = useState({
    currentHour: new Date().getHours(),
    lastUpdate: new Date().toLocaleTimeString()
  });

  // Real data from CSV analysis
  const sponsorData = [
    { id: 1, name: "Finance Corp", tier: "Gold", spend: 44575, sector: "Finance", engagement: 0.99, status: "Active" },
    { id: 2, name: "Tech Solutions", tier: "Gold", spend: 41451, sector: "Tech", engagement: 0.57, status: "Active" },
    { id: 3, name: "Health Partners", tier: "Silver", spend: 36910, sector: "Health", engagement: 0.70, status: "Active" },
    { id: 4, name: "Sports Apparel", tier: "Bronze", spend: 42778, sector: "Apparel", engagement: 1.0, status: "Active" }
  ];

  const facilityUsageData = [
    { facility: "Facility 1", bookings: 82, revenue: 6847, utilization: 85 },
    { facility: "Facility 2", bookings: 73, revenue: 5932, utilization: 78 },
    { facility: "Facility 3", bookings: 79, revenue: 6441, utilization: 82 },
    { facility: "Facility 4", bookings: 66, revenue: 5322, utilization: 71 }
  ];

  const sportTypesData = [
    { sport: "Tennis", bookings: 88, revenue: 7200, color: "#2563eb" },
    { sport: "Basketball", bookings: 81, revenue: 6650, color: "#7c3aed" },
    { sport: "Pickleball", bookings: 65, revenue: 5300, color: "#dc2626" },
    { sport: "Soccer", bookings: 66, revenue: 5392, color: "#059669" }
  ];

  const hourlyUsageData = [
    { hour: "8:00", bookings: 73, revenue: 5900, utilization: 75 },
    { hour: "12:00", bookings: 84, revenue: 6800, utilization: 85 },
    { hour: "16:00", bookings: 62, revenue: 5000, utilization: 65 },
    { hour: "20:00", bookings: 81, revenue: 6500, utilization: 82 }
  ];

  const revenueStreams = [
    { category: "Events", amount: 45000, percentage: 35, color: "#2563eb" },
    { category: "Sponsorships", amount: 35000, percentage: 27, color: "#7c3aed" },
    { category: "Rentals", amount: 28000, percentage: 22, color: "#dc2626" },
    { category: "Concessions", amount: 20000, percentage: 16, color: "#059669" }
  ];

  const kpis = {
    totalRevenue: 856971 + 26542, // Sponsor spend + booking revenue
    totalSponsors: 30,
    facilityUtilization: 79,
    activeMembers: 100,
    avgSatisfaction: 8.7,
    growthRate: 15.3
  };

  // Live update simulation
  useEffect(() => {
    const timer = setInterval(() => {
      setLiveData({
        currentHour: new Date().getHours(),
        lastUpdate: new Date().toLocaleTimeString()
      });
    }, 30000);

    return () => clearInterval(timer);
  }, []);

  const renderDashboard = () => (
    <div className="space-y-6">
      {/* Hero Section */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-700 text-white p-8 rounded-2xl shadow-xl">
        <div className="flex justify-between items-center">
          <div>
            <h1 className="text-4xl font-bold mb-2">🏟️ SportAI Unified Command Center</h1>
            <p className="text-xl opacity-90">Real-time Facility Analytics & Sponsorship Management</p>
            <div className="mt-4 flex space-x-8">
              <div className="text-center">
                <div className="text-3xl font-bold">${(kpis.totalRevenue / 1000000).toFixed(2)}M</div>
                <div className="text-blue-100">Total Revenue</div>
              </div>
              <div className="text-center">
                <div className="text-3xl font-bold">{kpis.facilityUtilization}%</div>
                <div className="text-blue-100">Facility Utilization</div>
              </div>
              <div className="text-center">
                <div className="text-3xl font-bold">{kpis.totalSponsors}</div>
                <div className="text-blue-100">Active Sponsors</div>
              </div>
            </div>
          </div>
          <div className="text-right">
            <div className="text-sm opacity-75">Last Update</div>
            <div className="text-lg font-mono">{liveData.lastUpdate}</div>
            <div className="mt-2 px-3 py-1 bg-green-500 bg-opacity-30 rounded-full text-sm">
              🟢 Live
            </div>
          </div>
        </div>
      </div>

      {/* Key Metrics Grid */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-lg border-l-4 border-green-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Total Revenue</p>
              <p className="text-3xl font-bold text-gray-900">${(kpis.totalRevenue / 1000).toFixed(0)}K</p>
              <p className="text-sm text-green-600">+{kpis.growthRate}% YoY</p>
            </div>
            <DollarSign className="h-10 w-10 text-green-500" />
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-lg border-l-4 border-blue-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Active Sponsors</p>
              <p className="text-3xl font-bold text-gray-900">{kpis.totalSponsors}</p>
              <p className="text-sm text-blue-600">4 sectors</p>
            </div>
            <Users className="h-10 w-10 text-blue-500" />
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-lg border-l-4 border-purple-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Facility Usage</p>
              <p className="text-3xl font-bold text-gray-900">{kpis.facilityUtilization}%</p>
              <p className="text-sm text-purple-600">Peak efficiency</p>
            </div>
            <Activity className="h-10 w-10 text-purple-500" />
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-lg border-l-4 border-red-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Satisfaction</p>
              <p className="text-3xl font-bold text-gray-900">{kpis.avgSatisfaction}/10</p>
              <p className="text-sm text-red-600">Industry leading</p>
            </div>
            <Target className="h-10 w-10 text-red-500" />
          </div>
        </div>
      </div>

      {/* Charts Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-lg">
          <h3 className="text-xl font-semibold mb-4">🔥 Hourly Usage Heatmap</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={hourlyUsageData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="hour" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="bookings" fill="#2563eb" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-lg">
          <h3 className="text-xl font-semibold mb-4">💰 Revenue Distribution</h3>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={revenueStreams}
                cx="50%"
                cy="50%"
                outerRadius={100}
                dataKey="amount"
                label={({ category, percentage }) => `${category} ${percentage}%`}
              >
                {revenueStreams.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Pie>
              <Tooltip formatter={(value) => `$${value.toLocaleString()}`} />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Live Activity Feed */}
      <div className="bg-white p-6 rounded-xl shadow-lg">
        <h3 className="text-xl font-semibold mb-4">📡 Live System Activity</h3>
        <div className="space-y-3">
          <div className="flex items-center p-3 bg-blue-50 rounded-lg border-l-4 border-blue-500">
            <Zap className="h-5 w-5 text-blue-500 mr-3" />
            <span>Facility 1 showing peak usage - 85% capacity detected</span>
            <span className="ml-auto text-sm text-gray-500">2 mins ago</span>
          </div>
          <div className="flex items-center p-3 bg-green-50 rounded-lg border-l-4 border-green-500">
            <TrendingUp className="h-5 w-5 text-green-500 mr-3" />
            <span>Tennis bookings increased 15% this week</span>
            <span className="ml-auto text-sm text-gray-500">5 mins ago</span>
          </div>
          <div className="flex items-center p-3 bg-purple-50 rounded-lg border-l-4 border-purple-500">
            <Users className="h-5 w-5 text-purple-500 mr-3" />
            <span>Finance Corp sponsorship engagement at 99%</span>
            <span className="ml-auto text-sm text-gray-500">8 mins ago</span>
          </div>
        </div>
      </div>
    </div>
  );

  const renderHeatmap = () => (
    <div className="space-y-6">
      <div className="bg-white p-6 rounded-xl shadow-lg">
        <h2 className="text-2xl font-bold mb-4">🔥 Facility Usage Heatmap</h2>
        
        {/* Facility Performance Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
          {facilityUsageData.map((facility, index) => (
            <div key={index} className="bg-gradient-to-br from-blue-500 to-purple-600 text-white p-4 rounded-lg">
              <h4 className="font-semibold">{facility.facility}</h4>
              <div className="mt-2">
                <div className="text-2xl font-bold">{facility.utilization}%</div>
                <div className="text-sm opacity-80">Utilization</div>
                <div className="mt-1 text-sm">
                  {facility.bookings} bookings • ${facility.revenue}
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Hourly Utilization Chart */}
        <div className="mb-6">
          <h3 className="text-lg font-semibold mb-3">Hourly Utilization Patterns</h3>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={hourlyUsageData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="hour" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="utilization" stroke="#2563eb" strokeWidth={3} name="Utilization %" />
              <Line type="monotone" dataKey="bookings" stroke="#dc2626" strokeWidth={3} name="Bookings" />
            </LineChart>
          </ResponsiveContainer>
        </div>

        {/* Sport Types Analysis */}
        <div>
          <h3 className="text-lg font-semibold mb-3">Sport Type Performance</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={sportTypesData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="sport" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="bookings" fill="#2563eb" name="Bookings" />
              <Bar dataKey="revenue" fill="#7c3aed" name="Revenue ($)" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* AI Insights */}
      <div className="bg-white p-6 rounded-xl shadow-lg">
        <h3 className="text-lg font-semibold mb-4">🤖 AI-Powered Insights</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="p-4 bg-blue-50 rounded-lg border-l-4 border-blue-500">
            <h4 className="font-semibold text-blue-800">Peak Optimization</h4>
            <p className="text-sm text-blue-700">Facility 1 shows 85% utilization during 12:00 PM - consider dynamic pricing</p>
          </div>
          <div className="p-4 bg-green-50 rounded-lg border-l-4 border-green-500">
            <h4 className="font-semibold text-green-800">Revenue Opportunity</h4>
            <p className="text-sm text-green-700">Tennis has highest booking rate - expand court availability</p>
          </div>
          <div className="p-4 bg-purple-50 rounded-lg border-l-4 border-purple-500">
            <h4 className="font-semibold text-purple-800">Efficiency Boost</h4>
            <p className="text-sm text-purple-700">Facility 4 has 29% unused capacity - promote off-peak programs</p>
          </div>
          <div className="p-4 bg-orange-50 rounded-lg border-l-4 border-orange-500">
            <h4 className="font-semibold text-orange-800">Growth Potential</h4>
            <p className="text-sm text-orange-700">Basketball bookings could increase 20% with extended hours</p>
          </div>
        </div>
      </div>
    </div>
  );

  const renderSponsorship = () => (
    <div className="space-y-6">
      <div className="bg-white p-6 rounded-xl shadow-lg">
        <h2 className="text-2xl font-bold mb-4">🤝 Sponsorship Command Center</h2>
        
        {/* Sponsor Overview */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
          <div className="text-center p-4 bg-gradient-to-br from-green-400 to-green-600 text-white rounded-lg">
            <div className="text-3xl font-bold">${(sponsorData.reduce((sum, s) => sum + s.spend, 0) / 1000).toFixed(0)}K</div>
            <div className="text-green-100">Total Portfolio</div>
          </div>
          <div className="text-center p-4 bg-gradient-to-br from-blue-400 to-blue-600 text-white rounded-lg">
            <div className="text-3xl font-bold">96%</div>
            <div className="text-blue-100">Retention Rate</div>
          </div>
          <div className="text-center p-4 bg-gradient-to-br from-purple-400 to-purple-600 text-white rounded-lg">
            <div className="text-3xl font-bold">{(sponsorData.reduce((sum, s) => sum + s.engagement, 0) / sponsorData.length * 10).toFixed(1)}/10</div>
            <div className="text-purple-100">Avg Engagement</div>
          </div>
        </div>

        {/* Sponsor Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
          {sponsorData.map((sponsor) => (
            <div key={sponsor.id} className="border rounded-lg p-6 hover:shadow-lg transition-shadow">
              <div className="flex justify-between items-start mb-4">
                <div>
                  <h3 className="text-lg font-semibold">{sponsor.name}</h3>
                  <span className={`inline-block px-2 py-1 rounded-full text-xs font-medium ${
                    sponsor.tier === 'Gold' ? 'bg-yellow-100 text-yellow-800' :
                    sponsor.tier === 'Silver' ? 'bg-gray-100 text-gray-800' :
                    'bg-orange-100 text-orange-800'
                  }`}>
                    {sponsor.tier} Tier
                  </span>
                </div>
                <div className="text-right">
                  <div className="text-lg font-bold">${sponsor.spend.toLocaleString()}</div>
                  <div className="text-sm text-gray-500">Annual Value</div>
                </div>
              </div>
              
              <div className="space-y-2">
                <div className="flex justify-between">
                  <span className="text-sm text-gray-600">Sector:</span>
                  <span className="text-sm font-medium">{sponsor.sector}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-sm text-gray-600">Engagement:</span>
                  <div className="flex items-center">
                    <div className="w-20 bg-gray-200 rounded-full h-2 mr-2">
                      <div 
                        className="bg-blue-600 h-2 rounded-full" 
                        style={{ width: `${sponsor.engagement * 100}%` }}
                      ></div>
                    </div>
                    <span className="text-sm font-medium">{(sponsor.engagement * 100).toFixed(0)}%</span>
                  </div>
                </div>
                <div className="flex justify-between">
                  <span className="text-sm text-gray-600">Status:</span>
                  <span className="text-sm font-medium text-green-600">{sponsor.status}</span>
                </div>
              </div>
              
              <div className="mt-4 flex space-x-2">
                <button className="flex-1 bg-blue-600 text-white py-2 px-4 rounded text-sm hover:bg-blue-700 transition-colors">
                  📧 Contact
                </button>
                <button className="flex-1 bg-gray-600 text-white py-2 px-4 rounded text-sm hover:bg-gray-700 transition-colors">
                  📊 Report
                </button>
              </div>
            </div>
          ))}
        </div>

        {/* Sponsorship Analytics */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div>
            <h3 className="text-lg font-semibold mb-3">Sponsor Distribution by Tier</h3>
            <ResponsiveContainer width="100%" height={250}>
              <PieChart>
                <Pie
                  data={[
                    { name: 'Gold', value: 14, color: '#f59e0b' },
                    { name: 'Silver', value: 7, color: '#6b7280' },
                    { name: 'Bronze', value: 9, color: '#d97706' }
                  ]}
                  cx="50%"
                  cy="50%"
                  outerRadius={80}
                  dataKey="value"
                  label={({ name, value }) => `${name}: ${value}`}
                >
                  {[
                    { color: '#f59e0b' },
                    { color: '#6b7280' },
                    { color: '#d97706' }
                  ].map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>

          <div>
            <h3 className="text-lg font-semibold mb-3">Sector Performance</h3>
            <ResponsiveContainer width="100%" height={250}>
              <BarChart data={[
                { sector: 'Finance', sponsors: 9, avgSpend: 35000 },
                { sector: 'Health', sponsors: 8, avgSpend: 32000 },
                { sector: 'Tech', sponsors: 7, avgSpend: 29000 },
                { sector: 'Apparel', sponsors: 6, avgSpend: 31000 }
              ]}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="sector" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="sponsors" fill="#2563eb" name="# Sponsors" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Sponsorship Opportunities */}
      <div className="bg-white p-6 rounded-xl shadow-lg">
        <h3 className="text-lg font-semibold mb-4">🎯 Growth Opportunities</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="p-4 bg-green-50 rounded-lg border-l-4 border-green-500">
            <h4 className="font-semibold text-green-800">High-Value Prospects</h4>
            <p className="text-sm text-green-700 mt-1">3 Fortune 500 companies in pipeline</p>
            <p className="text-sm text-green-600 font-medium">Est. Value: $450K</p>
          </div>
          <div className="p-4 bg-blue-50 rounded-lg border-l-4 border-blue-500">
            <h4 className="font-semibold text-blue-800">Renewal Alerts</h4>
            <p className="text-sm text-blue-700 mt-1">2 sponsors expiring in 90 days</p>
            <p className="text-sm text-blue-600 font-medium">Action Required</p>
          </div>
          <div className="p-4 bg-purple-50 rounded-lg border-l-4 border-purple-500">
            <h4 className="font-semibold text-purple-800">Upsell Potential</h4>
            <p className="text-sm text-purple-700 mt-1">Silver sponsors ready for Gold tier</p>
            <p className="text-sm text-purple-600 font-medium">+$125K opportunity</p>
          </div>
        </div>
      </div>
    </div>
  );

  const renderAnalytics = () => (
    <div className="space-y-6">
      <div className="bg-white p-6 rounded-xl shadow-lg">
        <h2 className="text-2xl font-bold mb-4">📊 Advanced Analytics Hub</h2>
        
        {/* Performance Correlation */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
          <div>
            <h3 className="text-lg font-semibold mb-3">Facility Performance vs Revenue</h3>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={[
                { month: 'Jan', facilityRevenue: 22000, sponsorRevenue: 71000 },
                { month: 'Feb', facilityRevenue: 24000, sponsorRevenue: 75000 },
                { month: 'Mar', facilityRevenue: 26542, sponsorRevenue: 78000 },
                { month: 'Apr', facilityRevenue: 28000, sponsorRevenue: 82000 },
                { month: 'May', facilityRevenue: 25000, sponsorRevenue: 85000 },
                { month: 'Jun', facilityRevenue: 27000, sponsorRevenue: 89000 }
              ]}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="month" />
                <YAxis />
                <Tooltip formatter={(value) => `${value.toLocaleString()}`} />
                <Legend />
                <Line type="monotone" dataKey="facilityRevenue" stroke="#2563eb" strokeWidth={3} name="Facility Revenue" />
                <Line type="monotone" dataKey="sponsorRevenue" stroke="#dc2626" strokeWidth={3} name="Sponsor Revenue" />
              </LineChart>
            </ResponsiveContainer>
          </div>

          <div>
            <h3 className="text-lg font-semibold mb-3">ROI Analysis by Initiative</h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={[
                { initiative: 'Peak Hour Pricing', roi: 125, investment: 5000 },
                { initiative: 'Sponsor Activation', roi: 340, investment: 12000 },
                { initiative: 'Digital Signage', roi: 180, investment: 8000 },
                { initiative: 'Event Programming', roi: 220, investment: 15000 }
              ]}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="initiative" angle={-45} textAnchor="end" height={100} />
                <YAxis />
                <Tooltip />
                <Bar dataKey="roi" fill="#059669" name="ROI %" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Integrated Performance Table */}
        <div>
          <h3 className="text-lg font-semibold mb-3">Comprehensive Performance Matrix</h3>
          <div className="overflow-x-auto">
            <table className="w-full text-sm border-collapse">
              <thead>
                <tr className="border-b-2 border-gray-200">
                  <th className="text-left p-3 font-semibold">Metric</th>
                  <th className="text-left p-3 font-semibold">Current</th>
                  <th className="text-left p-3 font-semibold">Target</th>
                  <th className="text-left p-3 font-semibold">Variance</th>
                  <th className="text-left p-3 font-semibold">Trend</th>
                </tr>
              </thead>
              <tbody>
                <tr className="border-b border-gray-100">
                  <td className="p-3 font-medium">Total Revenue</td>
                  <td className="p-3">${kpis.totalRevenue.toLocaleString()}</td>
                  <td className="p-3">$950,000</td>
                  <td className="p-3 text-red-600">-7.2%</td>
                  <td className="p-3">📈 +15.3% YoY</td>
                </tr>
                <tr className="border-b border-gray-100">
                  <td className="p-3 font-medium">Facility Utilization</td>
                  <td className="p-3">{kpis.facilityUtilization}%</td>
                  <td className="p-3">85%</td>
                  <td className="p-3 text-red-600">-6%</td>
                  <td className="p-3">📈 +5.2% vs last month</td>
                </tr>
                <tr className="border-b border-gray-100">
                  <td className="p-3 font-medium">Sponsor Retention</td>
                  <td className="p-3">96%</td>
                  <td className="p-3">95%</td>
                  <td className="p-3 text-green-600">+1%</td>
                  <td className="p-3">📈 Industry leading</td>
                </tr>
                <tr className="border-b border-gray-100">
                  <td className="p-3 font-medium">Average Booking Value</td>
                  <td className="p-3">$88</td>
                  <td className="p-3">$95</td>
                  <td className="p-3 text-red-600">-7.4%</td>
                  <td className="p-3">📊 Stable</td>
                </tr>
                <tr className="border-b border-gray-100">
                  <td className="p-3 font-medium">Member Satisfaction</td>
                  <td className="p-3">{kpis.avgSatisfaction}/10</td>
                  <td className="p-3">9.0/10</td>
                  <td className="p-3 text-red-600">-0.3</td>
                  <td className="p-3">📈 +0.3 improvement</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {/* Strategic Recommendations */}
      <div className="bg-white p-6 rounded-xl shadow-lg">
        <h3 className="text-lg font-semibold mb-4">🎯 Strategic Recommendations</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div className="p-4 bg-blue-50 rounded-lg border-l-4 border-blue-500">
            <h4 className="font-semibold text-blue-800">Revenue Optimization</h4>
            <p className="text-sm text-blue-700 mt-2">Implement dynamic pricing during peak hours (12:00 PM) to increase facility revenue by estimated 12%</p>
            <div className="mt-2 text-xs text-blue-600 font-medium">Impact: +$36K annually</div>
          </div>
          <div className="p-4 bg-green-50 rounded-lg border-l-4 border-green-500">
            <h4 className="font-semibold text-green-800">Sponsor Engagement</h4>
            <p className="text-sm text-green-700 mt-2">Focus on Finance sector sponsors - highest engagement (99%) and retention potential</p>
            <div className="mt-2 text-xs text-green-600 font-medium">Impact: +$125K pipeline</div>
          </div>
          <div className="p-4 bg-purple-50 rounded-lg border-l-4 border-purple-500">
            <h4 className="font-semibold text-purple-800">Facility Expansion</h4>
            <p className="text-sm text-purple-700 mt-2">Tennis shows highest demand (88 bookings) - consider adding court capacity</p>
            <div className="mt-2 text-xs text-purple-600 font-medium">Impact: +$48K annually</div>
          </div>
          <div className="p-4 bg-orange-50 rounded-lg border-l-4 border-orange-500">
            <h4 className="font-semibold text-orange-800">Off-Peak Programming</h4>
            <p className="text-sm text-orange-700 mt-2">Facility 4 has 29% unused capacity - develop specialized programs</p>
            <div className="mt-2 text-xs text-orange-600 font-medium">Impact: +$22K annually</div>
          </div>
          <div className="p-4 bg-red-50 rounded-lg border-l-4 border-red-500">
            <h4 className="font-semibold text-red-800">Technology Integration</h4>
            <p className="text-sm text-red-700 mt-2">Implement IoT sensors for real-time usage tracking and automated billing</p>
            <div className="mt-2 text-xs text-red-600 font-medium">Impact: +15% efficiency</div>
          </div>
          <div className="p-4 bg-indigo-50 rounded-lg border-l-4 border-indigo-500">
            <h4 className="font-semibold text-indigo-800">Member Retention</h4>
            <p className="text-sm text-indigo-700 mt-2">Focus on Silver tier members for loyalty program expansion</p>
            <div className="mt-2 text-xs text-indigo-600 font-medium">Impact: +8% retention</div>
          </div>
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Navigation */}
      <nav className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center space-x-8">
              <div className="flex-shrink-0">
                <h1 className="text-xl font-bold text-gray-900">🏟️ SportAI Enterprise</h1>
              </div>
              <div className="flex space-x-4">
                {[
                  { id: 'dashboard', label: '🏠 Dashboard', icon: Activity },
                  { id: 'heatmap', label: '🔥 Heatmap', icon: MapPin },
                  { id: 'sponsorship', label: '🤝 Sponsors', icon: Users },
                  { id: 'analytics', label: '📊 Analytics', icon: TrendingUp }
                ].map((item) => (
                  <button
                    key={item.id}
                    onClick={() => setActiveModule(item.id)}
                    className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                      activeModule === item.id
                        ? 'bg-blue-100 text-blue-700'
                        : 'text-gray-500 hover:text-gray-700 hover:bg-gray-100'
                    }`}
                  >
                    {item.label}
                  </button>
                ))}
              </div>
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        {activeModule === 'dashboard' && renderDashboard()}
        {activeModule === 'heatmap' && renderHeatmap()}
        {activeModule === 'sponsorship' && renderSponsorship()}
        {activeModule === 'analytics' && renderAnalytics()}
      </main>
    </div>
  );
};

export default SportAIUnifiedDashboard;