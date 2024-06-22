module.exports = function getAdmin() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: { line1: "Budget_Report_2023-2024" },
      A2: { line1: ".pdf" },
      A3: { line1: "1.5MB" },
      A4: { line1: "5/5/2023" },
      A5: { line1: "Policy_and_Procedure_Manual" },
      A6: { line1: ".docx" },
      A7: { line1: "2.0MB" },
      A8: { line1: "5/10/2023" },
      A9: { line1: "Board_Meeting_Minutes_Oct2023" },
      A10: { line1: ".pdf" },
      A11: { line1: "1.2MB" },
      A12: { line1: "5/15/2023" },
      A13: { line1: "Facility_Maintenance_Log" },
      A14: { line1: ".xlsx" },
      A15: { line1: "0.9MB" },
      A16: { line1: "5/20/2023" },
      A17: { line1: "Vendor_Contracts_2023" },
      A18: { line1: ".doc" },
      A19: { line1: "1.8MB" },
      A20: { line1: "5/25/2023" },
    };

    return data;
  } catch (err) {
    console.error('Error processing Budget and Policy data:', err);
    return {};
  }
};
