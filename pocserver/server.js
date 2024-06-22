const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const axios = require('axios');


const getNotifications = require('./dfm/get_notifications');
const getCalendar = require('./dfm/get_calendar');
const getInvPatients = require('./dfm/get_invpatients');
const getNot1 = require('./dfm/get_not1');
const getNot2 = require('./dfm/get_not2');
const getNot3 = require('./dfm/get_not3');
const getOnePatient = require('./dfm/get_onepatient');
const getRecords = require('./dfm/get_records');
const patientRecord202356789 = require('./files/Patient_Record_2023-56789');
const labTestResults00123 = require('./files/Lab_Test_Results_00123');
const insuranceClaimFormsAug2023 = require('./files/Insurance_Claim_Forms_Aug2023');
const prescriptionHistoryReport7890 = require('./files/Prescription_History_Report_7890');
const medicalHistorySummaryJaneDoe = require('./files/Medical_History_Summary_Jane_Doe');
const employeeContractTemplate = require('./files/employee_contract_template');
const staffRoaster = require('./files/staff_roaster');
const trainingScheduleNov2023 = require('./files/Training_Schedule_Nov2023');
const employeeHandbookUpdated = require('./files/Employee_Handbook_Updated');
const performanceReviewFormsQ4 = require('./files/Performance_Review_Forms_Q4');
const budgetReport20232024 = require('./files/Budget_Report_2023-2024');
const policyAndProcedureManual = require('./files/Policy_and_Procedure_Manual');
const boardMeetingMinutesOct2023 = require('./files/Board_Meeting_Minutes_Oct2023');
const facilityMaintenanceLog = require('./files/Facility_Maintenance_Log');
const vendorContracts2023 = require('./files/Vendor_Contracts_2023');
const medicalJournalArticleResearch = require('./files/Medical_Journal_Article_Research');
const continuingEducationCourseCatalog = require('./files/Continuing_Education_Course_Catalog');
const residencyProgramApplication = require('./files/Residency_Program_Application');
const medicalTerminologyGlossary = require('./files/Medical_Terminology_Glossary');
const surgicalTechniquesWorkshopSchedule = require('./files/Surgical_Techniques_Workshop_Schedule');
const radiologyImagingProtocols = require('./files/Radiology_Imaging_Protocols');
const nursingProtocolManual = require('./files/Nursing_Protocol_Manual');
const pharmacyInventoryLog = require('./files/Pharmacy_Inventory_Log');
const surgicalSupplyOrderForms = require('./files/Surgical_Supply_Order_Forms');
const patientTransferPolicyAndProcedures = require('./files/Patient_Transfer_Policy_and_Procedures');
const networkSecurityPolicy = require('./files/Network_Security_Policy');
const ehrDatabase = require('./files/Electronic_Health_Records_Database');
const itHelpdeskTroubleshootingGuide = require('./files/IT_Helpdesk_Troubleshooting_Guide');
const serverMaintenanceSchedule = require('./files/Server_Maintenance_Schedule');
const getAdmin = require('./dfm/get_admin')
const getDept = require('./dfm/get_dept')
const getMededu = require('./dfm/get_mededu')
const getStaff = require('./dfm/get_staff')
const getSys = require('./dfm/get_sys')
const getHome = require('./messenger/home')
const getEmma = require('./messenger/emma')
const getJohn = require('./messenger/john')
const getRon = require('./messenger/ron')

const app = express();
const port = 8080;

app.use(bodyParser.json());

// Event Handler Table (EHT)
const EHT = {
  'EID49': getNotifications,
  'EID51': getNot1,
  'EID52': getNot2,
  'EID53': getNot3,
  'EID69': getNot2,
  'EID70': getNot3,
  'EID66': getNotifications,
  'EID67': getNotifications,
  'EID95': getRecords, 
  'EID96': getStaff,
  'EID97': getAdmin,
  'EID98': getMededu,
  'EID99': getDept,
  'EID100': getSys,
  'EID48': getHome,
  'EID201': getJohn,
  'EID203': getRon,
  'EID204': getEmma,
  // ... (Other EID mappings)
};

function appendToChatFileAndReturn(eid, content) {
    let fileName;
    switch (eid) {
        case 'EID201':
            fileName = 'john.json';
            break;
        case 'EID203':
            fileName = 'ron.json';
            break;
        case 'EID204':
            fileName = 'emma.json';
            break;
        default:
            return null;
    }

    const filePath = path.join(__dirname, 'messenger', fileName);
    const fileData = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    const lastKey = `A${Object.keys(fileData).length}`;
    const lastEntry = fileData[lastKey];
    const nextLineKey = `line${Object.keys(lastEntry).length + 1}`;
    lastEntry[nextLineKey] = `Nishant: ${content}`;
    fileData[lastKey] = lastEntry;

    fs.writeFileSync(filePath, JSON.stringify(fileData, null, 2));
    return fileData;
}

// Function to get conversation data based on EID
function getConversationData(eid) {
    let fileName;
    switch (eid) {
        case 'EID201':
            fileName = 'john.json';
            break;
        case 'EID203':
            fileName = 'ron.json';
            break;
        case 'EID204':
            fileName = 'emma.json';
            break;
        default:
            return null;
    }

    const filePath = path.join(__dirname, 'messenger', fileName);
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

let recentEID = null;
let secondLastEID = null;

app.post('/event', (req, res) => {
    const eid = req.body.eid;
    const content = req.body.content;

    if (['EID201', 'EID203', 'EID204'].includes(eid)) {
        secondLastEID = recentEID;
        recentEID = eid;
    }

    // Special handling for EID1400
    if (eid === 'EID1400' && recentEID) {
        const updatedData = appendToChatFileAndReturn(recentEID, content);
        if (updatedData) {
            res.json(updatedData);
        } else {
            res.status(400).send('Invalid EID for conversation update');
        }
        return;
    }

    // Handling for EID182 (Refresh and send conversation data)
    if (eid === 'EID182' && secondLastEID) {
        const conversationData = getConversationData(secondLastEID);
        if (conversationData) {
            res.json(conversationData);
        } else {
            res.status(400).send('Invalid EID for conversation retrieval');
        }
        return;
    }

    // Handling standard EHT functions
    if (EHT[eid]) {
        const data = EHT[eid](req.body);
        res.json(data);
    } else {
        console.log(`Event ID not found: ${eid}`);
        res.status(404).send('Event ID not found');
    }
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});