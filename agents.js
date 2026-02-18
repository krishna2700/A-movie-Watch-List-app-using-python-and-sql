// Multi-Agent System
class Agent {
    constructor(id, name) {
        this.id = id;
        this.name = name;
        this.status = 'Ready';
    }

    log(message) {
        console.log(`[${this.name}] ${message}`);
    }

    activate() {
        this.status = 'Active';
        this.updateUI();
        this.log('Agent activated');
    }

    deactivate() {
        this.status = 'Ready';
        this.updateUI();
        this.log('Agent deactivated');
    }

    updateUI() {
        const agentElement = document.getElementById(this.id);
        if (agentElement) {
            const statusElement = agentElement.querySelector('.status');
            if (statusElement) {
                statusElement.textContent = this.status;
                statusElement.style.color = this.status === 'Active' ? '#007bff' : '#28a745';
            }
        }
    }
}

// Initialize agents
const agent1 = new Agent('agent1', 'Agent 1');
const agent2 = new Agent('agent2', 'Agent 2');
const agent3 = new Agent('agent3', 'Agent 3');

const agents = [agent1, agent2, agent3];

// Handle button click
function handleClick() {
    console.log('hello');
    
    // Activate all agents
    agents.forEach((agent, index) => {
        setTimeout(() => {
            agent.activate();
            agent.log('Processing click event');
        }, index * 200);
    });

    // Deactivate agents after animation
    setTimeout(() => {
        agents.forEach((agent) => {
            agent.deactivate();
        });
    }, 2000);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('Multi-Agent System Initialized');
    agents.forEach(agent => {
        agent.log('System ready');
    });
});
