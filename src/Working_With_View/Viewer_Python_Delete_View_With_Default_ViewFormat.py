# Import modules
import groupdocs_viewer_cloud
from Common_Utilities.Utils import Common_Utilities


class Viewer_Python_Delete_View_With_Default_ViewFormat:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_ViewerApi_Instance()
        
        try:
            deleteViewOptions = groupdocs_viewer_cloud.DeleteViewOptions()

            fileInfo = groupdocs_viewer_cloud.FileInfo()
            fileInfo.file_path = "viewerdocs\\password-protected.docx"
            fileInfo.password = "password"
            fileInfo.storage_name = Common_Utilities.myStorage
        
            deleteViewOptions.file_info = fileInfo;
        
            request = groupdocs_viewer_cloud.DeleteViewRequest(deleteViewOptions)
            api.delete_view(request)
        
            print("Expected response type is Void: View deleted with default View Format.")
        except groupdocs_viewer_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))