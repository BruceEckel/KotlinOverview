---
author: Bruce Eckel
title: Resisting Kotlin
date: October 1, 2017
---

## From Upcoming _Atomic Kotlin_
*

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

---

### Named and Default Arguments

```kotlin
// NamedAndDefaultArgs/NamedAndDefaultArgs.kt
import atomictest.eq

fun getColor1(
  red: Int = 0,
  green: Int = 0,
  blue: Int = 0
) = "($red, $green, $blue)"

fun main(args: Array<String>) {
  val darkRed = "(139, 0, 0)"
  val darkBlue = "(0, 0, 139)"
  val orange = "(255, 165, 0)"
  val purple = "(128, 0, 128)"
  getColor1(139) eq darkRed
  getColor1(blue = 139) eq darkBlue
  getColor1(255, 165) eq orange
  getColor1(red = 128, blue = 128) eq purple
}
```

---

### Lists are First-Class

```kotlin
// Summary2/ListCollection.kt
import atomictest.eq

fun main(args: Array<String>) {
  val l1 = listOf(19.2, 88.3, 22.1)
  l1 eq listOf(19.2, 88.3, 22.1)
  l1[1] eq 88.3 // Indexing
  l1.reversed() eq listOf(22.1, 88.3, 19.2)
  l1.sorted() eq listOf(19.2, 22.1, 88.3)
  l1.max() eq 88.3
  l1.min() eq 19.2
}
```

---

### Classes

```kotlin
// Summary2/ClassBodies.kt

class NoBody

class SomeBody {
  val name = "Janet Doe"
}

class EveryBody {
  val all = listOf(SomeBody(),
    SomeBody(), SomeBody())
}

fun main(args: Array<String>) {
  val nb = NoBody()
  val sb = SomeBody()
  val eb = EveryBody()
}
```

---

### Data Classes

```kotlin
// DataClasses/Simple.kt
import atomictest.*

data class Simple(val arg1: String, var arg2: Int)

fun main(args: Array<String>) {
  val s1 = Simple("Hi", 29)
  val s2 = Simple("Hi", 29)
  s1 eq s2
}
/* Output:
Simple(arg1=Hi, arg2=29)
*/
```

---

### Prefer Extension Functions to Inheritance

```kotlin
// Extensions/BookExtensions.kt
import atomictest.eq

data class Book(val title: String)

fun Book.categorize(category: String) =
  """title: "$title", category: $category"""

fun main(args: Array<String>) {
  Book("Dracula").categorize("Vampire") eq
    """title: "Dracula", category: Vampire"""
}
```

---

### Pattern Matching

```kotlin
// WhenExpressions/WhenExpressions.kt
import atomictest.eq

fun matchColor(color: String) =
  when (color) {                    // [1]
    "red" -> "RED"                  // [2]
    "blue" -> "BLUE"
    "green" -> "GREEN"
    else -> "UNKNOWN COLOR: $color" // [3]
  }

fun main(args: Array<String>) {
  matchColor("white") eq
    "UNKNOWN COLOR: white"
  matchColor("blue") eq "BLUE"
}
```

---

### Local Functions

```kotlin
// LocalFunctions/LocalExtensions.kt
import atomictest.eq

fun main(args: Array<String>) {
  fun String.exclaim() = "$this!"
  "Hello".exclaim() eq "Hello!"
  "Hallo".exclaim() eq "Hallo!"
  "Bonjour".exclaim() eq "Bonjour!"
  "Ciao".exclaim() eq "Ciao!"
}
```

---

### Null Safety


---

### Lambdas (1)

```kotlin
// Lambdas/LambdaTypeInference.kt
import atomictest.eq

fun main(args: Array<String>) {
  var s = ""
  listOf(1, 2, 3, 4).forEach({
    n -> s += "[$n]"
  })
  s eq "[1][2][3][4]"
}
```

---

### Lambdas (2)

```kotlin
// Lambdas/DisplayListWithLambda.kt
import atomictest.eq

fun main(args: Array<String>) {
  var s = ""
  (1..4).forEach { s += "[$it]" }
  s eq "[1][2][3][4]"
}
```

---

### Lambdas (3)

```kotlin
// Lambdas/TwoArgLambda.kt
import atomictest.eq

fun main(args: Array<String>) {
  var s = ""
  "Duck".forEachIndexed {
    n, c -> s += "[$n:$c]"
  }
  s eq "[0:D][1:u][2:c][3:k]"
}
```

---

### Functional Operations

```kotlin
// ListOperations/DisplayListMap.kt
import atomictest.eq

fun main(args: Array<String>) {
  (1..4).map {
    "[$it]"
  }.reduce {
    str, s -> str + s
  } eq "[1][2][3][4]"
}
```

---

### Operator Overloading

```kotlin
// Operators/Num.kt
package operators
import atomictest.eq

data class Num(val n: Int)

operator fun Num.plus(rval: Num) =
  Num(n + rval.n)

fun main(args: Array<String>) {
  Num(4) + Num(5) eq Num(9)
  Num(4).plus(Num(5)) eq Num(9)
}
```

---

### Many Other Powerful Features
* Easy two-way Java interoperability
* Coroutines (Kotlin 1.1)
* (go through book looking for features)
