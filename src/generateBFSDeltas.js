const fs =require('fs');
function calculateManhattanDeltas(dist) {
  var manD = [[0,0]];
  function inDist(x,y) {
    if (x*x + y*y <= dist) {
    return true;
    }
    return false;
  }
  for (let k = 0; k <= Math.ceil(Math.sqrt(dist) + 2); k++){
    for (let i = k; i >= 1; i--) {
    if(inDist(i, -k+i))
        manD.push([i, -k + i]);
    }
    for (let i = 0; i >= -k + 1; i--) {
    if(inDist(i, -k-i))
     manD.push([i, -k - i]);
    }
    for (let i = -k; i <= -1; i++) {
    if(inDist(i, k+i))
     manD.push([i, k + i]);
    }
    for (let i = 0; i <= k - 1; i++) {
    if(inDist(i, k-i))
     manD.push([i, k - i]);
    }
  }
  return manD;
}

fs.writeFileSync('bfs.txt', JSON.stringify(calculateManhattanDeltas(128)));