export enum TaskStatus {
  PENDING = 'pending',
  IN_PROGRESS = 'in_progress',
  COMPLETED = 'completed',
  STOPPED = 'stopped',
  PAUSED = 'paused'
}

export enum AgentStatus {
  ACTIVE = 'active',
  PAUSED = 'paused',
  STOPPED = 'stopped',
  COMPLETED = 'completed'
}

export interface Agent {
  id: string;
  name: string;
  status: AgentStatus;
  icon?: string;
}

export interface Task {
  id: string;
  title: string;
  status: TaskStatus;
  agents: Agent[];
  followupTasks?: Task[];
  parentTaskId?: string;
  isMainTask: boolean;
  createdAt: Date;
  updatedAt: Date;
}
