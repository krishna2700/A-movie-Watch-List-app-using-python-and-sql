import React, { useState } from 'react';
import { Agent, AgentStatus, TaskStatus } from '../types/task';

interface AgentIconsProps {
  agents: Agent[];
  taskStatus: TaskStatus;
  onPauseAgents?: (agentIds: string[]) => void;
  activeAgents?: Agent[];
  showStatus?: boolean;
}

export const AgentIcons: React.FC<AgentIconsProps> = ({
  agents,
  taskStatus,
  onPauseAgents,
  activeAgents = [],
  showStatus = false
}) => {
  const [selectedAgents, setSelectedAgents] = useState<Set<string>>(new Set());
  const [showPauseMenu, setShowPauseMenu] = useState(false);
  
  const handleAgentClick = (agentId: string) => {
    if (!onPauseAgents || activeAgents.length === 0) return;
    
    const newSelected = new Set(selectedAgents);
    if (newSelected.has(agentId)) {
      newSelected.delete(agentId);
    } else {
      newSelected.add(agentId);
    }
    setSelectedAgents(newSelected);
  };
  
  const handlePauseSelected = () => {
    if (onPauseAgents && selectedAgents.size > 0) {
      onPauseAgents(Array.from(selectedAgents));
      setSelectedAgents(new Set());
      setShowPauseMenu(false);
    }
  };
  
  const handlePauseAll = () => {
    if (onPauseAgents && activeAgents.length > 0) {
      onPauseAgents(activeAgents.map(a => a.id));
      setShowPauseMenu(false);
    }
  };
  
  const getAgentIconColor = (agent: Agent): string => {
    switch (agent.status) {
      case AgentStatus.ACTIVE:
        return 'bg-blue-500';
      case AgentStatus.PAUSED:
        return 'bg-yellow-500';
      case AgentStatus.STOPPED:
        return 'bg-red-500';
      case AgentStatus.COMPLETED:
        return 'bg-green-500';
      default:
        return 'bg-gray-500';
    }
  };
  
  const getAgentStatusLabel = (agent: Agent): string => {
    switch (agent.status) {
      case AgentStatus.ACTIVE:
        return 'Active';
      case AgentStatus.PAUSED:
        return 'Paused';
      case AgentStatus.STOPPED:
        return 'Stopped';
      case AgentStatus.COMPLETED:
        return 'Completed';
      default:
        return 'Unknown';
    }
  };
  
  // Show pause button if there are active agents and pause handler is provided
  const showPauseButton = onPauseAgents && activeAgents.length > 0 && taskStatus === TaskStatus.IN_PROGRESS;
  
  // Filter agents to show based on context
  // If showing status, show all agents
  // Otherwise, show all agents but highlight active ones when in progress
  const agentsToShow = agents;
  const activeAgentIds = new Set(activeAgents.map(a => a.id));
  
  return (
    <div className="flex items-center gap-2">
      {/* Agent Icons */}
      <div className="flex items-center gap-1">
        {agentsToShow.map(agent => {
          const isActive = activeAgentIds.has(agent.id);
          const isSelected = selectedAgents.has(agent.id);
          const isClickable = onPauseAgents && isActive;
          
          return (
            <div
              key={agent.id}
              className={`relative ${isClickable ? 'cursor-pointer' : ''} ${
                isSelected ? 'ring-2 ring-blue-400' : ''
              } ${taskStatus === TaskStatus.IN_PROGRESS && isActive ? 'ring-1 ring-blue-300' : ''}`}
              onClick={() => isClickable && handleAgentClick(agent.id)}
              title={`${agent.name} - ${getAgentStatusLabel(agent)}`}
            >
              <div className={`w-8 h-8 rounded-full ${getAgentIconColor(agent)} flex items-center justify-center text-white text-xs font-semibold ${
                taskStatus === TaskStatus.IN_PROGRESS && isActive ? 'animate-pulse' : ''
              }`}>
                {agent.icon || agent.name.charAt(0).toUpperCase()}
              </div>
              {showStatus && (
                <span className="absolute -bottom-4 left-1/2 transform -translate-x-1/2 text-xs whitespace-nowrap">
                  {getAgentStatusLabel(agent)}
                </span>
              )}
            </div>
          );
        })}
      </div>
      
      {/* Pause Button with Dropdown */}
      {showPauseButton && (
        <div className="relative">
          <button
            onClick={() => setShowPauseMenu(!showPauseMenu)}
            className="p-1 text-gray-600 hover:text-gray-800"
            title="Pause agents"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 9v6m4-6v6m7-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </button>
          
          {showPauseMenu && (
            <div className="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg z-10 border border-gray-200">
              <div className="py-1">
                {selectedAgents.size > 0 ? (
                  <button
                    onClick={handlePauseSelected}
                    className="w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                  >
                    Pause Selected ({selectedAgents.size})
                  </button>
                ) : (
                  <div className="px-4 py-2 text-xs text-gray-500">
                    Select agents to pause
                  </div>
                )}
                <button
                  onClick={handlePauseAll}
                  className="w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 border-t border-gray-200"
                >
                  Pause All ({activeAgents.length})
                </button>
              </div>
            </div>
          )}
        </div>
      )}
      
      {/* Show "Stopped" label if all agents are stopped */}
      {agents.length > 0 && agents.every(a => a.status === AgentStatus.STOPPED) && (
        <span className="text-sm text-red-600 font-medium">Stopped</span>
      )}
    </div>
  );
};
