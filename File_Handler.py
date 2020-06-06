class File_Handler():
    
    def __init__(self,path,separator):
        # self._validate_params(path,separator)
        self.path = path
        self.separator = separator 
      
    
    def __call__(self,path,separator):
        self._validate_params(path,separator)
        self.path = path
        self.separator = separator
    
    # def _validate_params(self,path,separator):
    #     from tc_logs import error_with_no_picture as Error_
    #     if path is None:
    #       Error_("File path Mandatory")
    #     if separator is None:
    #       Error_("Separator field Mandatory")
          
    def Read(self):
        with open(self.path, 'r') as file:
            self.lines = [ 
            line.rstrip().replace('"','').split(self.separator) 
                                    for line in file]
        return [ dict(zip(self.lines[0],line))
                            for line in self.lines[1:]]
                            
    def read_csv_file(self):
        with open(self.path, 'r') as file:
         return ([line for line in file])
         
    def write_csv_file(self,rows):
#       def return_str(row):
#            return self.separator.join(map(str,row.values()))
            
      def return_str(row):
           return ','.join(['"{0}"'.format(item)
              for item in list(row.rstrip().split(self.separator))])  
      with open(self.path, 'w') as file:
          file.writelines("\n".join([return_str(row)
                        for row in rows]))   
                                  
                            
    def Read_txt_with_header(self,header):
        self.header = [ str(column).strip() for column in header ]
        with open(self.path, 'r') as file:
          return [ dict(zip(self.header,line))
                            for line in  list((line.rstrip().replace('"','').split(self.separator) 
                                    for line in file)) ]
                                    
    def Write_txt_without_header(self,rows):
        
        def return_str(row):
            return self.separator.join(map(str,row.values()))
            
        with open(self.path, 'w') as file:
            file.writelines("\n".join([return_str(row) 
                                  for row in rows]))    
                                  
    
    def Write(self,rows):

        def return_str(row):
            return self.separator.join(map(str, [ f'"{item}"' 
            for item in row.values()]))

        self.header = self.separator.join(map(str, 
            [f'"{key}"' for key in rows[0].keys()]))
        with open(self.path, 'w') as file:
            file.write(f"{self.header}\n")
            file.writelines("".join([return_str(row) 
                                  for row in rows]))
                                  
