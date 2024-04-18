#!/usr/bin/node

const request = require('request');
const process = require('process');

function getMovieCharacters (movieId) {
  const filmUrl = `https://swapi.dev/api/films/${movieId}/`;
  return new Promise((resolve, reject) => {
    request.get(filmUrl, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      if (response.statusCode !== 200) {
        reject(`Failed to fetch movie data. Status code: ${response.statusCode}`);
        return;
      }
      const filmData = JSON.parse(body);
      const charactersUrls = filmData.characters;
      const characterRequests = charactersUrls.map(url => {
        return new Promise((resolve, reject) => {
          request.get(url, (error, response, body) => {
            if (error) {
              reject(error);
              return;
            }
            if (response.statusCode !== 200) {
              reject(`Failed to fetch character data. Status code: ${response.statusCode}`);
              return;
            }
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          });
        });
      });
      Promise.all(characterRequests)
        .then(characters => resolve(characters))
        .catch(error => reject(error));
    });
  });
}

function main () {
  const movieId = process.argv[2];
  if (!movieId) {
    console.log('Usage: node script.js <Movie_ID>');
    return;
  }

  getMovieCharacters(movieId)
    .then(characters => {
      if (characters.length > 0) {
        characters.forEach(character => {
          console.log(character);
        });
      } else {
        console.log('No characters found for the given movie ID.');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

main();
