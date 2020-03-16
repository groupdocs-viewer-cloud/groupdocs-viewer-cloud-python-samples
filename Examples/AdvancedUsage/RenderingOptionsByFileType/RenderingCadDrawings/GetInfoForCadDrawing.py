# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to retrieve view information for CAD drawing
class GetInfoForCadDrawing:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.InfoApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/with_layers_and_layouts.dwg"
        view_options.view_format = "HTML"

        request = groupdocs_viewer_cloud.GetInfoRequest(view_options)
        response = apiInstance.get_info(request)
        print(" Layers count: " + str(len(response.cad_view_info.layers)))
        print(" Layouts count: " + str(len(response.cad_view_info.layouts)))
        print("GetInfoForCadDrawing completed: " + str(len(response.pages)))
