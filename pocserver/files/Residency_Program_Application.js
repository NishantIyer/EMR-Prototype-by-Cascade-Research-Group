module.exports = function residencyProgramApplication() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Program Title: Medical Residency Program Application",
          line2: "Application Deadline: 2024-01-31",
          line3: "Program Details: Our residency program offers training in various medical specialties, including internal medicine, surgery, pediatrics, and more.",
          line4: "Application Requirements: Applicants must submit their medical school transcripts, letters of recommendation, personal statement, and curriculum vitae (CV)."
 }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};