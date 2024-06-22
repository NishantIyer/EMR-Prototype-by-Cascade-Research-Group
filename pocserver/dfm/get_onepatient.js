const fs = require('fs');
const path = require('path');

function getOnePatient(suffix) {
  // Convert suffix to patient index (e.g., 'a' -> 1)
  const patientIndex = suffix.charCodeAt(0) - 96;

  // Read the patients.json file
  const patientsData = JSON.parse(fs.readFileSync(path.join(__dirname, '../data/patients.json'), 'utf8'));

  // Check if patient exists at the specified index
  if (patientIndex > 0 && patientIndex <= patientsData.length) {
    const patient = patientsData[patientIndex - 1];
    return {
      [`IP${patientIndex}`]: {
        "line 1": patient.Name,
        "line 2": patient.Mobile,
        // Include other patient details as needed
      }
    };
  } else {
    // Handle cases where the patient does not exist
    return { error: "Patient not found" };
  }
}

module.exports = getOnePatient;
