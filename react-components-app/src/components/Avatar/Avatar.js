import React from 'react';
import './Avatar.css';

const Avatar = ({ name, src, size = 'medium', status, shape = 'circle' }) => {
  const getInitials = (name) => {
    if (!name) return '?';
    const parts = name.trim().split(' ');
    if (parts.length >= 2) {
      return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
    }
    return parts[0][0].toUpperCase();
  };

  const getColor = (name) => {
    if (!name) return '#6c757d';
    const colors = ['#4f46e5', '#0891b2', '#059669', '#d97706', '#dc2626', '#7c3aed', '#db2777', '#2563eb'];
    let hash = 0;
    for (let i = 0; i < name.length; i++) {
      hash = name.charCodeAt(i) + ((hash << 5) - hash);
    }
    return colors[Math.abs(hash) % colors.length];
  };

  return (
    <div className={`avatar avatar-${size} avatar-${shape}`}>
      {src ? (
        <img src={src} alt={name || 'Avatar'} className="avatar-img" />
      ) : (
        <div className="avatar-initials" style={{ backgroundColor: getColor(name) }}>
          {getInitials(name)}
        </div>
      )}
      {status && <span className={`avatar-status avatar-status-${status}`} />}
    </div>
  );
};

const AvatarGroup = ({ children, max = 4 }) => {
  const childArray = React.Children.toArray(children);
  const visible = childArray.slice(0, max);
  const remaining = childArray.length - max;

  return (
    <div className="avatar-group">
      {visible}
      {remaining > 0 && (
        <div className="avatar avatar-medium avatar-circle">
          <div className="avatar-initials avatar-remaining">+{remaining}</div>
        </div>
      )}
    </div>
  );
};

export { AvatarGroup };
export default Avatar;
