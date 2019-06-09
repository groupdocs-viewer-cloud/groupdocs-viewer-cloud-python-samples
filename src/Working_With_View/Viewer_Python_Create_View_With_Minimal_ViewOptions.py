# Import modules
import groupdocs_viewer_cloud
from Common_Utilities.Utils import Common_Utilities


class Viewer_Python_Create_View_With_Minimal_ViewOptions:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_ViewApi_Instance()
        
        try:
            viewOptions = groupdocs_viewer_cloud.ViewOptions()

            fileInfo = groupdocs_viewer_cloud.FileInfo()
            fileInfo.file_path = "viewerdocs\\password-protected.docx"
            fileInfo.password = "password"
            fileInfo.storage_name = Common_Utilities.myStorage
        
            viewOptions.file_info = fileInfo;
        
            request = groupdocs_viewer_cloud.CreateViewRequest(viewOptions)
            response = api.create_view(request)
        
            print("Expected response type is ViewResult: " + str(response))
        except groupdocs_viewer_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))
