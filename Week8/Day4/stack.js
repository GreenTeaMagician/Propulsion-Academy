//Javascript code creating specific datastructures: Queues, Stacks and Sets, with tests

class queue {
    constructor(array) {
        this.array = array
        this.copy = []
    }

    putIn(thing) {//enqueue(element)
        this.array[this.array.length] = thing
        return this.array
    }

    takeOut() { //dequeue()
        this.copy = []
        for (var i = 0; i <= this.array.length - 2; i++) {
            this.copy[i] = this.array[i + 1]
        }
        this.array = this.copy
        return this.array
    }

    top() { //first()
        return this.array[0]
    }

    isEmpty() {
        return this.array.length === 0 ? true : false
    }

    clear() {
        this.array = []
        return this.array
    }
}

class stack {
    constructor(array) {
        this.array = array
        this.copy = []
    }

    putIn(thing) { //push(element)
        this.array[this.array.length] = thing
        return this.array
    }

    takeOut() { //pop()
        this.copy = []
        for (var i = 0; i <= this.array.length - 2; i++) {
            this.copy[i] = this.array[i]
        }
        this.array = this.copy
        return this.array
    }

    top() {
        return this.array[0]
    }

    isEmpty() {
        return this.array.length === 0 ? true : false
    }

    clear() {
        this.array = []
        return this.array
    }
}

class set {
    constructor(array) {
        this.array = array
        this.copy = []
        this.arNum = 0
    }

    putIn(thing) { //insert(element)
        for (var i = 0; i <= this.array.length - 1; i++) {
            if (thing === this.array[i]) {
                return 'Element not added! Element already set.'
            }
        }
        this.array.push(thing)
        return this.array
    }

    takeOut(thing) { //remove()
        this.copy = []
        for (var i = 0; i <= this.array.length - 1; i++) {
            if (thing === this.array[i]) {
                for (var j = i; j < this.array.length-1; j++) {
                    this.copy[j] = this.array[j + 1]
                }
                this.array = this.copy
                return this.array
            }
            this.copy[i] = this.array[i]
        }
        return 'Element not found!'
    }

    has(element) {
        for(var i=0;i<=this.array.length;i++)    {
            if (element === this.array[i])   {
                return true
            }
        }
        return false
    }
    

    all() {
        return this.array
    }

    clear() {
        this.array = []
        return this.array
    }
}

sampleArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

module.exports = {
    queue : queue,
    stack : stack,
    set : set
};