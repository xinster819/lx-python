class LabsStat:
    ms_200 = 0;
    ms_500 = 0;
    ms_1000 = 0;
    ms_2000 = 0;
    ms_5000 = 0;
    req_count = 0;

    def __init__(self, date, type, uri):
      self.date = date;
      self.type = type;
      self.uri = uri;
