# Hashing

As we know the collision issue that occurs with Hashing, I have resolved that issue using these Two techinques.

**1. Chaining:**  
The idea is to make each cell of hash table point to a linked list of records that have same hash function value. Chaining is simple, but requires additional memory outside the table.  
Code - [**Hashing using Chaining.**](hashingChaining.py)

**2. Open Addressing:**  
The idea here is to calculate a hash value(i.e. index position) and place the element there, if an element already exists at that index position we use one of the following strategies to encounter this problem:  
1. **Linear Probing:** Add 1 in the original index position and calculate the hash value again, and try placing the element in this position. If collision is encountered again, add 1 in this index. Repeat untill we find a place.  
2. **Quadratic Probing:** Add **i<sup>2</sup>** factor to the original index position and calculate the hash value again, and try placing the element in this position. Repeat untill we find a place.  
3. **Double Hashing:** Use 2 hashing functions. One for finding index position, another to calculate new index position if collision is encountered.  

Code - [**Hashing with Collision Resolving Techniques.**](hashingStrategies.py)