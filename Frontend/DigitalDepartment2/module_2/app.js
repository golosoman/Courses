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
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
// Task 1.1
var getMaxValueFromArr = function (array) {
    var max_value = array[0];
    array.forEach(function (element) { max_value = element >= max_value ? element : max_value; });
    return max_value;
};
var arr = [1, 20, 3, 0, 10, 7, 2];
console.log(getMaxValueFromArr(arr));
// Task 1.2
var getBoolMatrix = function (matrix) {
    var new_matrix = [];
    for (var i = 0; i < matrix.length; i++) {
        new_matrix.push([]);
        for (var j = 0; j < matrix[i].length; j++) {
            var value = matrix[i][j].length % 2 === 0 ? false : true;
            new_matrix[i].push(value);
        }
    }
    return new_matrix;
};
var my_matrix = [
    ["12312", "2323", "32323", "232323"],
    ["1232312", "2332323", "32323", "232323"],
    ["12312", "232323", "322323323", "232323"],
    ["22", "223323", "3232323", "223"],
    ["12312", "232323", "3232323", "223232323"],
    ["122312", "2312", "32323123", "23232323"]
];
console.log(getBoolMatrix(my_matrix));
//Task 2
var compareTwoNumbers = function (box) {
    var first_number_list = box[0].toString().split("").map(function (element) { return Number(element); });
    var second_number_list = box[1].toString().split("").map(function (element) { return Number(element); });
    // console.log(first_number_list, second_number_list)
    var first_sum_elements = 0;
    var second_sum_elements = 0;
    first_number_list.forEach(function (element) { first_sum_elements += element; });
    second_number_list.forEach(function (element) { second_sum_elements += element; });
    // console.log(first_sum_elements, second_sum_elements)
    return first_sum_elements === second_sum_elements ? true : false;
};
console.log(compareTwoNumbers([14, 23]));
//Task 3
var RNK;
(function (RNK) {
    RNK["Adenin"] = "\u0410";
    RNK["Guanin"] = "\u0413";
    RNK["Citazin"] = "\u0426";
    RNK["Timin"] = "\u0422";
})(RNK || (RNK = {}));
;
var mes = RNK.Adenin + RNK.Citazin + RNK.Guanin + RNK.Timin + RNK.Citazin + RNK.Guanin;
console.log(mes);
//Task 4
var Pet = /** @class */ (function () {
    function Pet() {
        this.name = 'Some pet';
        this.age = -1;
    }
    Pet.prototype.speak = function () {
        return "No speak. I am fish!";
    };
    return Pet;
}());
var Dog = /** @class */ (function (_super) {
    __extends(Dog, _super);
    function Dog() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.label = "AngryHunter";
        _this.age = 8;
        return _this;
    }
    Dog.prototype.speak = function () {
        return "Yaw-Gaw!";
    };
    return Dog;
}(Pet));
var Cat = /** @class */ (function (_super) {
    __extends(Cat, _super);
    function Cat() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.name = 'Barsik';
        _this.age = 2;
        return _this;
    }
    Cat.prototype.speak = function () {
        return "Miyau!";
    };
    return Cat;
}(Pet));
function printInfo(param) {
    console.log(param);
}
printInfo(new Dog());
printInfo(new Cat());
var my_obj = {
    rnk: [RNK.Adenin, RNK.Citazin, RNK.Guanin, RNK.Timin, RNK.Citazin, RNK.Guanin],
    FIO: "Акакиев Акакий Акакиевич",
    phone: "+79220967829"
};
console.log(JSON.stringify(my_obj));
