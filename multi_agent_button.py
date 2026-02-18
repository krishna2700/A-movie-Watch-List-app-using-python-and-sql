"""
Multi-Agent Blue Button Application
====================================
A multi-agent system where clicking a blue button prints "hello" to the console.

Agents:
  - UIAgent:          Builds the tkinter GUI with a blue button
  - ClickAgent:       Handles button-click events and dispatches messages
  - OutputAgent:      Receives messages and prints output to the console
  - AgentCoordinator: Orchestrates message passing between agents
"""

import queue

try:
    import tkinter as tk
except ImportError:
    tk = None  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# Message protocol
# ---------------------------------------------------------------------------
class Message:
    """Simple message object passed between agents."""

    def __init__(self, sender: str, action: str, payload: str = ""):
        self.sender = sender
        self.action = action
        self.payload = payload

    def __repr__(self):
        return f"Message(sender={self.sender!r}, action={self.action!r}, payload={self.payload!r})"


# ---------------------------------------------------------------------------
# Agent base class
# ---------------------------------------------------------------------------
class BaseAgent:
    """Base class every agent inherits from."""

    def __init__(self, name: str, coordinator: "AgentCoordinator"):
        self.name = name
        self.coordinator = coordinator

    def handle(self, message: Message):
        raise NotImplementedError


# ---------------------------------------------------------------------------
# OutputAgent – prints to the console
# ---------------------------------------------------------------------------
class OutputAgent(BaseAgent):
    """Receives a 'print' action and writes the payload to the console."""

    def handle(self, message: Message):
        if message.action == "print":
            print(message.payload)


# ---------------------------------------------------------------------------
# ClickAgent – processes click events
# ---------------------------------------------------------------------------
class ClickAgent(BaseAgent):
    """Translates a 'button_clicked' event into a 'print' command for OutputAgent."""

    def handle(self, message: Message):
        if message.action == "button_clicked":
            self.coordinator.send(
                Message(sender=self.name, action="print", payload="hello"),
                recipient="OutputAgent",
            )


# ---------------------------------------------------------------------------
# UIAgent – builds the GUI
# ---------------------------------------------------------------------------
class UIAgent(BaseAgent):
    """Creates the tkinter window and the blue button."""

    def __init__(self, name: str, coordinator: "AgentCoordinator"):
        super().__init__(name, coordinator)
        self.root: tk.Tk | None = None

    def build(self):
        if tk is None:
            print("[UIAgent] tkinter not available – running in headless/CLI mode.")
            print("[UIAgent] Simulating blue-button click …")
            self._on_click()
            return

        self.root = tk.Tk()
        self.root.title("Multi-Agent Button")
        self.root.geometry("320x200")
        self.root.configure(bg="#f0f4f8")

        button = tk.Button(
            self.root,
            text="Click Me",
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            font=("Helvetica", 14, "bold"),
            padx=24,
            pady=10,
            relief="flat",
            cursor="hand2",
            command=self._on_click,
        )
        button.pack(expand=True)

        self.root.mainloop()

    def _on_click(self):
        self.coordinator.send(
            Message(sender=self.name, action="button_clicked"),
            recipient="ClickAgent",
        )

    def handle(self, message: Message):
        pass  # UIAgent doesn't receive messages in this flow


# ---------------------------------------------------------------------------
# AgentCoordinator – message router
# ---------------------------------------------------------------------------
class AgentCoordinator:
    """Central hub that routes messages between registered agents."""

    def __init__(self):
        self._agents: dict[str, BaseAgent] = {}
        self._queue: queue.Queue[tuple[str, Message]] = queue.Queue()

    def register(self, agent: BaseAgent):
        self._agents[agent.name] = agent

    def send(self, message: Message, recipient: str):
        """Deliver a message to the named recipient agent immediately."""
        agent = self._agents.get(recipient)
        if agent:
            agent.handle(message)
        else:
            print(f"[Coordinator] Unknown recipient: {recipient}")


# ---------------------------------------------------------------------------
# Bootstrap
# ---------------------------------------------------------------------------
def main():
    coordinator = AgentCoordinator()

    ui_agent = UIAgent("UIAgent", coordinator)
    click_agent = ClickAgent("ClickAgent", coordinator)
    output_agent = OutputAgent("OutputAgent", coordinator)

    coordinator.register(ui_agent)
    coordinator.register(click_agent)
    coordinator.register(output_agent)

    # Launch the GUI (blocking call)
    ui_agent.build()


if __name__ == "__main__":
    main()
