module.exports = {
    networks: {
    development: {
    host: "172.16.68.190",   
    port: 8545,            
    network_id: "*",       
    },
  },
  mocha: {
    // timeout: 100000
  },
  // Configure your compilers
  compilers: {
    solc: {
      version: "0.8.10",   
    } 
  },
};