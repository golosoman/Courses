/*
    1) Перейдите на сайт Node.js. Выполните установку программы версии,
    рекомендованной для большинства пользователей.

    2) Реализуйте стрелочную функцию и выполните её вызов для
    подтверждения корректности логики её работы

        Вариант №1. Реализуйте стрелочную функцию, возвращающую
    строку, составленную (см. конкатенация) из 2х чисел, передаваемых
    в качестве параметров.

    3) Выполните создание объектов – констант (const) и переменных (let) с
    указанием различных встроенных и специальных типов. Название
    переменной может быть любым. Количество объектов не более 8.

    4) Скопируйте и выполните преобразование объекта data к формату JSON в
    виде строки. Результат преобразования следует вывести в консоль.

    interface Entity {
    id: number;
    }
    interface ToJsonStringify extends
    Entity {
    name: string;
    surname?: string;
    }
    const data: ToJsonStringify = {
    id: 1,
    name: "Василий",
    }
*/

// Task 2
const concatTwoString = (first_number: number, second_number: number) => {
    return String(first_number) + String(second_number);
};

console.log(concatTwoString(1,2));

// Task 3

interface Student{
    name: string;
    num_ticket: number;
    course: number;
    faculty: string;
}

const first_student: Student = {
    name: "Васильев Василий Васильевич",
    num_ticket: 2192023,
    course: 3,
    faculty: "Информатики и кибернетики",
}

let num: number = 10;

let sentence = "Маленький шаг";

enum Season {
    Winter = "Зима",
    Spring = "Весна",
    Summer = "Лето",
    Autumn = "Осень "
    };    

// Task 4

interface Entity {
    id: number;
}

interface ToJsonStringify extends Entity {
    name: string;
    surname?: string;
}

const data: ToJsonStringify = {
    id: 1,
    name: "Василий",
}

const jsonData: string = JSON.stringify(data);

console.log(jsonData);