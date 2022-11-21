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

func main() {
	fmt.Println("Binary Tree")
	T := BinaryTree{}
	left := BinaryTree{}
	right := BinaryTree{}

	left.makeTree(20, nil, nil)
	right.makeTree(30, nil, nil)
	T.makeTree(10, &left, &right)

	T.preorder(&T)
	fmt.Println("")
	T.inorder(&T)
	fmt.Println("")
	T.postorder(&T)

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
		B.preorder(troot.root.left)
		fmt.Print(troot.root.element, " ")
		B.preorder(troot.root.right)
	}
}

func (B BinaryTree) postorder(troot *BinaryTree) {
	if troot != nil {
		B.preorder(troot.root.left)
		B.preorder(troot.root.right)
		fmt.Print(troot.root.element, " ")
	}
}
