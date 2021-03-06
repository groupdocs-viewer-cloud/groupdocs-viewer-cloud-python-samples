# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to adjust output image size
class AdjustOutputImageSize:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/with_layers_and_layouts.dwg"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.cad_options = groupdocs_viewer_cloud.CadOptions()
        view_options.render_options.cad_options.scale_factor = 0.3

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("AdjustOutputImageSize completed: " + str(len(response.pages)))
