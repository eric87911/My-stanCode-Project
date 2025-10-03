"""
File: my_drawing.py
Name:Eric
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    1.HAOPIECE

    2.This is my logo of my painting account,I am a ONEPIECE big fan,so I design a pirates flag pattern to be my icon.
    """
    window = GWindow(800, 800, title='haopiece')
    bg = GRect(800, 800)
    bg.filled = True
    bg.fill_color = 'black'
    window.add(bg)
    head = GOval(440, 340, x=180, y=230)
    head.filled = True
    head.fill_color = 'white'
    head.color = 'white'
    window.add(head)
    teeth_l = GPolygon()
    teeth_l.add_vertex((300, 520))
    teeth_l.add_vertex((300, 672))
    teeth_l.add_vertex((380, 680))
    teeth_l.add_vertex((380, 520))
    teeth_l.filled = True
    teeth_l.fill_color = 'white'
    teeth_l.color = 'white'
    window.add(teeth_l)
    teeth_2 = GPolygon()
    teeth_2.add_vertex((420, 520))
    teeth_2.add_vertex((420, 680))
    teeth_2.add_vertex((500, 672))
    teeth_2.add_vertex((500, 520))
    teeth_2.filled = True
    teeth_2.fill_color = 'white'
    teeth_2.color = 'white'
    window.add(teeth_2)
    eye = GOval(140, 140, x=420, y=352)
    eye.filled = True
    eye.fill_color = 'black'
    window.add(eye)
    h_l = GPolygon()
    h_l.add_vertex((312, 268))
    h_l.add_vertex((232, 432))
    h_l.add_vertex((228, 480))
    h_l.add_vertex((255, 434))
    h_l.add_vertex((320, 278))
    h_l.add_vertex((324, 265))
    h_l.filled = True
    h_l.fill_color = 'red'
    h_l.color = 'red'
    window.add(h_l)
    h_r = GPolygon()
    h_r.add_vertex((392, 280))
    h_r.add_vertex((305, 442))
    h_r.add_vertex((308, 488))
    h_r.add_vertex((335, 442))
    h_r.add_vertex((400, 284))
    h_r.add_vertex((398, 275))
    h_r.filled = True
    h_r.fill_color = 'red'
    h_r.color = 'red'
    window.add(h_r)
    h = GPolygon()
    h.add_vertex((240, 345))
    h.add_vertex((340, 390))
    h.add_vertex((385, 390))
    h.add_vertex((344, 365))
    h.filled = True
    h.fill_color = 'red'
    h.color = 'red'
    window.add(h)
    a = GLabel('A', x=380, y=540)
    a.font = '-50'
    window.add(a)
    a_ = GArc(60, 10, 0, 180)
    a_.filled = True
    a_.fill_color = 'black'
    window.add(a_, x=375, y=510)


if __name__ == '__main__':
    main()
