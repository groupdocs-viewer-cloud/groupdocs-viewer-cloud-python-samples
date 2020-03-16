# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to set output image size
class ImageViewerAdjustImageSize:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.docx"
        view_options.view_format = "JPG"
        view_options.render_options = groupdocs_viewer_cloud.ImageOptions()
        view_options.render_options.width = 600
        view_options.render_options.height = 800

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("ImageViewerAdjustImageSize completed: " + str(len(response.pages)))
