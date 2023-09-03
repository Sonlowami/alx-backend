import kue from 'kue';

const queue = kue.createQueue();
const target = 'push_notification_code';

function sendNotification(phoneNumber, message) {
  console.log(
    `Sending notification to ${phoneNumber} with message: ${message}`
  );
}
queue.process(target, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
