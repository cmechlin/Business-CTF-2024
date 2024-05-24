const profiler = require("v8-profiler-next");
const fs = require("fs");

profiler.startProfiling("Heap Snapshot");

setTimeout(() => {
  const profile = profiler.stopProfiling("Heap Snapshot");
  profile.export((error, result) => {
    fs.writeFileSync("heap-snapshot.heapsnapshot", result);
    profile.delete();
  });
}, 5000); // Adjust the timeout as needed to capture the desired state
