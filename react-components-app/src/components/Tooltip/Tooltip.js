import React, { useState, useRef } from 'react';
import './Tooltip.css';

const Tooltip = ({ children, text, position = 'top', delay = 200 }) => {
  const [visible, setVisible] = useState(false);
  const timeoutRef = useRef(null);

  const showTooltip = () => {
    timeoutRef.current = setTimeout(() => setVisible(true), delay);
  };

  const hideTooltip = () => {
    clearTimeout(timeoutRef.current);
    setVisible(false);
  };

  return (
    <div
      className="tooltip-wrapper"
      onMouseEnter={showTooltip}
      onMouseLeave={hideTooltip}
      onFocus={showTooltip}
      onBlur={hideTooltip}
    >
      {children}
      {visible && (
        <div className={`tooltip tooltip-${position}`} role="tooltip">
          <span className="tooltip-text">{text}</span>
        </div>
      )}
    </div>
  );
};

export default Tooltip;
