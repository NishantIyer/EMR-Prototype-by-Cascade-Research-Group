module.exports = function radiologyImagingProtocols() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Document Title: Radiology Imaging Protocols",
          line2: "Last Updated: 2023-10-05",
          line3: "Protocols: The document outlines imaging protocols for various radiological procedures, including X-rays, CT scans, MRIs, and ultrasounds.",
          line4: "Purpose: These protocols ensure consistent and high-quality image acquisition, aiding in accurate diagnosis and patient care." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};