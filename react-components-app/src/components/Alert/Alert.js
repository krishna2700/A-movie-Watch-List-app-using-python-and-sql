import React from 'react';
import './Alert.css';

const Alert = ({ 
  type = 'info', 
  children, 
  onClose,
  dismissible = false 
}) => {
  return (
    <div className={`alert alert-${type}`}>
      <div className="alert-content">
        {children}
      </div>
      {dismissible && (
        <button className="alert-close" onClick={onClose}>
          &times;
        </button>
      )}
    </div>
  );
};

export default Alert;
