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
  Section
} from './components';

function App() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [showAlert, setShowAlert] = useState(true);
  const [formData, setFormData] = useState({
    name: '',
    email: ''
  });
  const [errors, setErrors] = useState({});

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    
    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: ''
      }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const newErrors = {};
    
    if (!formData.name) {
      newErrors.name = 'Name is required';
    }
    
    if (!formData.email) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = 'Email is invalid';
    }
    
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
    } else {
      alert('Form submitted successfully!');
      setFormData({ name: '', email: '' });
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>React Reusable Components Library</h1>
        <p>A collection of beautiful, reusable React components</p>
      </header>

      <main className="App-main">
        {showAlert && (
          <Alert 
            type="info" 
            dismissible 
            onClose={() => setShowAlert(false)}
          >
            Welcome! This is a demo of reusable React components.
          </Alert>
        )}

        <Section
          title="Buttons"
          description="Choose variants and sizes for any action."
        >
          <div className="component-showcase">
            <Button variant="primary">Primary</Button>
            <Button variant="secondary">Secondary</Button>
            <Button variant="success">Success</Button>
            <Button variant="danger">Danger</Button>
          </div>
          <div className="component-showcase">
            <Button size="small">Small</Button>
            <Button size="medium">Medium</Button>
            <Button size="large">Large</Button>
          </div>
        </Section>

        <Section
          title="Badges"
          description="Add labels that communicate status at a glance."
        >
          <div className="component-showcase">
            <Badge variant="primary">Primary</Badge>
            <Badge variant="secondary">Secondary</Badge>
            <Badge variant="success">Success</Badge>
            <Badge variant="danger">Danger</Badge>
            <Badge variant="warning">Warning</Badge>
            <Badge variant="info">Info</Badge>
          </div>
          <div className="component-showcase">
            <Badge variant="primary" rounded>Rounded</Badge>
            <Badge variant="success" rounded>99+</Badge>
            <Badge variant="danger" rounded>New</Badge>
          </div>
        </Section>

        <Section
          title="Cards"
          description="Group content with consistent padding and elevation."
        >
          <div className="cards-grid">
            <Card
              title="Basic Card"
              subtitle="This is a subtitle"
              hoverable
            >
              <p>This is a basic card component with a title, subtitle, and body content.</p>
            </Card>
            
            <Card 
              title="Card with Footer" 
              hoverable
              footer={
                <div style={{ display: 'flex', gap: '10px' }}>
                  <Button size="small" variant="primary">Action</Button>
                  <Button size="small" variant="secondary">Cancel</Button>
                </div>
              }
            >
              <p>This card includes a footer with action buttons.</p>
            </Card>

            <Card hoverable>
              <h3 style={{ marginTop: 0 }}>No Header Card</h3>
              <p>This card has no header, just body content.</p>
              <Badge variant="success">Featured</Badge>
            </Card>
          </div>
        </Section>

        <Section
          title="Form Components"
          description="Compose accessible forms with reusable inputs."
        >
          <Card title="Sample Form">
            <form onSubmit={handleSubmit}>
              <Input
                label="Name"
                name="name"
                placeholder="Enter your name"
                value={formData.name}
                onChange={handleInputChange}
                error={errors.name}
                required
              />
              
              <Input
                type="email"
                label="Email"
                name="email"
                placeholder="Enter your email"
                value={formData.email}
                onChange={handleInputChange}
                error={errors.email}
                required
              />
              
              <div style={{ display: 'flex', gap: '10px', marginTop: '10px' }}>
                <Button type="submit" variant="primary">Submit</Button>
                <Button 
                  type="button" 
                  variant="secondary"
                  onClick={() => setFormData({ name: '', email: '' })}
                >
                  Reset
                </Button>
              </div>
            </form>
          </Card>
        </Section>

        <Section
          title="Modal"
          description="Display focused dialogs without leaving the page."
        >
          <Button onClick={() => setIsModalOpen(true)}>
            Open Modal
          </Button>
          
          <Modal
            isOpen={isModalOpen}
            onClose={() => setIsModalOpen(false)}
            title="Example Modal"
            footer={
              <>
                <Button 
                  variant="secondary" 
                  onClick={() => setIsModalOpen(false)}
                >
                  Close
                </Button>
                <Button 
                  variant="primary"
                  onClick={() => {
                    alert('Action confirmed!');
                    setIsModalOpen(false);
                  }}
                >
                  Confirm
                </Button>
              </>
            }
          >
            <p>This is a reusable modal component. It can contain any content you want!</p>
            <p>Click outside the modal or press the close button to dismiss it.</p>
          </Modal>
        </Section>

        <Section
          title="Alerts"
          description="Use alert messages to provide immediate feedback."
        >
          <Alert type="success">
            This is a success alert!
          </Alert>
          <Alert type="warning">
            This is a warning alert!
          </Alert>
          <Alert type="danger">
            This is a danger alert!
          </Alert>
        </Section>

        <Section
          title="Spinners"
          description="Show progress indicators while content loads."
        >
          <div className="component-showcase">
            <Spinner size="small" color="primary" />
            <Spinner size="medium" color="success" />
            <Spinner size="large" color="danger" />
          </div>
          <Spinner centered color="primary" />
        </Section>
      </main>

      <footer className="App-footer">
        <p>Built with React - Reusable Components Demo</p>
      </footer>
    </div>
  );
}

export default App;
