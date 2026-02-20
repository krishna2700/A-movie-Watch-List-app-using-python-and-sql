import React from 'react';
import './Alert.css';

const alertIcons = {
  info: '\u2139\uFE0F',
  success: '\u2705',
  warning: '\u26A0\uFE0F',
  danger: '\u274C',
};

const Alert = ({ type = 'info', children, onClose, dismissible = false, title }) => {
  return (
    <div className={`alert alert-${type}`} role="alert">
      <span className="alert-icon">{alertIcons[type]}</span>
      <div className="alert-content">
        {title && <strong className="alert-title">{title}</strong>}
        <div className="alert-message">{children}</div>
      </div>
      {dismissible && (
        <button className="alert-close" onClick={onClose} aria-label="Dismiss">
          &times;
        </button>
      )}
    </div>
  );
};

export default Alert;
