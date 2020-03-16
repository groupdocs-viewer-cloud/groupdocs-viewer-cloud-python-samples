# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to render document for display with text
class ImageViewerAddTextOverlay:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.docx"
        view_options.view_format = "PNG"
        view_options.render_options = groupdocs_viewer_cloud.ImageOptions()
        view_options.render_options.extract_text = True

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("ImageViewerAddTextOverlay completed: " + str(len(response.pages)))
