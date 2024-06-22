module.exports = function staffRoaster() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Employee ID, Employee Name, Position, Department, Hire Date",
          line2: "12345, John Doe, Senior Software Engineer, Engineering, 2023-01-15",
          line3: "23456, Jane Smith, Marketing Manager, Marketing, 2022-11-20",
          line4: "34567, Robert Johnson, Nurse, Healthcare, 2023-03-05",
          line5: "45678, Susan Brown, HR Specialist, Human Resources, 2023-02-10"
 }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};