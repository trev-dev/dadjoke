#! /usr/bin/node
const https = require('https')

const options = {
  headers: {
    'Accept': 'application/json'
  }
}

https.get('https://icanhazdadjoke.com', options, req => {
  let data = ''
  req.on('data', chunk => data += chunk)
  req.on('end', () => console.log(JSON.parse(data).joke))
}).on('error', e => console.error(e))
