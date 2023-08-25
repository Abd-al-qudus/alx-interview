#!/usr/bin/node

const request = require('request');
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = process.argv[2];

async function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterName = JSON.parse(body).name;
        resolve(characterName);
        console.log(characterName);
      }
    });
  });
}

async function main () {
  try {
    request(baseUrl + characterId, async function (error, resp, body) {
      if (error) {
        console.log(error);
      } else {
        const characterList = JSON.parse(body).characters;
        for (let i = 0; i < characterList.length; i++) {
          await getCharacterName(characterList[i]);
        }
      }
    });
  } catch (error) {
    console.log(error);
  }
}

main();
