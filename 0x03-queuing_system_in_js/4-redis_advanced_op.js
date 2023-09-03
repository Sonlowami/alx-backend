import { createClient, print } from 'redis';

const client = createClient();
const kv = {
	Portland: 50,
	Seattle: 80,
	'New York': 20,
	Bogota: 20,
	Cali: 40,
	Paris: 2
}

for (let [k, v] of Object.entries(kv)) {
  client.hset('HolbertonSchools', k, v, print)
}

client.hgetall('HolbertonSchools', (err, reply) => {
  if (err) { console.log(err); }
  if (reply) { console.log(reply); }
});
