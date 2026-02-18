import React, { useState } from 'react';
import { Task, Agent } from '../../types/task';
import { MultiAgentIconDisplay, AgentStatusIndicator } from '../AgentIcons';
import { FollowUpTaskCard } from './FollowUpTaskCard';

interface TaskCardProps {
  task: Task;
  onStart: (taskId: string) => void;
  onPauseAgents: (taskId: string, agentIds: string[]) => void;
  onComplete: (taskId: string) => void;
  onStartFollowUpTask: (taskId: string, followUpTaskId: string) => void;
  onPauseFollowUpTaskAgents: (taskId: string, followUpTaskId: string, agentIds: string[]) => void;
  onCompleteFollowUpTask: (taskId: string, followUpTaskId: string) => void;
  onAddFollowUpTask?: (taskId: string) => void;
}

/**
 * Main task card component with multi-agent support
 */
export const TaskCard: React.FC<TaskCardProps> = ({
  task,
  onStart,
  onPauseAgents,
  onComplete,
  onStartFollowUpTask,
  onPauseFollowUpTaskAgents,
  onCompleteFollowUpTask,
  onAddFollowUpTask
}) => {
  const [selectedAgents, setSelectedAgents] = useState<Set<string>>(new Set());
  const [showAgentSelector, setShowAgentSelector] = useState(false);

  const handleAgentToggle = (agentId: string) => {
    setSelectedAgents(prev => {
      const newSet = new Set(prev);
      if (newSet.has(agentId)) {
        newSet.delete(agentId);
      } else {
        newSet.add(agentId);
      }
      return newSet;
    });
  };

  const handlePauseSelectedAgents = () => {
    if (selectedAgents.size > 0) {
      onPauseAgents(task.id, Array.from(selectedAgents));
      setSelectedAgents(new Set());
      setShowAgentSelector(false);
    }
  };

  const getStatusColor = (status: Task['status']) => {
    switch (status) {
      case 'pending':
        return '#6b7280';
      case 'in-progress':
        return '#3b82f6';
      case 'completed':
        return '#10b981';
      case 'stopped':
        return '#ef4444';
      case 'failed':
        return '#dc2626';
      default:
        return '#6b7280';
    }
  };

  const getStatusLabel = (status: Task['status']) => {
    switch (status) {
      case 'in-progress':
        return 'In Progress';
      case 'stopped':
        return 'Stopped';
      default:
        return status.charAt(0).toUpperCase() + status.slice(1);
    }
  };

  const runningAgents = task.agents.filter(a => a.status === 'running');
  const hasRunningAgents = runningAgents.length > 0;

  return (
    <div
      style={{
        border: '2px solid #e5e7eb',
        borderRadius: '12px',
        padding: '20px',
        marginBottom: '16px',
        backgroundColor: 'white',
        boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)'
      }}
    >
      {/* Main Task Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div style={{ flex: 1 }}>
          <h3 style={{ margin: '0 0 8px 0', fontSize: '18px', fontWeight: '600' }}>
            {task.title}
          </h3>
          <p style={{ margin: '0', fontSize: '14px', color: '#6b7280' }}>
            {task.description}
          </p>
        </div>

        {/* Status Badge */}
        <div
          style={{
            padding: '6px 16px',
            borderRadius: '16px',
            backgroundColor: getStatusColor(task.status) + '20',
            border: `2px solid ${getStatusColor(task.status)}50`,
            fontSize: '14px',
            fontWeight: '600',
            color: getStatusColor(task.status),
            whiteSpace: 'nowrap',
            marginLeft: '16px'
          }}
        >
          {getStatusLabel(task.status)}
        </div>
      </div>

      {/* Agent Display */}
      <div style={{ marginTop: '16px' }}>
        <MultiAgentIconDisplay
          agents={task.agents}
          stoppedAgents={task.stoppedAgents}
          maxDisplay={3}
          showStatus={true}
        />
      </div>

      {/* Agent Status Indicator */}
      <AgentStatusIndicator
        agents={task.agents}
        stoppedAgents={task.stoppedAgents}
      />

      {/* Action Buttons */}
      <div style={{ marginTop: '16px', display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
        {task.status === 'pending' && (
          <button
            onClick={() => onStart(task.id)}
            style={{
              padding: '8px 16px',
              borderRadius: '8px',
              border: '1px solid #3b82f6',
              backgroundColor: '#3b82f6',
              color: 'white',
              cursor: 'pointer',
              fontSize: '14px',
              fontWeight: '600'
            }}
          >
            Start Task
          </button>
        )}

        {task.status === 'in-progress' && hasRunningAgents && (
          <>
            <button
              onClick={() => setShowAgentSelector(!showAgentSelector)}
              style={{
                padding: '8px 16px',
                borderRadius: '8px',
                border: '1px solid #f59e0b',
                backgroundColor: 'white',
                color: '#f59e0b',
                cursor: 'pointer',
                fontSize: '14px',
                fontWeight: '600',
                display: 'flex',
                alignItems: 'center',
                gap: '6px'
              }}
            >
              <span>⏸️</span>
              Pause Agents
            </button>

            <button
              onClick={() => onComplete(task.id)}
              style={{
                padding: '8px 16px',
                borderRadius: '8px',
                border: '1px solid #10b981',
                backgroundColor: '#10b981',
                color: 'white',
                cursor: 'pointer',
                fontSize: '14px',
                fontWeight: '600'
              }}
            >
              Complete Task
            </button>
          </>
        )}

        {task.status === 'stopped' && (
          <button
            onClick={() => onStart(task.id)}
            style={{
              padding: '8px 16px',
              borderRadius: '8px',
              border: '1px solid #3b82f6',
              backgroundColor: '#3b82f6',
              color: 'white',
              cursor: 'pointer',
              fontSize: '14px',
              fontWeight: '600'
            }}
          >
            Resume Task
          </button>
        )}

        {task.status === 'completed' && onAddFollowUpTask && (
          <button
            onClick={() => onAddFollowUpTask(task.id)}
            style={{
              padding: '8px 16px',
              borderRadius: '8px',
              border: '1px solid #8b5cf6',
              backgroundColor: 'white',
              color: '#8b5cf6',
              cursor: 'pointer',
              fontSize: '14px',
              fontWeight: '600'
            }}
          >
            + Add Follow-up Task
          </button>
        )}
      </div>

      {/* Agent Selector for Selective Pause */}
      {showAgentSelector && task.status === 'in-progress' && (
        <div
          style={{
            marginTop: '16px',
            padding: '16px',
            border: '1px solid #e5e7eb',
            borderRadius: '8px',
            backgroundColor: '#f9fafb'
          }}
        >
          <div style={{ fontSize: '14px', fontWeight: '600', marginBottom: '12px' }}>
            Select agents to pause:
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {runningAgents.map(agent => (
              <label
                key={agent.id}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px',
                  cursor: 'pointer',
                  padding: '6px 8px',
                  borderRadius: '4px',
                  backgroundColor: selectedAgents.has(agent.id) ? '#fef3c7' : 'white'
                }}
              >
                <input
                  type="checkbox"
                  checked={selectedAgents.has(agent.id)}
                  onChange={() => handleAgentToggle(agent.id)}
                  style={{ cursor: 'pointer' }}
                />
                <span style={{ fontSize: '14px' }}>
                  {agent.name} ({agent.type})
                </span>
              </label>
            ))}
          </div>
          <div style={{ marginTop: '12px', display: 'flex', gap: '8px' }}>
            <button
              onClick={handlePauseSelectedAgents}
              disabled={selectedAgents.size === 0}
              style={{
                padding: '8px 16px',
                borderRadius: '8px',
                border: '1px solid #ef4444',
                backgroundColor: '#ef4444',
                color: 'white',
                cursor: selectedAgents.size === 0 ? 'not-allowed' : 'pointer',
                fontSize: '14px',
                fontWeight: '600',
                opacity: selectedAgents.size === 0 ? 0.5 : 1
              }}
            >
              Pause Selected ({selectedAgents.size})
            </button>
            <button
              onClick={() => setShowAgentSelector(false)}
              style={{
                padding: '8px 16px',
                borderRadius: '8px',
                border: '1px solid #6b7280',
                backgroundColor: 'white',
                color: '#6b7280',
                cursor: 'pointer',
                fontSize: '14px',
                fontWeight: '600'
              }}
            >
              Cancel
            </button>
          </div>
        </div>
      )}

      {/* Follow-up Tasks Section */}
      {task.followUpTasks.length > 0 && (
        <div style={{ marginTop: '20px' }}>
          <div
            style={{
              fontSize: '16px',
              fontWeight: '600',
              marginBottom: '12px',
              paddingBottom: '8px',
              borderBottom: '2px solid #e5e7eb'
            }}
          >
            Follow-up Tasks ({task.followUpTasks.length})
          </div>
          {task.followUpTasks.map(followUpTask => (
            <FollowUpTaskCard
              key={followUpTask.id}
              followUpTask={followUpTask}
              onStart={(futId) => onStartFollowUpTask(task.id, futId)}
              onPauseAgents={(futId, agentIds) => onPauseFollowUpTaskAgents(task.id, futId, agentIds)}
              onComplete={(futId) => onCompleteFollowUpTask(task.id, futId)}
            />
          ))}
        </div>
      )}

      {/* Timestamps */}
      <div style={{ marginTop: '16px', fontSize: '12px', color: '#9ca3af' }}>
        <div>Created: {new Date(task.createdAt).toLocaleString()}</div>
        {task.startedAt && (
          <div>Started: {new Date(task.startedAt).toLocaleString()}</div>
        )}
        {task.completedAt && (
          <div>Completed: {new Date(task.completedAt).toLocaleString()}</div>
        )}
      </div>
    </div>
  );
};
