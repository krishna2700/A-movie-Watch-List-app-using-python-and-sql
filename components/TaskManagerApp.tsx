import React from 'react';
import { useTaskStatus } from '../hooks/useTaskStatus';
import { TaskCard } from './tasks/TaskCard';
import { Task, FollowUpTask, Agent } from '../types/task';

/**
 * Main Application Component
 * Demonstrates all the fixes for follow-up task status and agent display
 */
export const TaskManagerApp: React.FC = () => {
  const {
    tasks,
    setTasks,
    startFollowUpTask,
    pauseFollowUpTaskAgents,
    completeFollowUpTask,
    addFollowUpTask
  } = useTaskStatus();

  // Start or resume a main task
  const handleStartTask = (taskId: string) => {
    setTasks(prevTasks =>
      prevTasks.map(task => {
        if (task.id === taskId) {
          return {
            ...task,
            status: 'in-progress' as const,
            startedAt: task.startedAt || new Date(),
            agents: task.agents.map(agent => ({
              ...agent,
              status: 'running' as const
            }))
          };
        }
        return task;
      })
    );
  };

  // Pause selected agents in main task
  const handlePauseTaskAgents = (taskId: string, agentIds: string[]) => {
    setTasks(prevTasks =>
      prevTasks.map(task => {
        if (task.id === taskId) {
          const stoppedAgents: Agent[] = [];
          const runningAgents: Agent[] = [];

          task.agents.forEach(agent => {
            if (agentIds.includes(agent.id)) {
              stoppedAgents.push({
                ...agent,
                status: 'stopped' as const
              });
            } else {
              runningAgents.push(agent);
            }
          });

          const newStatus = runningAgents.length === 0 ? 'stopped' : 'in-progress';

          return {
            ...task,
            status: newStatus as const,
            agents: runningAgents,
            stoppedAgents: [...task.stoppedAgents, ...stoppedAgents]
          };
        }
        return task;
      })
    );
  };

  // Complete a main task
  const handleCompleteTask = (taskId: string) => {
    setTasks(prevTasks =>
      prevTasks.map(task => {
        if (task.id === taskId) {
          return {
            ...task,
            status: 'completed' as const,
            completedAt: new Date(),
            agents: task.agents.map(agent => ({
              ...agent,
              status: 'completed' as const
            }))
          };
        }
        return task;
      })
    );
  };

  // Add a new follow-up task
  const handleAddFollowUpTask = (taskId: string) => {
    const newFollowUpTask: Omit<FollowUpTask, 'parentTaskId'> = {
      id: `fut-${Date.now()}`,
      title: 'New Follow-up Task',
      description: 'Additional work based on completed task',
      status: 'pending',
      agents: [
        {
          id: `agent-${Date.now()}-1`,
          type: 'research',
          name: 'Research Agent',
          status: 'idle'
        },
        {
          id: `agent-${Date.now()}-2`,
          type: 'execution',
          name: 'Execution Agent',
          status: 'idle'
        }
      ],
      stoppedAgents: [],
      createdAt: new Date()
    };

    addFollowUpTask(taskId, newFollowUpTask);
  };

  // Initialize with sample data
  React.useEffect(() => {
    if (tasks.length === 0) {
      const sampleTask: Task = {
        id: 'task-1',
        title: 'Main Task: Data Analysis',
        description: 'Analyze customer data and generate insights',
        status: 'completed',
        agents: [],
        stoppedAgents: [],
        followUpTasks: [
          {
            id: 'fut-1',
            parentTaskId: 'task-1',
            title: 'Follow-up: Generate Report',
            description: 'Create detailed report from analysis',
            status: 'completed', // This demonstrates the bug - stays completed even when restarted
            agents: [
              {
                id: 'agent-fut-1-1',
                type: 'analysis',
                name: 'Analysis Agent',
                status: 'completed'
              },
              {
                id: 'agent-fut-1-2',
                type: 'validation',
                name: 'Validation Agent',
                status: 'completed'
              }
            ],
            stoppedAgents: [],
            createdAt: new Date(Date.now() - 3600000),
            startedAt: new Date(Date.now() - 3000000),
            completedAt: new Date(Date.now() - 1800000)
          }
        ],
        createdAt: new Date(Date.now() - 7200000),
        startedAt: new Date(Date.now() - 6000000),
        completedAt: new Date(Date.now() - 3600000)
      };

      const activeTask: Task = {
        id: 'task-2',
        title: 'Main Task: System Integration',
        description: 'Integrate new payment system',
        status: 'in-progress',
        agents: [
          {
            id: 'agent-2-1',
            type: 'research',
            name: 'API Research',
            status: 'running',
            progress: 45
          },
          {
            id: 'agent-2-2',
            type: 'execution',
            name: 'Integration',
            status: 'running',
            progress: 30
          },
          {
            id: 'agent-2-3',
            type: 'validation',
            name: 'Testing',
            status: 'running',
            progress: 15
          }
        ],
        stoppedAgents: [],
        followUpTasks: [],
        createdAt: new Date(Date.now() - 1800000),
        startedAt: new Date(Date.now() - 900000)
      };

      setTasks([sampleTask, activeTask]);
    }
  }, [tasks.length, setTasks]);

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '24px' }}>
      <header style={{ marginBottom: '32px' }}>
        <h1 style={{ fontSize: '32px', fontWeight: '700', margin: '0 0 8px 0' }}>
          Task Manager with Multi-Agent Support
        </h1>
        <p style={{ fontSize: '16px', color: '#6b7280', margin: '0' }}>
          Demonstrating fixes for follow-up task status and agent display issues
        </p>
      </header>

      <div style={{ marginBottom: '24px', padding: '16px', backgroundColor: '#eff6ff', borderRadius: '8px', border: '1px solid #bfdbfe' }}>
        <h3 style={{ margin: '0 0 8px 0', fontSize: '16px', fontWeight: '600', color: '#1e40af' }}>
          ✨ Implemented Fixes:
        </h3>
        <ul style={{ margin: '0', paddingLeft: '24px', color: '#1e3a8a', fontSize: '14px' }}>
          <li>Follow-up task status resets to "In Progress" when started (not stuck on "Completed")</li>
          <li>Selective agent pause - choose which agents to stop instead of stopping all</li>
          <li>Stopped agents show with "Stopped" status and display up to 2 agent icons</li>
          <li>Same multi-agent icon logic for both main and follow-up tasks</li>
          <li>Clear visibility of which agents are in progress</li>
        </ul>
      </div>

      <div>
        {tasks.map(task => (
          <TaskCard
            key={task.id}
            task={task}
            onStart={handleStartTask}
            onPauseAgents={handlePauseTaskAgents}
            onComplete={handleCompleteTask}
            onStartFollowUpTask={startFollowUpTask}
            onPauseFollowUpTaskAgents={pauseFollowUpTaskAgents}
            onCompleteFollowUpTask={completeFollowUpTask}
            onAddFollowUpTask={handleAddFollowUpTask}
          />
        ))}
      </div>

      {tasks.length === 0 && (
        <div style={{ textAlign: 'center', padding: '48px', color: '#9ca3af' }}>
          No tasks available. The app will initialize with sample data.
        </div>
      )}
    </div>
  );
};

export default TaskManagerApp;
