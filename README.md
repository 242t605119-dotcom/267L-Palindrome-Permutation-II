# Palindrome Permutation II

**LeetCode Problem:** 267
**Language:** Python

## Problem

Given a string `s`, generate all possible palindromic permutations of the string.

A palindrome reads the same from left to right and right to left.

If no palindromic permutation is possible, return an empty list.

Each permutation should appear only once.

## Example

Input:

```text id="r8x4kq"
s = "aabb"
```

The possible palindromic permutations are:

```text id="gq0x2s"
["abba", "baab"]
```

Output:

```text id="m9c1za"
["abba", "baab"]
```

Another example:

```text id="j2v5pn"
s = "abc"
```

Each character appears once, so there are three characters with odd frequency.

A palindrome cannot be formed.

Output:

```text id="e6y3tw"
[]
```

## Approach

First, count the frequency of every character.

For a palindrome to be possible, at most one character can have an odd frequency.

If more than one character has an odd frequency, the answer is an empty list.

Next, only half of the palindrome needs to be generated.

For example:

```text id="c7a5nm"
aabb
```

The left half can be:

```text id="0p3v8q"
ab
```

The other half is simply the reverse:

```text id="k2r6wd"
ba
```

So the complete palindrome becomes:

```text id="y8t1hs"
abba
```

If there is a character with an odd frequency, it becomes the middle character.

## Backtracking

Backtracking is used to generate all unique arrangements of the first half.

At every step, one unused character is selected.

After choosing a character, the algorithm continues recursively.

When the complete first half is created:

1. Join the first half.
2. Add the middle character.
3. Add the reverse of the first half.

This creates a complete palindrome.

## Avoiding Duplicates

If the same character appears multiple times, simply choosing identical characters in different positions would create duplicate permutations.

The condition:

```text id="x7k3pb"
if i > 0 and half[i] == half[i - 1] and not used[i - 1]:
```

helps skip duplicate arrangements.

## Complexity

The time complexity depends on the number of unique palindromic permutations generated.

Backtracking explores possible arrangements of half of the characters.

The extra space is mainly used for the frequency map, recursion, and generated results.

## Key Learning

This problem helped me practice:

* Hash maps
* Frequency counting
* Palindromes
* Backtracking
* Recursion
* Permutations
* Avoiding duplicate results

## Conclusion

The solution first checks whether a palindrome is possible using character frequencies. It then generates only the first half of each palindrome using backtracking and constructs the complete palindrome using its reverse.

**Author: T. Nandhini**
