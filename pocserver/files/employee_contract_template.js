module.exports = function employeeContractTemplate() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Employee Name: John Doe",
          line2: "Employee ID: 12345",
          line3: "Position: Senior Software Engineer",
          line4: "Employment Start Date: 2023-01-15",
          line5: "Employment End Date: 2024-01-15",
          line6: "Salary: $80,000 per annum",
          line7: "Benefits: Health Insurance, 401(k) Plan",
          line8: "Work Location: New York City"
 }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
/* Content for employee_contract_template */