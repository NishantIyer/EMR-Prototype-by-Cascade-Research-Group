module.exports = function getRecords() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: { line1: "Patient_Record_2023-56789" },
      A2: { line1: ".txt" },
      A3: { line1: "1.2kb" },
      A4: { line1: "4/12/2023" },
      A5: { line1: "Lab_Test_Results_00123" },
      A6: { line1: ".pdf" },
      A7: { line1: "3.4MB" },
      A8: { line1: "4/13/2023" },
      A9: { line1: "Insurance_Claim_Forms_Aug2023" },
      A10: { line1: ".docx" },
      A11: { line1: "0.8MB" },
      A12: { line1: "4/15/2023" },
      A13: { line1: "Prescription_History_Report_7890" },
      A14: { line1: ".pdf" },
      A15: { line1: "2.6MB" },
      A16: { line1: "4/18/2023" },
      A17: { line1: "Medical_History_Summary_Jane_Doe" },
      A18: { line1: ".pdf" },
      A19: { line1: "1.5MB" },
      A20: { line1: "4/22/2023" },
    };

    return data;
  } catch (err) {
    console.error('Error processing automated overlay data:', err);
    return {};
  }
};
