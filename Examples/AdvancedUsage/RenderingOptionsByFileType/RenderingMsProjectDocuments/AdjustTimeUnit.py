# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to render MS Project document by time interval
class AdjustTimeUnit:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.mpp"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.project_management_options = groupdocs_viewer_cloud.ProjectManagementOptions()    
        view_options.render_options.project_management_options.time_unit = "Days"

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("AdjustTimeUnit completed: " + str(len(response.pages)))
