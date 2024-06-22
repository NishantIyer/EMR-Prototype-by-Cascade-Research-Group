module.exports = function get_not1() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: { line1: "Research Paper Released" },
      A2: { line1: "Update on operating procedures" },
      A3: { line1: "Critical News" },
      A4: { line1: "Revolutionizing Healthcare with Personalized Medicine.",
      A5: { line1: "We are thrilled to announce the release of a groundbreaking research paper titled Revolutionizing Healthcare: The Power of Personalized Medicine This paper presents cutting-edge findings on the potential of personalized healthcare in improving patient outcomes and revolutionizing the healthcare industry as a whole. The research offers compelling evidence that tailoring medical treatments to individual genetic profiles and lifestyle factors can lead to more effective and efficient healthcare delivery. This paper is a must-read for healthcare professionals, policymakers, and anyone interested in the future of medicine." }
          }
    }
      return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
