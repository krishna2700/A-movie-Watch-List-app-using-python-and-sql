// Multi-Agent System for Blue Button
// Each agent has a specific responsibility

class Agent {
    constructor(name, task) {
        this.name = name;
        this.task = task;
    }

    execute() {
        console.log(`[${this.name}] Executing task: ${this.task}`);
        return this.task();
    }
}

class MultiAgentSystem {
    constructor() {
        this.agents = [];
    }

    addAgent(agent) {
        this.agents.push(agent);
    }

    executeAll() {
        console.log('--- Multi-Agent System Activated ---');
        this.agents.forEach(agent => {
            agent.execute();
        });
        console.log('--- All Agents Completed ---');
    }
}

// Initialize the multi-agent system
const agentSystem = new MultiAgentSystem();

// Agent 1: Logger Agent - Logs "hello"
const loggerAgent = new Agent('Logger Agent', () => {
    console.log('hello');
});

// Agent 2: Timestamp Agent - Logs the current timestamp
const timestampAgent = new Agent('Timestamp Agent', () => {
    console.log(`Timestamp: ${new Date().toISOString()}`);
});

// Agent 3: Counter Agent - Counts button clicks
let clickCount = 0;
const counterAgent = new Agent('Counter Agent', () => {
    clickCount++;
    console.log(`Button clicked ${clickCount} time(s)`);
});

// Add agents to the system
agentSystem.addAgent(loggerAgent);
agentSystem.addAgent(timestampAgent);
agentSystem.addAgent(counterAgent);

// Attach event listener to the button
document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('multiAgentButton');

    button.addEventListener('click', () => {
        agentSystem.executeAll();
    });
});
