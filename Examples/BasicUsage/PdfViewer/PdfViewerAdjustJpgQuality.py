# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to adjust JPG image quality in the output PDF document
class PdfViewerAdjustJpgQuality:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/with_jpg_image.pptx"
        view_options.view_format = "PDF"
        view_options.render_options = groupdocs_viewer_cloud.PdfOptions()
        view_options.render_options.jpg_quality = 50        

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("PdfViewerAdjustJpgQuality completed: " + response.file.path)
