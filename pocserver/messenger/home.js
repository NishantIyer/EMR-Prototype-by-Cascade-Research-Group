module.exports = function getHome() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: { line1: "John" },
      A2: { line1: "Ron" },
      A3: { line1: "Emma" }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
