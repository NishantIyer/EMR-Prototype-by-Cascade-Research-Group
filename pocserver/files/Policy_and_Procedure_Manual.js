module.exports = function policyAndProcedureManual() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Manual Title: Hospital Policy and Procedure Manual",
          line2: "Last Revision Date: 2023-07-15",
          line3: "Table of Contents: Introduction, Patient Care Policies, Administrative Policies, Emergency Procedures, Employee Conduct",
          line4: "Code of Ethics: Our hospital's code of ethics guides our actions and interactions with patients, staff, and the community...",
          line5: "Contact Information: General Inquiries - info@examplehospital.com, Phone: (555) 123-7890" }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};