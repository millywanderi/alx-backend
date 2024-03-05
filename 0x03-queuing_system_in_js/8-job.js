export default function createPushNotificationsJobs(jobs, queue) {
  if (Array.isArray(jobs)) {
    jobs.forEach((data) => {
      const pushThree = queue.create('push_notification_code_3', data).save((err) => {
        if (!err) console.log(`Notification job created: ${pushThree.id}`);
      });
      pushThree.on('complete', () => {
        console.log(`Notification job ${pushThree.id} completed`);
      }).on('progress', (progress) => {
        console.log(`Notification job ${pushThree.id} ${progress}% complete`);
      }).on('failed', (err) => {
        console.log(`Notification job ${pushThree.id} failed: ${err}`);
      });
    });
  } else {
    throw new Error('Jobs is not an array');
  }
}
