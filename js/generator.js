// Import J names from j-names.json


const jnamesdb = require('j-names.json');
console.log(jnamesdb)

function rand()
{
    let rand_int = Math.floor(Math.random() * 10);
    let rand_name = jnamesdb[rand_int];
    return this.rand_name
}
    