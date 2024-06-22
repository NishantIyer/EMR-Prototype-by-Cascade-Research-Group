module.exports = function itHelpdeskTroubleshootingGuide() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Guide Title: IT Helpdesk Troubleshooting Guide",
          line2: "Last Revised: 2023-09-05",
          line3: "Troubleshooting Steps: The guide provides IT staff with step-by-step instructions for diagnosing and resolving common technical issues.",
          line4: "User Support: It emphasizes timely and effective user support to minimize disruptions in hospital operations." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
/* Content for IT_Helpdesk_Troubleshooting_Guide */