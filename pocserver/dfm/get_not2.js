module.exports = function get_not2() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: { line1: "Research Paper Released" },
      A2: { line1: "Update on operating procedures" },
      A3: { line1: "Critical News" },
      A4: { line1: "Important Update: Revised Operating Procedures in Hospital"},
      A5: { line1: "We are pleased to announce the implementation of revised operating procedures aimed at enhancing patient care and safety. These updated protocols have been carefully designed to streamline operations, improve efficiency, and ensure the highest standards of care for our patients. ", line2: "Key highlights of the revised operating procedures include ", line3: "Enhanced infection control measures to mitigate the spread of communicable diseases within the hospital premises. Streamlined patient intake and discharge processes to minimize wait times and improve overall patient experience.", line4: "We believe that these updated operating procedures will further elevate the quality of care we provide and reinforce our commitment to excellence in healthcare delivery. We appreciate your cooperation and dedication to upholding these new standards." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
