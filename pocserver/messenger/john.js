const fs = require('fs');
const path = require('path');

// Function to get data from JSON file
function getDataFromJson(filename) {
  try {
    const filePath = path.join(__dirname, filename);
    const fileContent = fs.readFileSync(filePath, 'utf8');
    return JSON.parse(fileContent);
  } catch (err) {
    console.error(`Error reading file ${filename}:`, err);
    return {};
  }
}

module.exports = function getJohn() {
  // Replace hardcoded data with data from JSON file
  const data = getDataFromJson('john.json');
  return data;
};
