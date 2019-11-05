from dataclasses import dataclass


@dataclass
class Dier:
    naam: str
    soort: ""
    aantalPoten: 0
    kleur: ""
    geluid: ""


def parse_line(line : str) -> Dier:
    naam, soort, aantalpoten, kleur, geluid = line.split(' - ')
    d = Dier(naam, soort, int(aantalpoten), kleur, geluid)
    return d


def parse_text(str : str) -> [Dier]:
    dieren = []
    for line in str.splitlines():
        d = parse_line(line)
        dieren.append(d)
    return dieren


if __name__ == '__main__':
    dieren = []
    # r = tekst lezen
    # rb = binaire code lezen (image)
    # w = schrijven
    
    # functie "open" is contentmanager
    # dankzij with niet nodig om file te closen
    with open('dieren.txt', 'r') as f:
        dieren = parse_text(f.read())

    for dier in dieren:
        print(dier)