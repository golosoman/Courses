const getAllMarks = (arr_marks) => {
    let sentence = "";
    for (let mark of arr_marks) {
        sentence += `${mark["subject"]}: ${mark["mark"]}\n` 
    }
    return sentence;
};

const printToConsoleStudent = (student) => {
    console.log(`Привет! Я ${student["first_name"]} ${student["second_name"]} мои оценки ниже:\n${getAllMarks(student["arr_marks"])}`);
};

const toJSON = (object) => { return JSON.stringify(object); };