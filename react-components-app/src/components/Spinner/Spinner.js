import React from 'react';
import './Spinner.css';

const Spinner = ({ size = 'medium', color = 'primary', centered = false, label }) => {
  const spinner = (
    <div className="spinner-inner">
      <div className={`spinner spinner-${size} spinner-${color}`} role="status" />
      {label && <span className="spinner-label">{label}</span>}
    </div>
  );

  if (centered) {
    return <div className="spinner-container">{spinner}</div>;
  }

  return spinner;
};

export default Spinner;
