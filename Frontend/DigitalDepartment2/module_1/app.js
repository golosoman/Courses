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
var concatTwoString = function (first_number, second_number) {
    return String(first_number) + String(second_number);
};
console.log(concatTwoString(1, 2));
var first_student = {
    name: "Васильев Василий Васильевич",
    num_ticket: 2192023,
    course: 3,
    faculty: "Информатики и кибернетики",
};
var num = 10;
var sentence = "Маленький шаг";
var Season;
(function (Season) {
    Season["Winter"] = "\u0417\u0438\u043C\u0430";
    Season["Spring"] = "\u0412\u0435\u0441\u043D\u0430";
    Season["Summer"] = "\u041B\u0435\u0442\u043E";
    Season["Autumn"] = "\u041E\u0441\u0435\u043D\u044C ";
})(Season || (Season = {}));
;
var data = {
    id: 1,
    name: "Василий",
};
var jsonData = JSON.stringify(data);
console.log(jsonData);
