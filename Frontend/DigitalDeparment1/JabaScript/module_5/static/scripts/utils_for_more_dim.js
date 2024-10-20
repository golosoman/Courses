const generateIntArray = (length, max) => (
    Array(length).fill().map(() => Math.floor(Math.random() * max))
);

const generateMatrix = (row, col, max) => (
    Array(row).fill().map(() => generateIntArray(col, max))
);

function getArrMinEvenElements(matrix) {
    let new_arr = [];
    
    for (row of matrix) {
        let min_even_element = null;

        for (element of row) {
            if (element % 2 === 0) {
                if (element < min_even_element || min_even_element === null) {
                    min_even_element = element;
                }
            }
        }

        if (min_even_element !== null) {
            new_arr.push(min_even_element);
        }
    }
    return new_arr;
}