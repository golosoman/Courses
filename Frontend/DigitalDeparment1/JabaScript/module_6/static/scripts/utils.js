const generateIntArray = (length, max) => (
    Array(length).fill().map(() => Math.floor(Math.random() * max))
);

function printElementsInMap(map_collection){
    for (let element of map_collection) {
        console.log(element); 
    }
}

function getNumberElements(arr) {
    let number_occurrences = new Map();

    for (element of arr) {
        if (number_occurrences.has(element)) {
            number_occurrences.set(element, number_occurrences.get(element) + 1);
        }
        else{
            number_occurrences.set(element, 1);
        }
    }

    return number_occurrences
}