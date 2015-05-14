class Scanner(object):

  def __init__(self, source, line):

    self.line = line
    self.row = 0;
    self.column = 0
    self.ended = False
    
    self.source = source
    self.source = source.split('\n')

    for i in range(len(self.source)):
        self.source[i] = self.source[i].strip()
        self.source[i] = self.source[i].split(' ')
      
  def next(self):

    if (self.ended):
        return None

    line = self.source[self.row]
    term = line[self.column]

    if (self.column < len(line)-1):
        self.column += 1
    
    elif (self.row < len(self.source)-1):
        self.row += 1
        self.line += 1
        self.column = 0

    else:
        self.ended = True

    return term
