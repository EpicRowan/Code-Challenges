
class balanced:
	def find(self,sought):
		current = self
		while current:
			if current.data == sought:
				return True
			elif sought < current.data:
				current = current.left
			elif sought >current.data:
				current = current.right
