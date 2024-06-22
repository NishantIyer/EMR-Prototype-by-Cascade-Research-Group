module.exports = function getTwo() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Lab Results Report Title: Lab Results Report Date: 2023-12-05 Patient Information: - Patient Name: John Doe - Date of Birth: 1980-05-15 - Gender: Male - Medical Record Number: 1234567890 Test Results: This report contains the results of recent laboratory tests conducted for the patient. These tests provide valuable information about the patient's health and aid in diagnosis and treatment decisions. Hematology Panel: - Hemoglobin: 12.5 g/dL - Hematocrit: 38% - White Blood Cell Count: 6,000/mm³ - Platelet Count: 200,000/mm³ Blood Chemistry: - Glucose: 120 mg/dL - Total Cholesterol: 180 mg/dL - LDL Cholesterol: 90 mg/dL - HDL Cholesterol: 50 mg/dL - Triglycerides: 120 mg/dL Urinalysis: - Color: Yellow - Appearance: Clear - Glucose: Negative - Protein: Negative - pH: 6.5 - Specific Gravity: 1.020 Radiology: - X-Ray of Chest: No significant abnormalities detected. Summary: The laboratory results indicate that the patient's hematology panel, blood chemistry, and urinalysis are within normal ranges. The chest X-ray did not reveal any significant abnormalities. These results provide valuable information for assessing the patient's overall health. Any abnormal findings or concerns will be discussed with the patient, and further tests or treatment may be recommended as necessary." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
