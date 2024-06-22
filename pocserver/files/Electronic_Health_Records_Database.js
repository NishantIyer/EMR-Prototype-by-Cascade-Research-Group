module.exports = function ehrDatabase() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Database Title: Electronic Health Records Database",
          line2: "Database Schema: Tables - Patients, Medical Records, Lab Results, User Access Logs",
          line3: "Data Management: The database stores and manages electronic health records for patients, ensuring data accuracy and accessibility.",
          line4: "Access Logs: User access logs are maintained for auditing and security purposes." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
