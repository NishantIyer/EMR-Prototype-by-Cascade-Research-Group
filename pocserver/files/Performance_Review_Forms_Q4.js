module.exports = function performanceReviewFormsQ4() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Employee Name: John Doe",
          line2: "Employee ID: 12345",
          line3: "Review Period: Q4 2023",
          line4: "Supervisor: Sarah Johnson",
          line5: "Performance Ratings: Communication - 4/5, Collaboration - 5/5, Punctuality - 4/5, Problem Solving - 4/5",
          line6: "Comments: John has consistently demonstrated strong teamwork and communication skills..."
 }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};