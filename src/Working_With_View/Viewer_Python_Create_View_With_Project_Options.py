# Import modules
import groupdocs_viewer_cloud
from Common_Utilities.Utils import Common_Utilities


class Viewer_Python_Create_View_With_Project_Options:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_ViewerApi_Instance()
        
        try:
            viewOptions = groupdocs_viewer_cloud.ViewOptions()

            fileInfo = groupdocs_viewer_cloud.FileInfo()
            fileInfo.file_path = "viewerdocs\\sample.mpp"
            fileInfo.password = ""
            fileInfo.storage_name = Common_Utilities.myStorage
        
            viewOptions.file_info = fileInfo;
            
            renderOptions = groupdocs_viewer_cloud.RenderOptions()

            projectManagementOptions = groupdocs_viewer_cloud.ProjectManagementOptions()
            projectManagementOptions.page_size = "Unknown"
            projectManagementOptions.time_unit = "Months"
            projectManagementOptions.start_date = "2008/07/01"
            projectManagementOptions.end_date = "2008/07/31"
        
            renderOptions.project_management_options = projectManagementOptions
            viewOptions.render_options = renderOptions
        
            request = groupdocs_viewer_cloud.CreateViewRequest(viewOptions)
            response = api.create_view(request)
        
            print("Expected response type is ViewResult: " + str(response))
        except groupdocs_viewer_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))