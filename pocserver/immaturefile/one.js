module.exports = function getOne() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Patient Record Title: Patient Information Record Date: 2023-12-05 Patient Details: This record contains essential information about the patient, including their personal details, medical history, and current health status. It serves as a comprehensive reference for healthcare providers to ensure effective patient care and treatment. Patient Information: - Name: John Doe - Date of Birth: 1980-05-15 - Gender: Male - Contact Number: (555) 123-4567 - Address: 123 Main Street, Anytown, USA Medical History: - Allergies: None - Chronic Conditions: Hypertension, Diabetes - Surgical History: Appendectomy in 2005 - Medications: - Lisinopril (10mg daily) for hypertension - Metformin (500mg twice daily) for diabetes Current Health Status: - Chief Complaint: High blood pressure - Current Medications: As listed above - Recent Tests: - Blood Pressure: 140/90 mmHg - Blood Glucose: 150 mg/dL This patient record is vital for providing appropriate medical care, as it contains key information about the patient's health history and current condition. Healthcare professionals use this record to make informed decisions regarding diagnosis, treatment, and ongoing care." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
