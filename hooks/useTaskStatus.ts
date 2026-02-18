import { useState, useCallback } from 'react';
import { Task, FollowUpTask, TaskStatus, Agent } from '../types/task';

export const useTaskStatus = () => {
  const [tasks, setTasks] = useState<Task[]>([]);

  /**
   * Fix 1: Reset follow-up task status when it starts
   * When a follow-up task begins execution, reset status from 'completed' to 'in-progress'
   */
  const startFollowUpTask = useCallback((taskId: string, followUpTaskId: string) => {
    setTasks(prevTasks => 
      prevTasks.map(task => {
        if (task.id === taskId) {
          return {
            ...task,
            followUpTasks: task.followUpTasks.map(fut => {
              if (fut.id === followUpTaskId) {
                return {
                  ...fut,
                  status: 'in-progress' as TaskStatus,
                  startedAt: new Date(),
                  // Reset agents to running status
                  agents: fut.agents.map(agent => ({
                    ...agent,
                    status: 'running' as const
                  })),
                  stoppedAgents: [] // Clear stopped agents when restarting
                };
              }
              return fut;
            })
          };
        }
        return task;
      })
    );
  }, []);

  /**
   * Fix 2: Selective agent pause for follow-up tasks
   * Allow pausing individual agents instead of all agents
   */
  const pauseFollowUpTaskAgents = useCallback(
    (taskId: string, followUpTaskId: string, agentIds: string[]) => {
      setTasks(prevTasks =>
        prevTasks.map(task => {
          if (task.id === taskId) {
            return {
              ...task,
              followUpTasks: task.followUpTasks.map(fut => {
                if (fut.id === followUpTaskId) {
                  const stoppedAgents: Agent[] = [];
                  const runningAgents: Agent[] = [];

                  fut.agents.forEach(agent => {
                    if (agentIds.includes(agent.id)) {
                      stoppedAgents.push({
                        ...agent,
                        status: 'stopped' as const
                      });
                    } else {
                      runningAgents.push(agent);
                    }
                  });

                  // Determine overall task status
                  let newStatus: TaskStatus = fut.status;
                  if (runningAgents.length === 0 && stoppedAgents.length > 0) {
                    // All agents stopped
                    newStatus = 'stopped';
                  } else if (runningAgents.some(a => a.status === 'running')) {
                    // Some agents still running
                    newStatus = 'in-progress';
                  }

                  return {
                    ...fut,
                    status: newStatus,
                    agents: runningAgents,
                    stoppedAgents: [...fut.stoppedAgents, ...stoppedAgents]
                  };
                }
                return fut;
              })
            };
          }
          return task;
        })
      );
    },
    []
  );

  /**
   * Fix 3: Update agent status for follow-up tasks
   */
  const updateFollowUpTaskAgentStatus = useCallback(
    (taskId: string, followUpTaskId: string, agentId: string, status: Agent['status']) => {
      setTasks(prevTasks =>
        prevTasks.map(task => {
          if (task.id === taskId) {
            return {
              ...task,
              followUpTasks: task.followUpTasks.map(fut => {
                if (fut.id === followUpTaskId) {
                  return {
                    ...fut,
                    agents: fut.agents.map(agent =>
                      agent.id === agentId ? { ...agent, status } : agent
                    )
                  };
                }
                return fut;
              })
            };
          }
          return task;
        })
      );
    },
    []
  );

  /**
   * Complete follow-up task
   */
  const completeFollowUpTask = useCallback(
    (taskId: string, followUpTaskId: string) => {
      setTasks(prevTasks =>
        prevTasks.map(task => {
          if (task.id === taskId) {
            return {
              ...task,
              followUpTasks: task.followUpTasks.map(fut => {
                if (fut.id === followUpTaskId) {
                  return {
                    ...fut,
                    status: 'completed' as TaskStatus,
                    completedAt: new Date(),
                    agents: fut.agents.map(agent => ({
                      ...agent,
                      status: 'completed' as const
                    }))
                  };
                }
                return fut;
              })
            };
          }
          return task;
        })
      );
    },
    []
  );

  /**
   * Add follow-up task to completed main task
   */
  const addFollowUpTask = useCallback(
    (taskId: string, followUpTask: Omit<FollowUpTask, 'parentTaskId'>) => {
      setTasks(prevTasks =>
        prevTasks.map(task => {
          if (task.id === taskId) {
            return {
              ...task,
              followUpTasks: [
                ...task.followUpTasks,
                {
                  ...followUpTask,
                  parentTaskId: taskId,
                  status: 'pending' as TaskStatus, // Start as pending
                  stoppedAgents: []
                }
              ]
            };
          }
          return task;
        })
      );
    },
    []
  );

  return {
    tasks,
    setTasks,
    startFollowUpTask,
    pauseFollowUpTaskAgents,
    updateFollowUpTaskAgentStatus,
    completeFollowUpTask,
    addFollowUpTask
  };
};
