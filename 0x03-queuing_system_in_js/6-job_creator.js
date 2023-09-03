import kue from 'kue';

const queue = kue.createQueue();
const job_data = { phoneNumber: '000', message: 'Hello' };
const name = 'push_notification_code';

const job = queue.create(name, job_data).save();

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});
job.on('completed', () => { console.log('Notification job created'); });
job.on('failed', () => { console.log('Notification job failed'); });
