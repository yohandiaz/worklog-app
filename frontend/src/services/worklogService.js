
const API_URL = process.env.REACT_APP_API_URL;

console.log("API_URL", API_URL);

export const getWorklogs = async (skip = 0, limit = 100) => {
  try {
    const response = await fetch(`${API_URL}/worklogs?skip=${skip}&limit=${limit}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error(`Error fetching worklogs: ${response.statusText}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching worklogs:", error);
    throw error;
  }
};

export const createWorklog = async (worklog) => {
  try {
    const response = await fetch(`${API_URL}/worklogs/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(worklog),
    });

    if (!response.ok) {
      throw new Error(`Error creating worklog: ${response.statusText}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error creating worklog:", error);
    throw error;
  }
};

export const updateWorklog = async (id, worklog) => {
    try {
        const response = await fetch(`${API_URL}/worklogs/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(worklog),
        });

        if (!response.ok) {
            throw new Error(`Error updating worklog: ${response.statusText}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error updating worklog:", error);
        throw error;
    }
};

export const deleteWorklog = async (id) => {
    try {
        const response = await fetch(`${API_URL}/worklogs/${id}`, {
            method: 'DELETE',
        });

        if (!response.ok) {
            throw new Error(`Error deleting worklog: ${response.statusText}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error deleting worklog:", error);
        throw error;
    }
};
