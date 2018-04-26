var test = require("tape");
var tapSpec = require("tap-spec");

// we import an object that contains all our functions
var functions = require("./node.js");

// we could 'extract' these functions into individual variables
// var add = functions.add;
// var pow = functions.add;

test
  .createStream()
  .pipe(tapSpec())
  .pipe(process.stdout);

test("Passing tests", function(t) {
  var test1_1 = functions.isString("hi");
  var test1_2 = functions.isString([2, {}, 10]);
  var test1_3 = functions.isString({ a: 2 });
  var test1_4 = functions.isString(["hello"]);

  var test2_1 = functions.isArray("hello");
  var test2_2 = functions.isArray(["hello"]);
  var test2_3 = functions.isArray([2, {}, 10]);
  var test2_4 = functions.isArray({ a: 2 });

  var test3_1 = functions.areSameType(["hello", "world", "long sentence"]);
  var test3_2 = functions.areSameType([1, 2, 9, 10]);
  var test3_3 = functions.areSameType([["hello"], "hello", ["bye"]]);
  var test3_4 = functions.areSameType([["hello"], [1, 2, 3], [{ a: 2 }]]);

  var test4_1 = functions.longest("abcccaa", "acddddffzzz");
  var test4_2 = functions.longest(
    "wearethechampions",
    "thisisthefinalcountdown"
  );

  var test5_1 = functions.convert(62934);
  var test5_2 = functions.convert(774744398);

  var test6_1 = functions.countArr([
    "kerouac",
    "fante",
    "fante",
    "buk",
    "hemingway",
    "hornby",
    "kerouac",
    "buk",
    "fante"
  ]);

  var test7_1 = functions.isCaught('C.....m')
  var test7_2 = functions.isCaught('C..m')
  var test7_3 = functions.isCaught('..C..m')

  var test8_1 = functions.splitTheBill({
    Amy: 20,
    Bill: 15,
    Chris: 10
  });

  var test9_1 = functions.exp(5, 3);
  var test9_2 = functions.exp(2, 4);
  var test9_3 = functions.exp(5, 1);
  var test9_4 = functions.exp(6, 0);

  var test10_1 = functions.factorial(5);
  var test10_2 = functions.factorial(4);
  var test10_3 = functions.factorial(0);

  var test11_1 = functions.fibs(3);
  var test11_2 = functions.fibs(7);
  var test11_3 = functions.fibs(1);

  var test12_1 = functions.zeroSum([1, 5, 0, -5, 3, -1])
  var test12_2 = functions.zeroSum([1, -1])
  var test12_3 = functions.zeroSum([0, 4, 3, 5])







  console.log("Exercise 1");

  t.equal(test1_1, true);
  t.equal(test1_2, false);
  t.equal(test1_3, false);
  t.equal(test1_4, false);

  console.log("Exercise 2");

  t.equal(test2_1, false);
  t.equal(test2_2, true);
  t.equal(test2_3, true);
  t.equal(test2_4, false);

  console.log("Exercise 3");

  t.equal(test3_1, true);
  t.equal(test3_2, true);
  t.equal(test3_3, false);
  t.equal(test3_4, true);

  console.log("Exercise 4");

  t.equal(test4_1, "abcdfz");
  t.equal(test4_2, "acdefhilmnoprstuw");

  console.log("Exercise 5");

  t.deepEqual(test5_1, [9, 6, 4, 3, 2]);
  t.deepEqual(test5_2, [9, 8, 7, 7, 7, 4, 4, 4, 3]);

  console.log("Exercise 6");

  t.deepEqual(test6_1, {
    kerouac: 2,
    fante: 3,
    buk: 2,
    hemingway: 1,
    hornby: 1
  });

  console.log("Exercise 7");

  t.equal(test7_1, false);
  t.equal(test7_2, true);
  t.equal(test7_3, true);
  
  console.log("Exercise 8");

  t.deepEqual(test8_1, { Amy: -5, Bill: -0, Chris: 5 });

  console.log("Exercise 9");

  t.equal(test9_1, 125);
  t.equal(test9_2, 16);
  t.equal(test9_3, 5);
  t.equal(test9_4, 1);

  console.log("Exercise 10");

  t.equal(test10_1, 120);
  t.equal(test10_2, 24);
  t.equal(test10_3, 1);

  console.log("Exercise 11");

  t.deepEqual(test11_1, [0, 1, 1]);
  t.deepEqual(test11_2, [0, 1, 1, 2, 3, 5, 8]);
  t.deepEqual(test11_3, [0]);

  console.log("Exercise 12");

  t.deepEqual(test12_1, [[0, 5], [1, 3]]);
  t.deepEqual(test12_2, [[0, 1]]);
  t.deepEqual(test12_3, []);

  t.end();
});
