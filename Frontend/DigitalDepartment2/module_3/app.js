/*
    Задание № 3 включает в себя 3 раздела:
    1) Реализация класса, реализация интерфейса

    2) Работа с наследованием в классах и интерфейсах

    3) Работа с обобщениями классов и интерфейсов

    1) Реализуйте интерфейс Владелец (Owner) со следующими свойствами:
        • Фамилия
        • Имя
        • Отчество
        • Дата рождения
        • Тип документа (использовать отдельный тип перечисления)
        • Серия документа
        • Номер документа
        • Метод, выводящий в консоль все вышеперечисленные сведения о
        владельце
    Реализуйте интерфейс Транспортное средство (Vehicle) со следующими
    свойствами и определениями методов:
        • Марка
        • Модель
        • Год выпуска
        • VIN-номер
        • Регистрационный номер
        • Сведения о владельце
        • Метод, выводящий в консоль сведения о транспортном средстве
    без сведений о владельце
    Создайте класс, реализующий интерфейс Транспортное средство.
    Создайте класс, реализующий интерфейс Владелец.
    Каждый класс должен иметь конструктор, который имеет все
    необходимые параметры для инициализации объекта типа,
    Примечание! Поля внутри класса должны быть приватными. Для
    получения доступа к их содержимому и модификации следует
    использовать Геттеры и Сеттеры.

    2) Создайте интерфейс Автомобиль (Car), наследующий интерфейс
    Транспортное средство с свойствами и определениями методов:
        • Тип кузова (как перечисление)
        • Класс автомобиля (как перечисление)
    Создайте класс, реализующий интерфейс Автомобиль. Метод,
    выводящий в консоль сведения о транспортном средстве без сведений о
    владельце следует модифицировать для вывода дополнительных полей
    класса Автомобиль.
    Создайте интерфейс Мотоцикл (Motorbike), наследующий интерфейс
    Транспортное средство с свойствами и определениями методов:
        • Тип рамы (строка)
        • Для спорта (булево значение)
    Создайте класс, реализующий интерфейс Мотоцикл. Метод, выводящий в
    консоль сведения о транспортном средстве без сведений о владельце
    следует модифицировать для вывода дополнительных полей класса
    Мотоцикл.

    3) Реализуйте интерфейс Хранилище (VehicleStorage) с обобщением типа T,
    ограниченное типом Транспортное средство. Хранилище содержит
    следующие свойства и определения методов:
        • Дата создания хранилища,
        • Массив T, хранящий сведения о тех или иных типах Транспортных
        средств,
        • Метод, возвращающий все элементы массива типа Т.
        Создайте класс, реализующий интерфейс Хранилище с аналогичным
        обобщением, как в интерфейсе.

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
//Task 1
var documents;
(function (documents) {
    documents["passport"] = "\u041F\u0430\u0441\u043F\u043E\u0440\u0442";
    documents["driver_license"] = "\u041F\u0440\u0430\u0432\u0430";
    documents["technical_passport"] = "\u0422\u0435\u0445\u043D\u0438\u0447\u0435\u0441\u043A\u0438\u0439 \u043F\u0430\u0441\u043F\u043E\u0440\u0442";
})(documents || (documents = {}));
;
var Owner = /** @class */ (function () {
    function Owner(_lastName, _firstName, _middleName, _dateBirth, _typeDocument, _serialDocument, _numberDocument) {
        this._lastName = _lastName;
        this._firstName = _firstName;
        this._middleName = _middleName;
        this._dateBirth = _dateBirth;
        this._typeDocument = _typeDocument;
        this._serialDocument = _serialDocument;
        this._numberDocument = _numberDocument;
    }
    Object.defineProperty(Owner.prototype, "lastName", {
        get: function () { return this._lastName; },
        set: function (name) { this._lastName = name; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Owner.prototype, "firstName", {
        get: function () { return this._firstName; },
        set: function (name) { this._firstName = name; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Owner.prototype, "middleName", {
        get: function () { return this._middleName; },
        set: function (name) { this._middleName = name; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Owner.prototype, "dateBirth", {
        get: function () { return this._lastName; },
        set: function (date) { this._lastName = date; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Owner.prototype, "typeDocument", {
        get: function () { return this._typeDocument; },
        set: function (type) { this._typeDocument = type; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Owner.prototype, "serialDocument", {
        get: function () { return this._serialDocument; },
        set: function (serial) { this._serialDocument = serial; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Owner.prototype, "numberDocument", {
        get: function () { return this._numberDocument; },
        set: function (number) { this._numberDocument = number; },
        enumerable: false,
        configurable: true
    });
    Owner.prototype.showInfo = function () {
        return "\u0424\u0418\u041E \u0438 \u0434\u0430\u0442\u0430: ".concat(this._lastName, " ").concat(this._firstName, " ").concat(this._middleName, " ").concat(this._dateBirth, "\n\n                \u0414\u0430\u043D\u043D\u044B\u0435 \u043F\u043E \u0434\u043E\u043A\u0443\u043C\u0435\u043D\u0442\u0443: ").concat(this._typeDocument, " ").concat(this._serialDocument, " ").concat(this._numberDocument);
    };
    return Owner;
}());
var Vehicle = /** @class */ (function () {
    function Vehicle(_mark, _model, _vinNumber, _regNumber, _userInfo) {
        this._mark = _mark;
        this._model = _model;
        this._vinNumber = _vinNumber;
        this._regNumber = _regNumber;
        this._userInfo = _userInfo;
    }
    Object.defineProperty(Vehicle.prototype, "mark", {
        get: function () { return this._mark; },
        set: function (name) { this._mark = name; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Vehicle.prototype, "model", {
        get: function () { return this._model; },
        set: function (name) { this._model = name; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Vehicle.prototype, "vinNumber", {
        get: function () { return this._vinNumber; },
        set: function (number) { this._vinNumber = number; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Vehicle.prototype, "regNumber", {
        get: function () { return this._regNumber; },
        set: function (number) { this._regNumber = number; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Vehicle.prototype, "userInfo", {
        get: function () { return this._userInfo; },
        set: function (info) { this._userInfo = info; },
        enumerable: false,
        configurable: true
    });
    Vehicle.prototype.showInfoCar = function () { return "\u0410\u0432\u0442\u043E\u043C\u043E\u0431\u0438\u043B\u044C: ".concat(this._mark, " ").concat(this._model, " ").concat(this._vinNumber, " ").concat(this._regNumber, " ").concat(this._userInfo); };
    return Vehicle;
}());
//Task 2
var bodyType;
(function (bodyType) {
    bodyType["sedan"] = "\u0421\u0435\u0434\u0430\u043D";
    bodyType["compartment"] = "\u041A\u0443\u043F\u0435";
    bodyType["crossover"] = "\u041A\u0440\u043E\u0441\u0441\u043E\u0432\u0435\u0440";
})(bodyType || (bodyType = {}));
var carClass;
(function (carClass) {
    carClass["a"] = "A";
    carClass["b"] = "B";
    carClass["c"] = "C";
})(carClass || (carClass = {}));
// class Car implements ICar{
//     mark: string;
//     model: string;
//     vinNumber: string;
//     regNumber: number;
//     userInfo: string;
//     constructor(private _body, private _class){ }
//     public get body(): bodyType{ return this._body; }
//     public set body(n: bodyType){ this._body = n; }
//     public get class(): carClass{ return this._class; }
//     public set class(n: carClass){ this._class = n; }
//     showInfoCar(){ return `${this.mark} ${this.model} ${this.vinNumber} ${this.regNumber} ${this._body} ${this._class}`; }
// }
var Car = /** @class */ (function (_super) {
    __extends(Car, _super);
    function Car(_mark, _model, _vinNumber, _regNumber, _userInfo, _body, _class) {
        var _this = _super.call(this, _mark, _model, _vinNumber, _regNumber, _userInfo) || this;
        _this._body = _body;
        _this._class = _class;
        return _this;
    }
    Object.defineProperty(Car.prototype, "mark", {
        get: function () { return _super.prototype.mark; },
        set: function (name) { _super.prototype.mark = name; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Car.prototype, "model", {
        get: function () { return _super.prototype.model; },
        set: function (name) { _super.prototype.model = name; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Car.prototype, "vinNumber", {
        get: function () { return _super.prototype.vinNumber; },
        set: function (number) { _super.prototype.vinNumber = number; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Car.prototype, "regNumber", {
        get: function () { return _super.prototype.regNumber; },
        set: function (number) { _super.prototype.regNumber = number; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Car.prototype, "body", {
        // public get userInfo(): string{ return super.userInfo; }
        // public set userInfo(info: string){ super.userInfo = info; }
        get: function () { return this._body; },
        set: function (n) { this._body = n; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Car.prototype, "class", {
        get: function () { return this._class; },
        set: function (n) { this._class = n; },
        enumerable: false,
        configurable: true
    });
    Car.prototype.showInfoCar = function () { return "".concat(this.mark, " ").concat(this.model, " ").concat(this.vinNumber, " ").concat(this.regNumber, " ").concat(this._body, " ").concat(this._class); };
    return Car;
}(Vehicle));
var Bike = /** @class */ (function () {
    function Bike(_typeRam, _forSports) {
        this._typeRam = _typeRam;
        this._forSports = _forSports;
    }
    Object.defineProperty(Bike.prototype, "typeRam", {
        get: function () { return this._typeRam; },
        set: function (type) { this._typeRam = type; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Bike.prototype, "forSports", {
        get: function () { return this._forSports; },
        set: function (value) { this._forSports = value; },
        enumerable: false,
        configurable: true
    });
    Bike.prototype.showInfoCar = function () { return "".concat(this.mark, " ").concat(this.model, " ").concat(this.vinNumber, " ").concat(this.regNumber, " ").concat(this._typeRam, " ").concat(this._forSports); };
    return Bike;
}());
var VehicleStorage = /** @class */ (function () {
    function VehicleStorage(_dataCreate, _infoAboutVehicle) {
        this._dataCreate = _dataCreate;
        this._infoAboutVehicle = _infoAboutVehicle;
    }
    Object.defineProperty(VehicleStorage.prototype, "dataCreate", {
        get: function () { return this._dataCreate; },
        set: function (date) { this._dataCreate = date; },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(VehicleStorage.prototype, "infoAboutVehicle", {
        get: function () { return this._infoAboutVehicle; },
        set: function (info) { this._infoAboutVehicle = info; },
        enumerable: false,
        configurable: true
    });
    VehicleStorage.prototype.getElements = function (arr) { return arr.join(" "); };
    return VehicleStorage;
}());
