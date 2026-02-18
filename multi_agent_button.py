"""
Multi-Agent Blue Button Application (Web-based)

A multi-agent system where:
- UIAgent: Serves the HTML page with a blue button.
- ClickAgent: Handles incoming click events from the browser.
- OutputAgent: Produces the output ("hello" to console).

Each agent operates independently and communicates via a shared message bus.
Run this file and open http://localhost:8000 in your browser.
"""

import threading
import queue
import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class MessageBus:
    """Shared message bus for inter-agent communication."""

    def __init__(self):
        self._queues = {}
        self._lock = threading.Lock()

    def register(self, agent_name):
        with self._lock:
            self._queues[agent_name] = queue.Queue()

    def send(self, target_agent, message):
        with self._lock:
            if target_agent in self._queues:
                self._queues[target_agent].put(message)

    def receive(self, agent_name, timeout=0.1):
        try:
            return self._queues[agent_name].get(timeout=timeout)
        except queue.Empty:
            return None


class BaseAgent(threading.Thread):
    """Base class for all agents."""

    def __init__(self, name, message_bus):
        super().__init__(daemon=True)
        self.agent_name = name
        self.bus = message_bus
        self.bus.register(self.agent_name)
        self.running = True

    def stop(self):
        self.running = False


class OutputAgent(BaseAgent):
    """Agent 3: Responsible for producing console output when it receives a message."""

    def __init__(self, message_bus):
        super().__init__("output_agent", message_bus)

    def run(self):
        while self.running:
            msg = self.bus.receive(self.agent_name)
            if msg and msg.get("action") == "print_hello":
                print("hello")


class ClickAgent(BaseAgent):
    """Agent 2: Handles click events and delegates to OutputAgent."""

    def __init__(self, message_bus):
        super().__init__("click_agent", message_bus)

    def run(self):
        while self.running:
            msg = self.bus.receive(self.agent_name)
            if msg and msg.get("action") == "button_clicked":
                self.bus.send("output_agent", {"action": "print_hello"})


HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multi-Agent Button</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: #1e1e2e;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .container {
            text-align: center;
        }
        h1 {
            color: #cdd6f4;
            margin-bottom: 30px;
            font-size: 1.5rem;
            font-weight: 300;
        }
        button {
            background: #2196F3;
            color: white;
            border: none;
            padding: 16px 48px;
            font-size: 18px;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 15px rgba(33, 150, 243, 0.4);
        }
        button:hover {
            background: #1976D2;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(33, 150, 243, 0.6);
        }
        button:active {
            transform: translateY(0);
            box-shadow: 0 2px 10px rgba(33, 150, 243, 0.3);
        }
        .status {
            color: #a6adc8;
            margin-top: 20px;
            font-size: 0.85rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Multi-Agent System</h1>
        <button onclick="handleClick()">Click Me</button>
        <p class="status" id="status">Agents: ui_agent, click_agent, output_agent</p>
    </div>
    <script>
        async function handleClick() {
            const status = document.getElementById('status');
            try {
                const res = await fetch('/click', { method: 'POST' });
                const data = await res.json();
                status.textContent = data.message;
                console.log("hello");
            } catch (e) {
                status.textContent = 'Error communicating with agents';
            }
        }
    </script>
</body>
</html>
"""


class UIAgent:
    """Agent 1: Serves the web UI and routes click events to ClickAgent."""

    def __init__(self, message_bus, host="0.0.0.0", port=8000):
        self.agent_name = "ui_agent"
        self.bus = message_bus
        self.bus.register(self.agent_name)
        self.host = host
        self.port = port

    def run(self):
        bus = self.bus

        class RequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(HTML_PAGE.encode())

            def do_POST(self):
                if self.path == "/click":
                    bus.send("click_agent", {"action": "button_clicked"})
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    response = json.dumps({
                        "message": "click_agent -> output_agent -> hello printed to console"
                    })
                    self.wfile.write(response.encode())
                else:
                    self.send_response(404)
                    self.end_headers()

            def log_message(self, format, *args):
                pass  # Suppress default HTTP logs

        server = HTTPServer((self.host, self.port), RequestHandler)
        print(f"[ui_agent] Serving on http://{self.host}:{self.port}")
        server.serve_forever()


def main():
    bus = MessageBus()

    output_agent = OutputAgent(bus)
    click_agent = ClickAgent(bus)
    ui_agent = UIAgent(bus)

    output_agent.start()
    click_agent.start()

    print("=" * 45)
    print("  Multi-Agent Blue Button System")
    print("=" * 45)
    print("[output_agent] Started - listens for print requests")
    print("[click_agent]  Started - listens for click events")
    print("-" * 45)

    try:
        ui_agent.run()
    except KeyboardInterrupt:
        print("\nShutting down agents...")
        output_agent.stop()
        click_agent.stop()


if __name__ == "__main__":
    main()
