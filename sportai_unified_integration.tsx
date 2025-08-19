import React, { useState, useEffect } from 'react';
import { BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, AreaChart, Area } from 'recharts';
import { 
  Calendar, DollarSign, TrendingUp, AlertTriangle, CheckCircle, Clock, Users, Target, MapPin, FileText, Bell, Activity, Star,
  Camera, Mail, Phone, MessageSquare, CreditCard, Upload, Download, Settings, Search, Filter, Eye, Edit, Trash2,
  BarChart3, TrendingDown, Award, Zap, Globe, Smartphone, Wifi, Database, Cloud, Lock,
  PlayCircle, PauseCircle, StopCircle, RotateCcw, RefreshCw, Maximize2, Minimize2, Share2, Link, Copy, QrCode,
  UserPlus, UserCheck, UserX, Building, Briefcase, CheckSquare, Home, Menu, X,
  AlertCircle, Info, XCircle, ThumbsUp, ThumbsDown, Heart, MessageCircle, Send, Paperclip, Image, Video
} from 'lucide-react';

const SportAIUnifiedSystem = () => {
  const [currentModule, setCurrentModule] = useState('dashboard');
  const [currentTime, setCurrentTime] = useState(new Date());
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [sponsorData, setSponsorData] = useState([]);
  const [heatmapData, setHeatmapData] = useState([]);
  const [performanceMetrics, setPerformanceMetrics] = useState({});
  const [searchQuery, setSearchQuery] = useState('');

  // Initialize all data
  useEffect(() => {
    initializeUnifiedData();
    const timer = setInterval(() => {
      setCurrentTime(new Date());
      updateRealTimeData();
    }, 30000);
    return () => clearInterval(timer);
  }, []);

  const initializeUnifiedData = () => {
    // Sponsor data
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
        fulfillment: { overall: 95, signage: 98, digital: 92, events: 97 },
        performance: { exposureValue: 3200000, digitalImpressions: 2500000, leadGeneration: 340 },
        satisfaction: { score: 9.2 }
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
        fulfillment: { overall: 88, signage: 85, digital: 90, events: 92 },
        performance: { exposureValue: 1800000, digitalImpressions: 1200000, leadGeneration: 185 },
        satisfaction: { score: 8.7 }
      },
      {
        id: 3,
        name: 'TD Ameritrade',
        tier: 'Gold',
        value: 320000,
        status: 'Active',
        renewal: '2024-06-30',
        contact: {
          primary: 'Jennifer Liu',
          email: 'j.liu@tdameritrade.com',
          phone: '555-0789',
          title: 'Sponsorship Manager'
        },
        fulfillment: { overall: 92, signage: 95, digital: 88, events: 94 },
        performance: { exposureValue: 950000, digitalImpressions: 800000, leadGeneration: 95 },
        satisfaction: { score: 8.9 }
      }
    ]);

    // Heatmap data for facility usage
    const facilities = [
      'Main Dome', 'Basketball Court 1', 'Basketball Court 2', 'Basketball Court 3', 'Basketball Court 4',
      'Outdoor Field A', 'Outdoor Field B', 'Outdoor Field C', 'Outdoor Field D',
      'Walking Track', 'Wellness Center', 'Esports Arena'
    ];
    
    const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
    const hours = Array.from({length: 16}, (_, i) => i + 6); // 6 AM to 10 PM
    
    const heatmapEntries = [];
    days.forEach((day, dayIndex) => {
      hours.forEach(hour => {
        facilities.forEach(facility => {
          // Generate realistic usage patterns
          let baseUsage = 30;
          
          // Peak times
          if ((hour >= 17 && hour <= 21) || (hour >= 7 && hour <= 9)) {
            baseUsage += 40;
          }
          
          // Weekend boost
          if (dayIndex >= 5) {
            baseUsage += 20;
          }
          
          // Facility-specific patterns
          if (facility.includes('Basketball')) {
            baseUsage += (hour >= 18 && hour <= 21) ? 30 : 0;
          } else if (facility.includes('Field')) {
            baseUsage += (hour >= 16 && hour <= 20) ? 25 : 0;
          }
          
          const usage = Math.min(100, Math.max(10, baseUsage + (Math.random() - 0.5) * 30));
          const revenue = usage * (Math.random() * 50 + 25);
          
          heatmapEntries.push({
            day,
            dayIndex,
            hour,
            facility,
            usage: Math.round(usage),
            revenue: Math.round(revenue),
            isPrimetime: (hour >= 17 && hour <= 21) || (hour >= 7 && hour <= 9),
            isWeekend: dayIndex >= 5
          });
        });
      });
    });
    
    setHeatmapData(heatmapEntries);

    // Performance metrics
    setPerformanceMetrics({
      totalRevenue: 2695000,
      revenueGrowth: 15.3,
      sponsorRetention: 96.8,
      averageFulfillment: 91.7,
      customerSatisfaction: 8.93,
      facilityUtilization: 78.4,
      newSponsorsThisYear: 3,
      pipelineValue: 450000
    });
  };

  const updateRealTimeData = () => {
    // Simulate real-time updates
    setPerformanceMetrics(prev => ({
      ...prev,
      totalRevenue: prev.totalRevenue + Math.random() * 2000,
      facilityUtilization: Math.max(65, Math.min(95, prev.facilityUtilization + (Math.random() - 0.5) * 2))
    }));
  };

  // Main Dashboard
  const renderMainDashboard = () => (
    <div className="space-y-6">
      {/* Header */}
      <div className="bg-gradient-to-r from-blue-600 via-purple-600 to-green-600 text-white p-6 rounded-xl shadow-2xl">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div>
            <h1 className="text-3xl font-bold mb-2">🏟️ SportAI Enterprise Suite™</h1>
            <p className="text-blue-100">Unified Sports Facility Management Platform</p>
            <div className="mt-4 text-sm">
              <div>Real-time updates: {currentTime.toLocaleTimeString()}</div>
              <div className="flex items-center mt-1">
                <div className="w-2 h-2 bg-green-400 rounded-full mr-2 animate-pulse"></div>
                All Systems Operational
              </div>
            </div>
          </div>
          <div className="text-center">
            <div className="text-4xl font-bold">${((performanceMetrics.totalRevenue || 0) / 1000000).toFixed(2)}M</div>
            <div className="text-blue-100">Total Revenue</div>
            <div className="text-sm mt-1">+{(performanceMetrics.revenueGrowth || 0).toFixed(1)}% YoY Growth</div>
          </div>
          <div className="text-center">
            <div className="text-4xl font-bold">{(performanceMetrics.facilityUtilization || 0).toFixed(1)}%</div>
            <div className="text-blue-100">Facility Utilization</div>
            <div className="text-sm mt-1">AI Optimized</div>
          </div>
        </div>
      </div>

      {/* Unified KPIs */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-lg border-l-4 border-green-500 hover:shadow-xl transition-shadow">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Active Sponsors</p>
              <p className="text-3xl font-bold text-gray-900">{sponsorData.length}</p>
              <p className="text-sm text-green-600">+{performanceMetrics.newSponsorsThisYear || 0} new</p>
            </div>
            <Users className="h-10 w-10 text-green-500" />
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-lg border-l-4 border-blue-500 hover:shadow-xl transition-shadow">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Retention Rate</p>
              <p className="text-3xl font-bold text-gray-900">{(performanceMetrics.sponsorRetention || 0).toFixed(1)}%</p>
              <p className="text-sm text-blue-600">Industry leading</p>
            </div>
            <Target className="h-10 w-10 text-blue-500" />
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-lg border-l-4 border-purple-500 hover:shadow-xl transition-shadow">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Satisfaction</p>
              <p className="text-3xl font-bold text-gray-900">{(performanceMetrics.customerSatisfaction || 0).toFixed(1)}</p>
              <p className="text-sm text-purple-600">Out of 10</p>
            </div>
            <Star className="h-10 w-10 text-purple-500" />
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-lg border-l-4 border-orange-500 hover:shadow-xl transition-shadow">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Pipeline Value</p>
              <p className="text-3xl font-bold text-gray-900">${((performanceMetrics.pipelineValue || 0) / 1000).toFixed(0)}K</p>
              <p className="text-sm text-orange-600">Growth potential</p>
            </div>
            <TrendingUp className="h-10 w-10 text-orange-500" />
          </div>
        </div>
      </div>

      {/* Quick Access Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          className="bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-all cursor-pointer border-2 border-transparent hover:border-blue-500"
          onClick={() => setCurrentModule('sponsorship')}
        >
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-lg font-semibold text-gray-900">🤝 Sponsorship Center</h3>
              <p className="text-gray-600">Manage sponsors, contracts & fulfillment</p>
              <div className="mt-2">
                <span className="text-2xl font-bold text-green-600">${((sponsorData.reduce((sum, s) => sum + (s.value || 0), 0)) / 1000000).toFixed(1)}M</span>
                <span className="text-sm text-gray-500 ml-2">Total Value</span>
              </div>
            </div>
            <Users className="h-12 w-12 text-blue-500" />
          </div>
        </div>

        <div 
          className="bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-all cursor-pointer border-2 border-transparent hover:border-purple-500"
          onClick={() => setCurrentModule('heatmap')}
        >
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-lg font-semibold text-gray-900">🔥 Usage Heatmap</h3>
              <p className="text-gray-600">Real-time facility utilization</p>
              <div className="mt-2">
                <span className="text-2xl font-bold text-purple-600">{(performanceMetrics.facilityUtilization || 0).toFixed(1)}%</span>
                <span className="text-sm text-gray-500 ml-2">Current Usage</span>
              </div>
            </div>
            <BarChart3 className="h-12 w-12 text-purple-500" />
          </div>
        </div>

        <div 
          className="bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-all cursor-pointer border-2 border-transparent hover:border-green-500"
          onClick={() => setCurrentModule('analytics')}
        >
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-lg font-semibold text-gray-900">📊 Analytics Hub</h3>
              <p className="text-gray-600">Performance insights & reports</p>
              <div className="mt-2">
                <span className="text-2xl font-bold text-green-600">{(performanceMetrics.averageFulfillment || 0).toFixed(1)}%</span>
                <span className="text-sm text-gray-500 ml-2">Avg Performance</span>
              </div>
            </div>
            <Activity className="h-12 w-12 text-green-500" />
          </div>
        </div>
      </div>

      {/* Real-time Activity Feed */}
      <div className="bg-white p-6 rounded-xl shadow-lg">
        <h3 className="text-lg font-semibold mb-4 flex items-center">
          <Activity className="h-5 w-5 mr-2 text-green-500" />
          Live System Activity
        </h3>
        <div className="space-y-3">
          <div className="flex items-start space-x-3 p-3 bg-green-50 rounded-lg">
            <CheckCircle className="h-5 w-5 text-green-500 mt-0.5" />
            <div>
              <p className="text-sm font-medium">Wells Fargo sponsorship fulfillment updated</p>
              <p className="text-xs text-gray-500">Championship Court signage installed - 3 minutes ago</p>
            </div>
          </div>
          <div className="flex items-start space-x-3 p-3 bg-blue-50 rounded-lg">
            <BarChart3 className="h-5 w-5 text-blue-500 mt-0.5" />
            <div>
              <p className="text-sm font-medium">Facility utilization spike detected</p>
              <p className="text-xs text-gray-500">Main Dome at 94% capacity - 8 minutes ago</p>
            </div>
          </div>
          <div className="flex items-start space-x-3 p-3 bg-purple-50 rounded-lg">
            <Mail className="h-5 w-5 text-purple-500 mt-0.5" />
            <div>
              <p className="text-sm font-medium">Automated renewal reminder sent</p>
              <p className="text-xs text-gray-500">TD Ameritrade contract expires in 90 days - 12 minutes ago</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  // Sponsorship Management Module
  const renderSponsorshipCenter = () => (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-3xl font-bold text-gray-900">🤝 NXS Sponsorship Command Center</h2>
          <p className="text-gray-600 mt-1">Comprehensive sponsor relationship management</p>
        </div>
        <div className="flex space-x-3">
          <div className="relative">
            <Search className="h-4 w-4 absolute left-3 top-3 text-gray-400" />
            <input
              type="text"
              placeholder="Search sponsors..."
              className="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>
          <button className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 flex items-center shadow-lg">
            <UserPlus className="h-4 w-4 mr-2" />
            Add Sponsor
          </button>
        </div>
      </div>

      {/* Sponsorship Overview Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-gradient-to-br from-blue-500 to-blue-600 text-white p-6 rounded-xl">
          <h3 className="text-lg font-semibold">Total Portfolio</h3>
          <p className="text-3xl font-bold mt-2">${((sponsorData.reduce((sum, s) => sum + (s.value || 0), 0)) / 1000000).toFixed(2)}M</p>
          <p className="text-blue-100 text-sm">Annual contract value</p>
        </div>
        <div className="bg-gradient-to-br from-green-500 to-green-600 text-white p-6 rounded-xl">
          <h3 className="text-lg font-semibold">Active Sponsors</h3>
          <p className="text-3xl font-bold mt-2">{sponsorData.filter(s => s.status === 'Active').length}</p>
          <p className="text-green-100 text-sm">Currently engaged</p>
        </div>
        <div className="bg-gradient-to-br from-purple-500 to-purple-600 text-white p-6 rounded-xl">
          <h3 className="text-lg font-semibold">Avg Fulfillment</h3>
          <p className="text-3xl font-bold mt-2">{(sponsorData.reduce((sum, s) => sum + (s.fulfillment?.overall || 0), 0) / sponsorData.length).toFixed(1)}%</p>
          <p className="text-purple-100 text-sm">Above target</p>
        </div>
        <div className="bg-gradient-to-br from-orange-500 to-orange-600 text-white p-6 rounded-xl">
          <h3 className="text-lg font-semibold">Satisfaction</h3>
          <p className="text-3xl font-bold mt-2">{(sponsorData.reduce((sum, s) => sum + (s.satisfaction?.score || 0), 0) / sponsorData.length).toFixed(1)}</p>
          <p className="text-orange-100 text-sm">Out of 10</p>
        </div>
      </div>

      {/* Sponsor Cards */}
      <div className="grid gap-6">
        {sponsorData.map(sponsor => (
          <div key={sponsor.id} className="bg-white rounded-xl shadow-lg border border-gray-200 hover:shadow-xl transition-shadow">
            <div className="p-6 border-b border-gray-200">
              <div className="flex justify-between items-start">
                <div className="flex items-center space-x-4">
                  <div className={`w-6 h-20 rounded-full ${
                    sponsor.tier === 'Diamond' ? 'bg-gradient-to-b from-blue-400 to-blue-600' :
                    sponsor.tier === 'Platinum' ? 'bg-gradient-to-b from-gray-300 to-gray-500' :
                    sponsor.tier === 'Gold' ? 'bg-gradient-to-b from-yellow-400 to-yellow-600' :
                    'bg-gradient-to-b from-orange-400 to-orange-600'
                  }`}></div>
                  <div>
                    <h3 className="text-2xl font-bold text-gray-900">{sponsor.name}</h3>
                    <p className="text-gray-600 text-lg">{sponsor.tier} Tier • ${(sponsor.value || 0).toLocaleString()}</p>
                    <div className="flex items-center space-x-4 mt-3">
                      <span className={`px-3 py-1 rounded-full text-sm font-medium ${
                        sponsor.status === 'Active' ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'
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
                  <p className="text-sm text-gray-500">Contract Renewal</p>
                  <p className="font-semibold text-lg">{new Date(sponsor.renewal).toLocaleDateString()}</p>
                  <p className="text-sm text-gray-500">
                    {Math.ceil((new Date(sponsor.renewal) - new Date()) / (1000 * 60 * 60 * 24))} days remaining
                  </p>
                </div>
              </div>
            </div>

            <div className="p-6">
              <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
                <div className="text-center">
                  <p className="text-sm text-gray-600">Overall Fulfillment</p>
                  <div className="mt-2">
                    <div className="relative w-16 h-16 mx-auto">
                      <svg className="w-16 h-16 transform -rotate-90" viewBox="0 0 36 36">
                        <path
                          d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                          fill="none"
                          stroke="#e5e7eb"
                          strokeWidth="3"
                        />
                        <path
                          d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                          fill="none"
                          stroke="#3b82f6"
                          strokeWidth="3"
                          strokeDasharray={`${sponsor.fulfillment?.overall || 0}, 100`}
                        />
                      </svg>
                      <div className="absolute inset-0 flex items-center justify-center">
                        <span className="text-sm font-bold">{sponsor.fulfillment?.overall || 0}%</span>
                      </div>
                    </div>
                  </div>
                </div>
                <div className="text-center">
                  <p className="text-sm text-gray-600">Exposure Value</p>
                  <p className="text-xl font-bold text-green-600">${((sponsor.performance?.exposureValue || 0) / 1000000).toFixed(1)}M</p>
                </div>
                <div className="text-center">
                  <p className="text-sm text-gray-600">Digital Reach</p>
                  <p className="text-xl font-bold text-blue-600">{((sponsor.performance?.digitalImpressions || 0) / 1000000).toFixed(1)}M</p>
                </div>
                <div className="text-center">
                  <p className="text-sm text-gray-600">ROI</p>
                  <p className="text-xl font-bold text-purple-600">
                    {(((sponsor.performance?.exposureValue || 0) / (sponsor.value || 1)) * 100).toFixed(0)}%
                  </p>
                </div>
              </div>

              <div className="mt-6 pt-6 border-t border-gray-200">
                <div className="flex justify-between items-center">
                  <div className="text-sm text-gray-600">
                    Contact: {sponsor.contact?.primary || 'N/A'} • {sponsor.contact?.email || 'N/A'}
                  </div>
                  <div className="flex space-x-2">
                    <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 flex items-center text-sm">
                      <Eye className="h-4 w-4 mr-1" />
                      Details
                    </button>
                    <button className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 flex items-center text-sm">
                      <FileText className="h-4 w-4 mr-1" />
                      Report
                    </button>
                    <button className="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 flex items-center text-sm">
                      <Mail className="h-4 w-4 mr-1" />
                      Contact
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  // Enhanced Heatmap Module
  const renderHeatmapCenter = () => {
    // Process heatmap data for visualization
    const facilityUsageData = heatmapData.reduce((acc, entry) => {
      if (!acc[entry.facility]) {
        acc[entry.facility] = [];
      }
      acc[entry.facility].push(entry);
      return acc;
    }, {});

    const avgUsageByFacility = Object.keys(facilityUsageData).map(facility => ({
      facility,
      avgUsage: facilityUsageData[facility].reduce((sum, entry) => sum + entry.usage, 0) / facilityUsageData[facility].length,
      avgRevenue: facilityUsageData[facility].reduce((sum, entry) => sum + entry.revenue, 0) / facilityUsageData[facility].length
    }));

    const hourlyUsage = Array.from({length: 16}, (_, i) => {
      const hour = i + 6;
      const hourData = heatmapData.filter(entry => entry.hour === hour);
      return {
        hour: `${hour}:00`,
        usage: hourData.reduce((sum, entry) => sum + entry.usage, 0) / hourData.length,
        revenue: hourData.reduce((sum, entry) => sum + entry.revenue, 0) / hourData.length
      };
    });

    return (
      <div className="space-y-6">
        <div className="flex justify-between items-center">
          <div>
            <h2 className="text-3xl font-bold text-gray-900">🔥 Enhanced Usage Heatmap</h2>
            <p className="text-gray-600 mt-1">Real-time facility utilization and revenue analytics</p>
          </div>
          <div className="flex items-center space-x-4">
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
              <span className="text-sm text-gray-600">Live Data</span>
            </div>
            <span className="text-sm text-gray-500">Updated: {currentTime.toLocaleTimeString()}</span>
          </div>
        </div>

        {/* Heatmap Overview */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div className="bg-gradient-to-br from-green-500 to-green-600 text-white p-6 rounded-xl">
            <h3 className="text-lg font-semibold">Overall Utilization</h3>
            <p className="text-3xl font-bold mt-2">{(heatmapData.reduce((sum, entry) => sum + entry.usage, 0) / heatmapData.length).toFixed(1)}%</p>
            <p className="text-green-100 text-sm">Across all facilities</p>
          </div>
          <div className="bg-gradient-to-br from-blue-500 to-blue-600 text-white p-6 rounded-xl">
            <h3 className="text-lg font-semibold">Peak Usage</h3>
            <p className="text-3xl font-bold mt-2">{Math.max(...heatmapData.map(entry => entry.usage)).toFixed(0)}%</p>
            <p className="text-blue-100 text-sm">Highest recorded today</p>
          </div>
          <div className="bg-gradient-to-br from-purple-500 to-purple-600 text-white p-6 rounded-xl">
            <h3 className="text-lg font-semibold">Revenue Generated</h3>
            <p className="text-3xl font-bold mt-2">${(heatmapData.reduce((sum, entry) => sum + entry.revenue, 0) / 1000).toFixed(0)}K</p>
            <p className="text-purple-100 text-sm">Total today</p>
          </div>
          <div className="bg-gradient-to-br from-orange-500 to-orange-600 text-white p-6 rounded-xl">
            <h3 className="text-lg font-semibold">Active Facilities</h3>
            <p className="text-3xl font-bold mt-2">{new Set(heatmapData.map(entry => entry.facility)).size}</p>
            <p className="text-orange-100 text-sm">Currently monitored</p>
          </div>
        </div>

        {/* Facility Usage Charts */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="bg-white p-6 rounded-xl shadow-lg">
            <h3 className="text-xl font-semibold mb-4">Hourly Usage Patterns</h3>
            <ResponsiveContainer width="100%" height={300}>
              <AreaChart data={hourlyUsage}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="hour" />
                <YAxis />
                <Tooltip />
                <Area type="monotone" dataKey="usage" stroke="#3b82f6" fill="#3b82f6" fillOpacity={0.6} name="Usage %" />
              </AreaChart>
            </ResponsiveContainer>
          </div>

          <div className="bg-white p-6 rounded-xl shadow-lg">
            <h3 className="text-xl font-semibold mb-4">Facility Performance</h3>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={avgUsageByFacility.slice(0, 6)}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="facility" angle={-45} textAnchor="end" height={100} />
                <YAxis />
                <Tooltip />
                <Bar dataKey="avgUsage" fill="#8884d8" name="Avg Usage %" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Real-time Facility Status */}
        <div className="bg-white rounded-xl shadow-lg p-6">
          <h3 className="text-xl font-semibold mb-4">Live Facility Status</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {avgUsageByFacility.map((facility, index) => (
              <div key={index} className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
                <div className="flex justify-between items-start mb-2">
                  <h4 className="font-semibold text-gray-900">{facility.facility}</h4>
                  <span className={`px-2 py-1 rounded text-xs font-medium ${
                    facility.avgUsage >= 80 ? 'bg-red-100 text-red-800' :
                    facility.avgUsage >= 60 ? 'bg-yellow-100 text-yellow-800' :
                    'bg-green-100 text-green-800'
                  }`}>
                    {facility.avgUsage >= 80 ? 'High' : facility.avgUsage >= 60 ? 'Medium' : 'Low'}
                  </span>
                </div>
                <div className="space-y-2">
                  <div className="flex justify-between">
                    <span className="text-sm text-gray-600">Usage:</span>
                    <span className="text-sm font-medium">{facility.avgUsage.toFixed(1)}%</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div 
                      className={`h-2 rounded-full ${
                        facility.avgUsage >= 80 ? 'bg-red-500' :
                        facility.avgUsage >= 60 ? 'bg-yellow-500' :
                        'bg-green-500'
                      }`}
                      style={{ width: `${facility.avgUsage}%` }}
                    ></div>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-sm text-gray-600">Revenue:</span>
                    <span className="text-sm font-medium">${facility.avgRevenue.toFixed(0)}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* AI Insights */}
        <div className="bg-white rounded-xl shadow-lg p-6">
          <h3 className="text-xl font-semibold mb-4 flex items-center">
            <Zap className="h-5 w-5 mr-2 text-yellow-500" />
            AI-Powered Insights
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="p-4 bg-blue-50 rounded-lg border-l-4 border-blue-500">
              <h4 className="font-semibold text-blue-900">Peak Time Optimization</h4>
              <p className="text-sm text-blue-700 mt-1">Consider dynamic pricing during 6-8 PM for 15% revenue boost</p>
            </div>
            <div className="p-4 bg-green-50 rounded-lg border-l-4 border-green-500">
              <h4 className="font-semibold text-green-900">Capacity Opportunity</h4>
              <p className="text-sm text-green-700 mt-1">Walking Track has 40% unused capacity during afternoons</p>
            </div>
            <div className="p-4 bg-purple-50 rounded-lg border-l-4 border-purple-500">
              <h4 className="font-semibold text-purple-900">Revenue Growth</h4>
              <p className="text-sm text-purple-700 mt-1">Weekend programming could increase revenue by $25K/month</p>
            </div>
          </div>
        </div>
      </div>
    );
  };

  // Analytics Module
  const renderAnalyticsHub = () => (
    <div className="space-y-6">
      <div>
        <h2 className="text-3xl font-bold text-gray-900">📊 Analytics & Performance Hub</h2>
        <p className="text-gray-600 mt-1">Comprehensive insights across all platform modules</p>
      </div>

      {/* Performance Overview */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-lg">
          <h3 className="text-xl font-semibold mb-4">Revenue Distribution</h3>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={sponsorData.map(sponsor => ({
                  name: sponsor.name,
                  value: sponsor.value || 0
                }))}
                cx="50%"
                cy="50%"
                outerRadius={100}
                dataKey="value"
                label={({ name, percent }) => `${name.split(' ')[0]} ${(percent * 100).toFixed(0)}%`}
              >
                {sponsorData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={['#2563eb', '#7c3aed', '#dc2626', '#059669', '#ea580c'][index % 5]} />
                ))}
              </Pie>
              <Tooltip formatter={(value) => `${value.toLocaleString()}`} />
            </PieChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-lg">
          <h3 className="text-xl font-semibold mb-4">Facility vs Sponsorship Performance</h3>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={[
              { month: 'Jan', facilityUsage: 75, sponsorSatisfaction: 8.5 },
              { month: 'Feb', facilityUsage: 78, sponsorSatisfaction: 8.7 },
              { month: 'Mar', facilityUsage: 82, sponsorSatisfaction: 8.9 },
              { month: 'Apr', facilityUsage: 79, sponsorSatisfaction: 9.1 },
              { month: 'May', facilityUsage: 84, sponsorSatisfaction: 9.0 },
              { month: 'Jun', facilityUsage: 81, sponsorSatisfaction: 8.9 }
            ]}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="facilityUsage" stroke="#2563eb" strokeWidth={3} name="Facility Usage %" />
              <Line type="monotone" dataKey="sponsorSatisfaction" stroke="#dc2626" strokeWidth={3} name="Sponsor Satisfaction" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Unified Performance Table */}
      <div className="bg-white rounded-xl shadow-lg p-6">
        <h3 className="text-xl font-semibold mb-4">Integrated Performance Matrix</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-gray-200">
                <th className="text-left p-3 font-semibold">Sponsor</th>
                <th className="text-left p-3 font-semibold">Tier</th>
                <th className="text-left p-3 font-semibold">Value</th>
                <th className="text-left p-3 font-semibold">Fulfillment</th>
                <th className="text-left p-3 font-semibold">Satisfaction</th>
                <th className="text-left p-3 font-semibold">ROI</th>
                <th className="text-left p-3 font-semibold">Status</th>
              </tr>
            </thead>
            <tbody>
              {sponsorData.map(sponsor => (
                <tr key={sponsor.id} className="border-b border-gray-100 hover:bg-gray-50">
                  <td className="p-3 font-medium">{sponsor.name}</td>
                  <td className="p-3">
                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                      sponsor.tier === 'Diamond' ? 'bg-blue-100 text-blue-800' :
                      sponsor.tier === 'Platinum' ? 'bg-gray-100 text-gray-800' :
                      sponsor.tier === 'Gold' ? 'bg-yellow-100 text-yellow-800' :
                      'bg-orange-100 text-orange-800'
                    }`}>
                      {sponsor.tier}
                    </span>
                  </td>
                  <td className="p-3 font-semibold">${(sponsor.value || 0).toLocaleString()}</td>
                  <td className="p-3">
                    <div className="flex items-center">
                      <div className="w-12 bg-gray-200 rounded-full h-2 mr-2">
                        <div 
                          className="bg-green-500 h-2 rounded-full"
                          style={{ width: `${sponsor.fulfillment?.overall || 0}%` }}
                        ></div>
                      </div>
                      <span className="text-xs">{sponsor.fulfillment?.overall || 0}%</span>
                    </div>
                  </td>
                  <td className="p-3">{sponsor.satisfaction?.score || 0}/10</td>
                  <td className="p-3 font-semibold text-green-600">
                    {(((sponsor.performance?.exposureValue || 0) / (sponsor.value || 1)) * 100).toFixed(0)}%
                  </td>
                  <td className="p-3">
                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                      sponsor.status === 'Active' ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'
                    }`}>
                      {sponsor.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );

  // Main Navigation
  const navigationItems = [
    { id: 'dashboard', label: 'Dashboard', icon: Home, description: 'Main overview' },
    { id: 'sponsorship', label: 'Sponsorship Center', icon: Users, description: 'Sponsor management' },
    { id: 'heatmap', label: 'Usage Heatmap', icon: BarChart3, description: 'Facility analytics' },
    { id: 'analytics', label: 'Analytics Hub', icon: Activity, description: 'Performance insights' }
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Top Navigation Bar */}
      <div className="bg-white shadow-lg border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center space-x-4">
              <button
                onClick={() => setSidebarOpen(!sidebarOpen)}
                className="p-2 rounded-lg hover:bg-gray-100"
              >
                <Menu className="h-6 w-6 text-gray-600" />
              </button>
              <h1 className="text-2xl font-bold text-gray-900">🏟️ SportAI Enterprise Suite™</h1>
            </div>
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
                <span className="text-sm text-gray-600">Live System</span>
              </div>
              <div className="text-sm text-gray-500">{currentTime.toLocaleTimeString()}</div>
              <div className="relative">
                <Bell className="h-6 w-6 text-gray-600" />
                <div className="absolute -top-1 -right-1 w-3 h-3 bg-red-500 rounded-full"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="flex">
        {/* Sidebar Navigation */}
        <div className={`bg-white shadow-lg border-r border-gray-200 transition-all duration-300 ${sidebarOpen ? 'w-64' : 'w-16'}`}>
          <div className="p-4 space-y-2">
            {navigationItems.map(item => {
              const IconComponent = item.icon;
              return (
                <button
                  key={item.id}
                  onClick={() => setCurrentModule(item.id)}
                  className={`w-full text-left p-3 rounded-lg transition-all hover:bg-gray-100 ${
                    currentModule === item.id 
                      ? 'bg-blue-100 text-blue-700 border-l-4 border-blue-500' 
                      : 'text-gray-700 hover:text-gray-900'
                  }`}
                >
                  <div className="flex items-center space-x-3">
                    <IconComponent className="h-5 w-5 flex-shrink-0" />
                    {sidebarOpen && (
                      <div>
                        <div className="font-medium">{item.label}</div>
                        <div className="text-xs text-gray-500">{item.description}</div>
                      </div>
                    )}
                  </div>
                </button>
              );
            })}
          </div>
        </div>

        {/* Main Content Area */}
        <div className="flex-1 p-6">
          {currentModule === 'dashboard' && renderMainDashboard()}
          {currentModule === 'sponsorship' && renderSponsorshipCenter()}
          {currentModule === 'heatmap' && renderHeatmapCenter()}
          {currentModule === 'analytics' && renderAnalyticsHub()}
        </div>
      </div>

      {/* Footer */}
      <div className="bg-white border-t border-gray-200 p-4">
        <div className="max-w-7xl mx-auto text-center text-sm text-gray-500">
          SportAI Enterprise Suite™ - Unified Sports Facility Management Platform | 
          Real-time AI Analytics | Comprehensive Sponsorship Management | 
          © 2025 NXS Complex Solutions
        </div>
      </div>
    </div>
  );
};

export default SportAIUnifiedSystem;