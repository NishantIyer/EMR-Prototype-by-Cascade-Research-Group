module.exports = function serverMaintenanceSchedule() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Schedule Title: Server Maintenance Schedule",
          line2: "Maintenance Period: Monthly Maintenance, Weekends",
          line3: "Tasks: The schedule outlines routine server maintenance tasks, including updates, patches, and hardware checks.",
          line4: "Downtime Notifications: Maintenance activities are scheduled during low-traffic periods to minimize user impact." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};