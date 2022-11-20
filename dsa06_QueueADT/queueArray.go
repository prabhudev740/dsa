package main

import (
	"fmt"
)

type Queue struct {
	data []int
}

func (Q Queue) len() int {
	return len(Q.data)
}

func (Q Queue) isEmpty() bool {
	return Q.len() == 0
}

func (Q Queue) first() int {
	if Q.isEmpty() {
		fmt.Println("Queue is empty")
		return -1
	}
	return Q.data[0]
}

func (Q *Queue) enqueue(element int) {
	Q.data = append(Q.data, element)
}

func (Q *Queue) dequeue() int {
	if Q.isEmpty() {
		fmt.Println("Queue is Empty")
		return -1
	}
	res := Q.data[0]
	Q.data = Q.data[1:]
	return res
}

func main() {
	fmt.Println("-----Queue-----")
	q := Queue{}
	fmt.Println(q.data)
	q.enqueue(10)
	q.enqueue(20)
	q.enqueue(30)
	q.enqueue(40)
	fmt.Println(q.first())
	fmt.Println(q.data)
	fmt.Println(q.dequeue())
	fmt.Println(q.data)
	fmt.Println(q.dequeue())
	fmt.Println(q.data)
	fmt.Println(q.dequeue())
	fmt.Println(q.data)
	fmt.Println(q.dequeue())
	fmt.Println(q.data)
	fmt.Println(q.dequeue())
	fmt.Println(q.data)
	fmt.Println(q.first())
}
