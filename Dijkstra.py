import math
from Vertex import Vertex
import random
import pygame
import time

class Dijkstra:
	def __init__(self, vertexS, vertexT, points):
		self.startvx = Vertex(vertexS, start= True)
		self.targetvx = Vertex(vertexT,  target= True)
		self.all_vertex = list(Vertex(p) for p in points)
		self.all_vertex.append(self.startvx)
		self.all_vertex.append(self.targetvx)
		self.visited_list = []
		self.unvisited_list = []
		self.scan()

	def get_distence(self, v1, v2):
		distance =math.sqrt((v2[0]-v1[0])**2 +(v2[1]-v1[1])**2)
		return distance
	
	def unvisited(self,vtx):
		if vtx.isvisited:
			return False
		else:
			return True

	def set_unvisited_list(self):
		self.unvisited_list.clear()
		self.visited_list.clear()
		for v in self.all_vertex:
			if v.isvisited == True:
				self.visited_list.append(v)
			else:
				self.unvisited_list.append(v)
				
	def scan(self):
		start = self.startvx
		target = self.targetvx
		dist_index = (self.get_distence(start.vertex,target.vertex)/3)
		for vx in self.all_vertex:
			self.set_unvisited_list()
			if vx.vertex == start.vertex or vx.vertex == target.vertex:
				pass
			else:
				dist_vx = self.get_distence(start.vertex,vx.vertex)
				if dist_vx <= dist_index:
					vx.zone1 = True
				elif dist_vx <= (dist_index*2):
					vx.zone2 = True
				elif dist_vx > (dist_index*2):
					vx.zone3 = True
	
	def get_neighbors(self, step):
		neighbors1 = []
		neighbors2 = []
		neighbors3 = []
		for vx in self.all_vertex:
			if vx.zone1 and step==1:
				neighbors1.append(vx)
			elif vx.zone2 and step==2:
				neighbors2.append(vx)
			elif vx.zone3 and step==3:
				neighbors3.append(vx)
		if step ==1:
			return neighbors1
		elif step ==2:
			return neighbors2
		elif step ==3:
			return neighbors3
		
	def find_path(self,win):
		current_vx = [self.startvx]
		all_paths = [[],[],[],[]]
		for step in range(1,4):
			neighbor_vx = self.get_neighbors(step)
			for current in current_vx:
				for n in neighbor_vx:
					dist_n = (self.get_distence(current.vertex, n.vertex))+current.value
					if n.value == 0 or n.value >= dist_n:
						n.value = dist_n
						n.isvisited = True
						n.previous_vertex = current.vertex
						if len(all_paths[step-1])>0:
							if all_paths[step-1][1]>dist_n:
								all_paths[step-1].clear()
								all_paths[step-1].append(n.vertex)
								all_paths[step-1].append(dist_n)
							else:
								pass
						else:
							all_paths[step-1].append(n.vertex)
							all_paths[step-1].append(dist_n)
					else:
						n.isvisited = True
			current_vx.clear()
			current_vx= neighbor_vx.copy()
		target_vx= self.targetvx
		for current in current_vx:
			dist_n = (self.get_distence(current.vertex, target_vx.vertex))+current.value
			if target_vx.value == 0 or target_vx.value >= dist_n:
				target_vx.value = dist_n
				target_vx.isvisited = True
				target_vx.previous_vertex = current.vertex
				if len(all_paths[3])>0:
					if all_paths[3][1]>dist_n:
						all_paths[3].clear()
						all_paths[3].append(target_vx.vertex)
						all_paths[3].append(dist_n)
					else:
						pass
				else:
					all_paths[3].append(target_vx.vertex)
					all_paths[3].append(dist_n)
			else:
				target_vx.isvisited = True
		#
		retro_path=[]
		for vtx in self.all_vertex:
			retro_path.append([vtx.vertex,vtx.previous_vertex])
		
		#
		go = True
		path = []
		now_pos= self.targetvx.vertex
		next_pos = []
		while go:
			for retro in retro_path:
				if retro[0] == now_pos:
					next_pos = retro[1]
					if now_pos == self.startvx.vertex or next_pos == [0,0]:
						go = False
						break
					path.append([now_pos,next_pos])
					now_pos = next_pos
				else:
					pass
		else:
			for pa in path:
				pygame.draw.lines(win, (255,0,127),False,[(pa[0][0],pa[0][1]),(pa[1][0],pa[1][1])], 2)
				dist_c = (self.get_distence(self.startvx.vertex,self.targetvx.vertex)/3)
				pygame.draw.circle(win,(0,0,0),(self.startvx.vertex[0],self.startvx.vertex[1]),dist_c,2)
				pygame.draw.circle(win,(0,0,255),(self.startvx.vertex[0],self.startvx.vertex[1]),dist_c*2,2)
				pygame.display.update()
		

#start tests
pygame.init()
win = pygame.display.set_mode((1000,900))
run = True
red = (255,0,0)
yellow = (100,100,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
weight = 10

def show_point(win,vertex,color,weight=weight):
	v = vertex.vertex
	pygame.draw.circle(win,color,(v[0],v[1]),weight,0)
	fontpos = pygame.font.Font('freesansbold.ttf',15)
	idvx= fontpos.render(str(vertex.id_vertex),True,color)
	txtpos= fontpos.render(str(v[0])+":"+str(v[1]),True,color)
	prepos= fontpos.render("N.V:"+str(vertex.previous_vertex[0])+":"+str(vertex.previous_vertex[1]),True,red)#N.V: the nearest vertex
	win.blit(idvx,(v[0]-10,v[1]-30))
	win.blit(txtpos,(v[0]+weight,v[1]+weight))
	win.blit(prepos,(v[0]-10,v[1]+25))

while run:
	me= [200,315]
	tar =  [random.randint(0,800),random.randint(0,800)]
	positions = []
	for n in range (10):
		p = [random.randint(0,800),random.randint(0,800)]
		positions.append(p)
	dj = Dijkstra(me,tar,positions)
	win.fill(white)
	for p in dj.all_vertex:
		if p.zone1:
			show_point(win,p,black,weight)
		elif p.zone2:
			show_point(win,p,blue,weight)
		elif p.zone3:
			show_point(win,p,yellow,weight)
	show_point(win,dj.startvx,red,weight)
	show_point(win,dj.targetvx,green,weight)
	dj.find_path(win)
	time.sleep(1)
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
