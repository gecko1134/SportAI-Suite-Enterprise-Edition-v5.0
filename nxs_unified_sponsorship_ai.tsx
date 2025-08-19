import React, { useState, useEffect } from 'react';
import { BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { Calendar, DollarSign, TrendingUp, AlertTriangle, CheckCircle, Clock, Users, Target, MapPin, FileText, Bell, Activity, Star } from 'lucide-react';

const NXSUnifiedSponsorshipAI = () => {
  // State management for real-time data
  const [currentTime, setCurrentTime] = useState(new Date());
  const [selectedView, setSelectedView] = useState('dashboard');
  const [alerts, setAlerts] = useState([]);
  const [activeSponsors, setActiveSponsors] = useState([]);
  const [revenueData, setRevenueData] = useState([]);
  const [fulfillmentTracking, setFulfillmentTracking] = useState([]);

  // Update time every minute for real-time display
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTime(new Date());
      // Simulate real-time data updates
      updateRealTimeData();
    }, 60000);
    
    // Initialize data
    initializeData();
    
    return () => clearInterval(timer);
  }, []);

  const initializeData = () => {
    // Initialize sponsors based on NXS sponsorship books
    setActiveSponsors([
      {
        id: 1,
        name: 'Wells Fargo Bank',
        tier: 'Diamond',
        value: 1750000,
        status: 'Active',
        renewal: '2024-12-31',
        contact: 'Sarah Johnson',
        email: 'sarah.johnson@wellsfargo.com',
        phone: '555-0123',
        benefits: 'Full complex naming rights, dome & exterior signage, digital media, VIP suites',
        fulfillment: 95,
        exposureValue: 3200000,
        signageLocations: 15,
        digitalImpressions: 2500000,
        lastActivity: '2 days ago'
      },
      {
        id: 2,
        name: 'HyVee',
        tier: 'Platinum',
        value: 625000,
        status: 'Active',
        renewal: '2024-09-30',
        contact: 'Mike Chen',
        email: 'mike.chen@hy-vee.com',
        phone: '555-0456',
        benefits: 'Dome naming rights, premium interior/exterior signage, 4 corporate events/year',
        fulfillment: 88,
        exposureValue: 1800000,
        signageLocations: 8,
        digitalImpressions: 1200000,
        lastActivity: '1 week ago'
      },
      {
        id: 3,
        name: 'TD Ameritrade',
        tier: 'Gold',
        value: 320000,
        status: 'Active',
        renewal: '2024-06-30',
        contact: 'Jennifer Liu',
        email: 'j.liu@tdameritrade.com',
        phone: '555-0789',
        benefits: 'Outdoor field naming rights, light pole banners, scoreboard branding',
        fulfillment: 92,
        exposureValue: 950000,
        signageLocations: 6,
        digitalImpressions: 800000,
        lastActivity: '3 days ago'
      },
      {
        id: 4,
        name: 'Nebraska Medicine',
        tier: 'Silver',
        value: 150000,
        status: 'Pending Renewal',
        renewal: '2024-03-31',
        contact: 'Dr. Robert Kim',
        email: 'robert.kim@nebraskamed.com',
        phone: '555-0321',
        benefits: 'Indoor turf/court naming rights, scoreboard & event signage',
        fulfillment: 85,
        exposureValue: 420000,
        signageLocations: 4,
        digitalImpressions: 350000,
        lastActivity: '2 weeks ago'
      },
      {
        id: 5,
        name: 'Runza Restaurants',
        tier: 'Bronze',
        value: 50000,
        status: 'Active',
        renewal: '2024-08-15',
        contact: 'Lisa Martinez',
        email: 'lisa@runza.com',
        phone: '555-0654',
        benefits: 'Banners, small digital package, local event sponsorship',
        fulfillment: 78,
        exposureValue: 180000,
        signageLocations: 3,
        digitalImpressions: 120000,
        lastActivity: '5 days ago'
      }
    ]);

    // Initialize revenue data
    setRevenueData([
      { month: 'Jan', actual: 245000, projected: 230000, lastYear: 210000 },
      { month: 'Feb', actual: 268000, projected: 250000, lastYear: 235000 },
      { month: 'Mar', actual: 295000, projected: 275000, lastYear: 258000 },
      { month: 'Apr', actual: 312000, projected: 290000, lastYear: 275000 },
      { month: 'May', actual: 328000, projected: 310000, lastYear: 290000 },
      { month: 'Jun', actual: 345000, projected: 325000, lastYear: 305000 }
    ]);

    // Initialize fulfillment tracking
    setFulfillmentTracking([
      { category: 'Signage Installation', completed: 42, total: 45, percentage: 93 },
      { category: 'Digital Advertising', completed: 38, total: 40, percentage: 95 },
      { category: 'Event Activations', completed: 15, total: 20, percentage: 75 },
      { category: 'PR & Media', completed: 28, total: 30, percentage: 93 },
      { category: 'Corporate Events', completed: 8, total: 12, percentage: 67 }
    ]);

    // Initialize alerts
    setAlerts([
      {
        id: 1,
        type: 'urgent',
        title: 'Contract Renewal Alert',
        message: 'Nebraska Medicine contract expires in 45 days - schedule renewal meeting',
        timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000)
      },
      {
        id: 2,
        type: 'info',
        title: 'Fulfillment Milestone',
        message: 'TD Ameritrade signage installation completed ahead of schedule',
        timestamp: new Date(Date.now() - 4 * 60 * 60 * 1000)
      },
      {
        id: 3,
        type: 'opportunity',
        title: 'Revenue Opportunity',
        message: 'Highway 35 visibility package available - potential $15K/month additional revenue',
        timestamp: new Date(Date.now() - 6 * 60 * 60 * 1000)
      }
    ]);
  };

  const updateRealTimeData = () => {
    // Simulate real-time updates
    const variance = () => (Math.random() - 0.5) * 0.1;
    
    setActiveSponsors(prev => prev.map(sponsor => ({
      ...sponsor,
      fulfillment: Math.min(100, Math.max(0, sponsor.fulfillment + variance() * 5)),
      digitalImpressions: Math.floor(sponsor.digitalImpressions * (1 + variance() * 0.2))
    })));
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'Active': return 'text-green-600';
      case 'Pending Renewal': return 'text-yellow-600';
      case 'Expired': return 'text-red-600';
      default: return 'text-gray-600';
    }
  };

  const getTierColor = (tier) => {
    switch (tier) {
      case 'Diamond': return 'bg-gradient-to-r from-blue-600 to-purple-600';
      case 'Platinum': return 'bg-gradient-to-r from-gray-400 to-gray-600';
      case 'Gold': return 'bg-gradient-to-r from-yellow-400 to-yellow-600';
      case 'Silver': return 'bg-gradient-to-r from-gray-300 to-gray-500';
      case 'Bronze': return 'bg-gradient-to-r from-orange-400 to-orange-600';
      default: return 'bg-gray-500';
    }
  };

  const formatCurrency = (amount) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0
    }).format(amount);
  };

  const getDaysUntilRenewal = (renewalDate) => {
    const today = new Date();
    const renewal = new Date(renewalDate);
    const timeDiff = renewal.getTime() - today.getTime();
    return Math.ceil(timeDiff / (1000 * 3600 * 24));
  };

  const totalRevenue = activeSponsors.reduce((sum, sponsor) => sum + sponsor.value, 0);
  const avgFulfillment = activeSponsors.reduce((sum, sponsor) => sum + sponsor.fulfillment, 0) / activeSponsors.length;

  const renderDashboard = () => (
    <div className="space-y-6">
      {/* Real-time Header */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 text-white p-6 rounded-lg">
        <div className="flex justify-between items-center">
          <div>
            <h1 className="text-3xl font-bold">NXS Sponsorship Command Center</h1>
            <p className="text-blue-100">Real-time tracking and AI optimization</p>
          </div>
          <div className="text-right">
            <div className="text-2xl font-mono">{currentTime.toLocaleTimeString()}</div>
            <div className="text-sm text-blue-100">{currentTime.toLocaleDateString()}</div>
          </div>
        </div>
      </div>

      {/* Key Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-lg border-l-4 border-green-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Total Revenue</p>
              <p className="text-2xl font-bold text-gray-900">{formatCurrency(totalRevenue)}</p>
              <p className="text-sm text-green-600">+12.5% vs last year</p>
            </div>
            <DollarSign className="h-8 w-8 text-green-500" />
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-lg border-l-4 border-blue-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Active Sponsors</p>
              <p className="text-2xl font-bold text-gray-900">{activeSponsors.length}</p>
              <p className="text-sm text-blue-600">98% retention rate</p>
            </div>
            <Users className="h-8 w-8 text-blue-500" />
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-lg border-l-4 border-purple-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Avg Fulfillment</p>
              <p className="text-2xl font-bold text-gray-900">{avgFulfillment.toFixed(1)}%</p>
              <p className="text-sm text-purple-600">Above 90% target</p>
            </div>
            <Target className="h-8 w-8 text-purple-500" />
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-lg border-l-4 border-orange-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Urgent Renewals</p>
              <p className="text-2xl font-bold text-gray-900">2</p>
              <p className="text-sm text-orange-600">Next 60 days</p>
            </div>
            <Clock className="h-8 w-8 text-orange-500" />
          </div>
        </div>
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h3 className="text-lg font-semibold mb-4">Revenue Tracking</h3>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={revenueData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip formatter={(value) => formatCurrency(value)} />
              <Legend />
              <Line type="monotone" dataKey="actual" stroke="#2563eb" strokeWidth={3} name="Actual" />
              <Line type="monotone" dataKey="projected" stroke="#9333ea" strokeWidth={2} name="Projected" />
              <Line type="monotone" dataKey="lastYear" stroke="#6b7280" strokeWidth={2} name="Last Year" />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h3 className="text-lg font-semibold mb-4">Fulfillment Status</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={fulfillmentTracking}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="category" angle={-45} textAnchor="end" height={100} />
              <YAxis />
              <Tooltip />
              <Bar dataKey="percentage" fill="#8884d8" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Alerts */}
      <div className="bg-white rounded-lg shadow-lg p-6">
        <h3 className="text-lg font-semibold mb-4 flex items-center">
          <Bell className="h-5 w-5 mr-2" />
          Real-time Alerts
        </h3>
        <div className="space-y-3">
          {alerts.map(alert => (
            <div key={alert.id} className={`p-4 rounded-lg border-l-4 ${
              alert.type === 'urgent' ? 'border-red-500 bg-red-50' :
              alert.type === 'info' ? 'border-blue-500 bg-blue-50' :
              'border-green-500 bg-green-50'
            }`}>
              <div className="flex justify-between items-start">
                <div>
                  <h4 className="font-medium">{alert.title}</h4>
                  <p className="text-sm text-gray-600">{alert.message}</p>
                </div>
                <span className="text-xs text-gray-500">
                  {alert.timestamp.toLocaleTimeString()}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );

  const renderSponsors = () => (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold">Active Sponsors</h2>
        <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
          Add New Sponsor
        </button>
      </div>

      <div className="grid gap-6">
        {activeSponsors.map(sponsor => (
          <div key={sponsor.id} className="bg-white rounded-lg shadow-lg p-6">
            <div className="flex justify-between items-start mb-4">
              <div className="flex items-center space-x-4">
                <div className={`w-4 h-12 rounded ${getTierColor(sponsor.tier)}`}></div>
                <div>
                  <h3 className="text-xl font-bold">{sponsor.name}</h3>
                  <p className="text-gray-600">{sponsor.tier} Tier • {formatCurrency(sponsor.value)}</p>
                </div>
              </div>
              <div className="text-right">
                <span className={`font-medium ${getStatusColor(sponsor.status)}`}>
                  {sponsor.status}
                </span>
                <p className="text-sm text-gray-500">
                  Renewal: {getDaysUntilRenewal(sponsor.renewal)} days
                </p>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-4">
              <div>
                <p className="text-sm text-gray-600">Fulfillment</p>
                <div className="flex items-center">
                  <div className="flex-1 bg-gray-200 rounded-full h-2 mr-2">
                    <div 
                      className="bg-green-500 h-2 rounded-full"
                      style={{ width: `${sponsor.fulfillment}%` }}
                    ></div>
                  </div>
                  <span className="text-sm font-medium">{sponsor.fulfillment.toFixed(1)}%</span>
                </div>
              </div>

              <div>
                <p className="text-sm text-gray-600">Exposure Value</p>
                <p className="font-semibold">{formatCurrency(sponsor.exposureValue)}</p>
              </div>

              <div>
                <p className="text-sm text-gray-600">Digital Impressions</p>
                <p className="font-semibold">{sponsor.digitalImpressions.toLocaleString()}</p>
              </div>

              <div>
                <p className="text-sm text-gray-600">Signage Locations</p>
                <p className="font-semibold">{sponsor.signageLocations} active</p>
              </div>
            </div>

            <div className="border-t pt-4">
              <p className="text-sm text-gray-600 mb-2">Benefits Package:</p>
              <p className="text-sm">{sponsor.benefits}</p>
              <div className="flex justify-between items-center mt-3">
                <p className="text-xs text-gray-500">Last activity: {sponsor.lastActivity}</p>
                <div className="space-x-2">
                  <button className="bg-blue-600 text-white px-3 py-1 rounded text-sm hover:bg-blue-700">
                    View Details
                  </button>
                  <button className="bg-gray-600 text-white px-3 py-1 rounded text-sm hover:bg-gray-700">
                    Contact
                  </button>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  const renderAnalytics = () => (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold">Advanced Analytics</h2>
      
      {/* Performance Metrics */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h3 className="text-lg font-semibold mb-4">ROI by Tier</h3>
          <ResponsiveContainer width="100%" height={200}>
            <PieChart>
              <Pie
                data={[
                  { name: 'Diamond', value: 1750000, color: '#2563eb' },
                  { name: 'Platinum', value: 625000, color: '#6b7280' },
                  { name: 'Gold', value: 320000, color: '#eab308' },
                  { name: 'Silver', value: 150000, color: '#9ca3af' },
                  { name: 'Bronze', value: 50000, color: '#ea580c' }
                ]}
                cx="50%"
                cy="50%"
                outerRadius={80}
                dataKey="value"
                label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
              >
                {[
                  { name: 'Diamond', value: 1750000, color: '#2563eb' },
                  { name: 'Platinum', value: 625000, color: '#6b7280' },
                  { name: 'Gold', value: 320000, color: '#eab308' },
                  { name: 'Silver', value: 150000, color: '#9ca3af' },
                  { name: 'Bronze', value: 50000, color: '#ea580c' }
                ].map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Pie>
              <Tooltip formatter={(value) => formatCurrency(value)} />
            </PieChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h3 className="text-lg font-semibold mb-4">Renewal Pipeline</h3>
          <div className="space-y-3">
            {activeSponsors
              .sort((a, b) => new Date(a.renewal) - new Date(b.renewal))
              .slice(0, 5)
              .map(sponsor => {
                const days = getDaysUntilRenewal(sponsor.renewal);
                return (
                  <div key={sponsor.id} className="flex justify-between items-center p-2 bg-gray-50 rounded">
                    <span className="font-medium text-sm">{sponsor.name}</span>
                    <span className={`text-sm ${days < 30 ? 'text-red-600' : days < 60 ? 'text-yellow-600' : 'text-green-600'}`}>
                      {days} days
                    </span>
                  </div>
                );
              })}
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h3 className="text-lg font-semibold mb-4">AI Insights</h3>
          <div className="space-y-3">
            <div className="p-3 bg-blue-50 rounded border-l-4 border-blue-500">
              <p className="text-sm font-medium">Revenue Opportunity</p>
              <p className="text-xs text-gray-600">Upsell Runza to Silver tier could add $100K annual</p>
            </div>
            <div className="p-3 bg-green-50 rounded border-l-4 border-green-500">
              <p className="text-sm font-medium">Retention Alert</p>
              <p className="text-xs text-gray-600">Wells Fargo showing high engagement - renewal likely</p>
            </div>
            <div className="p-3 bg-yellow-50 rounded border-l-4 border-yellow-500">
              <p className="text-sm font-medium">Risk Assessment</p>
              <p className="text-xs text-gray-600">Nebraska Medicine activity down 40% - intervention needed</p>
            </div>
          </div>
        </div>
      </div>

      {/* Detailed Performance Table */}
      <div className="bg-white rounded-lg shadow-lg p-6">
        <h3 className="text-lg font-semibold mb-4">Sponsor Performance Matrix</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b">
                <th className="text-left p-2">Sponsor</th>
                <th className="text-left p-2">Value</th>
                <th className="text-left p-2">Fulfillment</th>
                <th className="text-left p-2">Exposure</th>
                <th className="text-left p-2">ROI</th>
                <th className="text-left p-2">Risk Score</th>
              </tr>
            </thead>
            <tbody>
              {activeSponsors.map(sponsor => {
                const roi = (sponsor.exposureValue / sponsor.value * 100).toFixed(0);
                const riskScore = getDaysUntilRenewal(sponsor.renewal) < 60 ? 'High' : 
                                sponsor.fulfillment < 80 ? 'Medium' : 'Low';
                return (
                  <tr key={sponsor.id} className="border-b hover:bg-gray-50">
                    <td className="p-2 font-medium">{sponsor.name}</td>
                    <td className="p-2">{formatCurrency(sponsor.value)}</td>
                    <td className="p-2">
                      <span className={`px-2 py-1 rounded text-xs ${
                        sponsor.fulfillment >= 90 ? 'bg-green-100 text-green-800' :
                        sponsor.fulfillment >= 80 ? 'bg-yellow-100 text-yellow-800' :
                        'bg-red-100 text-red-800'
                      }`}>
                        {sponsor.fulfillment.toFixed(1)}%
                      </span>
                    </td>
                    <td className="p-2">{formatCurrency(sponsor.exposureValue)}</td>
                    <td className="p-2 font-semibold text-green-600">{roi}%</td>
                    <td className="p-2">
                      <span className={`px-2 py-1 rounded text-xs ${
                        riskScore === 'Low' ? 'bg-green-100 text-green-800' :
                        riskScore === 'Medium' ? 'bg-yellow-100 text-yellow-800' :
                        'bg-red-100 text-red-800'
                      }`}>
                        {riskScore}
                      </span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Navigation */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex space-x-8">
              <button
                onClick={() => setSelectedView('dashboard')}
                className={`px-3 py-2 rounded-md text-sm font-medium ${
                  selectedView === 'dashboard' 
                    ? 'bg-blue-100 text-blue-700' 
                    : 'text-gray-500 hover:text-gray-700'
                }`}
              >
                Dashboard
              </button>
              <button
                onClick={() => setSelectedView('sponsors')}
                className={`px-3 py-2 rounded-md text-sm font-medium ${
                  selectedView === 'sponsors' 
                    ? 'bg-blue-100 text-blue-700' 
                    : 'text-gray-500 hover:text-gray-700'
                }`}
              >
                Sponsors
              </button>
              <button
                onClick={() => setSelectedView('analytics')}
                className={`px-3 py-2 rounded-md text-sm font-medium ${
                  selectedView === 'analytics' 
                    ? 'bg-blue-100 text-blue-700' 
                    : 'text-gray-500 hover:text-gray-700'
                }`}
              >
                Analytics
              </button>
            </div>
            <div className="flex items-center space-x-2">
              <Activity className="h-4 w-4 text-green-500" />
              <span className="text-sm text-gray-600">Live</span>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {selectedView === 'dashboard' && renderDashboard()}
        {selectedView === 'sponsors' && renderSponsors()}
        {selectedView === 'analytics' && renderAnalytics()}
      </div>
    </div>
  );
};

export default NXSUnifiedSponsorshipAI;