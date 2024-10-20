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

//Task 1
enum documents{
    passport = "Паспорт",
    driver_license = "Права",
    technical_passport = "Технический паспорт"
};

interface IOwner{
    lastName: string;
    firstName: string;
    middleName: string;
    dateBirth: string;
    typeDocument: documents;
    serialDocument: number;
    numberDocument: number;
    showInfo(): string;
}

class Owner implements IOwner{
    constructor(private _lastName, private _firstName, 
                private _middleName, private _dateBirth, 
                private _typeDocument, private _serialDocument, 
                private _numberDocument) { }
    
    public get lastName(): string{ return this._lastName; }
    public set lastName(name: string){ this._lastName = name; }

    public get firstName(): string{ return this._firstName; }
    public set firstName(name: string){ this._firstName = name; }

    public get middleName(): string{ return this._middleName; }
    public set middleName(name: string){ this._middleName = name; }

    public get dateBirth(): string{ return this._lastName; }
    public set dateBirth(date: string){ this._lastName = date; }

    public get typeDocument(): documents{ return this._typeDocument; }
    public set typeDocument(type: documents){ this._typeDocument = type; }

    public get serialDocument(): number{ return this._serialDocument; }
    public set serialDocument(serial: number){ this._serialDocument = serial; }

    public get numberDocument(): number{ return this._numberDocument; }
    public set numberDocument(number: number){ this._numberDocument = number; }

    public showInfo() {
        return `ФИО и дата: ${this._lastName} ${this._firstName} ${this._middleName} ${this._dateBirth}\n
                Данные по документу: ${this._typeDocument} ${this._serialDocument} ${this._numberDocument}`;
    }
}

interface IVehicle{
    mark: string;
    model: string;
    vinNumber: string;
    regNumber: number;
    userInfo: string;
    showInfoCar(): string;
}

class Vehicle implements IVehicle{
    constructor(private _mark, private _model, private _vinNumber, private _regNumber, private _userInfo) { }

    public get mark(): string{ return this._mark; }
    public set mark(name: string){ this._mark = name; }

    public get model(): string{ return this._model; }
    public set model(name: string){ this._model = name; }

    public get vinNumber(): string{ return this._vinNumber; }
    public set vinNumber(number: string){ this._vinNumber = number; }

    public get regNumber(): number{ return this._regNumber; }
    public set regNumber(number: number){ this._regNumber = number; }

    public get userInfo(): string{ return this._userInfo; }
    public set userInfo(info: string){ this._userInfo = info; }

    showInfoCar(){ return `Автомобиль: ${this._mark} ${this._model} ${this._vinNumber} ${this._regNumber} ${this._userInfo}`; }
}

//Task 2
enum bodyType{
    sedan = "Седан",
    compartment = "Купе",
    crossover = "Кроссовер"
}

enum carClass{
    a = "A",
    b = "B",
    c = "C"
}

interface ICar extends IVehicle{
    body: bodyType;
    class: carClass;
}

class Car implements ICar{
    mark: string;
    model: string;
    vinNumber: string;
    regNumber: number;
    userInfo: string;

    constructor(private _body, private _class){ }

    public get body(): bodyType{ return this._body; }
    public set body(n: bodyType){ this._body = n; }

    public get class(): carClass{ return this._class; }
    public set class(n: carClass){ this._class = n; }

    showInfoCar(){ return `${this.mark} ${this.model} ${this.vinNumber} ${this.regNumber} ${this._body} ${this._class}`; }
}

interface IBike extends IVehicle{
    typeRam: string;
    forSports: boolean;
}

class Bike implements IBike{
    mark: string;
    model: string;
    vinNumber: string;
    regNumber: number;
    userInfo: string;

    constructor(private _typeRam, private _forSports){ }

    public get typeRam(): string{ return this._typeRam; }
    public set typeRam(type: string){ this._typeRam = type; }

    public get forSports(): boolean{ return this._forSports; }
    public set forSports(value: boolean){ this._forSports = value; }

    showInfoCar(){ return `${this.mark} ${this.model} ${this.vinNumber} ${this.regNumber} ${this._typeRam} ${this._forSports}`; }
}

interface IVehicleStorage<T extends IVehicle> {
    dataCreate: string;
    infoAboutVehicle: T[];
    getElements(arr: T[]): string;
}

class VehicleStorage<T extends IVehicle> {
    constructor(private _dataCreate, private _infoAboutVehicle) { }

    public get dataCreate(): string{ return this._dataCreate; }
    public set dataCreate(date: string){ this._dataCreate = date; }

    public get infoAboutVehicle(): T[]{ return this._infoAboutVehicle; }
    public set infoAboutVehicle(info: T[]){ this._infoAboutVehicle = info; }

    getElements(arr: T[]){ return arr.join(" "); }
}