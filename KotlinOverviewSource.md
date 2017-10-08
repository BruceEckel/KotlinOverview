---
author: Bruce Eckel
title: Kotlin Overview for Java Programmers
---

## From Upcoming _Atomic Kotlin_
*

---

### TLDR: Kotlin Fixes the Java Annoyances
* Gets rid of almost all remnants of bad Java design
* Anything the language can do for you
* But interacts/integrates easily with Java

---

### Kotlin Enables Functional Programming
* First-class functions that are easy to manipulate
* Much more useful lambdas, without restrictions
* Invariance by default

---

### Top-Level Functions

{{Summary1/BasicFunctions.kt}}

---

### String templates

{{Summary1/StrTemplates.kt}}

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

---

### Named and Default Arguments

{{NamedAndDefaultArgs/NamedAndDefaultArgs.kt}}

---

### Lists are First-Class

{{Summary2/ListCollection.kt}}

---

### Classes

{{Summary2/ClassBodies.kt}}

---

### Data Classes

{{DataClasses/Simple.kt}}

---

### Prefer Extension Functions to Inheritance

{{Extensions/BookExtensions.kt}}

---

### Pattern Matching

{{WhenExpressions/WhenExpressions.kt}}

---

### Local Functions

{{LocalFunctions/LocalExtensions.kt}}

---

### Null Safety


---

### Lambdas (1)

{{Lambdas/LambdaTypeInference.kt}}

---

### Lambdas (2)

{{Lambdas/DisplayListWithLambda.kt}}

---

### Lambdas (3)

{{Lambdas/TwoArgLambda.kt}}

---

### Functional Operations

{{ListOperations/DisplayListMap.kt}}

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

### Liberation From Erasure!

```kotlin
inline fun <reified T: Any> type(c: T) = c::class.qualifiedName
```

---

### Many Other Powerful Features
* Simplified Generics
* Coroutines (Kotlin 1.1)
* (go through book looking for features)
