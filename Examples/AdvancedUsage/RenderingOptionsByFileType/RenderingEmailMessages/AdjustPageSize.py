# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to adjust output page size
class AdjustPageSize:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.msg"
        view_options.view_format = "PDF"
        view_options.render_options = groupdocs_viewer_cloud.PdfOptions()
        view_options.render_options.email_options = groupdocs_viewer_cloud.EmailOptions()
        view_options.render_options.email_options.page_size = "A4"

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("AdjustPageSize completed: " + response.file.path)
