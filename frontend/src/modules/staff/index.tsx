import React, {useState} from 'react';
export const StaffView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>STAFF - Staff - certifications, specialties, ava</h2><p>certified</p></div>
};
export default StaffView;
