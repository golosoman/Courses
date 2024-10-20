const generateFloatArray = (length, max) => (
    Array(length).fill().map(() => (Math.random() * max / 10))
);

function getMinMaxByIndexes(arr){
    let indexes = {"max": 0, "min": 0};

    for (let index = 0; index < arr.length; index++) {
        if (arr[indexes["max"]] <= arr[index]) {
            indexes["max"] = index;
        }

        if (arr[indexes["min"]] >= arr[index]) {
            indexes["min"] = index;
        }
    }

    return indexes;
}

function getStartEndIndex(indexes) {
    let start;
    let end;

    if (indexes["max"] > indexes["min"]) {
        end = indexes["max"];
        start = indexes["min"];
    }
    else{
        start = indexes["max"];
        end = indexes["min"];
    }

    return [start, end];
}

// Попробовать мап
function multiplicateElementsInArr(arr){
    let indexes = getMinMaxByIndexes(arr);
    let [start, end] = getStartEndIndex(indexes);
    let slice_arr = arr.slice(start + 1, end);

    console.log(start, end, slice_arr);

    if (slice_arr.length > 0) {
        let mul_elements = 1;

        for (let element of slice_arr) {
            // console.log(element);
            mul_elements *= element;
        }
    
        return mul_elements;
    }
    else{
        return "Нет таких элементов!";
    }
}