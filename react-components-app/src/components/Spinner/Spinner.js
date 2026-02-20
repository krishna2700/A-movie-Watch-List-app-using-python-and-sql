import React from 'react';
import './Spinner.css';

const Spinner = ({ 
  size = 'medium',
  color = 'primary',
  centered = false 
}) => {
  const className = `spinner spinner-${size} spinner-${color}`;
  
  if (centered) {
    return (
      <div className="spinner-container">
        <div className={className}></div>
      </div>
    );
  }
  
  return <div className={className}></div>;
};

export default Spinner;
