"""
File: Drawing
Name: Johnson
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=1130, height=1000, title='Girl with a Pearl Earring')

    background = GRect(1130, 1413)
    background.filled = True
    background.fill_color = 'black'
    background.color = 'black'
    window.add(background)

    face5 = GPolygon()
    face5.add_vertex((306, 189))
    face5.add_vertex((248, 277))
    face5.add_vertex((225, 354))
    face5.add_vertex((206, 489))
    face5.add_vertex((194, 677))
    face5.add_vertex((251, 686))
    face5.add_vertex((251, 730))
    face5.add_vertex((256, 774))
    face5.add_vertex((270, 818))
    face5.add_vertex((284, 842))
    face5.add_vertex((306, 864))
    face5.add_vertex((330, 875))
    face5.add_vertex((359, 880))
    face5.add_vertex((401, 874))
    face5.add_vertex((435, 861))
    face5.add_vertex((470, 845))
    face5.add_vertex((558, 794))
    face5.add_vertex((578, 776))
    face5.add_vertex((544, 759))
    face5.add_vertex((569, 728))
    face5.add_vertex((601, 691))
    face5.add_vertex((626, 657))
    face5.add_vertex((639, 629))
    face5.add_vertex((651, 588))
    face5.add_vertex((660, 551))
    face5.add_vertex((668, 505))
    face5.add_vertex((670, 459))
    face5.add_vertex((672, 431))
    face5.add_vertex((657, 387))
    face5.add_vertex((640, 342))
    face5.add_vertex((612, 292))
    face5.add_vertex((585, 245))
    face5.add_vertex((566, 217))
    face5.add_vertex((538, 185))
    face5.add_vertex((515, 162))
    face5.add_vertex((489, 141))
    face5.add_vertex((474, 129))
    face5.add_vertex((433, 93))
    face5.add_vertex((396, 111))
    face5.add_vertex((365, 129))
    face5.add_vertex((340, 152))
    face5.add_vertex((320, 171))
    face5.filled = True
    face5.fill_color = 'wheat'
    face5.color = 'wheat'
    window.add(face5)

    face1 = GPolygon()
    face1.add_vertex((230, 368))
    face1.add_vertex((208, 584))
    face1.add_vertex((286, 602))
    face1.add_vertex((280, 380))
    face1.filled = True
    face1.fill_color = 'cornsilk'
    face1.color = 'cornsilk'
    window.add(face1)

    face2 = GPolygon()
    face2.add_vertex((410, 133))
    face2.add_vertex((340, 217))
    face2.add_vertex((511, 311))
    face2.add_vertex((546, 290))
    face2.add_vertex((490, 202))
    face2.filled = True
    face2.fill_color = 'cornsilk'
    face2.color = 'cornsilk'
    window.add(face2)

    face3 = GPolygon()
    face3.add_vertex((662, 371))
    face3.add_vertex((600, 549))
    face3.add_vertex((515, 700))
    face3.add_vertex((567, 704))
    face3.add_vertex((630, 603))
    face3.add_vertex((658, 507))
    face3.add_vertex((659, 451))
    face3.filled = True
    face3.fill_color = 'tan'
    face3.color = 'tan'
    window.add(face3)

    face4 = GOval(10, 10, x=419, y=764)
    face4.filled = True
    face4.fill_color = 'black'
    face4.color = 'black'
    window.add(face4)

    eyelash1 = GPolygon()
    eyelash1.add_vertex((270, 256))
    eyelash1.add_vertex((270, 256))
    eyelash1.add_vertex((288, 269))
    eyelash1.add_vertex((304, 287))
    eyelash1.add_vertex((314, 305))
    eyelash1.filled = True
    eyelash1.fill_color = 'brown'
    eyelash1.color = 'brown'
    window.add(eyelash1)

    eyelash2 = GPolygon()
    eyelash2.add_vertex((372, 468))
    eyelash2.add_vertex((383, 486))
    eyelash2.add_vertex((404, 403))
    eyelash2.add_vertex((435, 378))
    eyelash2.add_vertex((467, 364))
    eyelash2.add_vertex((504, 354))
    eyelash2.add_vertex((528, 356))
    eyelash2.add_vertex((545, 367))
    eyelash2.add_vertex((561, 385))
    eyelash2.add_vertex((586, 429))
    eyelash2.add_vertex((578, 422))
    eyelash2.add_vertex((551, 381))
    eyelash2.add_vertex((530, 368))
    eyelash2.add_vertex((506, 364))
    eyelash2.add_vertex((459, 377))
    eyelash2.add_vertex((424, 404))
    eyelash2.add_vertex((387, 445))
    eyelash2.filled = True
    eyelash2.fill_color = 'brown'
    eyelash2.color = 'brown'
    window.add(eyelash2)

    eyelash3 = GPolygon()
    eyelash3.add_vertex((380, 497))
    eyelash3.add_vertex((404, 470))
    eyelash3.add_vertex((438, 444))
    eyelash3.add_vertex((464, 425))
    eyelash3.add_vertex((500, 434))
    eyelash3.add_vertex((536, 444))
    eyelash3.add_vertex((554, 457))
    eyelash3.add_vertex((570, 476))
    eyelash3.add_vertex((580, 501))
    eyelash3.add_vertex((560, 478))
    eyelash3.add_vertex((539, 454))
    eyelash3.add_vertex((500, 438))
    eyelash3.add_vertex((467, 438))
    eyelash3.add_vertex((440, 449))
    eyelash3.add_vertex((414, 467))
    eyelash3.filled = True
    eyelash3.fill_color = 'brown'
    eyelash3.color = 'brown'
    window.add(eyelash3)

    eyelash4 = GPolygon()
    eyelash4.add_vertex((243, 302))
    eyelash4.add_vertex((260, 303))
    eyelash4.add_vertex((278, 305))
    eyelash4.add_vertex((295, 316))
    eyelash4.add_vertex((308, 327))
    eyelash4.add_vertex((281, 315))
    eyelash4.add_vertex((264, 310))
    eyelash4.add_vertex((246, 308))
    eyelash4.filled = True
    eyelash4.fill_color = 'brown'
    eyelash4.color = 'brown'
    window.add(eyelash4)

    eyelash5 = GPolygon()
    eyelash5.add_vertex((393, 523))
    eyelash5.add_vertex((410, 549))
    eyelash5.add_vertex((438, 567))
    eyelash5.add_vertex((473, 572))
    eyelash5.add_vertex((504, 569))
    eyelash5.add_vertex((538, 555))
    eyelash5.add_vertex((567, 531))
    eyelash5.add_vertex((549, 554))
    eyelash5.add_vertex((507, 571))
    eyelash5.add_vertex((476, 577))
    eyelash5.add_vertex((442, 575))
    eyelash5.add_vertex((416, 561))
    eyelash5.filled = True
    eyelash5.fill_color = 'brown'
    eyelash5.color = 'brown'
    window.add(eyelash5)

    eye1 = GPolygon()
    eye1.add_vertex((386, 507))
    eye1.add_vertex((411, 494))
    eye1.add_vertex((438, 483))
    eye1.add_vertex((468, 477))
    eye1.add_vertex((500, 480))
    eye1.add_vertex((530, 487))
    eye1.add_vertex((550, 499))
    eye1.add_vertex((562, 507))
    eye1.add_vertex((548, 523))
    eye1.add_vertex((529, 535))
    eye1.add_vertex((499, 544))
    eye1.add_vertex((469, 549))
    eye1.add_vertex((439, 543))
    eye1.add_vertex((415, 529))
    eye1.filled = True
    eye1.fill_color = 'white'
    eye1.color = 'brown'
    window.add(eye1)

    eye2 = GPolygon()
    eye2.add_vertex((240, 317))
    eye2.add_vertex((260, 320))
    eye2.add_vertex((283, 327))
    eye2.add_vertex((301, 336))
    eye2.add_vertex((288, 346))
    eye2.add_vertex((270, 350))
    eye2.add_vertex((254, 352))
    eye2.add_vertex((237, 350))
    eye2.add_vertex((230, 346))
    eye2.filled = True
    eye2.fill_color = 'white'
    eye2.color = 'brown'
    window.add(eye2)

    eye3 = GOval(31, 29, x=250, y=323)
    eye3.filled = True
    eye3.fill_color = 'black'
    eye3.color = 'white'
    window.add(eye3)

    eye5 = GOval(68, 70, x=442, y=478)
    eye5.filled = True
    eye5.fill_color = 'black'
    eye5.color = 'white'
    window.add(eye5)

    eye5 = GOval(18, 18, x=448, y=492)
    eye5.filled = True
    eye5.fill_color = 'white'
    eye5.color = 'black'
    window.add(eye5)

    eye4 = GOval(11, 11, x=253, y=323)
    eye4.filled = True
    eye4.fill_color = 'white'
    eye4.color = 'black'
    window.add(eye4)

    nose1 = GPolygon()
    nose1.add_vertex((250, 685))
    nose1.add_vertex((349, 685))
    nose1.add_vertex((354, 656))
    nose1.add_vertex((339, 632))
    nose1.add_vertex((314, 621))
    nose1.add_vertex((285, 632))
    nose1.add_vertex((268, 648))
    nose1.filled = True
    nose1.fill_color = 'tan'
    nose1.color = 'tan'
    window.add(nose1)

    nose2 = GPolygon()
    nose2.add_vertex((279, 685))
    nose2.add_vertex((349, 685))
    nose2.add_vertex((339, 669))
    nose2.add_vertex((320, 662))
    nose2.add_vertex((304, 657))
    nose2.add_vertex((292, 666))
    nose2.filled = True
    nose2.fill_color = 'brown'
    nose2.color = 'brown'
    window.add(nose2)

    mouth = GPolygon()
    mouth.add_vertex((287, 774))
    mouth.add_vertex((304, 755))
    mouth.add_vertex((314, 752))
    mouth.add_vertex((329, 764))
    mouth.add_vertex((336, 769))
    mouth.add_vertex((354, 751))
    mouth.add_vertex((366, 747))
    mouth.add_vertex((389, 755))
    mouth.add_vertex((404, 779))
    mouth.add_vertex((411, 788))
    mouth.add_vertex((421, 793))
    mouth.add_vertex((430, 795))
    mouth.add_vertex((439, 799))
    mouth.add_vertex((423, 822))
    mouth.add_vertex((400, 833))
    mouth.add_vertex((379, 845))
    mouth.add_vertex((353, 848))
    mouth.add_vertex((333, 843))
    mouth.add_vertex((320, 828))
    mouth.add_vertex((314, 815))
    mouth.add_vertex((310, 800))
    mouth.add_vertex((311, 785))
    mouth.filled = True
    mouth.fill_color = 'chocolate'
    mouth.color = 'chocolate'
    window.add(mouth)

    mouth1 = GPolygon()
    mouth1.add_vertex((313, 792))
    mouth1.add_vertex((434, 800))
    mouth1.add_vertex((372, 798))
    mouth1.filled = True
    mouth1.fill_color = 'brown'
    mouth1.color = 'brown'
    window.add(mouth1)

    hair1 = GPolygon()
    hair1.add_vertex((672, 431))
    hair1.add_vertex((657, 387))
    hair1.add_vertex((640, 342))
    hair1.add_vertex((612, 292))
    hair1.add_vertex((585, 245))
    hair1.add_vertex((566, 217))
    hair1.add_vertex((538, 185))
    hair1.add_vertex((515, 162))
    hair1.add_vertex((489, 141))
    hair1.add_vertex((474, 129))
    hair1.add_vertex((433, 93))
    hair1.add_vertex((460, 80))
    hair1.add_vertex((485, 79))
    hair1.add_vertex((516, 79))
    hair1.add_vertex((550, 86))
    hair1.add_vertex((716, 244))
    hair1.add_vertex((681, 322))
    hair1.filled = True
    hair1.fill_color = 'lightblue'
    hair1.color = 'lightblue'
    window.add(hair1)

    hair2 = GPolygon()
    hair2.add_vertex((680, 322))
    hair2.add_vertex((713, 248))
    hair2.add_vertex((738, 207))
    hair2.add_vertex((774, 168))
    hair2.add_vertex((859, 216))
    hair2.add_vertex((852, 287))
    hair2.add_vertex((808, 322))
    hair2.add_vertex((752, 527))
    hair2.add_vertex((730, 438))
    hair2.filled = True
    hair2.fill_color = 'navy'
    hair2.color = 'navy'
    window.add(hair2)

    hair3 = GPolygon()
    hair3.add_vertex((675, 305))
    hair3.add_vertex((632, 323))
    hair3.add_vertex((673, 424))
    hair3.add_vertex((705, 487))
    hair3.add_vertex((721, 653))
    hair3.add_vertex((753, 521))
    hair3.add_vertex((730, 439))
    hair3.filled = True
    hair3.fill_color = 'darkgray'
    hair3.color = 'darkgray'
    window.add(hair3)

    hair4 = GPolygon()
    hair4.add_vertex((555, 89))
    hair4.add_vertex((715, 248))
    hair4.add_vertex((740, 206))
    hair4.add_vertex((776, 168))
    hair4.add_vertex((687, 67))
    hair4.add_vertex((645, 63))
    hair4.add_vertex((616, 65))
    hair4.add_vertex((584, 75))
    hair4.filled = True
    hair4.fill_color = 'lightskyblue'
    hair4.color = 'lightskyblue'
    window.add(hair4)

    hair5 = GPolygon()
    hair5.add_vertex((683, 61))
    hair5.add_vertex((720, 47))
    hair5.add_vertex((769, 39))
    hair5.add_vertex((820, 45))
    hair5.add_vertex((840, 55))
    hair5.add_vertex((872, 74))
    hair5.add_vertex((880, 85))
    hair5.add_vertex((904, 112))
    hair5.add_vertex((918, 151))
    hair5.add_vertex((942, 194))
    hair5.add_vertex((951, 217))
    hair5.add_vertex((958, 263))
    hair5.add_vertex((964, 301))
    hair5.add_vertex((772, 435))
    hair5.add_vertex((807, 325))
    hair5.add_vertex((851, 289))
    hair5.add_vertex((858, 215))
    hair5.add_vertex((824, 196))
    hair5.add_vertex((777, 168))
    hair5.filled = True
    hair5.fill_color = 'coral'
    hair5.color = 'coral'
    window.add(hair5)

    hair6 = GPolygon()
    hair6.add_vertex((850, 292))
    hair6.add_vertex((808, 322))
    hair6.add_vertex((752, 527))
    hair6.add_vertex((680, 840))
    hair6.add_vertex((786, 855))
    hair6.filled = True
    hair6.fill_color = 'yellow'
    hair6.color = 'yellow'
    window.add(hair6)

    hair7 = GPolygon()
    hair7.add_vertex((786, 855))
    hair7.add_vertex((850, 292))
    hair7.add_vertex((884, 287))
    hair7.add_vertex((825, 860))
    hair7.filled = True
    hair7.fill_color = 'gold'
    hair7.color = 'gold'
    window.add(hair7)

    hair8 = GPolygon()
    hair8.add_vertex((884, 287))
    hair8.add_vertex((916, 282))
    hair8.add_vertex((891, 860))
    hair8.add_vertex((825, 860))
    hair8.filled = True
    hair8.fill_color = 'yellow'
    hair8.color = 'yellow'
    window.add(hair8)

    hair9 = GPolygon()
    hair9.add_vertex((888, 810))
    hair9.add_vertex((990, 786))
    hair9.add_vertex((996, 474))
    hair9.add_vertex((957, 261))
    hair9.add_vertex((916, 282))
    hair9.filled = True
    hair9.fill_color = 'gold'
    hair9.color = 'gold'
    window.add(hair9)

    hair10 = GPolygon()
    hair10.add_vertex((960, 263))
    hair10.add_vertex((981, 302))
    hair10.add_vertex((997, 364))
    hair10.add_vertex((1016, 427))
    hair10.add_vertex((1036, 474))
    hair10.add_vertex((1056, 530))
    hair10.add_vertex((1075, 595))
    hair10.add_vertex((1064, 939))
    hair10.add_vertex((995, 868))
    hair10.add_vertex((990, 786))
    hair10.add_vertex((996, 474))
    hair10.add_vertex((957, 261))
    hair10.filled = True
    hair10.fill_color = 'lightskyblue'
    hair10.color = 'lightskyblue'
    window.add(hair10)

    hair11 = GPolygon()
    hair11.add_vertex((988, 787))
    hair11.add_vertex((896, 813))
    hair11.add_vertex((895, 893))
    hair11.add_vertex((981, 906))
    hair11.filled = True
    hair11.fill_color = 'lightblue'
    hair11.color = 'lightblue'
    window.add(hair11)

    hair12 = GPolygon()
    hair12.add_vertex((787, 858))
    hair12.add_vertex((896, 867))
    hair12.add_vertex((880, 959))
    hair12.add_vertex((784, 962))
    hair12.filled = True
    hair12.fill_color = 'lightskyblue'
    hair12.color = 'lightskyblue'
    window.add(hair12)

    ear1 = GPolygon()
    ear1.add_vertex((672, 422))
    ear1.add_vertex((669, 467))
    ear1.add_vertex((666, 513))
    ear1.add_vertex((660, 548))
    ear1.add_vertex((648, 589))
    ear1.add_vertex((635, 632))
    ear1.add_vertex((619, 664))
    ear1.add_vertex((595, 697))
    ear1.add_vertex((572, 724))
    ear1.add_vertex((543, 753))
    ear1.add_vertex((557, 766))
    ear1.add_vertex((582, 773))
    ear1.add_vertex((600, 768))
    ear1.add_vertex((684, 686))
    ear1.add_vertex((708, 671))
    ear1.add_vertex((720, 664))
    ear1.add_vertex((708, 489))
    ear1.filled = True
    ear1.fill_color = 'brown'
    ear1.color = 'brown'
    window.add(ear1)

    ear2 = GPolygon()
    ear2.add_vertex((672, 555))
    ear2.add_vertex((662, 599))
    ear2.add_vertex((659, 653))
    ear2.add_vertex((689, 647))
    ear2.add_vertex((704, 631))
    ear2.add_vertex((688, 627))
    ear2.add_vertex((680, 620))
    ear2.add_vertex((677, 608))
    ear2.add_vertex((684, 599))
    ear2.add_vertex((694, 599))
    ear2.add_vertex((705, 601))
    ear2.add_vertex((708, 576))
    ear2.add_vertex((701, 559))
    ear2.add_vertex((680, 555))
    ear2.filled = True
    ear2.fill_color = 'wheat'
    ear2.color = 'wheat'
    window.add(ear2)

    neck = GPolygon()
    neck.add_vertex((719, 664))
    neck.add_vertex((672, 686))
    neck.add_vertex((587, 773))
    neck.add_vertex((578, 776))
    neck.add_vertex((558, 794))
    neck.add_vertex((470, 845))
    neck.add_vertex((435, 861))
    neck.add_vertex((401, 874))
    neck.add_vertex((397, 971))
    neck.add_vertex((559, 885))
    neck.add_vertex((605, 866))
    neck.add_vertex((637, 855))
    neck.add_vertex((700, 838))
    neck.add_vertex((723, 686))
    neck.filled = True
    neck.fill_color = 'tan'
    neck.color = 'tan'
    window.add(neck)

    earring1 = GOval(116, 125, x=600, y=686)
    earring1.filled = True
    earring1.fill_color = 'brown'
    earring1.color = 'brown'
    window.add(earring1)

    earring2 = GOval(101, 107, x=608, y=692)
    earring2.filled = True
    earring2.fill_color = 'silver'
    earring2.color = 'silver'
    window.add(earring2)

    earring3 = GOval(65, 84, x=629, y=707)
    earring3.filled = True
    earring3.fill_color = 'brown'
    earring3.color = 'brown'
    window.add(earring3)

    earring4 = GOval(56, 68, x=633, y=715)
    earring4.filled = True
    earring4.fill_color = 'silver'
    earring4.color = 'silver'
    window.add(earring4)

    earring5 = GPolygon()
    earring5.add_vertex((657, 692))
    earring5.add_vertex((664, 708))
    earring5.add_vertex((666, 726))
    earring5.add_vertex((655, 753))
    earring5.add_vertex((645, 762))
    earring5.add_vertex((632, 769))
    earring5.add_vertex((617, 769))
    earring5.add_vertex((605, 766))
    earring5.add_vertex((607, 761))
    earring5.add_vertex((616, 762))
    earring5.add_vertex((627, 762))
    earring5.add_vertex((640, 760))
    earring5.add_vertex((647, 754))
    earring5.add_vertex((653, 740))
    earring5.add_vertex((657, 726))
    earring5.add_vertex((657, 692))
    earring5.add_vertex((658, 713))
    earring5.add_vertex((652, 702))
    earring5.add_vertex((648, 697))
    earring5.add_vertex((644, 693))
    earring5.filled = True
    earring5.fill_color = 'brown'
    earring5.color = 'brown'
    window.add(earring5)

    shirt1 = GPolygon()
    shirt1.add_vertex((337, 1000))
    shirt1.add_vertex((870, 1000))
    shirt1.add_vertex((872, 996))
    shirt1.add_vertex((784, 964))
    shirt1.add_vertex((786, 856))
    shirt1.add_vertex((707, 850))
    shirt1.add_vertex((702, 836))
    shirt1.add_vertex((648, 848))
    shirt1.add_vertex((594, 868))
    shirt1.add_vertex((547, 889))
    shirt1.add_vertex((508, 910))
    shirt1.add_vertex((468, 931))
    shirt1.add_vertex((438, 947))
    shirt1.add_vertex((401, 970))
    shirt1.add_vertex((374, 991))
    shirt1.filled = True
    shirt1.fill_color = 'brown'
    shirt1.color = 'brown'
    window.add(shirt1)

    shirt2 = GPolygon()
    shirt2.add_vertex((475, 970))
    shirt2.add_vertex((544, 946))
    shirt2.add_vertex((621, 932))
    shirt2.add_vertex((694, 930))
    shirt2.add_vertex((696, 855))
    shirt2.add_vertex((498, 924))
    shirt2.add_vertex((440, 952))
    shirt2.add_vertex((402, 977))
    shirt2.add_vertex((370, 1000))
    shirt2.filled = True
    shirt2.fill_color = 'white'
    shirt2.color = 'white'
    window.add(shirt2)


if __name__ == '__main__':
    main()
