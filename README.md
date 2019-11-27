# af-indexer

A repo of tools that creates index files for JTauber's [vocabulary-tools](https://github.com/jtauber/vocabulary-tools) for the Apostolic Fathers format that is being used by <https://github.com/jtauber/greek-texts>.

NB: It currently doesn't ignore in line markup and assumes that the only things on each line are tokens. (TODO ITEM)

NB: You will needed to generate a `tokens.txt` file where each token has the following format:

`index text-in-file normalized POS parse alt-parse lemma`

If you're not interested in a POS or the parse data then just include a place holder such as in the example below.

```
1 ܟܬܒܐ ܟܬܒܐ POS MTAG MTAGN ܟܬܒܐ
```

NB: The index is the index of the token in the corpus, not the file it comes from.


It defines four functions that map verses, chapters, books, and pericopes onto token index in the corpus:

* `create_verses`
* `create_chapters`
* `create_books`
* `create_pericopes`

It assumes that the books will be in separate files, but reads the book and chapter code from the file and thus *should* still work for works where all books are in the same file.

It also includes a `main.py` file which contains code that will read these index files. It assumes that you are generating verses, chapters, books, and pericopes. If not then edit this part:

```
ChunkType = enum.Enum("ChunkType", "book chapter verse pericope")
TokenType = enum.Enum("TokenType", "text form lemma")

chunk_data_filename = {
    ChunkType.book: "books.txt",
    ChunkType.chapter: "chapters.txt",
    ChunkType.verse: "verses.txt",
    ChunkType.pericope: "pericopes.txt",
}
```

It also includes `__init__.py` which like `main.py` was taken from JTauber's [vocabulary-tools](https://github.com/jtauber/vocabulary-tools). This init file is needed to be able to import the module to vocabulary-tools.

# Functions

## `create_verses`

Creates the following output which reads as `(booknum)(cpt_num)(verse_num) start_token end_token`:

```
010101 1 8
010102 9 18
010103 19 30
...
```
## `create_chapters`

Creates the following output which reads as: `(booknum)(cpt_num) start_token end_token`


```
0101 1 304
0102 305 636
0103 637 874
...
```


## `create_books`

Creates the following output which reada as `booknum start_token end_token`:

```
01 1 13979
02 13980 22772
03 22773 38006
...
```


## `create_pericopes`

Creates the following output which reads as `booknum§pericope_num start_token end_token`:

```
01§01 1 175
01§02 176 290
01§03 291 453
...
```




# Example usage

```
# Create indexes for project

import create_indexes

# an this should be a list of the file names relative to this script.
from utils import BOOKS

create_indexes.create_chapters(SYBOOKS, "chapters.txt")
create_indexes.create_verses(SYBOOKS, "verses.txt")
create_indexes.create_books(SYBOOKS, "books.txt")

# this should be called after create_verses as it depends on the verse list
create_indexes.create_pericopes("verses.txt", "sections.txt", "pericopes.txt")
```

Running the following will output:

* verses.txt
* chapters.txt
* books.txt
* pericopes.txt
