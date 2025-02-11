#!/usr/bin/node

const fs = require("fs");

// Get the file path from the command-line arguments
const filePath = process.argv[2];

if (!filePath) {
  console.error("Usage: ./0-readme.js <file_path>");
  process.exit(1);
}

// Read the file asynchronously in UTF-8 encoding
fs.readFile(filePath, "utf-8", (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
