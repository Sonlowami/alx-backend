import { createClient, print } from 'redis';
import { promisify } from 'util';


const client = createClient();
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
  });
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const get = promisify(client.get).bind(client);
  console.log(await get(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

