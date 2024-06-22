module.exports = function getThree() {
  try {
    // Hardcoded data as per your specification
    const data = {
      A1: {line1: "Insurance Claim Form Title: Insurance Claim Form Date: 2023-12-05 Claimant Information: - Claimant Name: Jane Smith - Date of Birth: 1990-08-20 - Policy Number: 1234567890 - Contact Number: (555) 987-6543 - Address: 456 Oak Street, Anytown, USA Incident Details: This form is used to report an insurance claim related to a specific incident or event. Please provide all necessary information to ensure prompt processing of your claim. Incident Date: 2023-11-30 Incident Time: 2:30 PM Incident Location: Intersection of Elm Street and Maple Avenue, Anytown, USA Incident Description: The claimant's vehicle was involved in a collision with another vehicle at the mentioned intersection. Please provide a detailed description of the incident and any injuries sustained. Vehicle Information (Claimant's Vehicle): - Make: Toyota - Model: Camry - Year: 2020 - License Plate Number: ABC-123 - Insurance Company: XYZ Insurance - Policy Number: 987654321 Driver Information (Claimant): - Driver's License Number: DL123456 - Driver's License State: Anytown - Date of Issue: 2010-05-10 - Date of Expiry: 2030-05-10 Other Party Involved: - Other Driver's Name: John Doe - Other Driver's Insurance Company: ABC Insurance - Other Driver's Policy Number: 123456789 Additional Information: - Police Report Number: PR-789012 - Description of Damages: Both vehicles sustained damage to the front bumper and headlights. - Injuries: Claimant reports minor neck pain and plans to seek medical attention. Witnesses: - Witness 1 Name: Sarah Johnson - Witness 1 Contact Number: (555) 123-4567 - Witness 2 Name: Michael Brown - Witness 2 Contact Number: (555) 789-0123 Please attach any relevant documents, such as photos of the accident scene, medical bills, and repair estimates. Summary: This insurance claim form provides essential details about the incident, the vehicles involved, and the parties affected. The claimant has reported damage to their vehicle and a minor injury. The insurance company will review this information to process the claim accordingly." }
    };

    return data;
  } catch (err) {
    console.error('Error processing dashboard data:', err);
    return {};
  }
};
