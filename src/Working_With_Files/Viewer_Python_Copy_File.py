# Import modules
import groupdocs_viewer_cloud
from Common_Utilities.Utils import Common_Utilities

class Viewer_Python_Copy_File:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FileApi_Instance()
        
        try:
            request = groupdocs_viewer_cloud.CopyFileRequest("viewerdocs\\one-page.docx", "viewerdocs\\one-page-copied.docx", Common_Utilities.myStorage, Common_Utilities.myStorage)
            api.copy_file(request)
            
            print("Expected response type is Void: 'viewerdocs/one-page.docx' file copied as 'viewerdocs/one-page-copied.docx'.")
        except groupdocs_viewer_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))