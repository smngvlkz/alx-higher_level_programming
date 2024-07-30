#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data:', response.statusCode);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  const printCharacter = (url, callback) => {
    request(url, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error('Failed to fetch data:', charResponse.statusCode);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
      callback();
    });
  };

  const printCharactersInOrder = (index) => {
    if (index === characters.length) return;
    printCharacter(characters[index], () => printCharactersInOrder(index + 1));
  };

  printCharactersInOrder(0);
});

