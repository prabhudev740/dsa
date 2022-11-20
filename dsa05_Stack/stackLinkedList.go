package main

import (
	"fmt"
)

type Node struct {
	val  int
	next *Node
}

type Stack struct {
	head *Node
	size int
}

func (S Stack) len() int {
	i := 0
	for S.head != nil {
		i++
		S.size++
		S.head = S.head.next
	}
	return i
}

func (S Stack) isEmpty() bool {
	return S.size == 0
}

func (S Stack) top() int {
	if S.isEmpty() {
		fmt.Println("Stack is Empty")
		return -1
	}
	return S.head.val
}

func (S *Stack) push(element int) {
	newest := Node{element, S.head}
	S.head = &newest
	S.size++
}

func (S Stack) display() {
	for S.head != nil {
		fmt.Printf("%d -> ", S.head.val)
		S.head = S.head.next
	}
	S.size++
}

func (S *Stack) pop() int {
	if S.isEmpty() {
		fmt.Println("--- Stack is Empty")
		return -1
	}
	res := S.head.val
	S.head = S.head.next
	S.size--
	return res
}

func main() {
	fmt.Println("----- Stack LinkedList ------")
	s := Stack{}
	s.push(30)
	s.push(20)
	s.push(10)
	fmt.Println(s.pop())
	fmt.Println(s.pop())
	s.display()
}
