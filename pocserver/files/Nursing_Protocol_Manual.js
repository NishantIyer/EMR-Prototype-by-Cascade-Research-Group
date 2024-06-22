module.exports = function nursingProtocolManual() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Manual Title: Nursing Protocol Manual",
          line2: "Last Revision Date: 2023-06-20",
          line3: "Table of Contents: Patient Assessment, Medication Administration, Infection Control, Patient Education, Emergency Response",
          line4: "Nursing Responsibilities: The manual provides guidelines and procedures for nursing staff to follow in various clinical scenarios." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
