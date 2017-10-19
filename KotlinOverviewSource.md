---
title: Kotlin Overview for Java Programmers
author: Bruce Eckel
---

## www.OnJava8.com

![](OnJav8Cover.jpg){ width=40% }

---

## Examples From Upcoming

![](Cover.jpg){ width=40% }

---

### TLDR: Fixes the Java Annoyances
* Gets rid of almost all remnants of bad Java design
* Anything the language can do for you
* But interacts/integrates easily with Java
* Runs on Java 6 JVM, official Android Language

---

### Enables Functional Programming
* Invariance by default
* First-class functions that are easy to manipulate
* Much more useful lambdas, without restrictions

---

### Top-Level Functions

{{Summary1/BasicFunctions.kt}}

* Multiple things in a file
* Don't have to use classes if you don't need them

---

### String templates

{{Summary1/StrTemplates.kt}}

* No constraints on file names

---

### Triple Quotes

{{Summary1/ThreeQuotes.kt}}

---

### No Primitives!

{{Summary1/NumberTypes.kt}}

---

### Iteration

{{Summary1/IterateThroughString.kt}}

---

### Ranges

{{Summary1/IntRange.kt}}

* Additional range support

---

### Named and Default Arguments

{{NamedAndDefaultArgs/NamedAndDefaultArgs.kt}}

---

### Lists are First-Class

{{Summary2/ListCollection.kt}}

* Immutable by default

---

### Classes

{{Summary2/ClassBodies.kt}}

* Like Python: **`new`** is redundant

---

### Data Classes

{{DataClasses/Simple.kt}}

* Creates **`toString()`**, **`hashCode()`**, **`equals()`**, **`compare()`**, **`copy()`**, etc.

---

### Prefer Extension Functions to Inheritance

{{Extensions/BookExtensions.kt}}

* Seems simple but it's surprising what they enable
* **Adapter** design pattern

---

### Pattern Matching

{{WhenExpressions/WhenExpressions.kt}}

* Far greater complexity possible

---

### Local Functions

{{LocalFunctions/LocalExtensions.kt}}

---

### Null Safety

{{Nullable/Dereference.kt}}

---

### Nullable Types Require Explicit Checks

{{SafeCalls/SafeCall.kt}}

* Plus significant additional support

---

### Lambdas (1)

{{Lambdas/LambdaTypeInference.kt}}

---

### Lambdas (2)

{{Lambdas/FormatListWithLambda.kt}}

---

### Lambdas (3)

{{Lambdas/TwoArgLambda.kt}}

---

### Functional Operations

{{ListOperations/DisplayListMap.kt}}

* Many more operations to produce functional-style chaining

---

### Operator Overloading

{{Operators/Num.kt}}

---

### Java Collection Invariance

```java
import java.util.*;

class Animal {}
class Cat extends Animal {}

public class Invariant {
  public static void main(String[] args) {
    List<Animal> animals = new ArrayList<Cat>();
    // error: incompatible types: ArrayList<Cat>
    // cannot be converted to List<Animal>
  }
}
```

* Because reasons
* ... which never quite make sense

---

### Automatic Covariance!

```kotlin
open class Animal
class Cat: Animal()

fun main(args: Array<String>) {
  val cats: List<Cat> = listOf(Cat(), Cat())
  val animals: List<Animal> = cats
}
```

---

### Generics are Easier and More Powerful

```kotlin
interface Animal
data class Cat(val name: String): Animal
data class Dog(val name: String): Animal

fun main(args: Array<String>) {
    val animals = listOf(
      Cat("Bob"), Dog("Alice"),
      Cat("Zomber"), Dog("Tweet"))
    println(animals.filterIsInstance<Cat>())
    println(animals.filterIsInstance<Dog>())
}
/* Output:
[Cat(name=Bob), Cat(name=Zomber)]
[Dog(name=Alice), Dog(name=Tweet)]
*/
```

---

### Many Other Powerful Features
* Domain-specific language (DSL) support
* Delegation
* Lazy & Late evaluation
* Coroutines (Kotlin 1.1)
* And Much More
* Watch this space: AtomicKotlin.com
