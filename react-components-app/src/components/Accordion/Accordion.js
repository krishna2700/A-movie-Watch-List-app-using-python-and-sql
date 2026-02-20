import React, { useState } from 'react';
import './Accordion.css';

const AccordionItem = ({ title, children, isOpen, onToggle }) => {
  return (
    <div className={`accordion-item ${isOpen ? 'accordion-item-open' : ''}`}>
      <button className="accordion-trigger" onClick={onToggle} aria-expanded={isOpen}>
        <span className="accordion-trigger-text">{title}</span>
        <span className="accordion-chevron">{isOpen ? '\u2212' : '\u002B'}</span>
      </button>
      <div className="accordion-panel" style={{ maxHeight: isOpen ? '500px' : '0' }}>
        <div className="accordion-panel-inner">
          {children}
        </div>
      </div>
    </div>
  );
};

const Accordion = ({ items, allowMultiple = false }) => {
  const [openIndices, setOpenIndices] = useState([]);

  const handleToggle = (index) => {
    if (allowMultiple) {
      setOpenIndices((prev) =>
        prev.includes(index) ? prev.filter((i) => i !== index) : [...prev, index]
      );
    } else {
      setOpenIndices((prev) => (prev.includes(index) ? [] : [index]));
    }
  };

  return (
    <div className="accordion">
      {items.map((item, index) => (
        <AccordionItem
          key={index}
          title={item.title}
          isOpen={openIndices.includes(index)}
          onToggle={() => handleToggle(index)}
        >
          {item.content}
        </AccordionItem>
      ))}
    </div>
  );
};

export default Accordion;
