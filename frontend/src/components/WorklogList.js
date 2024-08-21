import React from 'react';

function WorklogList({ worklogs, onEdit }) {
  if (worklogs.length === 0) {
    return <p>No logs available.</p>;
  }

  return (
    <div className="worklog-list">
      <h2>Work Logs</h2>
      <ul>
        {worklogs.map((worklog) => (
          <li key={worklog.id} className="worklog-item">
            <div className="worklog-details">
              <span className="worklog-task">{worklog.task}</span> - 
              <span className="worklog-description">{worklog.description}</span> - 
              <span className="worklog-date">{worklog.date}</span> 
              {worklog.is_highlighted && <span className="highlight-star">⭐</span>}
            </div>
            <button 
              className="edit-button" 
              onClick={() => onEdit(worklog)}
            >
              Edit
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default WorklogList;