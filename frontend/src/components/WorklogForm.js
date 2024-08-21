import React, { useState, useEffect } from 'react';
import { createWorklog, updateWorklog } from '../services/worklogService';

function WorklogForm({ worklogToEdit, onFormSubmit }) {
  const [worklog, setWorklog] = useState({
    task: '',
    description: '',
    date: '',
    is_highlighted: false,
  });

  useEffect(() => {
    if (worklogToEdit) {
      setWorklog(worklogToEdit);
    }
  }, [worklogToEdit]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setWorklog((prev) => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Convert empty date string to null
    const worklogData = {
      ...worklog,
      date: worklog.date.trim() === '' ? null : worklog.date,
    };

    if (worklog.id) {
      await updateWorklog(worklog.id, worklogData);
    } else {
      await createWorklog(worklogData);
    }

    setWorklog({
      task: '',
      description: '',
      date: '',
      is_highlighted: false,
    });

    onFormSubmit();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="task"
        value={worklog.task}
        onChange={handleChange}
        placeholder="Task"
        required
      />
      <input
        type="text"
        name="description"
        value={worklog.description}
        onChange={handleChange}
        placeholder="Description"
      />
      <input
        type="date"
        name="date"
        value={worklog.date}
        onChange={handleChange}
      />
      <label>
        Highlighted
        <input
          type="checkbox"
          name="is_highlighted"
          checked={worklog.is_highlighted}
          onChange={handleChange}
        />
      </label>
      <button type="submit">{worklog.id ? 'Update' : 'Add'} Worklog</button>
    </form>
  );
}

export default WorklogForm;
