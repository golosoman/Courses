/*
    В процессе написания лабораторной работы ознакомиться с процедурным
    подходом к программированию и рекурсией в языке JavaScript.

    Напишите функцию, которая принимает три числовых параметра и
    возвращает произведение двух максимальных из них.
*/

function multiplicate(x, y, z) {
    const maximum = (x, y, z) => { return x >= y && x >= z ? x : y >= x && y >= z ? y : z; };

    let first_max_value = maximum(x, y, z);
    
    if (first_max_value === x) {
        return first_max_value * maximum(y, y, z);
    }
    else if (first_max_value === y) {
        return first_max_value * maximum(z, z, x);
    }
    else{
        return first_max_value * maximum(x, x, y);
    }
}