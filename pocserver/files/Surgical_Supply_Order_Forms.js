module.exports = function surgicalSupplyOrderForms() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Form Title: Surgical Supply Order Forms",
          line2: "Last Updated: 2023-09-01",
          line3: "Ordering Supplies: Surgical staff can use these forms to request and order surgical supplies, instruments, and equipment.",
          line4: "Approval Process: All supply orders require approval from the department head to ensure proper allocation and budget adherence." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};