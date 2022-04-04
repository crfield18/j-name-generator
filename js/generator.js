// Import J names from j-names.json
const jnamesdb = require('./j-names.json')["j-names"];
let db_length = parseInt(jnamesdb.length);

// console.log(jnamesdb["j-names"][7]);

function jname() {
    let rand_int = Math.floor(Math.random() * db_length); // Generate random int between 0 and length of jnames.json
    let rand_name = jnamesdb[rand_int]; // 
    return(rand_int + ': ' + rand_name)
}
