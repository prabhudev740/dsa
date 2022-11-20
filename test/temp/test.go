// package main

// import (
// 	"fmt"
// 	"math"
// )

// func main() {
// 	fmt.Println("----Answers------")
// 	// fmt.Println(fib(1))
// 	// fmt.Println(isPrime(73))
// 	// fmt.Println(isPallindrom(1))
// 	// fmt.Println(isArmstrong(1))
// 	fmt.Println(fib(5))
// }

// func isPrime(n int) bool {
// 	if n < 2 {
// 		return false
// 	}
// 	for i := 2; i <= n/2; i++ {
// 		if n%i == 0 {
// 			return false
// 		}
// 	}
// 	return true
// }

// func isPallindrom(n int) bool {
// 	res := 0
// 	temp := n
// 	for temp > 0 {
// 		res = res*10 + temp%10
// 		temp /= 10
// 	}

// 	return res == n
// }

// func isArmstrong(n int) bool {
// 	res := 0
// 	temp := n

// 	for temp > 0 {
// 		res += int(math.Pow(float64(temp%10), 3))
// 		temp /= 10
// 	}

// 	return res == n
// }

// // nth fib number
// func fib(n int) int {
// 	if n < 2 {
// 		return n
// 	}
// 	return fib(n-1) + fib(n-2)
// }

package main

import (
	"fmt"
)

func pattern(n int) {
	for i := 1; i <= n; i++ {
		for j := n - i; j >= 1; j-- {
			fmt.Printf(" ")
		}

		for j := 1; j <= i; j++ {
			fmt.Printf("*")
		}

		for j := 1; j < i; j++ {
			fmt.Printf("*")
		}

		fmt.Printf("\n")
	}

}

func main() {
	pattern(5)
}
