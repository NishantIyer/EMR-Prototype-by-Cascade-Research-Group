module.exports = function getFour() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Prescription History Report Title: Prescription History Report Date: 2023-12-05 Patient Information: - Patient Name: Mary Johnson - Date of Birth: 1985-03-12 - Medical Record Number: 9876543210 - Gender: Female Prescription History: This report provides a comprehensive overview of the patient's prescription history, including details about medications prescribed, dispensing dates, and prescribing healthcare providers. Medication History: 1. Medication: Lisinopril - Prescribed By: Dr. Smith - Prescribing Date: 2022-05-15 - Dispensing Date: 2022-05-16 - Dosage: 10mg - Refills: 3 2. Medication: Metformin - Prescribed By: Dr. Johnson - Prescribing Date: 2022-07-20 - Dispensing Date: 2022-07-21 - Dosage: 500mg - Refills: 4 3. Medication: Levothyroxine - Prescribed By: Dr. Wilson - Prescribing Date: 2023-02-10 - Dispensing Date: 2023-02-11 - Dosage: 100mcg - Refills: 2 4. Medication: Ibuprofen - Prescribed By: Dr. Davis - Prescribing Date: 2023-08-05 - Dispensing Date: 2023-08-06 - Dosage: 200mg - Refills: 0 Summary: This prescription history report contains a record of the medications prescribed to the patient, including the prescribing healthcare provider's name, prescribing date, dispensing date, dosage, and refills. It serves as a valuable reference for healthcare professionals to track the patient's medication history and ensure safe and effective treatment." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
