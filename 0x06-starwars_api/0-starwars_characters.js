#!/usr/bin/node
// A script that prints all characters of a Star Wars movie in order.

const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];

  // Fetch the movie details
  request(`${API_URL}/films/${movieId}/`, (err, _, body) => {
    if (err) {
      console.error(err);
      return;
    }

    // Parse the response body
    let charUrls;
    try {
      charUrls = JSON.parse(body).characters;
    } catch (parseErr) {
      console.error('Error parsing JSON:', parseErr);
      return;
    }

    // Fetch each character's name in sequence
    const fetchCharacterName = (url) =>
      new Promise((resolve, reject) => {
        request(url, (charErr, __, charBody) => {
          if (charErr) {
            reject(charErr);
            return;
          }
          try {
            const name = JSON.parse(charBody).name;
            resolve(name);
          } catch (parseErr) {
            reject(parseErr);
          }
        });
      });

    // Resolve all character names and print them
    Promise.all(charUrls.map(fetchCharacterName))
      .then((names) => console.log(names.join('\n')))
      .catch((fetchErr) => console.error('Error fetching characters:', fetchErr));
  });
} else {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
}
