namespace Transport {
    export interface IVehicle{
        mark: string;
        model: string;
        vinNumber: string;
        regNumber: number;
        userInfo: string;
        showInfoCar(): string;
    }
    
    export class Vehicle implements IVehicle{
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

    export interface ICar extends IVehicle{
        body: bodyType;
        class: carClass;
    }
    
    export class Car implements ICar{
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
    
    export interface IBike extends IVehicle{
        typeRam: string;
        forSports: boolean;
    }
    
    export class Bike implements IBike{
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
}