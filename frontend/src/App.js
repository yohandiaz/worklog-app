import React, { useState, useEffect } from 'react';
import WorklogList from './components/WorklogList';
import WorklogForm from './components/WorklogForm';
import { getWorklogs } from './services/worklogService';
import './App.css';

function App() {
  const [worklogs, setWorklogs] = useState([]);
  const [editingWorklog, setEditingWorklog] = useState(null);
  const [error, setError] = useState(null);

  // Function to fetch worklogs
  const fetchWorklogs = async () => {
    try {
      const data = await getWorklogs();
      setWorklogs(data);
    } catch (error) {
      setError(error.message);
    }
  };

  useEffect(() => {
    fetchWorklogs(); // Fetch worklogs on component mount
  }, []);

  const handleEdit = (worklog) => {
    setEditingWorklog(worklog);
  };

  const handleFormSubmit = () => {
    setEditingWorklog(null);
    fetchWorklogs(); // Refresh the worklogs after form submission
  };

  return (
    <div className="App">
      <h1>Worklog</h1>
      {error && <div className="error">Error: {error}</div>}
      <WorklogForm worklogToEdit={editingWorklog} onFormSubmit={handleFormSubmit} />
      <WorklogList worklogs={worklogs} onEdit={handleEdit} />
    </div>
  );
}

export default App;