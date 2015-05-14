from cscanner import Scanner
from cparser import Parser

source = """BEGIN
OP 1997
LOOP n
LOOP n
OP 1
END
LOOP 12
OP 3
OP 3
END
END
END"""

# source = """BEGIN
# LOOP n
# OP 3
# END
# END"""

s = Scanner(source, 1)
p = Parser(s)

p.compile()
