# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to retrieve view information for outlook data file
class GetInfoForOutlookDataFile:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.InfoApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.ost"
        view_options.view_format = "HTML"

        request = groupdocs_viewer_cloud.GetInfoRequest(view_options)
        response = apiInstance.get_info(request)
        print(" Folders count: " + str(len(response.outlook_view_info.folders)))        
        print("GetInfoForOutlookDataFile completed: " + str(len(response.pages)))
