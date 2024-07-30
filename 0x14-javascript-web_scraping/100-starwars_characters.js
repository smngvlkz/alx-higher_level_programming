#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }

    const jsonData = JSON.parse(body);
    const charactersUrls = jsonData.characters;

    charactersUrls.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
            if (error) {
                console.error(error);
                return;
            }

            const characterData = JSON.parse(body);
            console.log(characterData.name);
        });
    });
});
