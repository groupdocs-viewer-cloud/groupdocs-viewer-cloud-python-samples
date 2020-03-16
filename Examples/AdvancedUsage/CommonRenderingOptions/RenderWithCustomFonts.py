# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to  to set custom font source when rendering documents
class RenderWithCustomFonts:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/with_missing_font.odg"
        view_options.view_format = "HTML"
        # NOTE: Upload fonts to the folder using storage API before rendering
        view_options.fonts_path = "Fonts"

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("RenderWithCustomFonts completed: " + str(len(response.pages)))
