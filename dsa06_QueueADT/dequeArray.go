package main

import (
	"fmt"
)

type Deque struct {
	data []int
}

func (D Deque) len() int {
	return len(D.data)
}

func (D Deque) isEmpty() bool {
	return D.len() == 0
}

func (D Deque) first() int {
	if D.isEmpty() {
		fmt.Println("Deque is empty")
		return -1
	}
	return D.data[0]
}

func (D Deque) last() int {
	if D.isEmpty() {
		fmt.Println("Deque is empty")
		return -1
	}
	return D.data[D.len()-1]
}

func (D *Deque) addLast(element int) {
	D.data = append(D.data, element)
}

func (D *Deque) addFirst(element int) {
	D.data = append([]int{element}, D.data...)
}

func (D *Deque) removeLast() int {
	if D.isEmpty() {
		fmt.Println("Deque is Empty")
		return -1
	}
	res := D.data[len(D.data)-1]
	D.data = D.data[:len(D.data)-1]
	return res
}

func (D *Deque) removeFirst() int {
	if D.isEmpty() {
		fmt.Println("Deque is Empty")
		return -1
	}
	res := D.data[0]
	D.data = D.data[1:]
	return res
}

func main() {
	fmt.Println("-----Deque-----")
	d := Deque{}
	fmt.Println(d.data)
	d.addLast(10)
	d.addLast(20)
	d.addLast(30)
	fmt.Println(d.data)
	d.addFirst(5)
	d.addFirst(3)
	fmt.Println(d.data)
	fmt.Println(d.first())
	fmt.Println(d.last())
	// fmt.Println(d.removeLast())
	// fmt.Println(d.removeLast())
	// fmt.Println(d.removeLast())
	// fmt.Println(d.removeLast())
	// fmt.Println(d.removeLast())
	// fmt.Println(d.removeLast())
	fmt.Println(d.removeFirst())
	fmt.Println(d.removeFirst())
	fmt.Println(d.removeFirst())
	fmt.Println(d.removeFirst())
	fmt.Println(d.removeFirst())
	fmt.Println(d.removeFirst())
	fmt.Println(d.first())
	fmt.Println(d.last())
	fmt.Println(d.data)
	d.addFirst(10)
	fmt.Println(d.data)
}
