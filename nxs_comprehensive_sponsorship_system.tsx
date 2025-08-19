import React, { useState, useEffect } from 'react';
import { BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, AreaChart, Area } from 'recharts';
import { 
  Calendar, DollarSign, TrendingUp, AlertTriangle, CheckCircle, Clock, Users, Target, MapPin, FileText, Bell, Activity, Star,
  Camera, Mail, Phone, MessageSquare, CreditCard, Upload, Download, Settings, Search, Filter, Eye, Edit, Trash2,
  BarChart3, TrendingDown, Award, Zap, Globe, Smartphone, Wifi, Database, Cloud, Lock,
  PlayCircle, PauseCircle, StopCircle, RotateCcw, RefreshCw, Maximize2, Minimize2, Share2, Link, Copy, QrCode,
  UserPlus, UserCheck, UserX, Building, Briefcase, CheckSquare,
  AlertCircle, Info, XCircle, ThumbsUp, ThumbsDown, Heart, MessageCircle, Send, Paperclip, Image, Video
} from 'lucide-react';

const NXSComprehensiveSponsorshipSystem = () => {
  // Enhanced state management
  const [currentModule, setCurrentModule] = useState('dashboard');
  const [currentTime, setCurrentTime] = useState(new Date());
  const [sponsorData, setSponsorData] = useState([]);
  const [fulfillmentTasks, setFulfillmentTasks] = useState([]);
  const [campaigns, setCampaigns] = useState([]);
  const [proposals, setProposals] = useState([]);
  const [events, setEvents] = useState([]);
  const [performanceMetrics, setPerformanceMetrics] = useState({});
  const [searchQuery, setSearchQuery] = useState('');

  // Initialize comprehensive data
  useEffect(() => {
    initializeComprehensiveData();
    const timer = setInterval(() => {
      setCurrentTime(new Date());
      updateRealTimeMetrics();
    }, 30000);
    return () => clearInterval(timer);
  }, []);

  const initializeComprehensiveData = () => {
    // Enhanced sponsor data
    setSponsorData([
      {
        id: 1,
        name: 'Wells Fargo Bank',
        tier: 'Diamond',
        value: 1750000,
        status: 'Active',
        renewal: '2024-12-31',
        contact: {
          primary: 'Sarah Johnson',
          email: 'sarah.johnson@wellsfargo.com',
          phone: '555-0123',
          title: 'Marketing Director'
        },
        fulfillment: {
          overall: 95,
          signage: 98,
          digital: 92,
          events: 97,
          hospitality: 94
        },
        performance: {
          exposureValue: 3200000,
          digitalImpressions: 2500000,
          leadGeneration: 340
        },
        financials: {
          totalPaid: 1312500,
          remaining: 437500,
          nextPayment: '2024-04-01'
        },
        satisfaction: {
          score: 9.2,
          feedback: 'Excellent partnership, exceeding expectations'
        }
      },
      {
        id: 2,
        name: 'HyVee',
        tier: 'Platinum',
        value: 625000,
        status: 'Active',
        renewal: '2024-09-30',
        contact: {
          primary: 'Mike Chen',
          email: 'mike.chen@hy-vee.com',
          phone: '555-0456',
          title: 'Community Relations Manager'
        },
        fulfillment: {
          overall: 88,
          signage: 85,
          digital: 90,
          events: 92,
          hospitality: 86
        },
        performance: {
          exposureValue: 1800000,
          digitalImpressions: 1200000,
          leadGeneration: 185
        },
        financials: {
          totalPaid: 468750,
          remaining: 156250,
          nextPayment: '2024-04-01'
        },
        satisfaction: {
          score: 8.7,
          feedback: 'Strong community connection, good ROI'
        }
      }
    ]);

    // Fulfillment tasks
    setFulfillmentTasks([
      {
        id: 1,
        sponsorName: 'Wells Fargo Bank',
        task: 'Install new championship court signage',
        category: 'Signage',
        status: 'In Progress',
        assignee: 'Mike Rodriguez',
        dueDate: '2024-03-15',
        priority: 'High',
        progress: 75
      },
      {
        id: 2,
        sponsorName: 'HyVee',
        task: 'Update dome exterior banner',
        category: 'Signage',
        status: 'Completed',
        assignee: 'Sarah Kim',
        dueDate: '2024-02-28',
        priority: 'Medium',
        progress: 100
      }
    ]);

    // Marketing campaigns
    setCampaigns([
      {
        id: 1,
        name: 'Spring Tournament Series',
        sponsorName: 'Wells Fargo Bank',
        type: 'Event Activation',
        status: 'Active',
        budget: 75000,
        spent: 45000,
        metrics: {
          impressions: 1250000,
          clicks: 8500,
          conversions: 340,
          engagement: 4.2
        }
      }
    ]);

    // Proposals
    setProposals([
      {
        id: 1,
        prospectName: 'First National Bank',
        proposedTier: 'Silver',
        proposedValue: 180000,
        status: 'Under Review',
        probability: 75,
        contact: {
          name: 'Robert Martinez',
          email: 'rmartinez@fnb.com'
        }
      }
    ]);

    // Events
    setEvents([
      {
        id: 1,
        title: 'Wells Fargo Youth Basketball Tournament',
        date: '2024-03-23',
        time: '09:00',
        location: 'Championship Court',
        expectedAttendance: 500,
        status: 'Confirmed'
      }
    ]);

    // Performance metrics
    setPerformanceMetrics({
      totalRevenue: 2375000,
      revenueGrowth: 12.5,
      sponsorRetention: 94.2,
      averageFulfillment: 91.5,
      customerSatisfaction: 8.95,
      newSponsorsThisYear: 2,
      pipelineValue: 180000
    });
  };

  const updateRealTimeMetrics = () => {
    setPerformanceMetrics(prev => ({
      ...prev,
      totalRevenue: prev.totalRevenue + Math.random() * 1000
    }));
  };

  const renderDashboard = () => (
    <div className="space-y-6">
      {/* Header */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 text-white p-6 rounded-lg">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div>
            <h2 className="text-2xl font-bold mb-2">NXS Sponsorship Command Center</h2>
            <p className="text-blue-100">Real-time performance monitoring</p>
            <div className="mt-4 text-sm">
              <div>Last updated: {currentTime.toLocaleTimeString()}</div>
              <div className="flex items-center mt-1">
                <div className="w-2 h-2 bg-green-400 rounded-full mr-2 animate-pulse"></div>
                System Status: Online
              </div>
            </div>
          </div>
          <div className="text-center">
            <div className="text-3xl font-bold">${((performanceMetrics.totalRevenue || 0) / 1000000).toFixed(2)}M</div>
            <div className="text-blue-100">Total Annual Revenue</div>
            <div className="text-sm mt-1">+{(performanceMetrics.revenueGrowth || 0).toFixed(1)}% YoY</div>
          </div>
          <div className="text-center">
            <div className="text-3xl font-bold">{(performanceMetrics.sponsorRetention || 0).toFixed(1)}%</div>
            <div className="text-blue-100">Retention Rate</div>
          </div>
        </div>
      </div>

      {/* KPIs */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-white p-6 rounded-lg shadow-lg border-l-4 border-green-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Active Sponsors</p>
              <p className="text-2xl font-bold text-gray-900">{sponsorData.length}</p>
              <p className="text-sm text-green-600">+{performanceMetrics.newSponsorsThisYear || 0} new this year</p>
            </div>
            <Users className="h-8 w-8 text-green-500" />
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-lg border-l-4 border-blue-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Avg Fulfillment</p>
              <p className="text-2xl font-bold text-gray-900">{performanceMetrics.averageFulfillment || 0}%</p>
              <p className="text-sm text-blue-600">Above target</p>
            </div>
            <Target className="h-8 w-8 text-blue-500" />
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-lg border-l-4 border-purple-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Satisfaction Score</p>
              <p className="text-2xl font-bold text-gray-900">{(performanceMetrics.customerSatisfaction || 0).toFixed(1)}</p>
              <p className="text-sm text-purple-600">Out of 10</p>
            </div>
            <Star className="h-8 w-8 text-purple-500" />
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-lg border-l-4 border-orange-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Pipeline Value</p>
              <p className="text-2xl font-bold text-gray-900">${((performanceMetrics.pipelineValue || 0) / 1000).toFixed(0)}K</p>
              <p className="text-sm text-orange-600">Potential revenue</p>
            </div>
            <TrendingUp className="h-8 w-8 text-orange-500" />
          </div>
        </div>
      </div>

      {/* Activity and Tasks */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h3 className="text-lg font-semibold mb-4 flex items-center">
            <Activity className="h-5 w-5 mr-2 text-green-500" />
            Live Activity Feed
          </h3>
          <div className="space-y-3">
            <div className="flex items-start space-x-3 p-3 bg-green-50 rounded-lg">
              <CheckCircle className="h-5 w-5 text-green-500 mt-0.5" />
              <div>
                <p className="text-sm font-medium">Signage installation completed</p>
                <p className="text-xs text-gray-500">HyVee dome banner - 2 minutes ago</p>
              </div>
            </div>
            <div className="flex items-start space-x-3 p-3 bg-blue-50 rounded-lg">
              <Mail className="h-5 w-5 text-blue-500 mt-0.5" />
              <div>
                <p className="text-sm font-medium">Renewal reminder sent</p>
                <p className="text-xs text-gray-500">Wells Fargo payment due - 15 minutes ago</p>
              </div>
            </div>
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h3 className="text-lg font-semibold mb-4">Upcoming Tasks</h3>
          <div className="space-y-3">
            {fulfillmentTasks.filter(task => task.status !== 'Completed').map(task => (
              <div key={task.id} className="flex items-center justify-between p-3 border rounded-lg">
                <div>
                  <p className="font-medium text-sm">{task.task}</p>
                  <p className="text-xs text-gray-500">{task.sponsorName} • Due: {task.dueDate}</p>
                </div>
                <div className={`px-2 py-1 rounded text-xs ${
                  task.priority === 'High' ? 'bg-red-100 text-red-800' :
                  task.priority === 'Medium' ? 'bg-yellow-100 text-yellow-800' :
                  'bg-green-100 text-green-800'
                }`}>
                  {task.priority}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );

  const renderSponsorManagement = () => (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold">Sponsor Management</h2>
        <div className="flex space-x-3">
          <div className="relative">
            <Search className="h-4 w-4 absolute left-3 top-3 text-gray-400" />
            <input
              type="text"
              placeholder="Search sponsors..."
              className="pl-10 pr-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>
          <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 flex items-center">
            <UserPlus className="h-4 w-4 mr-2" />
            Add Sponsor
          </button>
        </div>
      </div>

      <div className="grid gap-6">
        {sponsorData.map(sponsor => (
          <div key={sponsor.id} className="bg-white rounded-lg shadow-lg border border-gray-200">
            {/* Sponsor Header */}
            <div className="p-6 border-b border-gray-200">
              <div className="flex justify-between items-start">
                <div className="flex items-center space-x-4">
                  <div className={`w-4 h-16 rounded ${
                    sponsor.tier === 'Diamond' ? 'bg-gradient-to-b from-blue-400 to-blue-600' :
                    sponsor.tier === 'Platinum' ? 'bg-gradient-to-b from-gray-300 to-gray-500' :
                    sponsor.tier === 'Gold' ? 'bg-gradient-to-b from-yellow-400 to-yellow-600' :
                    'bg-gradient-to-b from-gray-200 to-gray-400'
                  }`}></div>
                  <div>
                    <h3 className="text-xl font-bold">{sponsor.name}</h3>
                    <p className="text-gray-600">{sponsor.tier} Tier • ${sponsor.value.toLocaleString()}</p>
                    <div className="flex items-center space-x-4 mt-2">
                      <span className={`px-2 py-1 rounded text-xs font-medium ${
                        sponsor.status === 'Active' ? 'bg-green-100 text-green-800' :
                        'bg-yellow-100 text-yellow-800'
                      }`}>
                        {sponsor.status}
                      </span>
                      <span className="text-sm text-gray-500">
                        Satisfaction: {sponsor.satisfaction?.score || 0}/10
                      </span>
                    </div>
                  </div>
                </div>
                <div className="text-right">
                  <p className="text-sm text-gray-500">Renewal</p>
                  <p className="font-medium">{new Date(sponsor.renewal).toLocaleDateString()}</p>
                  <p className="text-xs text-gray-500">
                    {Math.ceil((new Date(sponsor.renewal) - new Date()) / (1000 * 60 * 60 * 24))} days
                  </p>
                </div>
              </div>
            </div>

            {/* Performance Metrics */}
            <div className="p-6 border-b border-gray-200">
              <h4 className="font-semibold mb-3">Performance Metrics</h4>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div className="text-center">
                  <p className="text-sm text-gray-600">Fulfillment</p>
                  <p className="text-2xl font-bold text-blue-600">{sponsor.fulfillment?.overall || 0}%</p>
                </div>
                <div className="text-center">
                  <p className="text-sm text-gray-600">Exposure Value</p>
                  <p className="text-lg font-semibold">${((sponsor.performance?.exposureValue || 0) / 1000000).toFixed(1)}M</p>
                </div>
                <div className="text-center">
                  <p className="text-sm text-gray-600">Digital Impressions</p>
                  <p className="text-lg font-semibold">{((sponsor.performance?.digitalImpressions || 0) / 1000000).toFixed(1)}M</p>
                </div>
                <div className="text-center">
                  <p className="text-sm text-gray-600">ROI</p>
                  <p className="text-lg font-semibold text-green-600">
                    {(((sponsor.performance?.exposureValue || 0) / (sponsor.value || 1)) * 100).toFixed(0)}%
                  </p>
                </div>
              </div>
            </div>

            {/* Contact Info */}
            <div className="p-6 border-b border-gray-200">
              <h4 className="font-semibold mb-3">Contact Information</h4>
              <div>
                <p className="text-sm font-medium">Primary Contact</p>
                <p className="text-sm">{sponsor.contact?.primary || 'N/A'} - {sponsor.contact?.title || 'N/A'}</p>
                <div className="flex items-center space-x-4 mt-1">
                  <a href={`mailto:${sponsor.contact?.email || ''}`} className="text-blue-600 hover:text-blue-800 flex items-center">
                    <Mail className="h-4 w-4 mr-1" />
                    Email
                  </a>
                  <a href={`tel:${sponsor.contact?.phone || ''}`} className="text-blue-600 hover:text-blue-800 flex items-center">
                    <Phone className="h-4 w-4 mr-1" />
                    Call
                  </a>
                </div>
              </div>
            </div>

            {/* Actions */}
            <div className="p-6">
              <div className="flex flex-wrap gap-2">
                <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 flex items-center">
                  <Eye className="h-4 w-4 mr-2" />
                  View Details
                </button>
                <button className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 flex items-center">
                  <FileText className="h-4 w-4 mr-2" />
                  Generate Report
                </button>
                <button className="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 flex items-center">
                  <Calendar className="h-4 w-4 mr-2" />
                  Schedule Meeting
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  const renderAnalytics = () => (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold">Analytics Dashboard</h2>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h3 className="text-lg font-semibold mb-4">Revenue by Tier</h3>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={[
                  { name: 'Diamond', value: 1750000 },
                  { name: 'Platinum', value: 625000 }
                ]}
                cx="50%"
                cy="50%"
                outerRadius={100}
                dataKey="value"
                label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
              >
                <Cell fill="#2563eb" />
                <Cell fill="#6b7280" />
              </Pie>
              <Tooltip formatter={(value) => `$${value.toLocaleString()}`} />
            </PieChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h3 className="text-lg font-semibold mb-4">Performance Trends</h3>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={[
              { month: 'Jan', satisfaction: 8.5, fulfillment: 89 },
              { month: 'Feb', satisfaction: 8.7, fulfillment: 91 },
              { month: 'Mar', satisfaction: 8.9, fulfillment: 92 }
            ]}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="satisfaction" stroke="#2563eb" strokeWidth={2} name="Satisfaction" />
              <Line type="monotone" dataKey="fulfillment" stroke="#16a34a" strokeWidth={2} name="Fulfillment %" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Performance Table */}
      <div className="bg-white rounded-lg shadow-lg p-6">
        <h3 className="text-lg font-semibold mb-4">Sponsor Performance Matrix</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b">
                <th className="text-left p-2">Sponsor</th>
                <th className="text-left p-2">Tier</th>
                <th className="text-left p-2">Contract Value</th>
                <th className="text-left p-2">Fulfillment</th>
                <th className="text-left p-2">ROI</th>
              </tr>
            </thead>
            <tbody>
              {sponsorData.map(sponsor => (
                <tr key={sponsor.id} className="border-b hover:bg-gray-50">
                  <td className="p-2 font-medium">{sponsor.name}</td>
                  <td className="p-2">
                    <span className={`px-2 py-1 rounded text-xs ${
                      sponsor.tier === 'Diamond' ? 'bg-blue-100 text-blue-800' :
                      'bg-gray-100 text-gray-800'
                    }`}>
                      {sponsor.tier}
                    </span>
                  </td>
                  <td className="p-2">${(sponsor.value || 0).toLocaleString()}</td>
                  <td className="p-2">
                    <span className="px-2 py-1 rounded text-xs bg-green-100 text-green-800">
                      {sponsor.fulfillment?.overall || 0}%
                    </span>
                  </td>
                  <td className="p-2 font-semibold text-green-600">
                    {(((sponsor.performance?.exposureValue || 0) / (sponsor.value || 1)) * 100).toFixed(0)}%
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );

  // Navigation items
  const navigationItems = [
    { id: 'dashboard', label: 'Dashboard', icon: Activity },
    { id: 'sponsors', label: 'Sponsors', icon: Users },
    { id: 'analytics', label: 'Analytics', icon: BarChart3 }
  ];

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Navigation */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex space-x-1">
              {navigationItems.map(item => {
                const IconComponent = item.icon;
                return (
                  <button
                    key={item.id}
                    onClick={() => setCurrentModule(item.id)}
                    className={`px-3 py-2 rounded-md text-sm font-medium flex items-center ${
                      currentModule === item.id 
                        ? 'bg-blue-100 text-blue-700' 
                        : 'text-gray-500 hover:text-gray-700'
                    }`}
                  >
                    <IconComponent className="h-4 w-4 mr-2" />
                    {item.label}
                  </button>
                );
              })}
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
              <span className="text-sm text-gray-600">Live System</span>
              <span className="text-sm text-gray-400">|</span>
              <span className="text-sm text-gray-600">{currentTime.toLocaleTimeString()}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {currentModule === 'dashboard' && renderDashboard()}
        {currentModule === 'sponsors' && renderSponsorManagement()}
        {currentModule === 'analytics' && renderAnalytics()}
      </div>
    </div>
  );
};

export default NXSComprehensiveSponsorshipSystem;