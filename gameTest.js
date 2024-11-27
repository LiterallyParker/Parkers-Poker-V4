const runPokerGame = () => {
    const { exec } = require("child_process");

    return new Promise((resolve, reject) => {
        exec('python3 ./poker/__init__.py', (error, stdout, stderr) => {
            if (error) {
                console.error('Exec error:', error);
                reject(`Error executing python script: ${error.message}`);
                return;
            };

            if (stderr) {
                console.error(`stderr: ${stderr}`);
            };

            resolve(stdout); // Resolve with the output
        });
    });
};

runPokerGame()
    .then(result => {
        console.log(result);
    })
    .catch(err => {
        console.error('Error running poker game:', err);
    });