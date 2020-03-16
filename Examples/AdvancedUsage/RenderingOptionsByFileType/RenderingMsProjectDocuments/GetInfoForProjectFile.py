# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to retrieve view information for MS Project document
class GetInfoForProjectFile:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.InfoApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.mpp"
        view_options.view_format = "HTML"

        request = groupdocs_viewer_cloud.GetInfoRequest(view_options)
        response = apiInstance.get_info(request)
        print(" Start date: " + str(response.project_management_view_info.start_date))
        print(" End date: " + str(response.project_management_view_info.end_date))
        print("GetInfoForProjectFile completed: " + str(len(response.pages)))
