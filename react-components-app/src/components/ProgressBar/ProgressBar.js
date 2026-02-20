import React from 'react';
import './ProgressBar.css';

const ProgressBar = ({
  value = 0,
  max = 100,
  variant = 'primary',
  size = 'medium',
  showLabel = false,
  animated = false,
  striped = false,
}) => {
  const percentage = Math.min(Math.max((value / max) * 100, 0), 100);

  return (
    <div className="progress-wrapper">
      {showLabel && (
        <div className="progress-label">
          <span>{Math.round(percentage)}%</span>
        </div>
      )}
      <div className={`progress-track progress-track-${size}`}>
        <div
          className={`progress-fill progress-fill-${variant} ${striped ? 'progress-striped' : ''} ${animated ? 'progress-animated' : ''}`}
          style={{ width: `${percentage}%` }}
          role="progressbar"
          aria-valuenow={value}
          aria-valuemin={0}
          aria-valuemax={max}
        />
      </div>
    </div>
  );
};

export default ProgressBar;
