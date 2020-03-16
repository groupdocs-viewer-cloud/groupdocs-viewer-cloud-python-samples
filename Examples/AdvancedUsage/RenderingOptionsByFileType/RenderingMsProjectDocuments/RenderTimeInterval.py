# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to render MS Project document using StartDate and EndDate
class RenderTimeInterval:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.mpp"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.project_management_options = groupdocs_viewer_cloud.ProjectManagementOptions()    
        view_options.render_options.project_management_options.start_date = "2008/06/01"
        view_options.render_options.project_management_options.end_date = "2008/07/01"

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("RenderTimeInterval completed: " + str(len(response.pages)))
