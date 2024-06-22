const fs = require('fs');

function createFile(filename, content) {
  fs.writeFileSync(filename, content, 'utf8');
}

// EID95
createFile('files/Patient_Record_2023-56789.js', '/* Content for Patient_Record_2023-56789 */');
createFile('files/Lab_Test_Results_00123.js', '/* Content for Lab_Test_Results_00123 */');
createFile('files/Insurance_Claim_Forms_Aug2023.js', '/* Content for Insurance_Claim_Forms_Aug2023 */');
createFile('files/Prescription_History_Report_7890.js', '/* Content for Prescription_History_Report_7890 */');
createFile('files/Medical_History_Summary_Jane_Doe.js', '/* Content for Medical_History_Summary_Jane_Doe */');

// EID96
createFile('files/employee_contract_template.js', '/* Content for employee_contract_template */');
createFile('files/staff_roaster.js', '/* Content for staff_roaster */');
createFile('files/Training_Schedule_Nov2023.js', '/* Content for Training_Schedule_Nov2023 */');
createFile('files/Employee_Handbook_Updated.js', '/* Content for Employee_Handbook_Updated */');
createFile('files/Performance_Review_Forms_Q4.js', '/* Content for Performance_Review_Forms_Q4 */');

// EID97
createFile('files/Budget_Report_2023-2024.js', '/* Content for Budget_Report_2023-2024 */');
createFile('files/Policy_and_Procedure_Manual.js', '/* Content for Policy_and_Procedure_Manual */');
createFile('files/Board_Meeting_Minutes_Oct2023.js', '/* Content for Board_Meeting_Minutes_Oct2023 */');
createFile('files/Facility_Maintenance_Log.js', '/* Content for Facility_Maintenance_Log */');
createFile('files/Vendor_Contracts_2023.js', '/* Content for Vendor_Contracts_2023 */');

// EID98
createFile('files/Medical_Journal_Article_Research.js', '/* Content for Medical_Journal_Article_Research */');
createFile('files/Continuing_Education_Course_Catalog.js', '/* Content for Continuing_Education_Course_Catalog */');
createFile('files/Residency_Program_Application.js', '/* Content for Residency_Program_Application */');
createFile('files/Medical_Terminology_Glossary.js', '/* Content for Medical_Terminology_Glossary */');
createFile('files/Surgical_Techniques_Workshop_Schedule.js', '/* Content for Surgical_Techniques_Workshop_Schedule */');

// EID99
createFile('files/Radiology_Imaging_Protocols.js', '/* Content for Radiology_Imaging_Protocols */');
createFile('files/Nursing_Protocol_Manual.js', '/* Content for Nursing_Protocol_Manual */');
createFile('files/Pharmacy_Inventory_Log.js', '/* Content for Pharmacy_Inventory_Log */');
createFile('files/Surgical_Supply_Order_Forms.js', '/* Content for Surgical_Supply_Order_Forms */');
createFile('files/Patient_Transfer_Policy_and_Procedures.js', '/* Content for Patient_Transfer_Policy_and_Procedures */');

// EID100
createFile('files/Backup_Restoration_Log.js', '/* Content for Backup_Restoration_Log */');
createFile('files/Network_Security_Policy.js', '/* Content for Network_Security_Policy */');
createFile('files/Electronic_Health_Records_Database.js', '/* Content for Electronic_Health_Records_Database */');
createFile('files/IT_Helpdesk_Troubleshooting_Guide.js', '/* Content for IT_Helpdesk_Troubleshooting_Guide */');
createFile('files/Server_Maintenance_Schedule.js', '/* Content for Server_Maintenance_Schedule */');

console.log('Files created successfully.');
