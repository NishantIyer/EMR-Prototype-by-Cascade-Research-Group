module.exports = function prescriptionHistoryReport7890() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Patient ID: 7890",
          line2: "Prescription History: 1. Medication: Amoxicillin 500mg, Prescribed by: Dr. Emily Davis, Date: 2023-02-20, 2. Medication: Ibuprofen 200mg, Prescribed by: Dr. Mark Johnson, Date: 2022-12-10"
 }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};