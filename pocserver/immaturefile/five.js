module.exports = function getFive() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Medical History Summary for Jane Doe Date: 2023-12-05 Patient Information: - Patient Name: Jane Doe - Date of Birth: 1990-09-25 - Medical Record Number: 123456789 Medical History Summary: This summary provides an overview of Jane Doe's medical history, including past illnesses, surgeries, allergies, and current health conditions. Medical History: - Allergies: None reported - Chronic Conditions: 1. Hypertension: Diagnosed in 2010. Currently managed with Lisinopril (10mg daily). 2. Asthma: Diagnosed in childhood. Controlled with an albuterol inhaler as needed. - Surgical History: 1. Appendectomy: Performed in 2008. 2. Tonsillectomy: Performed in 1999. - Hospitalizations: None reported - Family History: No significant family history of hereditary medical conditions. - Immunizations: Up to date according to recommended schedules. - Current Medications: Lisinopril (10mg daily) for hypertension. Allergies: No known allergies to medications or substances. Summary: Jane Doe has a relatively unremarkable medical history. She has a history of hypertension, diagnosed in 2010, which is well-controlled with medication. She also has a history of childhood asthma, which is managed with an albuterol inhaler as needed. Jane has a surgical history that includes an appendectomy in 2008 and a tonsillectomy in 1999. Her family history does not indicate any significant hereditary medical conditions. Jane's immunizations are up to date, and she has no known allergies to medications or substances. This medical history summary serves as a reference for healthcare providers to understand Jane's medical background and make informed decisions regarding her care." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
