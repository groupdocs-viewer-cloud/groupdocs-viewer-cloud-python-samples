# Import modules
import groupdocs_viewer_cloud
from Common_Utilities.Utils import Common_Utilities

class Viewer_Python_Delete_File:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FileApi_Instance()
        
        try:
            request = groupdocs_viewer_cloud.DeleteFileRequest("viewerdocs1\\one-page.docx", Common_Utilities.myStorage)
            api.delete_file(request)
            
            print("Expected response type is Void: 'viewerdocs1/one-page.docx' deleted.")
        except groupdocs_viewer_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))