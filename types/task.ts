export type TaskStatus = 'pending' | 'in-progress' | 'completed' | 'stopped' | 'failed';

export type AgentType = 'research' | 'analysis' | 'execution' | 'validation';

export interface Agent {
  id: string;
  type: AgentType;
  name: string;
  status: 'idle' | 'running' | 'stopped' | 'completed' | 'failed';
  progress?: number;
}

export interface FollowUpTask {
  id: string;
  parentTaskId: string;
  title: string;
  description: string;
  status: TaskStatus;
  agents: Agent[];
  stoppedAgents: Agent[];
  createdAt: Date;
  startedAt?: Date;
  completedAt?: Date;
}

export interface Task {
  id: string;
  title: string;
  description: string;
  status: TaskStatus;
  agents: Agent[];
  stoppedAgents: Agent[];
  followUpTasks: FollowUpTask[];
  createdAt: Date;
  startedAt?: Date;
  completedAt?: Date;
}
