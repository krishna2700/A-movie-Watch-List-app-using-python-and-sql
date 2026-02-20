import React, { useState } from 'react';
import './Tabs.css';

const Tabs = ({ tabs, defaultActiveIndex = 0, variant = 'default', onChange }) => {
  const [activeIndex, setActiveIndex] = useState(defaultActiveIndex);

  const handleTabClick = (index) => {
    setActiveIndex(index);
    if (onChange) onChange(index);
  };

  return (
    <div className={`tabs tabs-${variant}`}>
      <div className="tabs-header" role="tablist">
        {tabs.map((tab, index) => (
          <button
            key={index}
            className={`tabs-tab ${activeIndex === index ? 'tabs-tab-active' : ''}`}
            onClick={() => handleTabClick(index)}
            role="tab"
            aria-selected={activeIndex === index}
            disabled={tab.disabled}
          >
            {tab.label}
          </button>
        ))}
      </div>
      <div className="tabs-content" role="tabpanel">
        {tabs[activeIndex] && tabs[activeIndex].content}
      </div>
    </div>
  );
};

export default Tabs;
