# af-indexer

A repo of tools that creates index files for the Apostolic Fathers format that is being used by <https://github.com/jtauber/greek-texts>.

It defines four functions that map verses, chapters, books, and pericopes onto token index in the corpus:

* `create_verses`
* `create_chapters`
* `create_books`
* `create_pericopes`

It assumes that the books will be in separate files, but reads the book and chapter code from the file and thus *should* still work for works where all books are in the same file.

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
