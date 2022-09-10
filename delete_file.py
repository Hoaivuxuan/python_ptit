# import os
# os.remove("D:\\Hoai\projects\data\ex\demofile.txt")
# 
import os
if os.path.exists("D:\\Hoai\projects\data\ex\demofile.txt"):
  os.remove("D:\\Hoai\projects\data\ex\demofile.txt")
else:
  print("The file does not exist")
#  delete folder    
# import os
# os.rmdir("D:\\Hoai\projects\data\ex")