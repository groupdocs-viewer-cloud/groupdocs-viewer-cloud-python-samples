# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to print out archive contents
class GetInfoForArchiveFile:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.InfoApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/with_folders.zip"
        view_options.view_format = "HTML"

        request = groupdocs_viewer_cloud.GetInfoRequest(view_options)
        response = apiInstance.get_info(request)
        folders = response.archive_view_info.folders
        for folder in folders:
            print(folder)
        print("GetInfoForArchiveFile completed: " + str(len(response.pages)))
