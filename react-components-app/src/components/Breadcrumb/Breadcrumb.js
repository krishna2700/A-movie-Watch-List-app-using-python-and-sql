import React from 'react';
import './Breadcrumb.css';

const Breadcrumb = ({ items = [], separator = '/', size = 'medium', onNavigate }) => {
  const classes = ['breadcrumb', `breadcrumb-${size}`].join(' ');

  return (
    <nav aria-label="Breadcrumb">
      <ol className={classes}>
        {items.map((item, index) => {
          const isLast = index === items.length - 1;

          return (
            <li key={index} className="breadcrumb-item">
              {isLast ? (
                <span className="breadcrumb-active" aria-current="page">
                  {item.label}
                </span>
              ) : (
                <button
                  className="breadcrumb-link"
                  onClick={() => onNavigate && onNavigate(item)}
                  type="button"
                >
                  {item.label}
                </button>
              )}
              {!isLast && (
                <span className="breadcrumb-separator" aria-hidden="true">
                  {separator}
                </span>
              )}
            </li>
          );
        })}
      </ol>
    </nav>
  );
};

export default Breadcrumb;
