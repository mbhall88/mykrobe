#!/usr/bin/env python3

import os
filename = os.path.join("mccortex", "libs", "xxHash", "xxhsum.c")
lines = []
to_replace = "#if defined(MSDOS) || defined(OS2) || defined(WIN32) || defined(_WIN32) || defined(__CYGWIN__)\n"
replace_with = "#if defined(MSDOS) || defined(OS2) || defined(WIN32) || defined(_WIN32)\n"

with open(filename) as f:
    for line in f:
        if line == to_replace:
            line = replace_with
        lines.append(line)


with open(filename, "w") as f:
    print(*lines, sep="", file=f)



filename = os.path.join("mccortex", "libs", "bit_array", "bit_array.c")
lines = []
to_replace = "  c = (word_t)(w * ((word_t)~(word_t)0/255)) >> (sizeof(word_t) - 1) * 8;\n"
replace_with = "  return (word_t)(w * ((word_t)~(word_t)0/255)) >> (sizeof(word_t) - 1) * 8;\n"

with open(filename) as f:
    for line in f:
        if line == to_replace:
            line = replace_with
        lines.append(line)


with open(filename, "w") as f:
    print(*lines, sep="", file=f)
