#!/usr/bin/node

// Use Axios
const axios = require('axios');

const mvId = process.argv[2];

async function getCharacters(mvId) {
  try {
    const url = `https://swapi-api.hbtn.io/api/films/${mvId}`;
    const response = await axios.get(url);
    const charactersArray = response.data.characters;
    
    for (const character of charactersArray) {
      const characterResponse = await axios.get(character);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error(error);
  }
}

getCharacters(mvId);
