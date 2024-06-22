module.exports = function patientRecord202356789() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Patient Name: John Smith",
          line2: "Date of Birth: 1980-05-15",
          line3: "Gender: Male",
          line4: "Medical History: Hypertension, Diabetes Type 2",
          line5: "Allergies: None",
          line6: "Current Medications: Lisinopril 10mg (Once daily), Metformin 500mg (Twice daily)",
          line7: "Past Surgeries: Appendectomy (2005), Knee Surgery (2010)"
 }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};