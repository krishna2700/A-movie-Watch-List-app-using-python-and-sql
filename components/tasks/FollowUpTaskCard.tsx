import React, { useState } from 'react';
import { FollowUpTask, Agent } from '../../types/task';
import { MultiAgentIconDisplay, AgentStatusIndicator } from '../AgentIcons';

interface FollowUpTaskCardProps {
  followUpTask: FollowUpTask;
  onStart: (followUpTaskId: string) => void;
  onPauseAgents: (followUpTaskId: string, agentIds: string[]) => void;
  onComplete: (followUpTaskId: string) => void;
}

/**
 * Fix: Follow-up task card with proper status management and agent display
 */
export const FollowUpTaskCard: React.FC<FollowUpTaskCardProps> = ({
  followUpTask,
  onStart,
  onPauseAgents,
  onComplete
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
      onPauseAgents(followUpTask.id, Array.from(selectedAgents));
      setSelectedAgents(new Set());
      setShowAgentSelector(false);
    }
  };

  const getStatusColor = (status: FollowUpTask['status']) => {
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

  const getStatusLabel = (status: FollowUpTask['status']) => {
    switch (status) {
      case 'in-progress':
        return 'In Progress';
      case 'stopped':
        return 'Stopped';
      default:
        return status.charAt(0).toUpperCase() + status.slice(1);
    }
  };

  const runningAgents = followUpTask.agents.filter(a => a.status === 'running');
  const hasRunningAgents = runningAgents.length > 0;

  return (
    <div
      style={{
        border: '1px solid #e5e7eb',
        borderRadius: '8px',
        padding: '16px',
        marginTop: '12px',
        backgroundColor: '#f9fafb'
      }}
    >
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div style={{ flex: 1 }}>
          <h4 style={{ margin: '0 0 4px 0', fontSize: '16px', fontWeight: '600' }}>
            {followUpTask.title}
          </h4>
          <p style={{ margin: '0', fontSize: '14px', color: '#6b7280' }}>
            {followUpTask.description}
          </p>
        </div>

        {/* Status Badge */}
        <div
          style={{
            padding: '4px 12px',
            borderRadius: '12px',
            backgroundColor: getStatusColor(followUpTask.status) + '20',
            border: `1px solid ${getStatusColor(followUpTask.status)}50`,
            fontSize: '12px',
            fontWeight: '500',
            color: getStatusColor(followUpTask.status),
            whiteSpace: 'nowrap',
            marginLeft: '12px'
          }}
        >
          {getStatusLabel(followUpTask.status)}
        </div>
      </div>

      {/* Agent Display - Same logic as main task */}
      <div style={{ marginTop: '12px' }}>
        <MultiAgentIconDisplay
          agents={followUpTask.agents}
          stoppedAgents={followUpTask.stoppedAgents}
          maxDisplay={3}
          showStatus={true}
        />
      </div>

      {/* Agent Status Indicator - Shows what's in progress */}
      <AgentStatusIndicator
        agents={followUpTask.agents}
        stoppedAgents={followUpTask.stoppedAgents}
      />

      {/* Action Buttons */}
      <div style={{ marginTop: '12px', display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
        {followUpTask.status === 'pending' && (
          <button
            onClick={() => onStart(followUpTask.id)}
            style={{
              padding: '6px 12px',
              borderRadius: '6px',
              border: '1px solid #3b82f6',
              backgroundColor: '#3b82f6',
              color: 'white',
              cursor: 'pointer',
              fontSize: '14px',
              fontWeight: '500'
            }}
          >
            Start Task
          </button>
        )}

        {followUpTask.status === 'in-progress' && hasRunningAgents && (
          <>
            <button
              onClick={() => setShowAgentSelector(!showAgentSelector)}
              style={{
                padding: '6px 12px',
                borderRadius: '6px',
                border: '1px solid #f59e0b',
                backgroundColor: 'white',
                color: '#f59e0b',
                cursor: 'pointer',
                fontSize: '14px',
                fontWeight: '500',
                display: 'flex',
                alignItems: 'center',
                gap: '4px'
              }}
            >
              <span>⏸️</span>
              Pause Agents
            </button>

            {hasRunningAgents && (
              <button
                onClick={() => onComplete(followUpTask.id)}
                style={{
                  padding: '6px 12px',
                  borderRadius: '6px',
                  border: '1px solid #10b981',
                  backgroundColor: '#10b981',
                  color: 'white',
                  cursor: 'pointer',
                  fontSize: '14px',
                  fontWeight: '500'
                }}
              >
                Complete Task
              </button>
            )}
          </>
        )}

        {followUpTask.status === 'stopped' && (
          <button
            onClick={() => onStart(followUpTask.id)}
            style={{
              padding: '6px 12px',
              borderRadius: '6px',
              border: '1px solid #3b82f6',
              backgroundColor: '#3b82f6',
              color: 'white',
              cursor: 'pointer',
              fontSize: '14px',
              fontWeight: '500'
            }}
          >
            Resume Task
          </button>
        )}
      </div>

      {/* Agent Selector for Selective Pause */}
      {showAgentSelector && followUpTask.status === 'in-progress' && (
        <div
          style={{
            marginTop: '12px',
            padding: '12px',
            border: '1px solid #e5e7eb',
            borderRadius: '6px',
            backgroundColor: 'white'
          }}
        >
          <div style={{ fontSize: '14px', fontWeight: '500', marginBottom: '8px' }}>
            Select agents to pause:
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
            {runningAgents.map(agent => (
              <label
                key={agent.id}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px',
                  cursor: 'pointer',
                  padding: '4px'
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
          <div style={{ marginTop: '8px', display: 'flex', gap: '8px' }}>
            <button
              onClick={handlePauseSelectedAgents}
              disabled={selectedAgents.size === 0}
              style={{
                padding: '6px 12px',
                borderRadius: '6px',
                border: '1px solid #ef4444',
                backgroundColor: '#ef4444',
                color: 'white',
                cursor: selectedAgents.size === 0 ? 'not-allowed' : 'pointer',
                fontSize: '14px',
                fontWeight: '500',
                opacity: selectedAgents.size === 0 ? 0.5 : 1
              }}
            >
              Pause Selected ({selectedAgents.size})
            </button>
            <button
              onClick={() => setShowAgentSelector(false)}
              style={{
                padding: '6px 12px',
                borderRadius: '6px',
                border: '1px solid #6b7280',
                backgroundColor: 'white',
                color: '#6b7280',
                cursor: 'pointer',
                fontSize: '14px',
                fontWeight: '500'
              }}
            >
              Cancel
            </button>
          </div>
        </div>
      )}

      {/* Timestamps */}
      <div style={{ marginTop: '12px', fontSize: '12px', color: '#9ca3af' }}>
        {followUpTask.startedAt && (
          <div>Started: {new Date(followUpTask.startedAt).toLocaleString()}</div>
        )}
        {followUpTask.completedAt && (
          <div>Completed: {new Date(followUpTask.completedAt).toLocaleString()}</div>
        )}
      </div>
    </div>
  );
};
