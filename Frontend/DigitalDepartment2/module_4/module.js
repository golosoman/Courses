"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Transport = void 0;
var Transport;
(function (Transport) {
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
    Transport.Vehicle = Vehicle;
    var bodyType;
    (function (bodyType) {
        bodyType["sedan"] = "\u0421\u0435\u0434\u0430\u043D";
        bodyType["compartment"] = "\u041A\u0443\u043F\u0435";
        bodyType["crossover"] = "\u041A\u0440\u043E\u0441\u0441\u043E\u0432\u0435\u0440";
    })(bodyType = Transport.bodyType || (Transport.bodyType = {}));
    var carClass;
    (function (carClass) {
        carClass["a"] = "A";
        carClass["b"] = "B";
        carClass["c"] = "C";
    })(carClass = Transport.carClass || (Transport.carClass = {}));
    var Car = /** @class */ (function () {
        function Car(_body, _class) {
            this._body = _body;
            this._class = _class;
        }
        Object.defineProperty(Car.prototype, "body", {
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
    }());
    Transport.Car = Car;
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
    Transport.Bike = Bike;
})(Transport || (exports.Transport = Transport = {}));
