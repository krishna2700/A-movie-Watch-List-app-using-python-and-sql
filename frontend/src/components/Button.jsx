import React from "react";
import PropTypes from "prop-types";

/**
 * Reusable Button component with multiple variants, sizes, and states.
 *
 * @example
 * <Button variant="primary" size="md" onClick={handleClick}>Click Me</Button>
 * <Button variant="outline" size="lg" loading>Submitting...</Button>
 * <Button variant="danger" disabled>Disabled</Button>
 */

const variantClasses = {
  primary:
    "bg-indigo-600 text-white hover:bg-indigo-700 focus:ring-indigo-500 active:bg-indigo-800",
  secondary:
    "bg-gray-600 text-white hover:bg-gray-700 focus:ring-gray-500 active:bg-gray-800",
  outline:
    "border-2 border-indigo-600 text-indigo-600 bg-transparent hover:bg-indigo-50 focus:ring-indigo-500 active:bg-indigo-100",
  ghost:
    "bg-transparent text-gray-700 hover:bg-gray-100 focus:ring-gray-400 active:bg-gray-200",
  danger:
    "bg-red-600 text-white hover:bg-red-700 focus:ring-red-500 active:bg-red-800",
};

const sizeClasses = {
  sm: "px-3 py-1.5 text-sm rounded-md",
  md: "px-5 py-2.5 text-base rounded-lg",
  lg: "px-7 py-3.5 text-lg rounded-xl",
};

function Spinner({ size }) {
  const spinnerSize = {
    sm: "h-4 w-4",
    md: "h-5 w-5",
    lg: "h-6 w-6",
  };

  return (
    <svg
      className={`animate-spin ${spinnerSize[size] || spinnerSize.md}`}
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      aria-hidden="true"
    >
      <circle
        className="opacity-25"
        cx="12"
        cy="12"
        r="10"
        stroke="currentColor"
        strokeWidth="4"
      />
      <path
        className="opacity-75"
        fill="currentColor"
        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
      />
    </svg>
  );
}

function Button({
  children,
  variant = "primary",
  size = "md",
  disabled = false,
  loading = false,
  fullWidth = false,
  className = "",
  type = "button",
  ...rest
}) {
  const isDisabled = disabled || loading;

  const baseClasses =
    "inline-flex items-center justify-center gap-2 font-semibold transition-all duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-offset-2 select-none";

  const disabledClasses = isDisabled
    ? "opacity-50 cursor-not-allowed pointer-events-none"
    : "cursor-pointer";

  const widthClass = fullWidth ? "w-full" : "";

  const classes = [
    baseClasses,
    variantClasses[variant] || variantClasses.primary,
    sizeClasses[size] || sizeClasses.md,
    disabledClasses,
    widthClass,
    className,
  ]
    .filter(Boolean)
    .join(" ");

  return (
    <button
      type={type}
      className={classes}
      disabled={isDisabled}
      aria-busy={loading}
      {...rest}
    >
      {loading && <Spinner size={size} />}
      {children}
    </button>
  );
}

Button.propTypes = {
  /** Button content */
  children: PropTypes.node.isRequired,
  /** Visual style variant */
  variant: PropTypes.oneOf(["primary", "secondary", "outline", "ghost", "danger"]),
  /** Button size */
  size: PropTypes.oneOf(["sm", "md", "lg"]),
  /** Whether the button is disabled */
  disabled: PropTypes.bool,
  /** Whether to show a loading spinner */
  loading: PropTypes.bool,
  /** Whether the button should take full width */
  fullWidth: PropTypes.bool,
  /** Additional CSS classes */
  className: PropTypes.string,
  /** HTML button type attribute */
  type: PropTypes.oneOf(["button", "submit", "reset"]),
};

export default Button;
