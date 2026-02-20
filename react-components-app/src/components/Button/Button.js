import React from 'react';
import './Button.css';

const Button = ({ 
  children, 
  variant = 'primary', 
  size = 'medium', 
  onClick, 
  disabled = false,
  type = 'button',
  fullWidth = false 
}) => {
  const className = `btn btn-${variant} btn-${size} ${fullWidth ? 'btn-full-width' : ''}`;
  
  return (
    <button 
      className={className}
      onClick={onClick}
      disabled={disabled}
      type={type}
    >
      {children}
    </button>
  );
};

export default Button;
