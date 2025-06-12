import React, {useState} from 'react';
export const AnalyticsView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>ANALYTICS - Analytics - occupancy, retail, retention</h2><p>occupancy</p></div>
};
export default AnalyticsView;
