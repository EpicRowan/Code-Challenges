
def get_total_nodes(node):
	if not node.children:
		return 1
	count = 0
	for child in node.children:
		count += get_total_nodes(child)
	return 1 + count
