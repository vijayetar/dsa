from dsa.data_structures.tree.tree import BinaryTree

def find_sum(tree):
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

if __name__ == "__main__":
    bt=BinaryTree()
    bt.add(1)
    bt.add(7)
    bt.add(8)
    print(find_sum(bt))
