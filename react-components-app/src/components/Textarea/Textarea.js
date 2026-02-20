import React from 'react';
import './Textarea.css';

const Textarea = ({
  label,
  placeholder,
  value,
  onChange,
  error,
  disabled = false,
  required = false,
  name,
  id,
  rows = 4,
  maxLength,
  resize = 'vertical',
}) => {
  const textareaId = id || name;

  return (
    <div className="textarea-wrapper">
      {label && (
        <label htmlFor={textareaId} className="textarea-label">
          {label}
          {required && <span className="textarea-required">*</span>}
        </label>
      )}
      <textarea
        id={textareaId}
        name={name}
        className={`textarea ${error ? 'textarea-error' : ''}`}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        disabled={disabled}
        required={required}
        rows={rows}
        maxLength={maxLength}
        style={{ resize }}
      />
      <div className="textarea-footer">
        {error && <span className="textarea-error-message">{error}</span>}
        {maxLength && (
          <span className="textarea-counter">
            {(value || '').length}/{maxLength}
          </span>
        )}
      </div>
    </div>
  );
};

export default Textarea;
