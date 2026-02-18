import { Task, TaskStatus } from '../types/task';

/**
 * Updates task status based on its state and followup tasks
 * When followup tasks start, the parent task status should restart from completed
 */
export function updateTaskStatus(task: Task): TaskStatus {
  // If task has followup tasks that are starting or in progress
  if (task.followupTasks && task.followupTasks.length > 0) {
    const hasActiveFollowups = task.followupTasks.some(
      ft => ft.status === TaskStatus.IN_PROGRESS || ft.status === TaskStatus.PENDING
    );
    
    // If followup tasks are active, parent should not stay completed
    if (hasActiveFollowups && task.status === TaskStatus.COMPLETED) {
      return TaskStatus.IN_PROGRESS;
    }
    
    // Check if any followup is in progress
    const followupInProgress = task.followupTasks.some(
      ft => ft.status === TaskStatus.IN_PROGRESS
    );
    
    if (followupInProgress) {
      return TaskStatus.IN_PROGRESS;
    }
  }
  
  // If task has agents that are active
  const hasActiveAgents = task.agents.some(
    agent => agent.status === 'active' || agent.status === 'paused'
  );
  
  if (hasActiveAgents && task.status === TaskStatus.COMPLETED) {
    return TaskStatus.IN_PROGRESS;
  }
  
  return task.status;
}

/**
 * Determines if a task should show as in progress when it has active followups
 */
export function shouldRestartStatusForFollowups(task: Task): boolean {
  if (!task.followupTasks || task.followupTasks.length === 0) {
    return false;
  }
  
  // If main task is completed but followups are starting
  const followupStarting = task.followupTasks.some(
    ft => ft.status === TaskStatus.PENDING || ft.status === TaskStatus.IN_PROGRESS
  );
  
  return task.status === TaskStatus.COMPLETED && followupStarting;
}
