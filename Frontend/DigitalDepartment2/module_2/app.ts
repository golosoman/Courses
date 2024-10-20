/*
    Задание № 2 включает в себя 6 разделов:
    1) Работа со структурой Array (Массив): одномерными и двумерными
    Вариант №1. Реализовать метод, возвращающий максимальное
    число из массива вещественных чисел.

    Вариант №6. Реализовать метод, возвращающий матрицу булевых
    значений, составленный из матрицы строк. Если количество
    символов в элементе матрицы нечетное, то значение true, иначе
    false.

    2) Работа со структурой Tuple (Кортеж)
    Вариант №6. Создайте кортеж, который может содержать только 2
    числовых значения. Реализуйте метод, возвращающий истину, если
    сумма цифр 1го числового значения совпадает с суммой цифр 2го
    числового значения.


    3) Работа со структурой Enum (Перечисление)
    Создайте тип перечисление для азотистых оснований
    для РНК (Аденин, Гуанин и т.д). Выведите какой-либо тип
    аминокислоты в консоль.

    4) Работа с Generics (Дженерик)
    Вставьте следующий код в ваш проект: 
    --- КОД ВСТАВЛЕН НИЖЕ ---

    Реализуйте метод, который будет выводить информацию в
    консоль о создаваемом объекте типа Cat или Dog, применяя
    Обобщенный тип, ограниченный типом Pet.

    5) Реализация кастомных (собственных) типов/
    Создайте тип с применением перечисления из 3го задания (для
    использования его в качестве типа поля, для некоторых случаев
    возможно его использование при реализации массива). Добавьте
    собственные поля стандартных типов, корректно характеризующие ту
    или иную предметную область, совпадающую с вашим типом
    перечисления. Создайте объект на основе вашего типа и выведите его в
    консоль в формате JSON.

*/

// Task 1.1
const getMaxValueFromArr = (array: number[]) =>{
    let max_value: number = array[0];
    array.forEach(element => { max_value = element >= max_value? element: max_value; });
    return max_value;
}

const arr: number[] = [1, 20, 3, 0, 10, 7, 2];

console.log(getMaxValueFromArr(arr))

// Task 1.2
const getBoolMatrix = (matrix: string[][]) => {
    let new_matrix: boolean[][] = [];
    for (let i = 0; i < matrix.length; i++) {
        new_matrix.push([]);
        for (let j = 0; j < matrix[i].length; j++) {
            let value = matrix[i][j].length % 2 === 0? false: true;
            new_matrix[i].push(value);
        }
    }
    return new_matrix;
}

const my_matrix: string[][] = [
    ["12312", "2323", "32323", "232323"],
    ["1232312", "2332323", "32323", "232323"],
    ["12312", "232323", "322323323", "232323"],
    ["22", "223323", "3232323", "223"],
    ["12312", "232323", "3232323", "223232323"],
    ["122312", "2312", "32323123", "23232323"]
];

console.log(getBoolMatrix(my_matrix));

//Task 2
const compareTwoNumbers = (box: [number, number]) => {
    let first_number_list: number[] = box[0].toString().split("").map((element) => Number(element));
    let second_number_list: number[] = box[1].toString().split("").map((element) => Number(element));

    // console.log(first_number_list, second_number_list)

    let first_sum_elements = 0;
    let second_sum_elements = 0;

    first_number_list.forEach(element => { first_sum_elements += element; });
    second_number_list.forEach(element => { second_sum_elements += element; });

    // console.log(first_sum_elements, second_sum_elements)

    return first_sum_elements === second_sum_elements? true: false;
}

console.log(compareTwoNumbers([14, 23]));

//Task 3
enum RNK{
    Adenin = "А", 
    Guanin = "Г", 
    Citazin = "Ц", 
    Timin = "Т"
};

let mes: string = RNK.Adenin + RNK.Citazin + RNK.Guanin + RNK.Timin + RNK.Citazin + RNK.Guanin;

console.log(mes);

//Task 4
class Pet {
    name: string = 'Some pet'
    age: number = -1
    speak() {
        return "No speak. I am fish!";
    }
}

class Dog extends Pet {
    label = "AngryHunter";
    age = 8;
    speak() {
        return "Yaw-Gaw!";
    }
}

class Cat extends Pet {
    name = 'Barsik';
    age = 2;
    speak() {
        return "Miyau!";
    }
}

function printInfo<T extends Pet>(param: T): void {
    console.log(param);
}

printInfo(new Dog());
printInfo(new Cat());

//Task 5

interface MyObject {
    rnk: RNK[];
    FIO: string;
    phone: string;
}

const my_obj = {
    rnk: [RNK.Adenin, RNK.Citazin, RNK.Guanin, RNK.Timin, RNK.Citazin, RNK.Guanin],
    FIO: "Акакиев Акакий Акакиевич",
    phone: "+79220967829"
};

console.log(JSON.stringify(my_obj));