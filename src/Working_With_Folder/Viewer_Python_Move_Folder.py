# Import modules
import groupdocs_viewer_cloud
from Common_Utilities.Utils import Common_Utilities

class Viewer_Python_Move_Folder:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FolderApi_Instance()
        
        try:
            request = groupdocs_viewer_cloud.MoveFolderRequest("viewerdocs1", "viewerdocs1\\viewerdocs", Common_Utilities.myStorage, Common_Utilities.myStorage)
            api.move_folder(request)
            
            print("Expected response type is Void: 'viewerdocs1' folder moved to 'viewerdocs/viewerdocs1'.")
        except groupdocs_viewer_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))