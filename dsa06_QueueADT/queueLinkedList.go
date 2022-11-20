package main

import (
	"fmt"
)

type Node struct {
	val  int
	next *Node
}

type Queue struct {
	front *Node
	rear  *Node
	size  int
}

func (Q Queue) len() int {
	return Q.size
}

func (Q Queue) isEmpty() bool {
	return Q.size == 0
}

func (Q Queue) display() {
	for Q.front != nil {
		fmt.Printf("%d ->", Q.front.val)
		Q.front = Q.front.next
	}
	fmt.Println("")
}

func (Q *Queue) enqueue(element int) {
	new := &Node{element, nil}
	if Q.isEmpty() {
		Q.front = new
	} else {
		Q.rear.next = new
	}
	Q.rear = new
	Q.size++
}

func (Q *Queue) dequeue() int {
	if Q.isEmpty() {
		fmt.Println("Queue is Empty")
		return -1
	}

	res := Q.front.val
	Q.front = Q.front.next

	if Q.isEmpty() {
		Q.rear = Q.rear.next
	}
	Q.size--
	return res
}

func (Q Queue) first() int {
	if Q.isEmpty() {
		fmt.Println("Queue is Empty")
		return -1
	}
	return Q.rear.val
}

func main() {
	fmt.Println("----Queue-----")
	q := Queue{}
	q.display()
	q.enqueue(10)
	q.enqueue(20)
	q.enqueue(30)
	q.enqueue(40)
	fmt.Println(q.first())
	q.display()
	fmt.Println(q.dequeue())
	q.display()
	fmt.Println(q.dequeue())
	q.display()
	fmt.Println(q.dequeue())
	q.display()
	fmt.Println(q.dequeue())
	q.display()
	fmt.Println(q.dequeue())
	q.display()
	fmt.Println(q.first())
}
