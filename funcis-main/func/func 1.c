//Минимум. Опишите функцию с именем min, которая вычисляет минимальное из двух чисел, переданных в неё.
//Входные данные: Два целых числа. Выходные данные: Одно целое число - минимум из чисел, переданных в функцию.
#include <stdio.h>
int min(int a, int b) {
    int mn;
    if (a > b)
        mn = a;
    if (a < b)
        mn = b;
    return mn;
}

int main(){
    int v, z;
    scanf("%d %d", &v, &z);
    
   printf("%d", min(v,z));
    
    return 0;
}