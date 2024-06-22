module.exports = function networkSecurityPolicy() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Policy Title: Network Security Policy",
          line2: "Effective Date: 2023-07-01",
          line3: "Policy Scope: This policy outlines security measures to protect the hospital's network infrastructure and sensitive data.",
          line4: "Security Controls: It includes guidelines for access control, firewall configurations, and encryption protocols." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
