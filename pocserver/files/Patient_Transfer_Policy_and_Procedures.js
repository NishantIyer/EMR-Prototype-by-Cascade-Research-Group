module.exports = function patientTransferPolicyAndProcedures() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Document Title: Patient Transfer Policy and Procedures",
          line2: "Last Revised: 2023-04-10",
          line3: "Transfer Guidelines: This document outlines the protocols and procedures for transferring patients between healthcare facilities.",
          line4: "Patient Safety: The policy aims to ensure the safe and coordinated transfer of patients, maintaining their continuity of care." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};