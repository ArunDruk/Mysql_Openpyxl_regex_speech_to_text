
from File_Handler import File_Handler as _TXTOBJ
from text_headers import payroll_txt_file_header as _HEADERS

def Write_txt_without_header(rows):
    def return_str(row):
        return '    '.join(map(str, row.values()))

    with open("MANGL_BLKLN_JE_EXTRACT.tsv", 'w') as file:
        file.writelines("\n".join([return_str(row) for row in rows]))

def Read_txt_with_header(self, header):
        self.header = [str(column).strip() for column in header]
        with open(self.path, 'r') as file:
            return [dict(zip(self.header, line))
                    for line in list((line.rstrip().replace('"', '').split(self.separator)
                                      for line in file))]


def process_files():
    def counter(index,**kwargs):
      # import datetime as dt
      from datetime import date
      import random
      # kwargs['REFERENCE21'] = int(dt.datetime.now().strftime("%Y%m%d%H%M%S%f"))+int(index)
      kwargs['ACCOUNTING_DATE'] = date.today().strftime("%m/%d/%Y")
      return kwargs
    #for number in range(0,4):
    path = "MANGL_BLKLN_JE_EXTRACT.tsv"  #PS_CAUTO_Accrual__BW191108.txt"  #PS_401Bill_GL_CAUTO.txt"   #C:\IS_Pyrl_Trsy_Files\\"+files[number]
    cobj = _TXTOBJ(path,"   ")
    cobj.Write_txt_without_header([counter(index+1,**row) for index, row in enumerate(cobj.Read_txt_with_header(_HEADERS()))])


process_files()