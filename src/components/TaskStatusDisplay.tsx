import React from 'react';
import { Task, TaskStatus, AgentStatus } from '../types/task';
import { updateTaskStatus } from '../utils/taskStatus';
import { AgentIcons } from './AgentIcons';

interface TaskStatusDisplayProps {
  task: Task;
  onPauseAgents?: (agentIds: string[]) => void;
  onResumeAgents?: (agentIds: string[]) => void;
}

export const TaskStatusDisplay: React.FC<TaskStatusDisplayProps> = ({
  task,
  onPauseAgents,
  onResumeAgents
}) => {
  // Calculate the actual status considering followup tasks
  const actualStatus = updateTaskStatus(task);
  
  // Get agents that are stopped/paused
  const stoppedAgents = task.agents.filter(
    agent => agent.status === AgentStatus.STOPPED || agent.status === AgentStatus.PAUSED
  );
  
  // Get active agents (for pause selection)
  const activeAgents = task.agents.filter(
    agent => agent.status === AgentStatus.ACTIVE
  );
  
  const getStatusLabel = (status: TaskStatus): string => {
    switch (status) {
      case TaskStatus.IN_PROGRESS:
        return 'In Progress';
      case TaskStatus.COMPLETED:
        return 'Completed';
      case TaskStatus.STOPPED:
        return 'Stopped';
      case TaskStatus.PAUSED:
        return 'Paused';
      default:
        return 'Pending';
    }
  };
  
  const getStatusColor = (status: TaskStatus): string => {
    switch (status) {
      case TaskStatus.IN_PROGRESS:
        return 'text-blue-600';
      case TaskStatus.COMPLETED:
        return 'text-green-600';
      case TaskStatus.STOPPED:
        return 'text-red-600';
      case TaskStatus.PAUSED:
        return 'text-yellow-600';
      default:
        return 'text-gray-600';
    }
  };
  
  return (
    <div className="task-status-display">
      <div className="flex items-center gap-2">
        <span className={`font-semibold ${getStatusColor(actualStatus)}`}>
          {getStatusLabel(actualStatus)}
        </span>
        
        {/* Show agent icons - same logic for main and followup tasks */}
        {task.agents.length > 0 && (
          <div className="flex items-center gap-2">
            <AgentIcons
              agents={task.agents}
              taskStatus={actualStatus}
              onPauseAgents={onPauseAgents ? (agentIds) => onPauseAgents(agentIds) : undefined}
              activeAgents={activeAgents}
            />
            {/* Show active agents info when in progress */}
            {actualStatus === TaskStatus.IN_PROGRESS && activeAgents.length > 0 && (
              <span className="text-sm text-gray-600">
                ({activeAgents.length} active)
              </span>
            )}
          </div>
        )}
        
        {/* Show stopped agents count if any */}
        {stoppedAgents.length > 0 && (
          <div className="flex items-center gap-1 text-red-600">
            <span className="text-sm">Stopped:</span>
            <AgentIcons
              agents={stoppedAgents}
              taskStatus={TaskStatus.STOPPED}
              showStatus={true}
            />
          </div>
        )}
      </div>
      
      {/* Show followup tasks status if applicable */}
      {task.followupTasks && task.followupTasks.length > 0 && (
        <div className="mt-2 ml-4">
          <div className="text-sm text-gray-600">Followup Tasks:</div>
          {task.followupTasks.map(followup => (
            <TaskStatusDisplay
              key={followup.id}
              task={followup}
              onPauseAgents={onPauseAgents}
              onResumeAgents={onResumeAgents}
            />
          ))}
        </div>
      )}
    </div>
  );
};
