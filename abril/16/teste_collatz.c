#include <stdio.h>
#include <assert.h>
#include "collatz.h"

void test_1();
void test_2();
void test_3();
void test_4();
void test_5();
void test_6();
void test_7();


int main() {
    test_1();
    test_2();
    test_3();
    test_4();
    test_5();
    test_6();
    test_7();
    puts("Testes passando!");
    return 0;
}

void test_1() {
    int entrada = 1;
    int saida_esperada[1] = {1};

    int *retorno = collatz(entrada);
    for (int i = 0; i < 1; ++i) {
        assert(saida_esperada[i] == retorno[i]);
    }
}

void test_2() {
    int entrada = 2;
    int saida_esperada[2] = {2, 1};

    int *retorno = collatz(entrada);
    for (int i = 0; i < 1; ++i) {
        assert(saida_esperada[i] == retorno[i]);
    }
}

void test_3() {
    int entrada = 3;
    int saida_esperada[8] = {3, 10, 5, 16, 8, 4, 2, 1};

    int *retorno = collatz(entrada);
    for (int i = 0; i < 8; ++i) {
        assert(saida_esperada[i] == retorno[i]);
    }
}

void test_4() {
    int entrada = 4;
    int saida_esperada[3] = {4, 2, 1};

    int *retorno = collatz(entrada);
    for (int i = 0; i < 3; ++i) {
        assert(saida_esperada[i] == retorno[i]);
    }
}

void test_5() {
    int entrada = 5;
    int saida_esperada[6] = {5, 16, 8, 4, 2, 1};

    int *retorno = collatz(entrada);
    for (int i = 0; i < 6; ++i) {
        assert(saida_esperada[i] == retorno[i]);
    }
}
void test_6() {
    int entrada = 6;
    int saida_esperada[9] = {6,3,10,5,16,8,4,2,1};

    int *retorno = collatz(entrada);
    for (int i = 0; i < 9; ++i) {
        assert(saida_esperada[i] == retorno[i]);
    }
}
void test_7() {
    int entrada = 7;
    int saida_esperada[17] = {7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1};

    int *retorno = collatz(entrada);
    for (int i = 0; i < 17; ++i) {
        assert(saida_esperada[i] == retorno[i]);
    }
}

