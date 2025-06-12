import React, {useState} from 'react';
export const ApiView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>API - API - REST for locations, staff, schedul</h2><p>POST location</p></div>
};
export default ApiView;
