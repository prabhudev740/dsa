package main

import (
	"fmt"
)

type Node struct {
	val  int
	next *Node
}

type Dqueue struct {
	front *Node
	rear  *Node
	size  int
}

func (D Dqueue) isEmpty() bool {
	return D.size == 0
}

func (D Dqueue) display() {
	for D.front != nil {
		fmt.Printf("%d -> ", D.front.val)
		D.front = D.front.next
	}
	fmt.Println("")
}

func (D *Dqueue) addLast(val int) {
	n := &Node{val, nil}
	if D.isEmpty() {
		D.front = n
	} else {
		D.rear.next = n
	}

	D.rear = n
	D.size++
}

func (D *Dqueue) addFirst(val int) {
	newest := &Node{val, nil}
	if D.isEmpty() {
		D.front = newest
		D.rear = newest
	} else {
		newest.next = D.front
		D.front = newest
	}
	D.size++
}

func (D *Dqueue) removeLast() int {
	if D.isEmpty() {
		fmt.Println("List is Empty")
		return -1
	}
	i := 0
	cur := D.front
	for i < D.size-2 {
		cur = cur.next
		i++
	}

	res := D.rear.val
	cur.next = nil
	D.rear = cur

	if D.isEmpty() {
		D.rear = D.rear.next
	}

	D.size--
	return res
}

func (D *Dqueue) removeFirst() int {
	if D.isEmpty() {
		fmt.Println("List is Empty")
		return -1
	}

	res := D.front.val
	D.front = D.front.next
	D.size--
	return res
}

func (D Dqueue) len() int {
	return D.size
}

func (D Dqueue) first() int {
	if D.isEmpty() {
		fmt.Println("Queue is Empty")
		return -1
	}
	return D.front.val
}

func (D Dqueue) last() int {
	if D.isEmpty() {
		fmt.Println("Queue is Empty")
		return -1
	}
	return D.rear.val
}

func main() {
	fmt.Println("___Dqueue Linked List___")
	d := Dqueue{}
	fmt.Println(d)

	d.addLast(10)
	d.addLast(20)
	d.addLast(30)
	d.display()
	d.addFirst(5)
	d.addFirst(3)
	d.display()
	// fmt.Println(d.removeFirst())
	// fmt.Println(d.removeFirst())
	// fmt.Println(d.removeFirst())
	// fmt.Println(d.removeFirst())
	// fmt.Println(d.removeFirst())
	// fmt.Println(d.removeLast())
	// fmt.Println(d.removeLast())
	// fmt.Println(d.removeLast())
	// fmt.Println(d.removeLast())
	// fmt.Println(d.removeLast())
	// fmt.Println(d.removeLast())
	fmt.Println(d.first())
	fmt.Println(d.last())
}
