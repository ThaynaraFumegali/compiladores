# Classe responsável por gerar os erros

class Error:
  def __init__(self, start_position, end_position, error_name, details):
    self.start_position = start_position
    self.end_position = end_position
    self.error_name = error_name
    self.details = details

  def __repr__(self):
    return f"{self.error_name}: {self.details}\nlinha: {self.start_position.line + 1}, coluna: {self.start_position.column}"
