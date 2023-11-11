#include <iostream>
#include <string>

#include "lib.hpp"
#include "include/libraryproject/libraryproject.hpp"


int main(int argc, char *argv[]) {
  auto const lib = library {};
  auto const message = "Hello12 from " + lib.name + "!";
  std::cout << message << '\n';
  printk();
  return 0; // main(argc, argv);
}
