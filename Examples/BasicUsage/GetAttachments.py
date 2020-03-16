# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how get attachments
class GetAttachments:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/with_attachments.msg"
        view_options.view_format = "HTML"

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("GetAttachments completed: " + str(len(response.attachments)))
