// Multi-Agent System Implementation

class Agent {
    constructor(name, task) {
        this.name = name;
        this.task = task;
    }

    async execute() {
        console.log(`[Agent: ${this.name}] Executing task: ${this.task}`);
        return await this.task();
    }
}

class MultiAgentSystem {
    constructor() {
        this.agents = [];
        this.consoleOutput = document.getElementById('console-output');
    }

    addAgent(agent) {
        this.agents.push(agent);
    }

    log(message, isAgent = false) {
        console.log(message);
        const logLine = document.createElement('div');
        logLine.className = 'console-line';
        if (isAgent) {
            logLine.innerHTML = `<span class="agent-log">${message}</span>`;
        } else {
            logLine.textContent = message;
        }
        this.consoleOutput.appendChild(logLine);
    }

    async executeAll() {
        this.log('=== Multi-Agent System Activated ===', true);
        
        for (const agent of this.agents) {
            try {
                await agent.execute();
            } catch (error) {
                console.error(`Agent ${agent.name} failed:`, error);
                this.log(`❌ Agent ${agent.name} failed: ${error.message}`);
            }
        }
        
        this.log('=== All Agents Completed ===', true);
    }
}

// Initialize Multi-Agent System
const multiAgentSystem = new MultiAgentSystem();

// Define agents
const consoleAgent = new Agent('ConsoleAgent', async () => {
    multiAgentSystem.log('[ConsoleAgent] Logging message...', true);
    console.log('hello');
    multiAgentSystem.log('✓ Logged: "hello"');
    return 'hello';
});

const apiAgent = new Agent('APIAgent', async () => {
    multiAgentSystem.log('[APIAgent] Calling backend...', true);
    try {
        const response = await fetch('/api/agent/hello', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const data = await response.json();
        multiAgentSystem.log(`✓ Backend response: ${data.message}`);
        return data;
    } catch (error) {
        multiAgentSystem.log(`⚠ Backend not available (running in standalone mode)`);
        return null;
    }
});

const displayAgent = new Agent('DisplayAgent', async () => {
    multiAgentSystem.log('[DisplayAgent] Updating UI...', true);
    multiAgentSystem.log('✓ UI updated successfully');
    return true;
});

// Add agents to the system
multiAgentSystem.addAgent(consoleAgent);
multiAgentSystem.addAgent(apiAgent);
multiAgentSystem.addAgent(displayAgent);

// Button click handler
document.getElementById('multiAgentButton').addEventListener('click', async () => {
    console.log('hello');
    await multiAgentSystem.executeAll();
});

// Initial log
multiAgentSystem.log('Multi-Agent System Ready. Click the button to activate.', true);
