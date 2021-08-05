# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to set output image size limits when rendering single image to PDF/HTML.
class HtmlViewerLimitImageSize:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.jpg"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.image_max_width = 800
        view_options.render_options.image_max_height = 600

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("HtmlViewerLimitImageSize completed: " + str(len(response.pages)))
