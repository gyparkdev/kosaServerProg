/*
function run() {
  const start = Date.now();
  for (let i = 0; i < 1000000000; i++) {}
  const end = Date.now();
  console.log(end - start + 'ms');
}

run();
console.log('Done !!!')
*/

/*
function run() {
  setTimeout(() => {
    const start = Date.now();
    for (let i = 0; i < 1000000000; i++) {}
    const end = Date.now();
    console.log(end - start + 'ms'); // 1초 뒤에 콘솔에 찍혀라.
  }, 1000);
}

run();
console.log('Done !!!');
  */

/*
function run(callback) {
  setTimeout(() => {
    const start = Date.now();
    for (let i = 0; i < 1000000000; i++) {}
    const end = Date.now();
    console.log(end - start + 'ms');
    callback();
  }, 1000);
}

run(() => {
  console.log('Done !!!');
});
*/

/*
function run() {
  return new Promise((resolve, reject) => {
      setTimeout(() => {
          const start = Date.now();
          for (let i = 0; i < 1000000000; i++) {}
          const end = Date.now();
          console.log(end - start + 'ms');
          resolve();
      }, 1000);
  });
}

run().then(() => {console.log('Done !!!');});
run().then(() => {return run()}).then(() => {console.log('Done !!!');});
*/

function run() {
  return new Promise((resolve, reject) => {
      setTimeout(() => {
          const start = Date.now();
          for (let i = 0; i < 1000000000; i++) {}
          const end = Date.now();
          console.log(end - start + 'ms');
          resolve();
      }, 1000);
  });
}

async function process() {
  await run();
  await run();
  console.log('Done !!!');
}

process();