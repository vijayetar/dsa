Vij :  Code Challenge 19
Problem Domain:
Create a function/method sum all the numbers in the binary tree
Output - an integer

Edge cases
Binary tree
Node vales are integers
No strings
No empty tree

Input = 20 -> 5 ->6 ->6  ->3
Output = 20 + 5 +6 +6 +3 = 40

BigO - On for space and time, O(h) h - log n

Algorithm:
Create a function find_sum with parameter of a tree
Check to ensure that tree has a root, raise exception if no root
variable sum = 0
Sum = recursive function with the tree.root, sum

Create a recursive function called walk, parameters, root_node, sum
Check if the root_node exits - return the sum
sum = sum and the root_node.value
If root_node.left exits - recurse the function walk with the new root - root.left, sum
Sum to the return of the recursive function
If root_node.right exits - recurse the function walk with the new root - root.right, sum
Sum to the return of the recursive function

Return sum

Pseudocode:
Def find_sum(tree):
	if the tree.root == None:
		raise Exception("this tree has no root")
	sum = 0
	def walk(root_node, sum):
		preorder traversal through each node of the tree
		if the root_node == None
			return sum
		update sum with the value of the root_node
		check if the root_node.left:
			sum = walk(root_node.left, sum)
		check if the root_node.right;
			sum= walk(root_node.right,sum)
		return sum
	sum = walk(tree.root, sum)
	return sum

Testing:
INPUT - None
Output = exception

Input  10
sum  0  +10 = 10
walk(10,0)
Output = 10

input 10->3(l) -> 4(r)
sum = 0 + 10 = 10+3 = 13 + 4 = 17
walk(10,0) => (3,10)=>(4,13)
Output => 17

input 10->3(l)->2(l) -> 1(r) ->4(r)
sum  0 +10=10+3=13+2=15+1=16+4=20
walk (10,0)=>(3,10)->(2,13)->(1,15) ->(4,16)
Output 20

Code:
Def find_sum(tree):
	if not tree.root:
		raise Exception("this tree has no root")
	sum = 0
	def walk(root_node, sum):
		if not root_node:
			return sum
		sum+=root_node.value
		if root_node.left:
			sum = walk(root_node.left, sum)
		if root_node.right:
			sum= walk(root_node.right,sum)
		return sum
	sum = walk(tree.root, sum)
	return sum
