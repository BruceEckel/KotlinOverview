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

### Many Other Powerful Features
* Easy two-way Java interoperability
* Coroutines (Kotlin 1.1)
* (go through book looking for features)
