import React, { useState } from 'react';
import './App.css';
import {
  Button,
  Card,
  Input,
  Modal,
  Alert,
  Badge,
  Spinner,
  Tabs,
  Accordion,
  Avatar,
  AvatarGroup,
  Tooltip,
  Toggle,
  ProgressBar,
  Select,
  Textarea,
  Breadcrumb,
  Dropdown,
  Skeleton,
  SkeletonCard,
} from './components';

function App() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [showAlert, setShowAlert] = useState(true);
  const [formData, setFormData] = useState({ name: '', email: '', role: '', message: '' });
  const [errors, setErrors] = useState({});
  const [darkMode, setDarkMode] = useState(false);
  const [notifications, setNotifications] = useState(true);
  const [autoSave, setAutoSave] = useState(false);
  const [loadingBtn, setLoadingBtn] = useState(false);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: '' }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const newErrors = {};
    if (!formData.name) newErrors.name = 'Name is required';
    if (!formData.email) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = 'Please enter a valid email';
    }
    if (!formData.role) newErrors.role = 'Please select a role';

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
    } else {
      setLoadingBtn(true);
      setTimeout(() => {
        setLoadingBtn(false);
        setFormData({ name: '', email: '', role: '', message: '' });
        alert('Form submitted successfully!');
      }, 1500);
    }
  };

  const roleOptions = [
    { value: 'developer', label: 'Developer' },
    { value: 'designer', label: 'Designer' },
    { value: 'manager', label: 'Project Manager' },
    { value: 'qa', label: 'QA Engineer' },
  ];

  const tabItems = [
    {
      label: 'Overview',
      content: (
        <div>
          <p style={{ margin: 0, lineHeight: 1.7, color: '#4b5563' }}>
            This component library provides a comprehensive set of 18 reusable React components
            designed for building modern web applications. Each component is customizable through
            props and follows consistent design patterns.
          </p>
        </div>
      ),
    },
    {
      label: 'Features',
      content: (
        <ul style={{ margin: 0, paddingLeft: 20, lineHeight: 2, color: '#4b5563' }}>
          <li>18 reusable components with consistent API</li>
          <li>Multiple variants, sizes, and states</li>
          <li>Keyboard accessible and ARIA compliant</li>
          <li>Smooth animations and transitions</li>
          <li>Responsive and mobile-friendly</li>
        </ul>
      ),
    },
    {
      label: 'Usage',
      content: (
        <pre style={{ margin: 0, background: '#f8fafc', padding: 16, borderRadius: 8, fontSize: 13, overflow: 'auto', color: '#334155' }}>
{`import { Button, Card, Input } from './components';

function MyPage() {
  return (
    <Card title="My Card" hoverable>
      <Input label="Name" name="name" />
      <Button variant="primary">Submit</Button>
    </Card>
  );
}`}
        </pre>
      ),
    },
  ];

  const accordionItems = [
    {
      title: 'What is this component library?',
      content:
        'A collection of 18 beautifully designed, reusable React components that you can use to build modern web applications quickly and consistently.',
    },
    {
      title: 'How do I install it?',
      content:
        'Simply copy the components directory into your React project. All components are self-contained with their own CSS files and can be imported from the central index.',
    },
    {
      title: 'Can I customize the components?',
      content:
        'Yes! Every component accepts props for customization including variants, sizes, colors, and behavior. You can also override the CSS to match your brand.',
    },
    {
      title: 'Are the components accessible?',
      content:
        'Components follow WAI-ARIA guidelines with proper roles, labels, and keyboard navigation support built in.',
    },
  ];

  return (
    <div className="App">
      <header className="App-header">
        <div className="header-content">
          <Badge variant="primary" rounded>v2.1</Badge>
          <h1>React Component Library</h1>
          <p>18 beautifully crafted, reusable components for modern web apps</p>
          <div className="header-actions">
            <Button variant="primary" size="large" onClick={() => {
              document.getElementById('components').scrollIntoView({ behavior: 'smooth' });
            }}>
              Explore Components
            </Button>
            <Button variant="primary" size="large" outline onClick={() => setIsModalOpen(true)}>
              Quick Start
            </Button>
          </div>
        </div>
      </header>

      <main className="App-main" id="components">
        {showAlert && (
          <Alert type="info" dismissible onClose={() => setShowAlert(false)} title="Welcome!">
            Explore all 15 reusable components below. Each one is fully customizable through props.
          </Alert>
        )}

        {/* Buttons Section */}
        <section className="section">
          <div className="section-header">
            <h2>Buttons</h2>
            <Badge variant="info" rounded>Interactive</Badge>
          </div>
          <p className="section-desc">Versatile button component with solid and outline variants, multiple sizes, and loading state.</p>
          <div className="subsection">
            <h3>Solid Variants</h3>
            <div className="component-showcase">
              <Button variant="primary">Primary</Button>
              <Button variant="secondary">Secondary</Button>
              <Button variant="success">Success</Button>
              <Button variant="danger">Danger</Button>
              <Button variant="warning">Warning</Button>
            </div>
          </div>
          <div className="subsection">
            <h3>Outline Variants</h3>
            <div className="component-showcase">
              <Button variant="primary" outline>Primary</Button>
              <Button variant="secondary" outline>Secondary</Button>
              <Button variant="success" outline>Success</Button>
              <Button variant="danger" outline>Danger</Button>
            </div>
          </div>
          <div className="subsection">
            <h3>Sizes &amp; States</h3>
            <div className="component-showcase">
              <Button size="small">Small</Button>
              <Button size="medium">Medium</Button>
              <Button size="large">Large</Button>
              <Button disabled>Disabled</Button>
              <Button loading>Loading</Button>
            </div>
          </div>
        </section>

        {/* Badges Section */}
        <section className="section">
          <div className="section-header">
            <h2>Badges</h2>
            <Badge variant="success" rounded dot>New</Badge>
          </div>
          <p className="section-desc">Lightweight labels for status indicators, counts, and categorization.</p>
          <div className="subsection">
            <h3>Variants</h3>
            <div className="component-showcase">
              <Badge variant="primary">Primary</Badge>
              <Badge variant="secondary">Secondary</Badge>
              <Badge variant="success">Success</Badge>
              <Badge variant="danger">Danger</Badge>
              <Badge variant="warning">Warning</Badge>
              <Badge variant="info">Info</Badge>
            </div>
          </div>
          <div className="subsection">
            <h3>Rounded &amp; Dot</h3>
            <div className="component-showcase">
              <Badge variant="primary" rounded>Rounded</Badge>
              <Badge variant="success" rounded>99+</Badge>
              <Badge variant="danger" rounded dot>Live</Badge>
              <Badge variant="info" dot>Active</Badge>
            </div>
          </div>
        </section>

        {/* Cards Section */}
        <section className="section">
          <div className="section-header">
            <h2>Cards</h2>
            <Badge variant="primary" rounded>Layout</Badge>
          </div>
          <p className="section-desc">Flexible container component for grouping related content with optional header and footer.</p>
          <div className="cards-grid">
            <Card title="Default Card" subtitle="With subtitle" hoverable>
              <p style={{ margin: 0, color: '#6b7280' }}>
                A standard card with title, subtitle, and body content. Hover to see the elevation effect.
              </p>
            </Card>

            <Card
              title="Card with Footer"
              hoverable
              footer={
                <div style={{ display: 'flex', gap: '8px' }}>
                  <Button size="small" variant="primary">Save</Button>
                  <Button size="small" variant="secondary" outline>Cancel</Button>
                </div>
              }
            >
              <p style={{ margin: 0, color: '#6b7280' }}>
                This card includes a footer area perfect for action buttons.
              </p>
            </Card>

            <Card variant="elevated" hoverable>
              <div style={{ textAlign: 'center', padding: '10px 0' }}>
                <Avatar name="Sarah Chen" size="large" status="online" />
                <h3 style={{ margin: '12px 0 4px', color: '#1f2937' }}>Sarah Chen</h3>
                <p style={{ margin: 0, color: '#6b7280', fontSize: 14 }}>Lead Developer</p>
                <div style={{ display: 'flex', gap: 6, justifyContent: 'center', marginTop: 12 }}>
                  <Badge variant="primary" size="small">React</Badge>
                  <Badge variant="success" size="small">Node.js</Badge>
                </div>
              </div>
            </Card>
          </div>
        </section>

        {/* Avatars Section */}
        <section className="section">
          <div className="section-header">
            <h2>Avatars</h2>
            <Badge variant="warning" rounded>Identity</Badge>
          </div>
          <p className="section-desc">User representation with initials, images, status indicators, and grouping.</p>
          <div className="subsection">
            <h3>Sizes &amp; Status</h3>
            <div className="component-showcase">
              <Avatar name="Alice Johnson" size="small" status="online" />
              <Avatar name="Bob Smith" size="medium" status="busy" />
              <Avatar name="Charlie Davis" size="large" status="away" />
              <Avatar name="Diana Prince" size="large" status="offline" />
            </div>
          </div>
          <div className="subsection">
            <h3>Shapes</h3>
            <div className="component-showcase">
              <Avatar name="John Doe" size="medium" shape="circle" />
              <Avatar name="Jane Smith" size="medium" shape="square" />
            </div>
          </div>
          <div className="subsection">
            <h3>Avatar Group</h3>
            <AvatarGroup max={4}>
              <Avatar name="Alice" size="medium" />
              <Avatar name="Bob" size="medium" />
              <Avatar name="Charlie" size="medium" />
              <Avatar name="Diana" size="medium" />
              <Avatar name="Eve" size="medium" />
              <Avatar name="Frank" size="medium" />
            </AvatarGroup>
          </div>
        </section>

        {/* Tabs Section */}
        <section className="section">
          <div className="section-header">
            <h2>Tabs</h2>
            <Badge variant="info" rounded>Navigation</Badge>
          </div>
          <p className="section-desc">Organize content into switchable panels with default and pill variants.</p>
          <div className="subsection">
            <h3>Default Tabs</h3>
            <Tabs tabs={tabItems} />
          </div>
          <div className="subsection">
            <h3>Pill Tabs</h3>
            <Tabs tabs={tabItems} variant="pills" />
          </div>
        </section>

        {/* Accordion Section */}
        <section className="section">
          <div className="section-header">
            <h2>Accordion</h2>
            <Badge variant="secondary" rounded>Disclosure</Badge>
          </div>
          <p className="section-desc">Collapsible content panels for organizing information in a compact space.</p>
          <div className="subsection">
            <h3>Single Expand</h3>
            <Accordion items={accordionItems} />
          </div>
        </section>

        {/* Progress Bars Section */}
        <section className="section">
          <div className="section-header">
            <h2>Progress Bars</h2>
            <Badge variant="success" rounded>Feedback</Badge>
          </div>
          <p className="section-desc">Visual indicators for task completion, loading states, and data metrics.</p>
          <div className="progress-demos">
            <div className="progress-demo-item">
              <span className="progress-demo-label">Project Alpha</span>
              <ProgressBar value={85} variant="primary" showLabel />
            </div>
            <div className="progress-demo-item">
              <span className="progress-demo-label">Design Phase</span>
              <ProgressBar value={60} variant="success" showLabel />
            </div>
            <div className="progress-demo-item">
              <span className="progress-demo-label">Bug Fixes</span>
              <ProgressBar value={35} variant="warning" showLabel striped animated />
            </div>
            <div className="progress-demo-item">
              <span className="progress-demo-label">Critical Issues</span>
              <ProgressBar value={15} variant="danger" showLabel />
            </div>
          </div>
          <div className="subsection">
            <h3>Sizes</h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
              <ProgressBar value={70} variant="primary" size="small" />
              <ProgressBar value={70} variant="primary" size="medium" />
              <ProgressBar value={70} variant="primary" size="large" />
            </div>
          </div>
        </section>

        {/* Toggles Section */}
        <section className="section">
          <div className="section-header">
            <h2>Toggles</h2>
            <Badge variant="primary" rounded>Controls</Badge>
          </div>
          <p className="section-desc">Switch controls for binary settings with labels and multiple sizes.</p>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 20 }}>
            <Toggle checked={darkMode} onChange={setDarkMode} label="Dark Mode" />
            <Toggle checked={notifications} onChange={setNotifications} label="Enable Notifications" />
            <Toggle checked={autoSave} onChange={setAutoSave} label="Auto-save Documents" />
            <Toggle checked={false} onChange={() => {}} label="Disabled Toggle" disabled />
          </div>
          <div className="subsection">
            <h3>Sizes</h3>
            <div className="component-showcase">
              <Toggle checked size="small" onChange={() => {}} label="Small" />
              <Toggle checked size="medium" onChange={() => {}} label="Medium" />
              <Toggle checked size="large" onChange={() => {}} label="Large" />
            </div>
          </div>
        </section>

        {/* Tooltips Section */}
        <section className="section">
          <div className="section-header">
            <h2>Tooltips</h2>
            <Badge variant="info" rounded>Overlay</Badge>
          </div>
          <p className="section-desc">Contextual information on hover with configurable positioning.</p>
          <div className="component-showcase" style={{ gap: 20 }}>
            <Tooltip text="Tooltip on top" position="top">
              <Button variant="secondary" outline>Top</Button>
            </Tooltip>
            <Tooltip text="Tooltip on bottom" position="bottom">
              <Button variant="secondary" outline>Bottom</Button>
            </Tooltip>
            <Tooltip text="Tooltip on left" position="left">
              <Button variant="secondary" outline>Left</Button>
            </Tooltip>
            <Tooltip text="Tooltip on right" position="right">
              <Button variant="secondary" outline>Right</Button>
            </Tooltip>
          </div>
        </section>

        {/* Form Section */}
        <section className="section">
          <div className="section-header">
            <h2>Form Components</h2>
            <Badge variant="danger" rounded>Forms</Badge>
          </div>
          <p className="section-desc">Complete form building blocks including inputs, selects, textareas with validation.</p>
          <Card title="Contact Form" subtitle="All fields with validation">
            <form onSubmit={handleSubmit}>
              <div className="form-row">
                <Input
                  label="Full Name"
                  name="name"
                  placeholder="Enter your full name"
                  value={formData.name}
                  onChange={handleInputChange}
                  error={errors.name}
                  required
                />
                <Input
                  type="email"
                  label="Email Address"
                  name="email"
                  placeholder="you@example.com"
                  value={formData.email}
                  onChange={handleInputChange}
                  error={errors.email}
                  required
                  helperText="We'll never share your email"
                />
              </div>
              <Select
                label="Role"
                name="role"
                options={roleOptions}
                value={formData.role}
                onChange={handleInputChange}
                error={errors.role}
                required
                placeholder="Choose your role"
              />
              <Textarea
                label="Message"
                name="message"
                placeholder="Tell us about your project..."
                value={formData.message}
                onChange={handleInputChange}
                rows={4}
                maxLength={500}
              />
              <div style={{ display: 'flex', gap: '10px', marginTop: '4px' }}>
                <Button type="submit" variant="primary" loading={loadingBtn}>
                  {loadingBtn ? 'Submitting...' : 'Submit Form'}
                </Button>
                <Button
                  type="button"
                  variant="secondary"
                  outline
                  onClick={() => {
                    setFormData({ name: '', email: '', role: '', message: '' });
                    setErrors({});
                  }}
                >
                  Reset
                </Button>
              </div>
            </form>
          </Card>
        </section>

        {/* Breadcrumb Section */}
        <section className="section">
          <div className="section-header">
            <h2>Breadcrumb</h2>
            <Badge variant="info" rounded>Navigation</Badge>
          </div>
          <p className="section-desc">Navigation breadcrumbs to show the current page location within a hierarchy.</p>
          <div className="subsection">
            <h3>Default</h3>
            <Breadcrumb
              items={[
                { label: 'Home', href: '/' },
                { label: 'Products', href: '/products' },
                { label: 'Electronics', href: '/products/electronics' },
                { label: 'Headphones' },
              ]}
              onNavigate={(item) => alert(`Navigate to: ${item.label}`)}
            />
          </div>
          <div className="subsection">
            <h3>Custom Separator</h3>
            <Breadcrumb
              items={[
                { label: 'Dashboard', href: '/' },
                { label: 'Settings', href: '/settings' },
                { label: 'Profile' },
              ]}
              separator="›"
              onNavigate={(item) => alert(`Navigate to: ${item.label}`)}
            />
          </div>
          <div className="subsection">
            <h3>Sizes</h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
              <Breadcrumb
                items={[{ label: 'Home' }, { label: 'Docs' }, { label: 'API' }]}
                size="small"
              />
              <Breadcrumb
                items={[{ label: 'Home' }, { label: 'Docs' }, { label: 'API' }]}
                size="medium"
              />
              <Breadcrumb
                items={[{ label: 'Home' }, { label: 'Docs' }, { label: 'API' }]}
                size="large"
              />
            </div>
          </div>
        </section>

        {/* Dropdown Section */}
        <section className="section">
          <div className="section-header">
            <h2>Dropdown</h2>
            <Badge variant="warning" rounded>Interactive</Badge>
          </div>
          <p className="section-desc">Trigger-based dropdown menus with keyboard navigation, dividers, and labels.</p>
          <div className="component-showcase" style={{ gap: 20 }}>
            <Dropdown
              trigger={<Button variant="primary">Actions</Button>}
              items={[
                { label: 'Edit', onClick: () => alert('Edit clicked') },
                { label: 'Duplicate', onClick: () => alert('Duplicate clicked') },
                { type: 'divider' },
                { label: 'Archive', onClick: () => alert('Archive clicked') },
                { label: 'Delete', onClick: () => alert('Delete clicked'), variant: 'danger' },
              ]}
            />
            <Dropdown
              trigger={<Button variant="secondary" outline>Options</Button>}
              items={[
                { type: 'label', text: 'Account' },
                { label: 'Profile', onClick: () => alert('Profile') },
                { label: 'Settings', onClick: () => alert('Settings') },
                { type: 'divider' },
                { type: 'label', text: 'Actions' },
                { label: 'Export Data', onClick: () => alert('Export') },
                { label: 'Disabled Item', disabled: true },
              ]}
            />
            <Dropdown
              trigger={<Button variant="success" outline>Right Aligned</Button>}
              align="right"
              items={[
                { label: 'Option A', onClick: () => alert('A') },
                { label: 'Option B', onClick: () => alert('B') },
                { label: 'Option C', onClick: () => alert('C') },
              ]}
            />
          </div>
        </section>

        {/* Skeleton Section */}
        <section className="section">
          <div className="section-header">
            <h2>Skeleton</h2>
            <Badge variant="secondary" rounded>Loading</Badge>
          </div>
          <p className="section-desc">Placeholder loading animations for content that is still being fetched.</p>
          <div className="subsection">
            <h3>Variants</h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
              <div>
                <span style={{ fontSize: 13, color: '#9ca3af', fontWeight: 500, display: 'block', marginBottom: 8 }}>Text Lines</span>
                <Skeleton variant="text" count={3} />
              </div>
              <div>
                <span style={{ fontSize: 13, color: '#9ca3af', fontWeight: 500, display: 'block', marginBottom: 8 }}>Heading</span>
                <Skeleton variant="heading" />
              </div>
              <div style={{ display: 'flex', gap: 12 }}>
                <div>
                  <span style={{ fontSize: 13, color: '#9ca3af', fontWeight: 500, display: 'block', marginBottom: 8 }}>Circle</span>
                  <Skeleton variant="circle" width={56} height={56} />
                </div>
                <div style={{ flex: 1 }}>
                  <span style={{ fontSize: 13, color: '#9ca3af', fontWeight: 500, display: 'block', marginBottom: 8 }}>Rectangle</span>
                  <Skeleton variant="rectangle" height={80} />
                </div>
              </div>
            </div>
          </div>
          <div className="subsection">
            <h3>Card Skeleton</h3>
            <div className="cards-grid">
              <SkeletonCard />
              <SkeletonCard />
            </div>
          </div>
        </section>

        {/* Alerts Section */}
        <section className="section">
          <div className="section-header">
            <h2>Alerts</h2>
            <Badge variant="warning" rounded>Feedback</Badge>
          </div>
          <p className="section-desc">Contextual feedback messages with icons, titles, and dismiss functionality.</p>
          <Alert type="info" title="Information">
            This is an informational alert with a title and description.
          </Alert>
          <Alert type="success" title="Success!">
            Your changes have been saved successfully.
          </Alert>
          <Alert type="warning" title="Warning">
            Please review your settings before proceeding.
          </Alert>
          <Alert type="danger" title="Error" dismissible onClose={() => {}}>
            Something went wrong. This alert can be dismissed.
          </Alert>
        </section>

        {/* Modal Section */}
        <section className="section">
          <div className="section-header">
            <h2>Modal</h2>
            <Badge variant="primary" rounded>Overlay</Badge>
          </div>
          <p className="section-desc">Dialog overlay with backdrop blur, keyboard support (Escape to close), and configurable sizes.</p>
          <div className="component-showcase">
            <Button onClick={() => setIsModalOpen(true)}>Open Modal</Button>
          </div>

          <Modal
            isOpen={isModalOpen}
            onClose={() => setIsModalOpen(false)}
            title="Getting Started"
            footer={
              <>
                <Button variant="secondary" outline onClick={() => setIsModalOpen(false)}>
                  Cancel
                </Button>
                <Button
                  variant="primary"
                  onClick={() => {
                    setIsModalOpen(false);
                  }}
                >
                  Got It
                </Button>
              </>
            }
          >
            <p>Welcome to the React Component Library! Here's how to get started:</p>
            <ol style={{ paddingLeft: 20, lineHeight: 2 }}>
              <li>Import components from the <code>./components</code> directory</li>
              <li>Use props to customize appearance and behavior</li>
              <li>Compose components together to build complex UIs</li>
            </ol>
            <Alert type="info">
              Press <strong>Escape</strong> or click outside to close this modal.
            </Alert>
          </Modal>
        </section>

        {/* Spinners Section */}
        <section className="section">
          <div className="section-header">
            <h2>Spinners</h2>
            <Badge variant="secondary" rounded>Loading</Badge>
          </div>
          <p className="section-desc">Loading indicators with multiple sizes, colors, and optional labels.</p>
          <div className="component-showcase">
            <Spinner size="small" color="primary" />
            <Spinner size="medium" color="success" />
            <Spinner size="large" color="danger" />
          </div>
          <Spinner centered color="primary" label="Loading content..." />
        </section>
      </main>

      <footer className="App-footer">
        <p>React Component Library &mdash; 18 Reusable Components</p>
        <p style={{ fontSize: 12, opacity: 0.7, marginTop: 4 }}>Built with React</p>
      </footer>
    </div>
  );
}

export default App;
