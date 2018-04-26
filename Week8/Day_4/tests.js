const Stack = require("./stack.js").stack
const Queue = require("./stack.js").queue
const Set = require("./stack.js").set

var test = require("tape");
var tapSpec = require("tap-spec");

var objects = require("./stack.js");

test
    .createStream()
    .pipe(tapSpec())
    .pipe(process.stdout);

test("Passing tests", function (t) {

    console.log('Testing Stack')

    var sampleArrayStack = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    var stack = new Stack(sampleArrayStack)

    var stackTop = stack.top();
    var stackAdd = stack.putIn('Laurent');
    var stackDel = stack.takeOut();
    var stackEmpty = stack.isEmpty();
    var stackClear = stack.clear();

    t.equal(stackTop, 0);
    t.deepEqual(stackAdd, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Laurent']);
    t.deepEqual(stackDel, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
    t.equal(stackEmpty, false);
    t.deepEqual(stackClear, []);

    console.log('\nTesting Queue')

    var sampleArrayQueue = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    var queue = new Queue(sampleArrayQueue)

    var queueTop = queue.top();
    var queueAdd = queue.putIn('Laurent');
    var queueDel = queue.takeOut();
    var queueEmpty = queue.isEmpty();
    var queueClear = queue.clear();

    t.equal(queueTop, 0);
    t.deepEqual(queueAdd, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Laurent']);
    t.deepEqual(queueDel, [1, 2, 3, 4, 5, 6, 7, 8, 9, 'Laurent']);
    t.equal(queueEmpty, false);
    t.deepEqual(queueClear, []);

    console.log('\nTesting Set')

    var samplearraySet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    var set = new Set(samplearraySet)

    var setAdd = set.putIn('Laurent');
    var setDel = set.takeOut(4);
    var setHas = set.has('Laurent');
    var setAll = set.all()
    var setClear = set.clear();

    t.deepEqual(setAdd, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Laurent']);
    t.deepEqual(setDel, [0, 1, 2, 3, 5, 6, 7, 8, 9, 'Laurent']);
    t.equal(setHas, true);
    t.deepEqual(setAll, [0, 1, 2, 3, 5, 6, 7, 8, 9, 'Laurent'])
    t.deepEqual(setClear, []);

    t.end()
});