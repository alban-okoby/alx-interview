#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    return;
  }

  const charactersArray = JSON.parse(body).characters;

  function fetchCharacter (characterUrl) {
    return new Promise((resolve, reject) => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          reject(new Error(error));
          return;
        }

        if (response.statusCode !== 200) {
          reject(new Error(`Failed to fetch character data. Status code: ${response.statusCode}`));
          return;
        }

        const characterName = JSON.parse(body).name;
        console.log(characterName);
        resolve();
      });
    });
  }

  async function fetchAndPrintCharacters () {
    for (const characterUrl of charactersArray) {
      try {
        await fetchCharacter(characterUrl);
      } catch (error) {
        console.error(error.message);
      }
    }
  }

  fetchAndPrintCharacters();
});
