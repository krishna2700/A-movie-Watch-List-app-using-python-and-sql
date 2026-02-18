import React, { useState } from 'react';
import { Task, TaskStatus, AgentStatus } from './types/task';
import { TaskCard } from './components/TaskCard';

function App() {
  const [tasks, setTasks] = useState<Task[]>([
    {
      id: '1',
      title: 'Main Task Example',
      status: TaskStatus.COMPLETED,
      isMainTask: true,
      agents: [
        { id: 'a1', name: 'Agent 1', status: AgentStatus.COMPLETED },
        { id: 'a2', name: 'Agent 2', status: AgentStatus.COMPLETED }
      ],
      followupTasks: [
        {
          id: 'f1',
          title: 'Followup Task 1',
          status: TaskStatus.IN_PROGRESS,
          isMainTask: false,
          parentTaskId: '1',
          agents: [
            { id: 'a3', name: 'Agent 3', status: AgentStatus.ACTIVE },
            { id: 'a4', name: 'Agent 4', status: AgentStatus.ACTIVE }
          ],
          createdAt: new Date(),
          updatedAt: new Date()
        }
      ],
      createdAt: new Date(),
      updatedAt: new Date()
    }
  ]);
  
  const handleTaskUpdate = (updatedTask: Task) => {
    setTasks(prev => prev.map(t => {
      if (t.id === updatedTask.id) {
        return updatedTask;
      }
      // Also update if it's a followup task
      if (t.followupTasks) {
        const updatedFollowups = t.followupTasks.map(ft =>
          ft.id === updatedTask.id ? updatedTask : ft
        );
        if (updatedFollowups.some(ft => ft.id === updatedTask.id)) {
          return { ...t, followupTasks: updatedFollowups };
        }
      }
      return t;
    }));
  };
  
  return (
    <div className="container mx-auto p-8">
      <h1 className="text-2xl font-bold mb-6">Task Management System</h1>
      
      {tasks.map(task => (
        <TaskCard
          key={task.id}
          task={task}
          onTaskUpdate={handleTaskUpdate}
        />
      ))}
    </div>
  );
}

export default App;
