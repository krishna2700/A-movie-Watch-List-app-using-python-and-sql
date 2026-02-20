import React from 'react';
import './Badge.css';

const Badge = ({ 
  children, 
  variant = 'primary',
  size = 'medium',
  rounded = false 
}) => {
  const className = `badge badge-${variant} badge-${size} ${rounded ? 'badge-rounded' : ''}`;
  
  return (
    <span className={className}>
      {children}
    </span>
  );
};

export default Badge;
