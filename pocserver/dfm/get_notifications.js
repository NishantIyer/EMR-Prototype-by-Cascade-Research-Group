module.exports = function getNotifications() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: { line1: "Research Paper Released" },
      A2: { line1: "Update on operating procedures" },
      A3: { line1: "Critical News" }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
