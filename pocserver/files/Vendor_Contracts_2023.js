module.exports = function vendorContracts2023() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Contract Title: Vendor Contracts for 2023",
          line2: "Contract Date: Various dates in 2023",
          line3: "Vendors: ABC Medical Supplies, XYZ Pharmaceuticals, GreenTech Solutions",
          line4: "Contract Details: The contracts outline terms and conditions for the supply of medical equipment, pharmaceuticals, and IT services." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};