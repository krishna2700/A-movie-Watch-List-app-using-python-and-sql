import React from 'react';
import './Toggle.css';

const Toggle = ({ checked = false, onChange, label, disabled = false, size = 'medium' }) => {
  const handleChange = () => {
    if (!disabled && onChange) {
      onChange(!checked);
    }
  };

  return (
    <label className={`toggle-wrapper ${disabled ? 'toggle-disabled' : ''}`}>
      <div
        className={`toggle toggle-${size} ${checked ? 'toggle-checked' : ''}`}
        onClick={handleChange}
        role="switch"
        aria-checked={checked}
        tabIndex={0}
        onKeyDown={(e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            handleChange();
          }
        }}
      >
        <div className="toggle-thumb" />
      </div>
      {label && <span className="toggle-label">{label}</span>}
    </label>
  );
};

export default Toggle;
