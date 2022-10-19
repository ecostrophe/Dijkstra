class Vertex:
	num_vertex= 0
	def __init__(self, point, start= False, target = False):
		self.id_vertex = self.num_vertex
		self.xpos = point[0]
		self.ypos = point[1]
		self.isvisited = False
		self.is_start_vertex = start
		self.is_target_vertex = target
		self.value = 0
		self.vertex = [self.xpos, self.ypos]
		self.previous_vertex =[0,0]
		self.zone1 = False
		self.zone2 = False
		self.zone3 = False
		Vertex.num_vertex +=1
		
	def __str__(self):
		return "id: "+str(self.id_vertex)+" visited: "+str(self.isvisited)+" value: "+str(self.value)+" first: "+str(self.is_start_vertex)+" target: "+str(self.is_target_vertex)

