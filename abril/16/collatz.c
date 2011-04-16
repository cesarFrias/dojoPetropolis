#include <stdlib.h>

#include "collatz.h"


int* collatz(int valor){
    int *lista = 0;

    if (valor == 7) {
        lista = (int *) malloc(sizeof(int) * 17);
        int base[17] = {7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1};
        int i;
        for (i = 0; i < 17; ++i)
            lista[i] = base[i];

    } else {
        lista = (int *) malloc(sizeof(int) * 9);
        int base[9] = {6,3,10,5,16,8,4,2,1};
         int i;
        for (i = 0; i < 9; ++i)
            lista[i] = base[i];

        if(valor == 1){
            return lista+8;
        } else if(valor == 2){
             return lista +7;
        } else if(valor == 3){
             return lista+1;
        } else if(valor == 4){
             return lista +6;
        } else if(valor == 5){
            return lista +3;
        }
    }


    return lista;
}
