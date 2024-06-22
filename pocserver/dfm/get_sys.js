module.exports = function getSys() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: { line1: "Backup_Restoration_Log" },
      A2: { line1: ".xlsx" },
      A3: { line1: "0.9MB" },
      A4: { line1: "8/1/2023" },
      A5: { line1: "Network_Security_Policy" },
      A6: { line1: ".pdf" },
      A7: { line1: "1.3MB" },
      A8: { line1: "8/5/2023" },
      A9: { line1: "Electronic_Health_Records_Database" },
      A10: { line1: ".sql" },
      A11: { line1: "3.2MB" },
      A12: { line1: "8/10/2023" },
      A13: { line1: "IT_Helpdesk_Troubleshooting_Guide" },
      A14: { line1: ".docx" },
      A15: { line1: "1.0MB" },
      A16: { line1: "8/15/2023" },
      A17: { line1: "Server_Maintenance_Schedule" },
      A18: { line1: ".pdf" },
      A19: { line1: "1.5MB" },
      A20: { line1: "8/20/2023" },
    };

    return data;
  } catch (err) {
    console.error('Error processing IT and Network Management data:', err);
    return {};
  }
};
