# Import modules
import groupdocs_viewer_cloud
from Common_Utilities.Utils import Common_Utilities


class Viewer_Python_Get_Info_With_Render_Hidden_Pages:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_ViewerApi_Instance()
        
        try:
            viewOptions = groupdocs_viewer_cloud.ViewOptions()

            fileInfo = groupdocs_viewer_cloud.FileInfo()
            fileInfo.file_path = "viewerdocs\\two-hidden-pages.vsd"
            fileInfo.password = ""
            fileInfo.storage_name = Common_Utilities.myStorage
        
            viewOptions.file_info = fileInfo;
            
            renderOptions = groupdocs_viewer_cloud.RenderOptions()
            renderOptions.render_hidden_pages = True
            
            viewOptions.render_options = renderOptions
        
            request = groupdocs_viewer_cloud.GetInfoRequest(viewOptions)
            response = api.get_info(request)
        
            print("Expected response type is InfoResult: " + str(response))
        except groupdocs_viewer_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))