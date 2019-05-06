#!/usr/bin/env python3

from zencad import *

def angle():
	z = 35
	s = 130 # длина сегмента
	t = 10
	f = 90 # удаление ребра жёсткости
	fo = f - t*math.sqrt(2)
	
	s_width = 30 #ширина крепления вала
	s_radius = 6 #радиус вала
	s_center = 85 # удаление оси вала от внутреннего
	
	m = box(s,t,z) + box(t,s,z)
	stifner = (
		polygon([(0,0,0), (f,0,0), (0,f,0)]) 
		- polygon([(0,0,0), (fo,0,0), (0,fo,0)])
	).extrude(z*2/3)
	
	m = m + stifner
	ear = (
		(
			box(s_width, t, s_radius*3/2) 
			- cylinder(h=t, r=s_radius)
				.rotateX(-deg(90))
					.up(s_radius)
						.right(s_width/2)
		)
		.right(s-s_width/2-s_center)
			.up(z)
	)

	return m + ear

ang1 = angle()
ang2 = angle().mirrorYZ().right(130*2)

disp(ang1)
disp(ang2)

show()