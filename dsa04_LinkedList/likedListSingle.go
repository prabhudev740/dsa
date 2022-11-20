package main

import (
	"fmt"
)

type Node struct {
	val  int
	next *Node
}

type LinkedList struct {
	head *Node
	tail *Node
	size int
}

func (L LinkedList) isEmpty() bool {
	return L.size == 0
}

func (L LinkedList) display() {
	for L.head != nil {
		fmt.Printf("%d -> ", L.head.val)
		L.head = L.head.next
	}
	fmt.Println("")
}

func (L *LinkedList) addLast(val int) {
	n := &Node{val, nil}
	if L.isEmpty() {
		L.head = n
	} else {
		L.tail.next = n
	}

	L.tail = n
	L.size++
}

func (L *LinkedList) addFirst(val int) {
	newest := &Node{val, nil}
	if L.isEmpty() {
		L.head = newest
		L.tail = newest
	} else {
		newest.next = L.head
		L.head = newest
	}
	L.size++
}

func (L LinkedList) search(key int) bool {
	for L.head != nil {
		if L.head.val == key {
			return true
		}
		L.head = L.head.next
	}
	return false
}

func (L *LinkedList) removeLast() int {
	if L.isEmpty() {
		fmt.Println("List is Empty")
		return -1
	}
	i := 0
	cur := L.head
	for i < L.size-2 {
		cur = cur.next
		i++
	}

	res := L.tail.val
	cur.next = nil
	L.tail = cur

	// if L.isEmpty() {
	// 	L.head = L.head.next
	// }

	L.size--
	return res
}

func (L *LinkedList) removeFirst() int {
	if L.isEmpty() {
		fmt.Println("List is Empty")
		return -1
	}

	res := L.head.val
	L.head = L.head.next
	L.size--
	return res
}

func main() {
	fmt.Println("___Linked List___")
	n := LinkedList{}
	fmt.Println(n)
	n.addLast(10)
	n.addLast(20)
	n.addLast(30)
	fmt.Println(n.size)

	n.addFirst(5)
	n.addFirst(1)
	n.addFirst(-10)
	fmt.Println(n.size)
	n.display()
	fmt.Println(n.search(-20))
	fmt.Println(n.removeLast())
	fmt.Println(n.removeLast())
	fmt.Println(n.removeLast())
	n.display()
	fmt.Println(n.removeFirst())
	fmt.Println(n.removeFirst())
	fmt.Println(n.removeFirst())
	fmt.Println(n.removeFirst())

	n.display()
	fmt.Println(n.size)
}
