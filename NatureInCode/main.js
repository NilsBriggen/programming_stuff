var a1a1 = 0.15;
var a2a2 = 0.35;
var a1a2 = 1 - (a1a1 + a2a2);

var p = a1a1 + (a1a2/2);
var q = 1 - p;

console.log("Generation 0:", a1a1, a1a2, a2a2)

a1a1 = p*p
a1a2 = 2*p*q
a2a2 = q*q

console.log("Generation 1:", a1a1, a1a2, a2a2)