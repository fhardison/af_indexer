# create index
import re

def create_verses(books_list, opath):
    with open(opath, 'w', encoding="UTF-8") as g:
        lemma_count = 0
        for FILE in books_list:
            with open(FILE, 'r', encoding="UTF-8") as f:
                for line in f:
                    ref, cons = line.strip().split(" ", maxsplit=1)
                    ws = cons.strip().split(" ")
                    start = lemma_count + 1
                    end = lemma_count + len(ws)
                    print(f"{ref} {start} {end}", file=g)
                    lemma_count = end

def create_chapters(books_list, opath):
    with open(opath, 'w', encoding="UTF-8") as g:
        cur_cpt = 1
        cpt_start = 1
        wcount = 0
        for BOOK in books_list:
            with open(BOOK, 'r', encoding="UTF-8") as f:
                for line in f:
                    ref, cons = line.strip().split(" ", maxsplit=1)
                    matches = re.match(r"(\d\d)(\d\d)(\d\d)", ref)
                    bk = int(matches.group(1))
                    cpt = int(matches.group(2))
                    wcount += len(cons.strip().split(" "))
                    if cpt > cur_cpt:
                        print(f"{bk:02d}{cur_cpt:02d} {cpt_start} {wcount}", file=g)
                        cur_cpt +=1
                        cpt_start = wcount + 1
                # print last line
                print(f"{bk:02d}{cur_cpt:02d} {cpt_start} {wcount}", file=g)


def create_pericopes(verses_file, pericopes_file, ofile):
    verses = {}
    with open(verses_file, 'r') as f:
        for l in f:
            verse, start, end = l.strip().split(" ")
            verses[verse] = (start, end)
    with open(ofile, 'w') as g:
        with open(pericopes_file, 'r') as f:
            for line in f:
                if line:
                    peri, start, end, title = line.strip().split(" ", maxsplit=3)
                    print(f"{peri} {verses[start][0]} {verses[end][1]}", file=g)

def create_books(books_list, books_file):
    books = []
    tstart = 1
    tend= 0
    bookref = ""
    with open(books_file, 'w', encoding="UTF-8") as g:
        for FILE in books_list:
            with open(FILE, 'r', encoding="UTF-8") as f:
                for line in f:
                    ref, cons = line.strip().split(' ', maxsplit=1)
                    tend += len(cons.split(' '))
                    bookref = ref[0:2]
                print(f"{bookref} {tstart} {tend}", file=g)
                tstart = tend + 1
