---
author: Bruce Eckel
title: Resisting Kotlin
date: October 1, 2017
---
### Ceremony makes you feel productive
* Everything in a class, a file for every class
* Plain functions -- who needs them?
* It's just not the same without
```java
public class Foo {
  public static void main(String[] args) {
    // ...
  }
}
```
* How can I know where the end is without semicolons?

---

### Top-Level Functions
```kotlin
// Summary1/BasicFunctions.kt

fun cube(x: Int): Int {
  return x * x * x
}

fun bang(s: String) = s + "!"

fun main(args: Array<String>) {
  println(cube(3))
  println(bang("pop"))
}
/* Output:
27
pop!
*/
```

---

### String templates
```kotlin
// Summary1/StrTemplates.kt

fun main(args: Array<String>) {
  val answer = 42
  println("Found $answer!")                  // [1]
  val condition = true
  println("${if (condition) 'a' else 'b'}")  // [2]
  println("printing a $1")                   // [3]
}
/* Output:
Found 42!
a
printing a $1
*/
```

---

### Triple Quotes
```kotlin
// Summary1/ThreeQuotes.kt

fun json(q: String, a: Int) = """{
    "question" : "$q",
    "answer" : $a
}"""

fun main(args: Array<String>) {
  println(json("The Ultimate", 42))
}
/* Output:
{
    "question" : "The Ultimate",
    "answer" : 42
}
*/
```

---

### No Primitives!
```kotlin
// Summary1/NumberTypes.kt

fun main(args: Array<String>) {
  val n = 1000    // Int
  val l = 1000L   // Long
  val d = 1000.0  // Double
  println("$n $l $d")
}
/* Output:
1000 1000 1000.0
*/
```

---

### Iteration
```kotlin
// Summary1/IterateThroughString.kt

fun main(args: Array<String>) {
  for(c in "Kotlin") {
    print("$c ")
    // c += 1 // error:
    // val cannot be reassigned
  }
}
/* Output:
K o t l i n
*/
```

---

### Ranges
```kotlin
// Summary1/IntRange.kt

fun main(args: Array<String>) {
  for(i in 1..10)
    print("$i ")
}
/* Output:
1 2 3 4 5 6 7 8 9 10
*/
```
