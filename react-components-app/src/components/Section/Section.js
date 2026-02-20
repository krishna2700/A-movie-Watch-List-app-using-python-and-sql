import React from 'react';
import './Section.css';

const Section = ({ title, description, children }) => {
  return (
    <section className="section">
      <div className="section-header">
        <h2>{title}</h2>
        {description && <p className="section-description">{description}</p>}
      </div>
      {children}
    </section>
  );
};

export default Section;
