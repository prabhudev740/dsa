package main

import (
	"fmt"
)

type Stack struct {
	data []int
}

func (S Stack) len() int {
	return len(S.data)
}

func (S Stack) isEmpty() bool {
	return S.len() == 0
}

func (S *Stack) push(element int) {
	S.data = append(S.data, element)
}

func (S *Stack) pop() int {
	if S.isEmpty() {
		fmt.Println("----Stack is Empty -----")
		return -1
	}

	res := S.top()

	S.data = S.data[0 : S.len()-1]

	return res
}

func (S Stack) top() int {
	if S.isEmpty() {
		fmt.Println("----Stack is Empty -----")
		return -1
	}
	return S.data[S.len()-1]
}

func main() {
	fmt.Println("--- Slice Stack---")
	s := Stack{}
	fmt.Println(s.len())
	s.push(10)
	s.push(20)
	s.push(30)
	fmt.Println(s.data)
	fmt.Println(s.len())
	fmt.Println(s.top())
	fmt.Println(s.pop())
	fmt.Println(s.pop())
	fmt.Println(s.pop())
	fmt.Println(s.data)
	fmt.Println(s.len())
	fmt.Println(s.top())
}
