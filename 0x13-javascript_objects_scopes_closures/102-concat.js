#!/usr/bin/node

const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

try {
	const content1 = fs.readFileSync(sourceFile1, 'utf8');
	const content2 = fs.readFileSync(sourceFile2, 'utf8');
	const combinedContent = content1 + content2;

	fs.writeFileSync(destinationFile, combinedContent);
	console.log(`Files ${sourceFile1} and ${sourceFile2}
		have been concatenated into ${destinationFile}.`);
} catch (error) {
	console.error('Error concatenating files:', error.message);
}
