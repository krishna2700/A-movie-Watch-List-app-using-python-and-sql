import React from 'react';
import './Badge.css';

const Badge = ({ children, variant = 'primary', size = 'medium', rounded = false, dot = false }) => {
  const classes = [
    'badge',
    `badge-${variant}`,
    `badge-${size}`,
    rounded ? 'badge-rounded' : '',
    dot ? 'badge-dot' : '',
  ]
    .filter(Boolean)
    .join(' ');

  return (
    <span className={classes}>
      {dot && <span className="badge-dot-indicator" />}
      {children}
    </span>
  );
};

export default Badge;
