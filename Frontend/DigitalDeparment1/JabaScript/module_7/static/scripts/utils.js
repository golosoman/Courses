const generateIntArray = (length, max) => (
    [...new Array(length)].map(() => Math.floor(Math.random() * max))
);

function shellSort(arr) {
    let gap = Math.floor(arr.length / 2);

    while (gap > 0) {
        for (let index = gap; index < arr.length; index++) {
            let current_value = arr[index];
            let position = index;

            while (position >= gap && arr[position - gap] > current_value) {
                arr[position] = arr[position - gap];
                position -= gap;
                arr[position] = current_value;
            }
        }
        gap = Math.floor(gap / 2);
    }
    return arr;
}

function shellForArrStudents(arr){
    let gap = Math.floor(arr.length / 2);

    while (gap > 0) {
        for (let index = gap; index < arr.length; index++) {
            let current_value = arr[index];
            let position = index;

            while (position >= gap && arr[position - gap].getMeanMark() < current_value.getMeanMark()) {
                arr[position] = arr[position - gap];
                position -= gap;
                arr[position] = current_value;
            }
        }
        gap = Math.floor(gap / 2);
    }
    return arr;
}

function printMeanMark(arr_students){
    for (student of arr_students) {
        console.log(`${student.first_name} ${student.second_name} средняя оценка: ${student.getMeanMark()}`);
    }
}