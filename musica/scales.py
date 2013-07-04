class Scale(list):

  def index(self):

  def current(self):

  def next(self):

  def previous(num=1):

  private:
  def get_at(index):
    if index >= 0
      at(index % self.size)
    else
      index = self.size + index
      get_at(index)