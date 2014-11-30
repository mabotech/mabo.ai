

var crypto =  require('crypto') ;

function sha1(password){
    
    var hashes = crypto.getHashes();

    //sha1
    var shasum = crypto.createHash('sha1');

    var v = shasum.update(password)
    
    //base64
    return '{SHA}' + v.digest('base64')
    
}

v = sha1("password")

console.log(v)