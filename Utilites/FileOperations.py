'''
@ Author - Shilpa Chatterjee Roy
@ Creation date - 07/06/2018
@ Description - Handles all the file handling operations. In case of any error, the class makes an entry to the log file
and returns fale to the clling class.
'''

import os
import shutil
from Utilites.LogFileUtility import LogFileUtility

class FileOperations:

    def __init__(self,v_log_file_path):
        self.logfile_path = v_log_file_path

#Method to copy a file from source to destination.
    def copy_file(self,v_source, v_destination):
        try:
            shutil.copyfile(v_source,v_destination)
            log = LogFileUtility(self.logfile_path)
            log.log_to_file("INFO", "File copied successfully.")
        except:
            log = LogFileUtility(self.logfile_path)
            log.log_to_file("ERROR", "Error while copying file. Either source or destination file is incorrect.")
            return False
        pass


#method to rename a file.
    def rename_file(self,v_source, v_destination):
        try:
            os.rename(v_source, v_destination)
            log = LogFileUtility(self.logfile_path)
            log.log_to_file("INFO", "File renamed successfully.")
        except:
            log = LogFileUtility(self.logfile_path)
            log.log_to_file("ERROR","Error while renaming file. Either source or destination file is incorrect.")
            return False


#Method to delete a file.
    def delete_file(self,v_file_name):
        try:
            os.remove(v_file_name)
            log = LogFileUtility(self.logfile_path)
            log.log_to_file("INFO", "File deleted successfully.")
        except:
            log = LogFileUtility(self.logfile_path)
            log.log_to_file("ERROR", "Error while deleting the file.")
            return False

#Method to read all the contents of the file(txt file)
    def read_all_content(self,v_file_name):
        try:
            with open(v_file_name, 'r') as v_file:
                v_content = v_file.read()
                v_file.close()
                log = LogFileUtility(self.logfile_path)
                log.log_to_file("INFO", "All content read successfully.")
            return v_content
        except:
            log = LogFileUtility(self.logfile_path)
            log.log_to_file("ERROR", "Error while reading all file content.")
            return False

#Method to read the contents line by line and returns the contents in List.
    def read_line(self, v_file_name):
        try:
            v_file_content = []
            with open(v_file_name, 'r') as v_file:
                for line in v_file.readlines():
                    v_file_content.append(line)
                return v_file_content

                log = LogFileUtility(self.logfile_path)
                log.log_to_file("INFO", "All content read successfully.")
            return v_content
        except:
            log = LogFileUtility(self.logfile_path)
            log.log_to_file("ERROR", "Error while reading all file content.")
            return False

        pass


# fo = FileOperations("D:\Logs\logs.txt")
# v_content = fo.read_all_content("D:\Business_Data\my_test.txt")
# print(v_content)

