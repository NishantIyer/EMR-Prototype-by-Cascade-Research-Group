module.exports = function trainingScheduleNov2023() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Training Date: 2023-11-10",
          line2: "Training Location: Conference Room A",
          line3: "Training Topics: Communication Skills, Team Collaboration, Time Management",
          line4: "Trainer: Emily Davis",
          line5: "Attendees: John Doe, Jane Smith, Robert Johnson, Susan Brown"
 }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};