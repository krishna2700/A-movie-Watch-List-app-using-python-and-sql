import React from 'react';
import { Agent } from '../types/task';

interface AgentIconProps {
  type: Agent['type'];
  size?: 'sm' | 'md' | 'lg';
}

const AGENT_ICONS = {
  research: '🔍',
  analysis: '📊',
  execution: '⚙️',
  validation: '✅'
};

const AGENT_COLORS = {
  research: '#3b82f6',
  analysis: '#8b5cf6',
  execution: '#f59e0b',
  validation: '#10b981'
};

export const AgentIcon: React.FC<AgentIconProps> = ({ type, size = 'md' }) => {
  const sizeMap = {
    sm: '16px',
    md: '20px',
    lg: '24px'
  };

  return (
    <span
      style={{
        fontSize: sizeMap[size],
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: sizeMap[size],
        height: sizeMap[size]
      }}
      title={type}
    >
      {AGENT_ICONS[type]}
    </span>
  );
};

interface MultiAgentIconDisplayProps {
  agents: Agent[];
  stoppedAgents?: Agent[];
  maxDisplay?: number;
  showStatus?: boolean;
}

/**
 * Fix 4: Multi-agent icon display logic consistent between main and follow-up tasks
 * Shows active agents and stopped agents (up to 2 stopped agents displayed)
 */
export const MultiAgentIconDisplay: React.FC<MultiAgentIconDisplayProps> = ({
  agents,
  stoppedAgents = [],
  maxDisplay = 3,
  showStatus = true
}) => {
  const runningAgents = agents.filter(a => a.status === 'running');
  const displayStoppedAgents = stoppedAgents.slice(0, 2); // Max 2 stopped agent icons
  const hasMoreStopped = stoppedAgents.length > 2;

  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
      {/* Running agents */}
      {runningAgents.slice(0, maxDisplay).map((agent) => (
        <div
          key={agent.id}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '2px',
            padding: '2px 6px',
            borderRadius: '12px',
            backgroundColor: AGENT_COLORS[agent.type] + '20',
            border: `1px solid ${AGENT_COLORS[agent.type]}50`
          }}
        >
          <AgentIcon type={agent.type} size="sm" />
          {showStatus && (
            <span style={{ fontSize: '10px', color: AGENT_COLORS[agent.type] }}>
              {agent.name}
            </span>
          )}
        </div>
      ))}

      {runningAgents.length > maxDisplay && (
        <span style={{ fontSize: '12px', color: '#6b7280' }}>
          +{runningAgents.length - maxDisplay}
        </span>
      )}

      {/* Stopped agents (max 2) */}
      {displayStoppedAgents.length > 0 && (
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '2px',
            padding: '2px 6px',
            borderRadius: '12px',
            backgroundColor: '#ef444420',
            border: '1px solid #ef444450'
          }}
        >
          {displayStoppedAgents.map((agent) => (
            <div key={agent.id} style={{ opacity: 0.6 }}>
              <AgentIcon type={agent.type} size="sm" />
            </div>
          ))}
          {hasMoreStopped && (
            <span style={{ fontSize: '10px', color: '#ef4444' }}>
              +{stoppedAgents.length - 2}
            </span>
          )}
        </div>
      )}
    </div>
  );
};

interface AgentStatusIndicatorProps {
  agents: Agent[];
  stoppedAgents?: Agent[];
}

/**
 * Fix 5: Show which agents are in progress
 * Clear indication of what's currently running
 */
export const AgentStatusIndicator: React.FC<AgentStatusIndicatorProps> = ({
  agents,
  stoppedAgents = []
}) => {
  const runningAgents = agents.filter(a => a.status === 'running');
  const completedAgents = agents.filter(a => a.status === 'completed');

  if (runningAgents.length === 0 && stoppedAgents.length === 0 && completedAgents.length === 0) {
    return null;
  }

  return (
    <div style={{ fontSize: '12px', color: '#6b7280', marginTop: '4px' }}>
      {runningAgents.length > 0 && (
        <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
          <span style={{ color: '#3b82f6' }}>●</span>
          <span>
            In Progress: {runningAgents.map(a => a.name).join(', ')}
          </span>
        </div>
      )}
      {stoppedAgents.length > 0 && (
        <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
          <span style={{ color: '#ef4444' }}>■</span>
          <span>
            Stopped: {stoppedAgents.map(a => a.name).join(', ')}
          </span>
        </div>
      )}
      {completedAgents.length > 0 && (
        <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
          <span style={{ color: '#10b981' }}>✓</span>
          <span>
            Completed: {completedAgents.map(a => a.name).join(', ')}
          </span>
        </div>
      )}
    </div>
  );
};
