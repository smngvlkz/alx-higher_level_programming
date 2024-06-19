#!/usr/bin/node

const occurrencesDict = require('./101-data').dict;
const usersByOccurrence = {};

for (const userId in occurrencesDict) {
	const occurrenceCount = occurrencesDict[userId];

	if (!usersByOccurrence[occurrenceCount]) {
		usersByOccurrence[occurrenceCount] = [];
	}

	usersByOccurrence[occurrenceCount].push(userId);
}

console.log(usersByOccurrence);
