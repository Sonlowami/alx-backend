import { createClient, print } from 'redis';

const subscriber = createClient();

const channelName = 'holberton school channel';
subscriber.subscribe(channelName);

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});
subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
subscriber.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(channelName);
    subscriber.quit();
  }
  console.log(message);
});
