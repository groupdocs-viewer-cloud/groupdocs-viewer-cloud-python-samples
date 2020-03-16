# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to apply the watermark to the output pages
class AddWatermark:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.docx"
        view_options.view_format = "HTML"
        view_options.watermark = groupdocs_viewer_cloud.Watermark()
        view_options.watermark.text = "This is a watermark"

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("AddWatermark completed: " + str(len(response.pages)))
