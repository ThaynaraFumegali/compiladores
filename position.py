class Position:
  def __init__(self, index, line, column):
    self.index = index
    self.line = line
    self.column = column

  def advance(self, current_char=None):
    self.index += 1
    self.column += 1

    if current_char == '\n':
      self.column = 0
      self.line += 1

    return self

  def position_copy(self):
    return Position(self.index, self.line, self.column)
