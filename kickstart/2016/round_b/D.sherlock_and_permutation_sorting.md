## D. Sherlock and Permutation Sorting

### 1. Primitive Chunk

Here we call a chunk p **primitive** if it cannot be divided into two parts where the elements in the first part are smaller than the elements in the second part. In other words, it does not contain a suffix chunk with size M that contains the largest M elements.

Example: [1] is primitive.

[2,1] is primitive but [1,2] is not.

[1,2,3], [2,1,3] is not primitive.

[1,3,2] is not primitive.

While [2,3,1], [3,2,1], [3,1,2] are all primitive.

Now we define g(N) as the number of primitive chunks with size N. We have:

$$
g(N) = N! - \sum_{i=0}^{N-1} (N-i)! \times g(i)
$$

The starting point is 

$$
g(0) = 0
$$

### 2. Sum of f(p)

Also, for a specific permutation p, denote p' as the prefix of p after removing the rightmost primitive chunk.

$$
\begin{aligned}
\sum_{|p|=N} f(p)
&= \sum_{i=1}^{N} \left[\sum_{|p'|=N-i} \bigl(f(p')+1\bigr)\, g(i)\right] \\
&= \sum_{i=1}^{N} \left[\left(\sum_{|p'|=N-i} f(p') + (N-i)!\right) g(i)\right]
\end{aligned}
$$

The starting point is:

$$
f(p) = 0, \qquad \text{for } |p| = 0
$$

### 3. Sum of square of f(p)
$$
\begin{aligned}
\sum_{|p|=N} f^2(p)
&= \sum_{i=1}^{N} \left[\sum_{|p'|=N-i} \bigl(f(p')+1\bigr)^2\, g(i)\right] \\
&= \sum_{i=1}^{N} \left[\left(\sum_{|p'|=N-i} f^2(p') + 2\sum_{|p'|=N-i} f(p') + (N-i)!\right) g(i)\right]
\end{aligned}
$$

The starting point is:

$$
f^2(p) = 0, \qquad \text{for } |p| = 0
$$
