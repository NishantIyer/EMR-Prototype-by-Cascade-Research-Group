module.exports = function getStaff() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: { line1: "Employee_Contract_Template" },
      A2: { line1: ".docx" },
      A3: { line1: "0.6MB" },
      A4: { line1: "4/10/2023" },
      A5: { line1: "Staff_Roster_2023" },
      A6: { line1: ".xlsx" },
      A7: { line1: "0.8MB" },
      A8: { line1: "4/15/2023" },
      A9: { line1: "Training_Schedule_Nov2023" },
      A10: { line1: ".pdf" },
      A11: { line1: "1.2MB" },
      A12: { line1: "4/20/2023" },
      A13: { line1: "Employee_Handbook_Updated" },
      A14: { line1: ".docx" },
      A15: { line1: "1.0MB" },
      A16: { line1: "4/25/2023" },
      A17: { line1: "Performance_Review_Forms_Q4" },
      A18: { line1: ".pdf" },
      A19: { line1: "0.7MB" },
      A20: { line1: "4/30/2023" },
    };

    return data;
  } catch (err) {
    console.error('Error processing Staff Information data:', err);
    return {};
  }
};
