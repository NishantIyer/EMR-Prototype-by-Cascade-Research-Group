module.exports = function getDept() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: { line1: "Radiology_Imaging_Protocols" },
      A2: { line1: ".docx" },
      A3: { line1: "1.5MB" },
      A4: { line1: "6/25/2023" },
      A5: { line1: "Nursing_Protocol_Manual" },
      A6: { line1: ".pdf" },
      A7: { line1: "2.0MB" },
      A8: { line1: "6/30/2023" },
      A9: { line1: "Pharmacy_Inventory_Log" },
      A10: { line1: ".xlsx" },
      A11: { line1: "0.7MB" },
      A12: { line1: "7/5/2023" },
      A13: { line1: "Surgical_Supply_Order_Forms" },
      A14: { line1: ".pdf" },
      A15: { line1: "1.2MB" },
      A16: { line1: "7/10/2023" },
      A17: { line1: "Patient_Transfer_Policy_and_Procedures" },
      A18: { line1: ".doc" },
      A19: { line1: "1.8MB" },
      A20: { line1: "7/15/2023" },
    };

    return data;
  } catch (err) {
    console.error('Error processing Hospital Protocols and Procedures data:', err);
    return {};
  }
};
