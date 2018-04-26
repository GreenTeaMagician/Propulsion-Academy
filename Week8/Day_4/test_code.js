var arr = [1, 2, 3, 4, 5, 6]

function has(array, element) {
    for(i=0;i<=array.length;i++)    {
        if (element === array[i])   {
            return true
        }
    }
    return false
}

console.log(has(arr, 3))
