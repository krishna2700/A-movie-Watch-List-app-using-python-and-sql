import React, { useState, useRef, useEffect, useCallback } from 'react';
import './Dropdown.css';

const Dropdown = ({ trigger, items = [], align = 'left' }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [focusedIndex, setFocusedIndex] = useState(-1);
  const dropdownRef = useRef(null);
  const menuRef = useRef(null);

  const actionableItems = items.filter((item) => item.type !== 'divider' && item.type !== 'label');

  const handleClose = useCallback(() => {
    setIsOpen(false);
    setFocusedIndex(-1);
  }, []);

  useEffect(() => {
    const handleClickOutside = (e) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
        handleClose();
      }
    };

    if (isOpen) {
      document.addEventListener('mousedown', handleClickOutside);
    }
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, [isOpen, handleClose]);

  const handleKeyDown = (e) => {
    if (!isOpen) {
      if (e.key === 'Enter' || e.key === ' ' || e.key === 'ArrowDown') {
        e.preventDefault();
        setIsOpen(true);
        setFocusedIndex(0);
      }
      return;
    }

    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        setFocusedIndex((prev) => (prev + 1) % actionableItems.length);
        break;
      case 'ArrowUp':
        e.preventDefault();
        setFocusedIndex((prev) => (prev - 1 + actionableItems.length) % actionableItems.length);
        break;
      case 'Enter':
      case ' ':
        e.preventDefault();
        if (focusedIndex >= 0 && actionableItems[focusedIndex]) {
          const item = actionableItems[focusedIndex];
          if (!item.disabled && item.onClick) {
            item.onClick();
          }
          handleClose();
        }
        break;
      case 'Escape':
        e.preventDefault();
        handleClose();
        break;
      default:
        break;
    }
  };

  let actionIndex = -1;

  return (
    <div className="dropdown" ref={dropdownRef} onKeyDown={handleKeyDown}>
      <div
        className="dropdown-trigger"
        onClick={() => {
          setIsOpen((prev) => !prev);
          setFocusedIndex(-1);
        }}
        role="button"
        tabIndex={0}
        aria-haspopup="true"
        aria-expanded={isOpen}
      >
        {trigger}
      </div>

      {isOpen && (
        <div
          className={`dropdown-menu ${align === 'right' ? 'dropdown-menu-right' : ''}`}
          ref={menuRef}
          role="menu"
        >
          {items.map((item, index) => {
            if (item.type === 'divider') {
              return <hr key={index} className="dropdown-divider" />;
            }

            if (item.type === 'label') {
              return (
                <div key={index} className="dropdown-label">
                  {item.text}
                </div>
              );
            }

            actionIndex++;
            const isFocused = actionIndex === focusedIndex;

            return (
              <button
                key={index}
                className={`dropdown-item ${item.variant === 'danger' ? 'dropdown-item-danger' : ''} ${isFocused ? 'dropdown-item-focused' : ''}`}
                onClick={() => {
                  if (!item.disabled && item.onClick) {
                    item.onClick();
                  }
                  handleClose();
                }}
                disabled={item.disabled}
                role="menuitem"
              >
                {item.label}
              </button>
            );
          })}
        </div>
      )}
    </div>
  );
};

export default Dropdown;
