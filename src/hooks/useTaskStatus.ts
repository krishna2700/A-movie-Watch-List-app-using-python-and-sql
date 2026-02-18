import { useState, useEffect, useCallback } from 'react';
import { Task, TaskStatus, AgentStatus } from '../types/task';
import { updateTaskStatus } from '../utils/taskStatus';

export function useTaskStatus(initialTask: Task) {
  const [task, setTask] = useState<Task>(initialTask);
  const [computedStatus, setComputedStatus] = useState<TaskStatus>(initialTask.status);
  
  // Recalculate status when task or followup tasks change
  useEffect(() => {
    const newStatus = updateTaskStatus(task);
    setComputedStatus(newStatus);
    
    // If followup tasks start and main task is completed, update status
    if (task.followupTasks && task.followupTasks.length > 0) {
      const hasActiveFollowups = task.followupTasks.some(
        ft => ft.status === TaskStatus.IN_PROGRESS || ft.status === TaskStatus.PENDING
      );
      
      if (hasActiveFollowups && task.status === TaskStatus.COMPLETED) {
        setTask(prev => ({
          ...prev,
          status: TaskStatus.IN_PROGRESS,
          updatedAt: new Date()
        }));
      }
    }
  }, [task, task.followupTasks, task.status]);
  
  const pauseAgents = useCallback((agentIds: string[]) => {
    setTask(prev => ({
      ...prev,
      agents: prev.agents.map(agent =>
        agentIds.includes(agent.id)
          ? { ...agent, status: AgentStatus.STOPPED }
          : agent
      ),
      updatedAt: new Date()
    }));
    
    // Update task status if all agents are stopped
    setTask(prev => {
      const allStopped = prev.agents.every(
        agent => agent.status === AgentStatus.STOPPED || agentIds.includes(agent.id)
      );
      
      if (allStopped && prev.status === TaskStatus.IN_PROGRESS) {
        return {
          ...prev,
          status: TaskStatus.STOPPED,
          updatedAt: new Date()
        };
      }
      
      return prev;
    });
  }, []);
  
  const resumeAgents = useCallback((agentIds: string[]) => {
    setTask(prev => ({
      ...prev,
      agents: prev.agents.map(agent =>
        agentIds.includes(agent.id)
          ? { ...agent, status: AgentStatus.ACTIVE }
          : agent
      ),
      updatedAt: new Date()
    }));
    
    // Update task status if agents resume
    setTask(prev => {
      const hasActiveAgents = prev.agents.some(
        agent => agent.status === AgentStatus.ACTIVE || agentIds.includes(agent.id)
      );
      
      if (hasActiveAgents && prev.status === TaskStatus.STOPPED) {
        return {
          ...prev,
          status: TaskStatus.IN_PROGRESS,
          updatedAt: new Date()
        };
      }
      
      return prev;
    });
  }, []);
  
  const startFollowupTasks = useCallback((followupTasks: Task[]) => {
    setTask(prev => ({
      ...prev,
      followupTasks: followupTasks.map(ft => ({
        ...ft,
        status: TaskStatus.IN_PROGRESS,
        updatedAt: new Date()
      })),
      // Reset status from completed to in_progress when followups start
      status: prev.status === TaskStatus.COMPLETED 
        ? TaskStatus.IN_PROGRESS 
        : prev.status,
      updatedAt: new Date()
    }));
  }, []);
  
  return {
    task,
    computedStatus,
    pauseAgents,
    resumeAgents,
    startFollowupTasks,
    setTask
  };
}
