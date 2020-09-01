
def has_connection(node1, node2):
	seen = set([node1])
	to_visit = [node1]
	while to_visit:
		current = to_visit.pop()
		if current is node2:
			return True
		else:
			for node in current.adjacent - seen:
				to_visit.append(node)
				seen.add(node)
	return False