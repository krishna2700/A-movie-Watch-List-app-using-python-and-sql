import React from 'react';
import { Task } from '../types/task';
import { TaskStatusDisplay } from './TaskStatusDisplay';
import { useTaskStatus } from '../hooks/useTaskStatus';

interface TaskCardProps {
  task: Task;
  onTaskUpdate?: (task: Task) => void;
}

export const TaskCard: React.FC<TaskCardProps> = ({ task, onTaskUpdate }) => {
  const { task: currentTask, computedStatus, pauseAgents, resumeAgents, startFollowupTasks } = useTaskStatus(task);
  
  React.useEffect(() => {
    if (onTaskUpdate) {
      onTaskUpdate(currentTask);
    }
  }, [currentTask, onTaskUpdate]);
  
  return (
    <div className="task-card border border-gray-200 rounded-lg p-4 mb-4">
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <h3 className="text-lg font-semibold mb-2">{currentTask.title}</h3>
          <div className="text-sm text-gray-600 mb-2">
            {currentTask.isMainTask ? 'Main Task' : 'Followup Task'}
          </div>
          
          <TaskStatusDisplay
            task={currentTask}
            onPauseAgents={pauseAgents}
            onResumeAgents={resumeAgents}
          />
        </div>
      </div>
      
      {/* Debug info - can be removed in production */}
      {process.env.NODE_ENV === 'development' && (
        <div className="mt-2 text-xs text-gray-400">
          Status: {currentTask.status} → Computed: {computedStatus}
        </div>
      )}
    </div>
  );
};
