// This problem was asked by Jane Street.
// Given integers M and N, write a program that returns positive integer 
// pairs (a, b) satisfy the following conditions:

// •	a + b = M
// •	a XOR b = N
////////
package main

import (
	"fmt"
)
////////

func numSumXor(M int, N int) [][]int {
	ctr := 0
	m := [][]int{}
	for i := 0; i <= M/2; i++ {
		a, b := i, M - i
		if a ^ b == N {
			ctr++
			m = append(m, []int{a, b})
		}
	}
	return m
}

////////
func main(){
	fmt.Println(numSumXor(10, 4))
	fmt.Println(numSumXor(16, 8))
}