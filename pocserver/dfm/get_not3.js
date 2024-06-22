module.exports = function get_not3() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: { line1: "Research Paper Released" },
      A2: { line1: "Update on operating procedures" },
      A3: { line1: "Critical News" },
      A4: { line1: "Important Update: Revised Operating Procedures in Hospital"},
      A5: { line1: "We regret to inform you of a critical news update that requires immediate attention. It has come to our attention that there is a potential security threat in the vicinity of our facility. As a precautionary measure, we urge all staff members to remain vigilant and report any suspicious activity to the designated authorities.", line2: "In light of this critical news, we have implemented heightened security protocols to ensure the safety and well-being of everyone within our premises. We advise all staff to adhere to these protocols and cooperate with security personnel as they work to address the situation.", line3: "We understand the gravity of this situation and assure you that we are taking all necessary steps to mitigate any potential risks. Your safety is our top priority, and we appreciate your cooperation during this time.Please stay tuned for further updates as the situation unfolds." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
