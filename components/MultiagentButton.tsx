import React from 'react';

interface MultiagentButtonProps {
  children?: React.ReactNode;
  className?: string;
}

const MultiagentButton: React.FC<MultiagentButtonProps> = ({ 
  children = 'Multiagent', 
  className = '' 
}) => {
  return (
    <button
      className={`multiagent-button ${className}`}
      style={{
        backgroundColor: '#0000FF',
        color: '#FFFFFF',
        border: 'none',
        padding: '10px 20px',
        borderRadius: '4px',
        cursor: 'pointer',
        fontSize: '16px',
        fontWeight: '500',
      }}
    >
      {children}
    </button>
  );
};

export default MultiagentButton;
