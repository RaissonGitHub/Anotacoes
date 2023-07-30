const os = require("os"); // carregar o modulo operacional system
console.log(os.version()); // imprime a vesao do os
console.log(os.machine()); // imprime a arquitetura do os
console.log(os.release()); // imprime o release do os
console.log(os.cpus()); // imprime os cpus do os
console.log(os.cpus()[0].model); // imprime os modelo do cpu1

const fs = require("fs"); // carregar o modulo file system
console.log(fs); //imprimir o conteudo do modulo fs
