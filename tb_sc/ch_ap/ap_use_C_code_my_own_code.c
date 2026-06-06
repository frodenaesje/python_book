// file: ap_use_C_code_my_own_code.c
#include <stdlib.h>

// Portable export macro: works on Windows, Linux and macOS
#ifdef _WIN32
    #define EXPORT __declspec(dllexport)
#else
    #define EXPORT
#endif

// Adds two integers and returns the result
EXPORT int add(int a, int b) {
    return a + b;
}

// Returns the absolute value of an integer
EXPORT int absolute_value(int x) {
    return abs(x);
}