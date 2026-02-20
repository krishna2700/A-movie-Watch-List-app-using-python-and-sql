import React from 'react';
import './Skeleton.css';

const Skeleton = ({ variant = 'text', width, height, count = 1, style = {} }) => {
  const getVariantClass = () => {
    switch (variant) {
      case 'circle':
        return 'skeleton-circle';
      case 'rectangle':
        return 'skeleton-rectangle';
      case 'heading':
        return 'skeleton-heading';
      case 'text':
      default:
        return 'skeleton-text';
    }
  };

  const defaultDimensions = () => {
    switch (variant) {
      case 'circle':
        return { width: width || 44, height: height || 44 };
      case 'rectangle':
        return { width: width || '100%', height: height || 120 };
      case 'heading':
        return { width: width || '60%', height: height || 24 };
      case 'text':
      default:
        return { width: width || '100%', height: height || 14 };
    }
  };

  const dims = defaultDimensions();

  const elements = Array.from({ length: count }, (_, i) => {
    const itemWidth =
      variant === 'text' && count > 1 && i === count - 1
        ? '75%'
        : dims.width;

    return (
      <div
        key={i}
        className={`skeleton ${getVariantClass()}`}
        style={{
          width: typeof itemWidth === 'number' ? `${itemWidth}px` : itemWidth,
          height: typeof dims.height === 'number' ? `${dims.height}px` : dims.height,
          ...style,
        }}
        aria-hidden="true"
      />
    );
  });

  if (count > 1) {
    return <div className="skeleton-group">{elements}</div>;
  }

  return elements[0];
};

const SkeletonCard = () => {
  return (
    <div className="skeleton-card">
      <div className="skeleton-card-header">
        <Skeleton variant="circle" width={48} height={48} />
        <div className="skeleton-card-lines">
          <Skeleton variant="heading" width="50%" />
          <Skeleton variant="text" width="30%" />
        </div>
      </div>
      <Skeleton variant="text" count={3} />
    </div>
  );
};

export { SkeletonCard };
export default Skeleton;
