import React from 'react';
import './Select.css';

const Select = ({
  label,
  options = [],
  value,
  onChange,
  placeholder = 'Select an option',
  error,
  disabled = false,
  required = false,
  name,
  id,
}) => {
  const selectId = id || name;

  return (
    <div className="select-wrapper">
      {label && (
        <label htmlFor={selectId} className="select-label">
          {label}
          {required && <span className="select-required">*</span>}
        </label>
      )}
      <div className="select-container">
        <select
          id={selectId}
          name={name}
          className={`select ${error ? 'select-error' : ''}`}
          value={value}
          onChange={onChange}
          disabled={disabled}
          required={required}
        >
          <option value="" disabled>
            {placeholder}
          </option>
          {options.map((option) => (
            <option key={option.value} value={option.value} disabled={option.disabled}>
              {option.label}
            </option>
          ))}
        </select>
        <span className="select-arrow">&#9662;</span>
      </div>
      {error && <span className="select-error-message">{error}</span>}
    </div>
  );
};

export default Select;
