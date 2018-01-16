function findKey(val,object){
    for (var key in object) {
        if(object[key] == val) {
            return key}
    }
 return false
}

function findRarestValue(obj) {

var counts = {};
var ages = Object.values(obj)

ages.forEach(function(x) {
  counts[x] = (counts[x] || 0 )+1;})

var countsArray = Object.values(counts)
var rarest = Math.min.apply( Math, countsArray )
var keyFound = findKey(rarest, counts)

return keyFound
}
