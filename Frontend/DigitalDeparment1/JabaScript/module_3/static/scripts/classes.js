class Mark{
    constructor(subject, mark){
        this.subject = subject;
        this.mark = mark;
    }

    greeting(){
        console.log(`Предмет: ${this.subject}\nОценка: ${this.mark}`);
    }
}

class Student{
    constructor(first_name, second_name, arr_marks){
        this.first_name = first_name;
        this.second_name = second_name;
        this.arr_marks = arr_marks;
    }

    getMeanMark(){
        let sum = 0;
        for (let current_mark of this.arr_marks) {
            sum += current_mark.mark;
        }
        return sum / this.arr_marks.length;
    }

    getMarks(subject){
        let marks = [];
        for (let current_mark of this.arr_marks) {
            if (current_mark.subject === subject) {
                marks.push(current_mark.mark);
            }
        }
        return marks;
    }

    addMark(subject, mark){
        this.arr_marks.push({"subject": subject, "mark": mark});
    }

    delMarks(subject){
        let indexes = []
        
        for (let index = 0; index < this.arr_marks.length; index++) {
            if (this.arr_marks[index].subject === subject) {
                indexes.push(index);
            }   
        }

        for (let index of indexes.reverse()) {
           delete this.arr_marks[index];
        }
    }

    getAllElementFromArrMarks(){
        let sentence = "";
        for (let current_mark of this.arr_marks) {
            sentence += `${current_mark.subject}: ${current_mark.mark}\n`;
        }
        return sentence;
    }

    greeting(){
        console.log(`Привет! Я ${this.first_name} ${this.second_name} мои оценки ниже:\n${this.getAllElementFromArrMarks()}`);
    }
}
