package main

import "fmt"

// func main() {

// left := TreeNode{}
// right := TreeNode{}
// T := BinaryTree{}

// left := makeTree(20, nil, nil)
// right := makeTree(30, nil, nil)
// T := makeTree(10, &left, &right)

// fmt.Printf("%T", T)
// fmt.Println(T.element)
// fmt.Println(T.left.element)
// fmt.Println(T.right.element)

// T.preorder()
// }

// type TreeNode struct {
// 	element int
// 	left    *TreeNode
// 	right   *TreeNode
// }

// func makeTree(element int, left *TreeNode, right *TreeNode) TreeNode {
// 	return TreeNode{element, left, right}
// }

// func (T *TreeNode) preorder() {
// 	if T != nil {
// 		fmt.Print(T.element, " ")
// 		T.left.preorder()
// 		T.right.preorder()
// 	}
// }

// * Queue implementation
type Node struct {
	val  *BinaryTree
	next *Node
}

type Queue struct {
	front *Node
	rear  *Node
	size  int
}

func (Q Queue) isEmpty() bool {
	return Q.size == 0
}

func (Q *Queue) enqueue(element *BinaryTree) {
	new := &Node{element, nil}
	if Q.isEmpty() {
		Q.front = new
	} else {
		Q.rear.next = new
	}
	Q.rear = new
	Q.size++
}

func (Q *Queue) dequeue() *BinaryTree {
	if Q.isEmpty() {
		fmt.Println("Queue is Empty")
		return nil
	}

	res := Q.front.val
	Q.front = Q.front.next

	if Q.isEmpty() {
		Q.rear = Q.rear.next
	}
	Q.size--
	return res
}

// * Binary tree implemetation

func main() {
	fmt.Println("Binary Tree")
	T := BinaryTree{}
	left := BinaryTree{}
	right := BinaryTree{}

	a := BinaryTree{}
	b := BinaryTree{}
	a.makeTree(40, nil, nil)
	b.makeTree(50, nil, nil)

	c := BinaryTree{}
	d := BinaryTree{}
	c.makeTree(60, nil, nil)
	d.makeTree(70, nil, nil)

	left.makeTree(20, &a, &b)
	right.makeTree(30, &c, &d)
	T.makeTree(10, &left, &right)

	T.preorder(&T)
	fmt.Println("")
	T.inorder(&T)
	fmt.Println("")
	T.postorder(&T)
	fmt.Println("")
	T.levelorder(&T)

	fmt.Println("")
	fmt.Println(T.serch(&T, 10))
}

type TreeNode struct {
	element int
	left    *BinaryTree
	right   *BinaryTree
}

type BinaryTree struct {
	root *TreeNode
}

func (B *BinaryTree) makeTree(ele int, left *BinaryTree, right *BinaryTree) {
	B.root = &TreeNode{ele, left, right}
}

func (B BinaryTree) preorder(troot *BinaryTree) {
	if troot != nil {
		fmt.Print(troot.root.element, " ")
		B.preorder(troot.root.left)
		B.preorder(troot.root.right)
	}
}

func (B BinaryTree) inorder(troot *BinaryTree) {
	if troot != nil {
		B.inorder(troot.root.left)
		fmt.Print(troot.root.element, " ")
		B.inorder(troot.root.right)
	}
}

func (B BinaryTree) postorder(troot *BinaryTree) {
	if troot != nil {
		B.postorder(troot.root.left)
		B.postorder(troot.root.right)
		fmt.Print(troot.root.element, " ")
	}
}

func (B BinaryTree) levelorder(troot *BinaryTree) {
	Q := Queue{}
	t := troot

	fmt.Print(t.root.element, " ")
	Q.enqueue(t)

	for !Q.isEmpty() {
		t = Q.dequeue()

		if t.root.left != nil {
			fmt.Print(t.root.left.root.element, " ")
			Q.enqueue(t.root.left)
		}

		if t.root.right != nil {
			fmt.Print(t.root.right.root.element, " ")
			Q.enqueue(t.root.right)
		}
	}
}

func (B BinaryTree) serch(troot *BinaryTree, key int) bool {
	res1 := false
	res2 := false

	if troot != nil {
		if key == troot.root.element {
			return true
		}

		res1 = B.serch(troot.root.left, key)
		res1 = B.serch(troot.root.right, key)
	}

	return res1 || res2
}
