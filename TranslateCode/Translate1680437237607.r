LENGTH = 1048576

gcd <- function(a, b) {
  while (b) {
    a <- b
    b <- a %% b
  }
  return(a)
}

key_gen <- function() {
  x <- sample(10^(LENGTH-1):10^LENGTH, 1)
  while (gcd(10^256, x) != 1) {
    x <- sample(10^(LENGTH-1):10^LENGTH, 1)
  }
  return(x)
}

key_gen()
